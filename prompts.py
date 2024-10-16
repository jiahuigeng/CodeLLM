from utils_llm import prompt_gpt

CodeCompletion_PROMPT = """{} is a new function introduced in {} Version {}. Here is the introduction: 
{} 

Please write 6 different examples for the user to complete the code in a function. All the examples need to use the function {}. All the examples have text prompts and contain function presentations to test the user's proficiency in {}. 
"""


def get_gpt_complete_prompt(func_name, lib, version, description):
    return CodeCompletion_PROMPT.format(func_name, lib, version, description, func_name, func_name)


def parse_examples_and_save(resp):
    pass
if __name__ == "__main__":
    func_name = "numpy.unstack"
    lib = "NumPy"
    version = '2.1.0'
    description = '''Page Title: numpy.bitwise_count — NumPy v2.1 Manual
numpy.bitwise_count — NumPy v2.1 Manual
numpy.bitwise_count
numpy.bitwise_count#
numpy.bitwise_count(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature]) = <ufunc 'bitwise_count'>#
Computes the number of 1-bits in the absolute value of x.
Analogous to the builtin int.bit_count or popcount in C++.
Parameters:
xarray_like, unsigned intInput array.
outndarray, None, or tuple of ndarray and None, optionalA location into which the result is stored. If provided, it must have
a shape that the inputs broadcast to. If not provided or None,
a freshly-allocated array is returned. A tuple (possible only as a
keyword argument) must have length equal to the number of outputs.
wherearray_like, optionalThis condition is broadcast over the input. At locations where the
condition is True, the out array will be set to the ufunc result.
Elsewhere, the out array will retain its original value.
Note that if an uninitialized out array is created via the default
out=None, locations within it where the condition is False will
remain uninitialized.
**kwargsFor other keyword-only arguments, see the
ufunc docs.
Returns:
yndarrayThe corresponding number of 1-bits in the input.
Returns uint8 for all integer types
This is a scalar if x is a scalar.
References
[1]
https://graphics.stanford.edu/~seander/bithacks.html#CountBitsSetParallel
[2]
Wikipedia, “Hamming weight”,
https://en.wikipedia.org/wiki/Hamming_weight
[3]
http://aggregate.ee.engr.uky.edu/MAGIC/#Population%20Count%20(Ones%20Count)
Examples
>>> import numpy as np
>>> np.bitwise_count(1023)
10
>>> a = np.array([2**i - 1 for i in range(16)])
>>> np.bitwise_count(a)
array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15],
dtype=uint8)
    '''
    
    resp = prompt_gpt(get_gpt_complete_prompt(func_name=func_name, lib=lib, version=version, description=description))
    print(resp)