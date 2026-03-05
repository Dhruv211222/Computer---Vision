🐶🐱 Dog vs Cat Image Classification using VGG16 Transfer Learning

📌 Project Overview

This project implements an image classification system that distinguishes between dogs and cats using Deep Learning and Transfer Learning.

The model uses the VGG16 pre-trained convolutional neural network from ImageNet as a feature extractor and adds custom classification layers for binary classification.

Transfer learning allows us to achieve high accuracy with fewer training samples and less training time compared to training a CNN from scratch.

The system is capable of learning complex visual features such as:
	•	Fur patterns
	•	Facial structure
	•	Ear shapes
	•	Animal body structure

This project demonstrates practical usage of Computer Vision techniques in real-world image classification tasks.

⸻

🧠 How It Works

Image Preprocessing

Before training the model, all images go through preprocessing:
	•	Images are resized to 160 × 160 pixels
	•	Pixel values are normalized between 0 and 1
	•	Data augmentation is applied to increase dataset diversity

Data augmentation techniques used:
	•	Rotation
	•	Horizontal flipping
	•	Zoom
	•	Width shift
	•	Height shift

These techniques help reduce overfitting and improve model generalization.

⸻

Transfer Learning with VGG16

Instead of training a CNN from scratch, we use VGG16, a deep convolutional neural network trained on the ImageNet dataset.

Steps:
	1.	Load VGG16 without the top classification layer
	2.	Freeze the base layers to retain learned features
	3.	Add custom classification layers
	4.	Train the model on the dog vs cat dataset
	5.	Fine-tune the last layers of VGG16 for better performance

⸻

⚙️ Technologies Used
	•	Python
	•	TensorFlow / Keras
	•	OpenCV
	•	NumPy
	•	Matplotlib
	•	Jupyter Notebook

🧩 Model Training

Training is performed in two phases.

Phase 1 — Feature Extraction
	•	Freeze all VGG16 layers
	•	Train only the newly added classification layers

Training Configuration
	•	Epochs: 7
	•	Optimizer: Adam
	•	Loss Function: Binary Crossentropy
	•	Batch Size: 64

⸻

Phase 2 — Fine Tuning

In the second phase:
	•	The last 16 layers of VGG16 are unfrozen
	•	The model is retrained with a lower learning rate

This helps the model adapt better to the dog vs cat dataset.

⸻

📈 Model Performance

During training, the following metrics are tracked:
	•	Training Accuracy
	•	Validation Accuracy
	•	Training Loss
	•	Validation Loss

The model achieves high validation accuracy (~90%+) on the validation dataset.

Graphs are plotted to visualize training progress.
