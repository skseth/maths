# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.5
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # How Numpy stores arrays
#
# All numpy arrays are actually flat 1D arrays. This can be stored in 2 ways:
#
# - C-Contiguous (like C) - Row Major (default) - so we have rows first, then columns
# - F-Contiguous (like fortran) - Column Major
#
# Numpy has a structure called the **strided array interface**, which outlines:
#
# - dtype - the datatype (int, float etc)
# - shape - e.g (3,4)
# - strides - a tuple (x,y,..) specifying how much to skip on each axes
#
# Dimensions are numbered from 0 to n-1.
#
# When there are more than 2 dimensions - say n dimensions - then row refers to the n-2 dimension, and column to the n-1. The remaining 0-(n-3) dimensions are just used as indexes to get to a specific row-column combination.
#
# Sparse matrices are not supported, this needs scipy.

# %%
import numpy as np

# Create a sample 3x3 array of 32-bit integers
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=np.int32)

# 1. Print standard structural metadata
print(f"Data Type (dtype): {arr.dtype}")
print(f"Array Shape:       {arr.shape}")
print(f"Dimensions (ndim): {arr.ndim}")
print(f"#Elements (Size):    {arr.size}")

# 2. Print memory layout metadata
print(f"Element Size:      {arr.itemsize} bytes")
print(f"Strides:           {arr.strides}") 
# (12, 4) means jump 12 bytes for next row, 4 bytes for next column

# 3. Print complete memory and layout flags
print("\n--- Detailed Memory Flags ---")
print(arr.flags)

# %% [markdown]
# ## DType Values
#
# You can have 
#
# - int8 to int64 - i1, i2, i4, 18
# - similarly uint - u1,u2, u4,u8
# - float16-float64 - f2,f4,f8
# - complex64 and complex128 - c8, c16
# - bool_ - b
# - datetime64 - M
# - timedelta64 - m
# - str_ - U e.g. U10
# - bytes - fixed width ASCII byte sequences
# - object_ - O - stores pointers to python objects

# %%
import numpy as np

ints = np.array([1,2,3], dtype='i2')

floats = np.array([4.2,2.2,3.1], 'f2')

intFromFloats = floats.astype(ints.dtype)

complex = np.array([2+0.j, 3+0.2j], dtype='c8')

display(ints)
display(floats)
display(intFromFloats)
display(complex)

# np.sqrt(np.array([-1,0,1])) - gives error

sqroots = np.sqrt(np.array([-1,0,1], dtype='c8'))  # works fine

display(sqroots.real)


# %% [markdown]
# ## Initializing arrays

# %%
display(np.zeros((3,3), dtype='f4'))  # 3x3 array of zeros, float32

# %%
display(np.ones((2,3), dtype='c8'))  # 2x3 array of ones, float64

# %%
# 2D only - for 3D or higher, use np.diagonal() or np.diagonal(a, offset=0, axis1=0, axis2=1)

display(np.diag(np.array([1,2,3], dtype='i4')))  # 3x3 diagonal matrix with int32

# %%
# A 3D array of shape (2, 3, 3)
array_3d = np.ones((2, 3, 3)) # 3D array

# Extracts diagonals across the last two axes (axis1=-2, axis2=-1)
print(np.diagonal(array_3d, axis1=-2, axis2=-1))

# %%
# 1D - use meshgrid or mgrid for 2D or higher
display(np.arange(10, 20, 2))  # 10 to 20 with step of 2

# %%
# floating step size makes this float, but use with care, or use linspace instead

display(np.arange(10, 20, 0.5))  # 10 to 20 with step of 2


# %%
display(np.linspace(0, 1, 5, dtype=np.float32))  # 5 evenly spaced numbers from 0 to 1

# %%
display(np.logspace(0, 100, num=5, base=10.0, dtype=np.float64))  # 5 numbers spaced evenly on a log scale from 10^0 to 10^1000

# %%
display(np.meshgrid(np.arange(3), np.arange(4)))  # 2D grid of coordinates

# %%

# 1. mgrid (Fills everything out)
m_grid = np.mgrid[0:5:2, 0:3]
print(m_grid[0].shape)  # Output: (3, 3) -> Fully broadcasted
print(m_grid[1].shape)  # Output: (3, 3) -> Fully broadcasted


# %%
# 2. ogrid (Saves memory by keeping it minimal)
o_grid = np.ogrid[0:5:2, 0:3]
print(o_grid[0].shape)  # Output: (3, 1) -> Just a 1D column
print(o_grid[1].shape)  # Output: (1, 3) -> Just a 1D row

# %%
np.fromfunction(lambda i, j: i + j, (3, 3), dtype=int)  # 3x3 array where each element is the sum of its indices

# %%
np.random.rand(3, 3)  # 3x3 array of random floats in [0.0, 1.0)

# %%
# Better recommended method
# Initialize the modern generator
rng = np.random.default_rng(seed=42)

# Generate a single integer from 0 to 9 (10 is exclusive)
single_int = rng.integers(low=0, high=10)

# Generate a 1D array of 5 integers between 10 and 50
array_1d = rng.integers(low=10, high=51, size=5)

