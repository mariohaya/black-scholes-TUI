#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 17:31:35 2026

@author: mario
"""

""" packages """
import math
from scipy.stats import norm

def formula(S, K, T, r, iv):
    d1 = (math.log(S/K)+(r+0.5*iv**2)*T)/(iv*math.sqrt(T))
    d2 = d1 - iv * math.sqrt(T)
    call_price = S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)
    return call_price

if __name__ == "__main__":
    S = 100
    K = 105
    T = 1
    r = 0.05
    sigma = 0.2
  
    price = formula(S, K, T, r, sigma)
    print("The call price is:", price)
