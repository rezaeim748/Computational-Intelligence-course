import numpy as np
from abc import ABC, abstractmethod

class Activation:
    def __init__(self) -> None:
        pass

    @abstractmethod
    def forward(self, Z: np.ndarray) -> np.ndarray:
        """
        Forward pass for activation function.
            args:
                Z: input to the activation function
            returns:
                A: output of the activation function
        """
        pass

    @abstractmethod
    def backward(self, dA: np.ndarray, Z: np.ndarray) -> np.ndarray:
        """
        Backward pass for activation function.
            args:
                dA: derivative of the cost with respect to the activation
                Z: input to the activation function
            returns:
                derivative of the cost with respect to Z
        """
        pass

class Sigmoid(Activation):
    def forward(self, Z: np.ndarray) -> np.ndarray:
        """
        Sigmoid activation function.
            args:
            x: input to the activation function
            returns:
                sigmoid(x)
        """
        # TODO: Implement sigmoid activation function
        A = 1/(1+np.exp(-Z))
        cache = Z
    
        return A

    def backward(self, dA: np.ndarray, Z: np.ndarray) -> np.ndarray:
        """
        Backward pass for sigmoid activation function.
            args:
                dA: derivative of the cost with respect to the activation
                Z: input to the activation function
            returns:
                derivative of the cost with respect to Z
        """
        A = self.forward(Z)
        # TODO: Implement backward pass for sigmoid activation function
        dZ = dA * A * (1 - A)
        return dZ
    

class ReLU(Activation):
    def forward(self, Z: np.ndarray) -> np.ndarray:
        """
        ReLU activation function.
            args:
                x: input to the activation function
            returns:
                relu(x)
        """
        # TODO: Implement ReLU activation function
        A = np.maximum(0, Z)
        return A

    def backward(self, dA: np.ndarray, Z: np.ndarray) -> np.ndarray:
        """
        Backward pass for ReLU activation function.
            args:
                dA: derivative of the cost with respect to the activation
                Z: input to the activation function
            returns:
                derivative of the cost with respect to Z
        """
        # TODO: Implement backward pass for ReLU activation function
        A = self.forward(Z)
        dZ = np.multiply(dA, np.int64(A > 0))
        dZ[Z <= 0] = 0

        return dZ
    
    

class Tanh(Activation):
    def forward(self, Z: np.ndarray) -> np.ndarray:
        """
        Tanh activation function.
            args:
                x: input to the activation function
            returns:
                tanh(x)
        """
        # TODO: Implement tanh activation function
        A = np.tanh(Z)
        return A

    def backward(self, dA: np.ndarray, Z: np.ndarray) -> np.ndarray:
        """
        Backward pass for tanh activation function.
            args:
                dA: derivative of the cost with respect to the activation
                Z: input to the activation function
            returns:
                derivative of the cost with respect to Z
        """
        A = self.forward(Z)
        # TODO: Implement backward pass for tanh activation function
        dZ = dA * (1 - np.square(A))
        return dZ
    
class LinearActivation(Activation):
    def linear(Z: np.ndarray) -> np.ndarray:
        """
        Linear activation function.
            args:
                x: input to the activation function
            returns:
                x
        """
        # TODO: Implement linear activation function

        n = len(Z)
        A = Z
        i = 0
        while i < n:
            if Z[i] >= 1:
                A[i] = 1
            else:
                A[i] = 0
            i = i + 1
        return A

    def backward(dA: np.ndarray, Z: np.ndarray) -> np.ndarray:
        """
        Backward pass for linear activation function.
            args:
                dA: derivative of the cost with respect to the activation
                Z: input to the activation function
            returns:
                derivative of the cost with respect to Z
        """
        # TODO: Implement backward pass for linear activation function
        dZ = dA
        return dZ

def get_activation(activation: str) -> tuple:
    """
    Returns the activation function and its derivative.
        args:
            activation: activation function name
        returns:
            activation function and its derivative
    """
    if activation == 'sigmoid':
        return Sigmoid
    elif activation == 'relu':
        return ReLU
    elif activation == 'tanh':
        return Tanh
    elif activation == 'linear':
        return LinearActivation
    else:
        raise ValueError('Activation function not supported')