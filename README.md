## Libraries required:
For the code provided, the torch library needs to be installed and you can do it with this command: pip install torch.

## Objective of the program:
This code allows the manipulation of two tensors using various mathematical operations, including: addition, multiplication, transpose, mean, standard deviation and subtraction, which have been included to manipulate tensors in a usefull way.

## Steps to follow:
1. Use the following command to import the necessary code:
from module_structure.practica_torch import TensorCalculator

2. Instantiate the class, in this case, TensorCalculator, like this:
tensor_calc = TensorCalculator()

3. create the tensors and assign values to each tensor, as shown:
tensor1_v = [[x, y], [x1, y1]] 
tensor2_v = [[x, y], [x1, y1]]  

4. Using the values specified in the lists tensor1_v and tensor2_v, respectively, with dimensions of 2x2:
tensor1 = tensor_calc.get_custom_tensor_values(2, 2, tensor1_v)
tensor2 = tensor_calc.get_custom_tensor_values(2, 2, tensor2_v)

5. Convert the tensors to float with the following code:
tensor1 = tensor1.float()
tensor2 = tensor2.float()

6. You can obtain tensors with all values set to zero, one, or randomly generated using the following commands: 
zeros_tensor = tensor_calc.custom_tensor_zeros(2, 2)
ones_tensor = tensor_calc.custom_tensor_ones(2, 2)
random_tensor = tensor_calc.custom_tensor_random(2, 2)

Proceed to use the various operations provided, such as:
(You can use any of these operations with the tensor that you want, but the examples provided will be with tensor1 and tensor2)

    - SUM: added_tensor = tensor_calc.custom_tensor_sum(tensor1, tensor2)
    
    - PRODUCT: multiplied_tensor = tensor_calc.custom_tensor_product(tensor1, tensor2)
    
    - TRANSPOSE: transposed_tensor1 = tensor_calc.custom_tensor_transpose(tensor1)
    
    - MEAN: mean_tensor1 = tensor_calc.custom_tensor_mean(tensor1)
    
    - STD: std_tensor1 = tensor_calc.custom_tensor_std(tensor1)
    
    - SUBTRACT: subtract_tensor = tensor_calc.custom_tensor_subtract(tensor1, tensor2)
    
