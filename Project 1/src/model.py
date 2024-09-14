from layers.convolution2d import Conv2D
from layers.maxpooling2d import MaxPool2D
from layers.fullyconnected import FC

from activations import Activation, get_activation
from activations import Sigmoid
from activations import ReLU
from activations import LinearActivation


import pickle
import tqdm
import numpy as np
import matplotlib.pyplot as plt
from random import shuffle

class Model:
    def __init__(self, arch, criterion, optimizer, name=None):
        """
        Initialize the model.
        args:
            arch: dictionary containing the architecture of the model
            criterion: loss 
            optimizer: optimizer
            name: name of the model
        """
        if name is None:
            self.model = arch
            self.criterion = criterion
            self.optimizer = optimizer
            self.layers_names = list(arch.keys())
        else:
            self.model, self.criterion, self.optimizer, self.layers_names = self.load_model(name)
    
    def is_layer(self, layer):
        """
        Check if the layer is a layer.
        args:
            layer: layer to be checked
        returns:
            True if the layer is a layer, False otherwise
        """
        # TODO: Implement check if the layer is a layer
        return type(layer) == MaxPool2D or type(layer) == Conv2D or type(layer) == FC

    def is_activation(self, layer):
        """
        Check if the layer is an activation function.
        args:
            layer: layer to be checked
        returns:
            True if the layer is an activation function, False otherwise
        """
        # TODO: Implement check if the layer is an activation
        return type(layer) == Sigmoid or type(layer) == LinearActivation or type(layer) == ReLU
    
    def forward(self, x):
        """
        Forward pass through the model.
        args:
            x: input to the model
        returns:
            output of the model
        """
        tmp = []
        A = x
        for i in range(0, len(self.layers_name), 2):
            Z = self.model[self.layers_name[i]].forward(A)
            tmp.append(np.copy(Z))
            A = self.model[self.layers_name[i + 1]].forward(Z)
            tmp.append(np.copy(A))
        return tmp
    
    def backward(self, dAL, tmp, x):
        """
        Backward pass through the model.
        args:
            dAL: derivative of the cost with respect to the output of the model
            tmp: list containing the intermediate values of Z and A
            x: input to the model
        returns:
            gradients of the model
        """
        dA = dAL
        grads = {}
        for i in range(len(tmp) - 1, -1, -2):
            if i > 2:
                Z,A = tmp[i - 1], tmp[i - 2]
            else:
                Z, A = tmp[i - 1], x
            dZ = self.model[self.layers_name[i]].backward(dA, Z)
            dA, grad = self.model[self.layers_name[i - 1]].backward(dZ, A)
            grads[self.layers_name[i - 1]] = grad

        return grads

    def update(self, grads):
        """
        Update the model.
        args:
            grads: gradients of the model
        """
        for name in self.layers_name:
            if self.isLayer(self.model[name]) and not self.isMaxpool(self.model[name]):
                self.model[name].update(self.optimizer, grads[name])
    
    def one_epoch(self, x, y, Batch_Size):
        """
        One epoch of training.
        args:
            x: input to the model
            y: labels
            batch_size: batch size
        returns:
            loss
        """
        # TODO: Implement one epoch of training
        tmp = self.forward(x, Batch_Size)
        AL = tmp[-1]
        loss = self.criterion.compute_cost(AL, y)
        dAL = self.criterion.backward(AL, y)
        grads = self.backward(dAL, tmp, x)
        self.update(grads)
        return loss
    
    def save(self, name):
        """
        Save the model.
        args:
            name: name of the model
        """
        with open(name, 'wb') as f:
            pickle.dump((self.model, self.criterion, self.optimizer, self.layers_names), f)
        
    def load_model(self, name):
        """
        Load the model.
        args:
            name: name of the model
        returns:
            model, criterion, optimizer, layers_names
        """
        with open(name, 'rb') as f:
            return pickle.load(f)
        
    def shuffle(self, m, shuffling):
        order = list(range(m))
        if shuffling:
            return np.random.shuffle(order)
        return order

    def batch(self, X, y, Batch_Size, index, order):
        """
        Get a batch of data.
        args:
            X: input to the model
            y: labels
            batch_size: batch size
            index: index of the batch
                e.g: if batch_size = 3 and index = 1 then the batch will be from index [3, 4, 5]
            order: order of the data
        returns:
            bx, by: batch of data
        """
        # TODO: Implement batch
        last_index = min((index + 1) * Batch_Size, len(order))
        batch = order[index * Batch_Size: last_index]
        if X.ndim == 2:
            bx = X[:, batch]
            by = y[:, batch]
            return bx, by
        else:
            bx = X[batch]
            by = y[batch]
            return bx, by

    def compute_loss(self, X, y, Batch_Size):
        """
        Compute the loss.
        args:
            X: input to the model
            y: labels
            Batch_Size: batch size
        returns:
            loss
        """
        # TODO: Implement compute loss
        m = X.shape[0] if X.ndim == 4 else X.shape[1]
        order = self.shuffle(m, False)
        cost = 0
        for b in range(m // Batch_Size):
            bx, by = self.load_batch(X, y, Batch_Size, b, order)
            tmp = self.forward(bx, Batch_Size)
            AL = tmp[-1]
            cost += self.criterion.compute_cost(AL, y) (m // Batch_Size)
        return cost

    def train(self, X, y, epochs, val=None, Batch_Size=3, shuffling=False, verbose=1, save_after=None):
        """
        Train the model.
        args:
            X: input to the model
            y: labels
            epochs: number of epochs
            val: validation data
            batch_size: batch size
            shuffling: if True shuffle the data
            verbose: if 1 print the loss after each epoch
            save_after: save the model after training
        """
        # TODO: Implement training
        train_cost = []
        val_cost = []
        # NOTICE: if your inputs are 4 dimensional m = X.shape[0] else m = X.shape[1]
        m = X.shape[0] if X.ndim == 4 else X.shape[1]
        for e in tqdm(1, epochs + 1):
            order = self.shuffle(m, shuffling)
            cost = 0
            for b in range(m // Batch_Size):
                bx, by = self.load_batch(X, y, Batch_Size, b, order)
                cost += self.one_epoch(X, y, Batch_Size) / (m // Batch_Size)
            train_cost.append(cost)
            if val is not None:
                # i doubt this one!!!!!!!!!!!
                val_cost.append(self.compute_loss(val[0], val[1], Batch_Size))
            if verbose != False:
                if e % verbose == 0:
                    print("Epoch {}: train cost = {}".format(e, cost))
                if val is not None:
                    print("Epoch {}: val cost = {}".format(e, val_cost[-1]))
        if save_after is not None:
            self.save(save_after)
        return train_cost, val_cost
    
    def predict(self, X):
        """
        Predict the output of the model.
        args:
            X: input to the model
        returns:
            predictions
        """
        # TODO: Implement prediction
        A0 = X
        AL = self.forward(A0, A0.shape[1])[-1]
        return AL