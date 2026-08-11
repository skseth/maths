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
# # Linear Equation Systems

# %%
from scipy import linalg as la
from scipy import optimize
import sympy
sympy.init_printing()
import numpy as np
import matplotlib.pyplot as plt

# %%
A = sympy.Matrix([[2,3], [5, 4]])
b = sympy.Matrix([4,3])
display(A.rank())
display(A.condition_number())
display(A.norm())

# %%
A = np.array([[2, 3], [5, 4]])
b = np.array([4, 3])
display(np.linalg.matrix_rank(A))
display(np.linalg.cond(A))
display(np.linalg.norm(A))


# %% [markdown]
# # LU Factorization

# %%
A = sympy.Matrix([[2,3], [5, 4]])
b = sympy.Matrix([4,3])
L, U, _ = A.LUdecomposition()
display(L)
display(U)  
display(L*U)
display(A.solve(b))



# %%
A = np.array([[2, 3], [5, 4]])
b = np.array([4, 3])
P, L, U = la.lu(A)
display(L)
display(U)
display(P)
P.dot(L.dot(U))
la.solve(A, b)

