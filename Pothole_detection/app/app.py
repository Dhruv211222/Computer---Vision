import sys
import os
import streamlit as st
import gdown

# ================= MODEL SETUP =================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "..", "best.pt")

FILE_ID = "1J391ph0-jzdI8vMh5WwZKgqZCl6wUenh"

# 🔥 DOWNLOAD MODEL BEFORE LOADING
if not os.path.exists(MODEL_PATH):
    with st.spinner("Downloading model... ⏳"):
        url = f"https://drive.google.com/uc?id={FILE_ID}"
        gdown.download(url, MODEL_PATH, quiet=False)

    st.success("Model downloaded ✅")

# 🔥 SAFETY CHECK
if not os.path.exists(MODEL_PATH):
    st.error("❌ Model not found even after download!")
    st.stop()

# ================= IMPORTS =================
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import cv2
import tempfile
import numpy as np
import folium
import pandas as pd

from utils.detector import PotholeDetector
from utils.tracker import SimpleTracker
from utils.report import generate_summary
from utils.map_utils import create_map
from utils.visualization import (
    plot_bar_chart,
    plot_pie_chart,
    show_risk_indicator,
    live_dashboard,
    plot_time_series,
    plot_heatmap
)

# ================= CONFIG =================
st.set_page_config(layout="wide")
st.title("🚗 Smart Road Damage Detection System")

# 🔥 LOAD MODEL AFTER DOWNLOAD
detector = PotholeDetector(MODEL_PATH)

BASE_LAT = 23.0225
BASE_LON = 72.5714


# =====================================================
# 📂 UPLOAD SECTION
# =====================================================
st.header("📂 Upload Image / Video")

uploaded_file = st.file_uploader(
    "Upload Image or Video",
    type=["jpg", "png", "jpeg", "mp4"]
)

if uploaded_file:

    if uploaded_file.type.startswith("image"):

        st.subheader("🖼 Image Result")

        file_bytes = uploaded_file.read()
        frame = cv2.imdecode(np.frombuffer(file_bytes, np.uint8), cv2.IMREAD_COLOR)

        frame, detections, stats, fps = detector.detect(frame)
        st.image(frame, channels="BGR")

        summary, total, risk = generate_summary(detections)

        st.subheader("📊 Summary")
        st.write(summary)
        st.success(f"Total Defects: {total}")
        show_risk_indicator(risk)

        st.subheader("📈 Visualization")
        plot_bar_chart(summary)
        plot_pie_chart(summary)

    elif uploaded_file.type.startswith("video"):

        st.subheader("🎥 Video Processing")

        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(uploaded_file.read())

        cap = cv2.VideoCapture(tfile.name)
        stframe = st.empty()

        tracker = SimpleTracker()
        unique_detections = []

        if st.button("▶️ Play Video"):

            frame_count = 0

            while True:
                ret, frame = cap.read()
                if not ret:
                    break

                if frame_count % 2 != 0:
                    frame_count += 1
                    continue

                frame = cv2.resize(frame, (640, 480))
                frame, detections, stats, fps = detector.detect(frame)

                for d in detections:
                    if tracker.is_new(d["bbox"]):
                        d["frame"] = frame_count
                        unique_detections.append(d)

                stframe.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                frame_count += 1

            cap.release()

            df = pd.DataFrame(unique_detections)
            summary, total, risk = generate_summary(unique_detections)

            st.subheader("📊 Video Summary")
            st.write(summary)
            st.success(f"Unique Defects: {total}")
            show_risk_indicator(risk)

            plot_bar_chart(summary)
            plot_pie_chart(summary)
            plot_time_series(df)


# =====================================================
# 🎥 LIVE CAMERA
# =====================================================
st.header("🎥 Live Detection (Laptop Camera)")

col1, col2 = st.columns(2)
start = col1.button("▶️ Start Camera")
stop = col2.button("⏹ Stop Camera")

if "run_camera" not in st.session_state:
    st.session_state.run_camera = False

if start:
    st.session_state.run_camera = True
    st.session_state.unique_detections = []
    st.session_state.map_points = []
    st.session_state.tracker = SimpleTracker()

if stop:
    st.session_state.run_camera = False

if st.session_state.run_camera:

    cap = cv2.VideoCapture(0)
    stframe = st.empty()
    stats_box = st.empty()

    frame_count = 0

    while st.session_state.run_camera:

        ret, frame = cap.read()
        if not ret:
            st.error("❌ Camera not working")
            break

        frame = cv2.resize(frame, (640, 480))
        frame, detections, stats, fps = detector.detect(frame)

        stframe.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        stats_box.write({"FPS": round(fps, 2), "Stats": stats})

        lat = BASE_LAT + frame_count * 0.00005
        lon = BASE_LON + frame_count * 0.00005

        for d in detections:
            if st.session_state.tracker.is_new(d["bbox"]):
                d["frame"] = frame_count
                st.session_state.unique_detections.append(d)

                if d["label"] == "pothole":
                    st.session_state.map_points.append((lat, lon))

        frame_count += 1

    cap.release()


# =====================================================
# 📊 REPORT + ANALYTICS
# =====================================================
if "unique_detections" in st.session_state and st.session_state.unique_detections:

    st.header("📊 Route Analysis")

    df = pd.DataFrame(st.session_state.unique_detections)
    summary, total, risk = generate_summary(st.session_state.unique_detections)

    st.write(summary)
    st.success(f"Total Unique Defects: {total}")
    show_risk_indicator(risk)

    live_dashboard(df)
    plot_time_series(df)

    st.subheader("📈 Distribution")
    plot_bar_chart(summary)
    plot_pie_chart(summary)

    os.makedirs("outputs", exist_ok=True)
    df.to_csv("outputs/final_report.csv", index=False)

    st.download_button(
        "📥 Download Report",
        data=df.to_csv(index=False),
        file_name="road_report.csv",
        mime="text/csv"
    )

    st.subheader("🗺️ Map")
    m = create_map(st.session_state.map_points)
    if m:
        st.components.v1.html(m._repr_html_(), height=400)

    plot_heatmap(st.session_state.map_points)


# =====================================================
# 📱 MOBILE
# =====================================================
st.header("📱 Mobile Detection")

camera_image = st.camera_input("📸 Capture Frame")

if camera_image:

    frame = cv2.imdecode(
        np.frombuffer(camera_image.read(), np.uint8),
        cv2.IMREAD_COLOR
    )

    frame, detections, stats, fps = detector.detect(frame)
    st.image(frame, channels="BGR")

    summary, total, risk = generate_summary(detections)

    st.subheader("📊 Mobile Summary")
    st.write(summary)
    st.success(f"Total Defects: {total}")
    show_risk_indicator(risk)

    plot_bar_chart(summary)
    plot_pie_chart(summary)
