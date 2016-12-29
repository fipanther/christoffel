from __future__ import division, print_function
from christoffel import christoffel2
import sympy
from sympy.matrices import Matrix
import numpy
import scipy

r, t = sympy.symbols('r t')

metric = Matrix([[1,0],[0,r**2]])

a = christoffel2(metric)

christoffel_trt = a.calculate((r, t), t, r, t)
christoffel_ttr = a.calculate((r,t), t,t,r)
christoffel_trr = a.calculate((r,t), t,r,r)

print(christoffel_trt, christoffel_ttr, christoffel_trr)



