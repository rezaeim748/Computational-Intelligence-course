
# MNIST Digit Classification Project

This repository contains the implementation of an Artificial Neural Network (ANN) designed to classify digits 2 and 5 from the popular MNIST dataset. This project was completed as part of the Spring 1402 term in the context of neural networks coursework.

## Project Overview

The goal of this project is to develop a neural network capable of distinguishing between the digits 2 and 5 from handwritten images in the MNIST dataset. The project utilizes a Convolutional Neural Network (CNN) to perform the classification task.

### Key Components:
- **Convolutional Layers**: Extract spatial features from the input images.
- **Pooling Layers**: Reduce the dimensionality of feature maps.
- **Fully Connected Layers**: Combine the extracted features to make final predictions.
- **Activation Functions**: Use common functions like ReLU to introduce non-linearity.
- **Cross-Entropy Loss Function**: Used to optimize the classification task.
- **Adam Optimizer**: Applied to minimize the loss function and update model weights.

## Setup Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/rezaeim748/MNIST-Digit-Classification.git
   cd MNIST-Digit-Classification
   ```

2. Ensure the MNIST dataset is available in the `datasets/MNIST/` directory. If the dataset is not available, it can be downloaded via the `torchvision.datasets` package in the notebook.

3. Open and run the Jupyter notebook:

   ```bash
   jupyter notebook notebooks/MNIST.ipynb
   ```

   This will load the dataset, train the model, and evaluate its performance on the classification task.

## Dataset

- **MNIST Dataset**: The MNIST dataset consists of grayscale images of handwritten digits. For this task, only the digits 2 and 5 are used for classification. The dataset is split into training and testing sets to train the model and evaluate its accuracy.

## Results

- The model achieved high accuracy in distinguishing between the digits 2 and 5 using a CNN. The results demonstrate the effectiveness of convolutional neural networks for simple digit classification tasks.

## Future Work

- Extend the model to classify all digits (0-9) in the MNIST dataset.
- Experiment with different neural network architectures and hyperparameter tuning to further improve performance.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
