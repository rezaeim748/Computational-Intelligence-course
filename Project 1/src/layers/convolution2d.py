import numpy as np

class Conv2D:
    def __init__(self, in_channels, out_channels, name, kernel_size=(1, 1), stride=(1, 1), padding=(1, 1), initialize_method="random"):
        self.in_channels = in_channels
        self.out_channels = out_channels
        self.name = name
        self.initialize_method = initialize_method

        self.kernel_size = (kernel_size, kernel_size) if isinstance(kernel_size, int) else kernel_size
        self.stride = (stride, stride) if isinstance(stride, int) else stride
        self.padding = (padding, padding) if isinstance(padding, int) else padding
        self.parameters = [self.initialize_weights(), self.initialize_bias()]


    def initialize_weights(self):
        """
        Initialize weights.
        returns:
            weights: initialized kernel with shape: (kernel_size[0], kernel_size[1], in_channels, out_channels)
        """
        # TODO: Implement initialization of weights

        params = [
            np.random.randn(self.kernel_size[0], self.kernel_size[1], self.in_channels, self.out_channels)
        ]
        
        if self.initialize_method == "random":
            return params * 0.01
        if self.initialize_method == "xavier":
            params = params * np.sqrt(1 / self.input_size)
            return params
        if self.initialize_method == "he":
            params = params * np.sqrt(2 / self.input_size)
            return params
        else:
            raise ValueError("Invalid initialization method")
        return None
        
    
    def initialize_bias(self):
        """
        Initialize bias.
        returns:
            bias: initialized bias with shape: (1, 1, 1, out_channels)
        
        """
        # TODO: Implement initialization of bias
        params = [
            np.zeros((1, 1, 1, self.out_channels))
        ]
        return params
    
    def target_shape(self, input_shape):
        """
        Calculate the shape of the output of the convolutional layer.
        args:
            input_shape: shape of the input to the convolutional layer
        returns:
            target_shape: shape of the output of the convolutional layer
        """
        # TODO: Implement calculation of target shape
        H = int(1 + (input_shape[0] + 2 * self.padding[0] - self.kernel_size[0]) / self.stride[0])
        W = int(1 + (input_shape[1] + 2 * self.padding[1] - self.kernel_size[1]) / self.stride[1])
        return H, W

    def pad(self, A, padding, pad_value=0):
        """
        Pad the input with zeros.
        args:
            A: input to be padded
            padding: tuple of padding for height and width
            pad_value: value to pad with
        returns:
            A_padded: padded input
        """
        A_padded = np.pad(A, ((0, 0), (padding[0], padding[0]), (padding[1], padding[1]), (0, 0)), mode="constant", constant_values=(pad_value, pad_value))
        return A_padded
    
    def single_step_convolve(self, a_slic_prev, W, b):
        """
        Convolve a slice of the input with the kernel.
        args:
            a_slic_prev: slice of the input data
            W: kernel
            b: bias
        returns:
            Z: convolved value
        """
        # TODO: Implement single step convolution
        Z = np.multiply(a_slic_prev,W)    # hint: element-wise multiplication
        Z = np.sum(Z)    # hint: sum over all elements
        Z = Z + b.astype(float)    # hint: add bias as type float using np.float(None)
        return Z

    def forward(self, A_prev):
        """
        Forward pass for convolutional layer.
            args:
                A_prev: activations from previous layer (or input data)
                A_prev.shape = (batch_size, H_prev, W_prev, C_prev)
            returns:
                A: output of the convolutional layer
        """
        # TODO: Implement forward pass
        W, b = self.parameters[0], self.parameters[1]
        (m, n_H_prev, n_W_prev, n_C_prev) = A_prev.shape
        (fh, fw, n_C_prev, n_C) = W.shape
        strideh, stridew = self.stride[0], self.stride[1]
        n_H, n_W = self.target_shape([n_H_prev, n_W_prev])
        Z = np.zeros((m, n_H, n_W, n_C))
        A_prev_pad = self.pad(A_prev, self.padding, 0)
        for i in range(m):
            a_prev_pad = A_prev_pad[i,:,:,:]
            for h in range(n_H):
                vert_start = h * strideh
                vert_end = vert_start + self.kernel_size[0]
                for w in range(n_W):
                    horiz_start = w * stridew
                    horiz_end = horiz_start + self.kernel_size[1]
                    for c in range(n_C):
                        a_slice_prev = a_prev_pad[vert_start:vert_end, horiz_start:horiz_end, :]
                        weights = W[:,:,:,c]
                        biases = b[:,:,:,c]
                        Z[i, h, w, c] = self.single_step_conv(a_slice_prev, weights, biases)
        return Z

    def backward(self, dZ, A_prev):
        """
        Backward pass for convolutional layer.
        args:
            dZ: gradient of the cost with respect to the output of the convolutional layer
            A_prev: activations from previous layer (or input data)
            A_prev.shape = (batch_size, H_prev, W_prev, C_prev)
        returns:
            dA_prev: gradient of the cost with respect to the input of the convolutional layer
            gradients: list of gradients with respect to the weights and bias
        """
        # attention: we have two W with different meanings

        # TODO: Implement backward pass
        W, b = self.parameters[0], self.parameters[1]
        (m, n_H_prev, n_W_prev, n_C_prev) = A_prev.shape
        (fh, fw, n_C_prev, n_C) = W.shape
        strideh, stridew = self.stride[0], self.stride[1]
        n_H, n_W = self.target_shape([n_H_prev, n_W_prev])
        dA_prev = np.zeros((m, n_H_prev, n_W_prev, n_C_prev))
        dW = np.zeros((fh, fw, n_C_prev, n_C))
        db = np.zeros((1, 1, 1, n_C))
        A_prev_pad = self.pad(A_prev, self.padding, 0)
        dA_prev_pad = self.pad(dA_prev, self.padding, 0)
        for i in range(m):
            a_prev_pad = A_prev_pad[i, :, :, :]
            da_prev_pad = dA_prev_pad[i, :, :, :]
            for h in range(n_H):
                for w in range(n_W):
                    for c in range(n_C):
                        vert_start = h * strideh
                        vert_end = vert_start + fh
                        horiz_start = w * stridew
                        horiz_end = horiz_start + fw
                        a_slice = a_prev_pad[vert_start:vert_end, horiz_start:horiz_end, :]
                        da_prev_pad[vert_start:vert_end, horiz_start:horiz_end, :] += W[:,:,:,c] * dZ[i, h, w, c]
                        dW[:,:,:,c] += a_slice * dZ[i, h, w, c]
                        db[:,:,:,c] += dZ[i, h, w, c]
            dA_prev[i, :, :, :] = da_prev_pad[self.padding[0]:-self.padding[0], self.padding[1]:-self.padding[1], :]
        grads = [dW, db]
        return dA_prev, grads
    
    def update_parameters(self, optimizer, grads):
        """
        Update parameters of the convolutional layer.
        args:
            optimizer: optimizer to use for updating parameters
            grads: list of gradients with respect to the weights and bias
        """
        self.parameters = optimizer.update(grads, self.name)