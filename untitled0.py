# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/143JN48KN3WI0xhT4y7UOVVdo2Sp5BRcq
"""

def f(x):
    return x**2+3*x-x

def falsePosition(x0,x1,e):
    step = 1
    condition = True
    while condition:
        x2 = x0 - (x1-x0) * f(x0)/( f(x1) - f(x0) )
        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2

        step = step + 1
        condition = abs(f(x2)) > e

x0 = input('yakam ')
x1 = input('dwam  ')
e = input('error ')

x0 = float(x0)
x1 = float(x1)
e = float(e)

    falsePosition(x0,x1,e)