import math

def Heaviside(t):
    s = floor(t) + .5
    return (s/abs(s)+1)/2

def edge(t,a):
    return Heaviside(t - a)

def step(t,a=0,b=1):
    return min(b,max(a,(t-a)/(b-a)))
