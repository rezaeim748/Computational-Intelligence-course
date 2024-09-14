import numpy as np

class MeanSquaredError:
    def __init__(self):
        pass

    def compute(self, y_pred, y_true):
        """
        computes the mean squared error loss
            args:
                y_pred: predicted labels (n_classes, batch_size)
                y_true: true labels (n_classes, batch_size)
            returns:
                mean squared error loss
        """
        # TODO: Implement mean squared error loss
        summation = 0
        n = len(y_true)
        for i in range(0, n):
            difference = y_true[i] - y_pred[i]
            squared_difference = difference ** 2
            summation = summation + squared_difference
        cost = summation / n
        batch_size = None
        return np.squeeze(cost)
    
    def backward(self, y_pred, y_true):
        """
        computes the derivative of the mean squared error loss
            args:
                y_pred: predicted labels (n_classes, batch_size)
                y_true: true labels (n_classes, batch_size)
            returns:
                derivative of the mean squared error loss
        """
        # TODO: Implement backward pass for mean squared error loss
        return y_pred - y_true