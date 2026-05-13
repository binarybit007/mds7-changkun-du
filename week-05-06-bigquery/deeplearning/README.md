
# Titanic Deep Learning ETLS Pipeline

## Project Overview
This project extends the Titanic classification pipeline from classical machine learning to deep learning using Keras Sequential neural networks.

## Dataset
The model uses the cleaned Titanic dataset: `titanic_clean.csv`.

## Preprocessing
- Target variable: `Survived`
- Feature matrix scaled using `StandardScaler`
- Train/test split: 80/20
- Random state: 42

## Model A: Shallow Network

**File:** `model_3_layers.h5`

Architecture:
- Dense hidden layer: 16 neurons, ReLU activation
- Output layer: 1 neuron, Sigmoid activation

Compilation:
- Optimizer: Adam
- Loss: Binary Crossentropy
- Metric: Accuracy

Test Accuracy: `0.4190`

## Model B: Deep Network

**File:** `model_5_layers.h5`

Architecture:
- Dense hidden layer 1: 64 neurons, ReLU activation
- Dense hidden layer 2: 32 neurons, ReLU activation
- Dense hidden layer 3: 16 neurons, ReLU activation
- Output layer: 1 neuron, Sigmoid activation

Compilation:
- Optimizer: Adam
- Loss: Binary Crossentropy
- Metric: Accuracy

Test Accuracy: `0.7263`

## Deployment
Artifacts were deployed to:
- AWS S3 bucket: `anshulmds1/deeplearning/`
- GitHub directory: `week-05-06-bigquery/deeplearning`

## Generated On
2026-05-13 10:25:48
