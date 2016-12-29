from __future__ import division, print_function
import sympy
import numpy
import scipy

class christoffel2:
    def __init__(self, metric):
        
        #   takes a Sympy matrix and makes the metric g_{ab}
        self.metric = metric
        self.metric_dim = numpy.shape(self.metric)
        
        #   raise an exception if the metric dimensions are not equal
        if not self.metric_dim[0]==self.metric_dim[1]:
            raise ValueError('Metric dimensions must be equal')
        
        #   takes the metric and calculates the inverse metric g^{ab}
        self.metric_inverse = self.metric.inv()
        

    def calculate(self, symbol_list, idx1, idx2, idx3):
    
        #   calculate one Christoffel symbol only - \Gamma^{idx1}_{idx2 idx3}
        self.symbol_list = symbol_list
        
        self.idx1 = idx1
        self.idx2 = idx2
        self.idx3 = idx3

        self.i_idx1 = self.symbol_list.index(idx1)
        self.i_idx2 = self.symbol_list.index(idx2)
        self.i_idx3 = self.symbol_list.index(idx3)
        
        out = 0
        
        #   now calculate the desired christoffel symbol
        for i in range(0, len(self.symbol_list)):
            out = out + (0.5*(self.metric_inverse[i, self.i_idx1]*(sympy.diff(self.metric[i, self.i_idx2], self.idx3)+sympy.diff(self.metric[i, self.i_idx3], self.idx2)-sympy.diff(self.metric[self.i_idx2, self.i_idx3], self.symbol_list[i]))))
                       
        return out





