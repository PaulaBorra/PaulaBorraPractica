import torch

__all__ = ['TensorCalculator']

class TensorCalculator:

    # Method to get tensors with specific values
    def get_custom_tensor_values(self, dim_x, dim_y, custom_tensor_values):
        values = custom_tensor_values
        return torch.tensor(values)

    # Method to create tensors of zeros
    def custom_tensor_zeros(self, custom_dim_x, custom_dim_y):
        zeros = torch.zeros([custom_dim_x, custom_dim_y])
        return zeros

    # Method to create tensors of ones
    def custom_tensor_ones(self, custom_dim_x, custom_dim_y):
        ones = torch.ones([custom_dim_x, custom_dim_y])
        return ones

    # Method to create random tensors
    def custom_tensor_random(self, custom_dim_x, custom_dim_y):
        random = torch.rand([custom_dim_x, custom_dim_y])
        return random

    # Method to sum tensors
    def custom_tensor_sum(self, custom_t1, custom_t2):
        if custom_t1.size() != custom_t2.size():
            print("Error: The sizes of the input tensors are not compatible for addition.")
            return None
        else:
            sum_tensors = torch.add(custom_t1, custom_t2)
            return sum_tensors

    # Method to multiply tensors
    def custom_tensor_product(self, custom_t1, custom_t2):
        if custom_t1.size() != custom_t2.size():
            print("Error: The sizes of the input tensors are not compatible for multiplication.")
            return None
        else:
            product_tensors = torch.mul(custom_t1, custom_t2)
            return product_tensors

    #ADDITIONAL FUNCTIONS
    # Method to transpose tensors
    def custom_tensor_transpose(self, custom_t):
        if custom_t.size(0) != custom_t.size(1):
            print("Error: The input tensor must be square for transposition.")
            return None
        else:
            transpose_tensor = torch.transpose(custom_t, 0, 1)
            return transpose_tensor

    # Method to subtract tensors
    def custom_tensor_subtract(self, custom_t1, custom_t2):
        if custom_t1.size() != custom_t2.size():
            print("Error: The sizes of the input tensors are not compatible for subtraction.")
            return None
        else:
            subtraction_tensor = torch.sub(custom_t1, custom_t2)
            return subtraction_tensor

    # Method to compute the mean of a tensor
    def custom_tensor_mean(self, custom_tensor):
        return torch.mean(custom_tensor)

    # Method to compute the standard deviation of a tensor
    def custom_tensor_std(self, custom_tensor):
        return torch.std(custom_tensor)
