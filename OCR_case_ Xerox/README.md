# OCR Case Study: Xerox Document Processing

A comprehensive image processing and analysis project focused on Optical Character Recognition (OCR) using document images. This project demonstrates advanced computer vision techniques for document analysis, compression assessment, and image quality evaluation.

## 📋 Table of Contents

- [Overview](#overview)
- [Tasks](#tasks)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Results](#results)
- [Dependencies](#dependencies)
- [Author](#author)

## 🎯 Overview

This project explores three core computer vision tasks on document images:

1. **Connected Component Analysis & Character Grouping** - Detecting and clustering similar characters in binary images
2. **Compression Quality Assessment** - Evaluating the impact of JPEG compression on document images using PSNR and SSIM metrics
3. **Lossless vs. Lossy Compression** - Comparing PNG (lossless) and JPEG (lossy) compression effects on document quality

## 📚 Tasks

### Task 1: Connected Component Analysis & Character Clustering

**Objective:** Identify individual characters in a document and group similar characters together.

**Methodology:**
- Convert grayscale image to binary (black & white)
- Apply connected components analysis to detect individual connected regions
- Remove noise (components with area < 10 pixels)
- Normalize character regions to 20×20 pixels
- Group characters using Mean Squared Error (MSE) similarity metric
- Reconstruct document using prototype characters from each group

**Key Parameters:**
- MSE Threshold: 0.2 (adjustable: 0.05, 0.2, 0.4)
- Minimum component area: 10 pixels
- Character normalization size: 20×20 pixels

**Output:**
- Total components detected: 1,091
- Unique symbol groups found: 60
- Side-by-side comparison of original vs. reconstructed images

---

### Task 2: JPEG Compression Quality Assessment

**Objective:** Analyze how JPEG compression quality affects image degradation using quality metrics.

**Methodology:**
- Compress images at multiple quality levels: 90, 70, 50, 30
- Calculate Peak Signal-to-Noise Ratio (PSNR)
- Calculate Structural Similarity Index (SSIM)
- Apply Canny edge detection to visualize compression artifacts

**Quality Metrics Evaluated:**
| Quality | PSNR  | SSIM  |
|---------|-------|-------|
| 90      | 44.52 | 0.9964|
| 70      | 38.69 | 0.9851|
| 50      | 37.50 | 0.9766|
| 30      | 36.62 | 0.9655|

**Key Insights:**
- PSNR decreases as compression quality decreases
- SSIM remains above 0.96 across all quality levels, indicating high perceptual similarity
- Canny edge detection reveals compression artifacts at lower quality levels

---

### Task 3: Lossless vs. Lossy Compression

**Objective:** Compare the impact of lossless (PNG) and lossy (JPEG) compression on document OCR.

**Methodology:**
- Save document in PNG format (lossless compression)
- Save document in JPEG format at 30% quality (lossy compression)
- Convert both to binary images using threshold of 127
- Calculate pixel-wise differences
- Analyze impact on connected components

**Findings:**
- Lossless compression (PNG) preserves all pixel information
- Lossy compression (JPEG 30%) introduces artifacts and compression noise
- Visual difference map highlights areas affected by lossy compression

---

## 💻 Installation

### Prerequisites
- Python 3.7+
- Jupyter Notebook

### Required Libraries

```bash
pip install opencv-python numpy matplotlib scikit-image
