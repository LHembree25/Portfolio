# MNIST Convolutional Neural Network Classifier

This project builds a convolutional neural network to classify handwritten digits from the MNIST dataset. The workflow includes data ingestion, preprocessing, architecture definition, training, evaluation, and error analysis. The notebook demonstrates a complete image classification pipeline using PyTorch and standard visualization tools. The work verifies model performance through accuracy measurement and confusion matrix inspection.

## Tools Used
- Python
- PyTorch
- Torchvision
- Matplotlib
- Seaborn
- Scikit‑learn

## Notebook Contents
- Loading the MNIST dataset
- Displaying the first five training images and labels
- Defining the CNN architecture
- Training loop execution
- Testing loop execution
- Accuracy calculation
- Confusion matrix generation
- Confusion matrix visualization
- Summarization of classifier performance

## Key Results
Test accuracy: 98.45 percent  
Confusion matrix shows strong diagonal values
Misclassifications occur in predictable locations such as 7→2, 9→7 or 8, and 4→9
Classifier demonstrates stable feature extraction for handwritten digit recognition
Errors align with natural variation in handwriting rather than model instability

## Why This Project Matters
This project demonstrates applied neural network construction and technician‑level workflow execution. The work shows how preprocessing, architecture definition, training, evaluation, and error analysis combine to produce a reliable classifier. The structure supports analysts who need repeatable pipelines for image classification tasks and verification of model behavior through quantitative and visual diagnostics.
