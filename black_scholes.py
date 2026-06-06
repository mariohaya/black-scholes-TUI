#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 17:31:35 2026

@author: mario
"""

""" packages """
import yfinance as yf
import pandas as pd
import numpy as np
from scipy.stats import norm
import math
from datetime import datetime, timezone

def formula(S, K, T, r, iv, option_type="call"):
    d1 = (math.log(S/K)+(r+0.5*iv**2)*T)/(iv*math.sqrt(T))
    d2 = d1 - iv * math.sqrt(T)
    call_price = S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)
    return call_price

if __name__ == "__main__":
    S = 100      # stock price
    K = 105      # strike
    T = 1        # time to maturity (years)
    r = 0.05     # risk-free rate
    sigma = 0.2  # volatility

    price = formula(S, K, T, r, sigma)
    print("Call Price:", price)
    
def greeks(S, K, T, r, iv):
    delta = norm.cdf(d1) -1
    gamma = pdf_d1 / (S * iv * math.sqrt(T))
    vega = S * pdf_d1 * math.sqrt(T)