# Generate a 2x3 matrix of integers
matrix_2d = rng.integers(low=0, high=100, size=(2, 3))

random_floats = rng.random(size=(2, 3))  # 2x3 matrix of random floats in [0.0, 1.0)


display(single_int, array_1d, matrix_2d, random_floats)

# %%

# Uniform floats between a custom range, e.g., -5.0 to 5.0
custom_uniform = rng.uniform(low=-5.0, high=5.0, size=5)

# Standard Normal (mean=0, standard deviation=1)
std_normal = rng.standard_normal(size=5)

# Custom Normal (mean=10, standard deviation=2)
custom_normal = rng.normal(loc=10, scale=2, size=5)

# 10 trials, 50% success chance (like flipping 10 coins), repeated 5 times
binomial_samples = rng.binomial(n=10, p=0.5, size=5)

# Lam (lambda) is the known average rate of occurrences (e.g., 3 website hits/minute)
poisson_samples = rng.poisson(lam=3, size=5)

# Scale is the inverse of the rate parameter (1/lambda)
exponential_samples = rng.exponential(scale=2.0, size=5)

display(custom_uniform, std_normal, custom_normal, binomial_samples, poisson_samples, exponential_samples)

# %%
items = ['apple', 'banana', 'cherry', 'date']

# Randomly select 2 items with replacement (items can repeat)
choices = rng.choice(items, size=2, replace=True)

# Randomly shuffle an array in-place
arr = np.array([1, 2, 3, 4, 5])
rng.shuffle(arr)

display(choices, arr)

# %% [markdown]
# # Reshaping and Manipulating Arrays
#

# %%
# Reshape existing array
data = np.array([[1, 2],[3, 4]])

newdata = np.reshape(data, (4,1))  # Reshape to 4 rows

anothernewdata = np.ravel(data)  # Flatten the array

newdata[0][0] = 98  # Modify the reshaped array
data[0][1] = 97
anothernewdata[2] = 96  # Modify the flattened array

display(data)
display(newdata)


display(anothernewdata)



# cannot reshape to (5, 1) because the total number of elements (4) does not match the new shape (5)
# display(np.reshape(data, (5, 1)))  # Reshape to 4 rows and 1 column


# %%
data = np.array([[1, 2],[3, 4]])

newdata = data.flatten()
newdata[0] = 99  # Modify the flattened array

display(data)
display(newdata)

# %%
data = np.arange(0,5)
column = data[:, np.newaxis]  # Convert to a column vector
column[0] = 99

# expand_dims can be used to add a new axis at a specified position, similar to np.newaxis. 
# For example, np.expand_dims(data, axis=1) would convert the 1D array data into a 2D column vector.

excolumn = np.expand_dims(data, axis=1)
excolumn[1][0] = 88
exrow = np.expand_dims(data, axis=0)
exrow[0][2] = 77

display(data)
display(column)
display(excolumn)
display(exrow)

display(data[2:4, np.newaxis])

# %%
## hstack, vstack, concatenate

data = np.arange(3)

display(np.vstack((data, data, data)))
display(np.hstack((data, data, data)))

coldata = data[:, np.newaxis]  # Convert to a column vector
display(np.vstack((coldata, coldata, coldata)))
display(np.hstack((coldata, coldata, coldata)))

# concatenating multiple row along row axis (0), results in just getting joined up
xdata = np.concatenate((data, data, data), axis=0)  # Concatenate along the first axis (rows)

# concatenating rows along the column axis (1) gives a better output
ydata = np.concatenate((coldata, coldata, coldata), axis=1)  # Concatenate along the second axis (columns)
display(xdata)
display(ydata)



# %% [markdown]
# ## Vectorized Operations

# %% [markdown]
# Numpy performs vectorized operations between arrays. This is where it's real power comes in, eliminating loops and leveraging the memory layout to minimize memory fetches.
#
# Usually binary operations may involve two arrays of the same shape. **Broadcasting** is the approach by which an array may (if it meets the criteria), be adjusted to match the shape of another during an operation. 
#
#

# %%
## Broadcasting example

one_row = np.arange(1,4)
one_col = one_row[:, np.newaxis]


display(one_row, one_col)

d = np.arange(11,14)
three_array = np.vstack((d, d+10, d+20))
display(three_array)

# broadcast scalars
display(three_array + 2)


# broadcast rows
display(three_array + one_row)

# broadcast columns
display(three_array + one_col)



# %%
# Arithmetric ops

x = np.array([[1,2],[3,4]])
y = x + 4

display(x * 2)


display(x + y)
display(y - x)
display(x * y)
display(y / x)
display(y // x)
display(y ** x)


# %%
# Functions

# Trig - sin, cos, tan, arccos, arcsin, arctan

data = np.pi / np.arange(1,5)

display(data)
display(np.round(np.cos(data), decimals=4))
display(np.arccos(np.cos(data)))

# Hyperbolic
data = np.pi / np.arange(1,5)

display(np.round(np.cosh(data), decimals=4))

# exp, log, log2, log10, sqrt

display(np.sqrt(data))

