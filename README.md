## Libraries required:
For the code provided, the torch library needs to be installed and you can do it with this command: pip install torch.

## Objective of the program:
This code allows the manipulation of two tensors using various mathematical operations, including: addition, multiplication, transpose, mean, standard deviation and subtraction, which have been included to manipulate tensors in a usefull way.

## Steps to follow:
To begin, use the following command to import the necessary code:
from module_structure.practica_torch import TensorCalculator

Then, instantiate the class, in this case, TensorCalculator, like this:
tensor_calc = TensorCalculator()

Next, create the tensors and assign values to each tensor, as shown:
tensor1_v = [[x, y], [x1, y1]] 
tensor2_v = [[x, y], [x1, y1]]  

Using the values specified in the lists tensor1_v and tensor2_v, respectively, with dimensions of 2x2:
tensor1 = tensor_calc.get_custom_tensor_values(2, 2, tensor1_v)
tensor2 = tensor_calc.get_custom_tensor_values(2, 2, tensor2_v)

You can obtain tensors with all values set to zero, one, or randomly generated using the following commands: 
zeros_tensor = tensor_calc.custom_tensor_zeros(2, 2)
ones_tensor = tensor_calc.custom_tensor_ones(2, 2)
random_tensor = tensor_calc.custom_tensor_random(2, 2)

Convert the tensors to float with the following code:
tensor1 = tensor1.float()
tensor2 = tensor2.float()

Proceed to use the various operations provided, such as:
    - SUM: added_tensor = tensor_calc.custom_tensor_sum(tensor1, tensor2)
    - PRODUCT: multiplied_tensor = tensor_calc.custom_tensor_product(tensor1, tensor2)
    - TRANSPOSE: (for instance, with tensor1, or any other valid tensors) 
      transposed_tensor1 = tensor_calc.custom_tensor_transpose(tensor1)
    - MEAN: mean_tensor1 = tensor_calc.custom_tensor_mean(tensor1)
    - STD: std_tensor1 = tensor_calc.custom_tensor_std(tensor1)
    - SUBTRACT: subtract_tensor = tensor_calc.custom_tensor_subtract(tensor1, tensor2)
