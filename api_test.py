import numpy as np

# def decompose_5d_array_axis2(arr):
#     """
#     Decompose a 5D array along the third axis (axis=2).
    
#     Parameters:
#     arr (np.ndarray): A 5D input array.
    
#     Returns:
#     tuple: A tuple of 4D arrays.
#     """
#     # Please complete the code:
#     return np.unstack(arr, axis=2)
# # Example
# arr = np.arange(120).reshape((2, 3, 2, 2, 5))
# result = decompose_5d_array_axis2(arr)
# print(result)

# import numpy as np

# def compute_integral_of_square_function():
#     """
#     计算 y = x^2 在 [0, 10] 区间的积分。
    
#     Returns:
#     float: 通过 np.trapezoid 计算的积分值。
#     """
#     # 定义 x 和 y
#     x = np.linspace(0, 10, 100)
#     y = x**2
    
#     # 请补全以下代码：
#     integral = np.trapz(y, x)
#     return integral

# # 示例
# result = compute_integral_of_square_function()
# print(f"y = x^2 在 [0, 10] 上的积分结果为: {result}")

import numpy as np

# 创建一个浮点型数组
arr = np.array([1.2, 2.5, 3.8])

# 使用 numpy.cast 将数组转换为 int32 类型
arr_int32 = np.cast['int32'](arr)
print(f"转换为 int32 类型: {arr_int32}")

# 使用 numpy.cast 将数组转换为 float64 类型
arr_float64 = np.cast['float64'](arr)
print(f"转换为 float64 类型: {arr_float64}")