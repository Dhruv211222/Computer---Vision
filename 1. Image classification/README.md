**LeNet-5 Handwritten Digit Classification using CNN (Keras / PyTorch)
**
📌 Project Overview

This project implements a handwritten digit classification model using the **LeNet-5 Convolutional Neural Network (CNN)** architecture trained on the **MNIST dataset**.

The objective of this project is to classify handwritten digits from **0 to 9** using deep learning techniques.

The repository includes two implementations of the same model:

- TensorFlow / Keras implementation
- PyTorch implementation

The model learns important visual patterns from grayscale images and predicts the correct digit class.

---

🧠 Model Architecture

The model is based on the classic **LeNet-5 CNN architecture** developed by Yann LeCun.

The architecture includes:

- Convolutional layers (Conv2D)
- Average Pooling layers
- Flatten layer
- Fully connected dense layers
- Softmax output layer

These layers help the model extract spatial features from images and perform accurate classification.

---

⚙️ Technologies Used

- Python
- TensorFlow / Keras
- PyTorch
- NumPy
- Matplotlib
- Jupyter Notebook

---

📊 Dataset

The model is trained using the **MNIST dataset**, which is a widely used benchmark dataset in machine learning.

Dataset details:

- 70,000 grayscale images
- Image size: **28 × 28 pixels**
- Training images: **60,000**
- Test images: **10,000**
- Total classes: **10 digits (0–9)**

Dataset loaded directly using:

```python
from tensorflow.keras.datasets import mnist
