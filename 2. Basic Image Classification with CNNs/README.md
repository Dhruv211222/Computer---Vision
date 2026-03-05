# CIFAR-10 Image Classification using Convolutional Neural Networks (CNN)

## 📌 Project Overview

This project implements an image classification model using a **Convolutional Neural Network (CNN)** trained on the **CIFAR-10 dataset**. The objective is to build a deep learning model capable of recognizing objects in small color images. The model learns hierarchical visual features from images and predicts the correct category among ten possible classes.

The project demonstrates the **complete workflow of building an image classification system**, including data preprocessing, CNN architecture design, model training, evaluation, and prediction visualization.

---

## 🧠 Model Architecture

The CNN architecture is designed to extract spatial features from images and classify them into different categories.

The model includes the following layers:

- Convolutional Layers (Conv2D) for feature extraction
- Batch Normalization for training stability
- MaxPooling Layers for spatial reduction
- Dropout Layers to reduce overfitting
- Fully Connected Dense Layers for classification
- Softmax Output Layer for multi-class prediction

This architecture enables the model to learn both low-level and high-level visual features.

---

## ⚙️ Technologies Used

- Python  
- TensorFlow / Keras  
- NumPy  
- Matplotlib  
- Jupyter Notebook  

---

## 📊 Dataset

This project uses the **CIFAR-10 dataset**, a widely used benchmark dataset for image classification tasks.

Dataset details:

- Total Images: **60,000**
- Training Images: **50,000**
- Test Images: **10,000**
- Image Size: **32 × 32 pixels**
- Channels: **RGB (3 channels)**
- Classes: **10 object categories**

The dataset classes include:

- airplane  
- automobile  
- bird  
- cat  
- deer  
- dog  
- frog  
- horse  
- ship  
- truck  

Dataset is loaded directly using:

```python
from tensorflow.keras.datasets import cifar10
