import math

def luas_kubus(sisi):
    return 6 * sisi ** 2

def luas_balok(p, l, t):
    return 2 * (p * l + p * t + l * t)

def luas_bola(r):
    return 4 * math.pi * r ** 2

def luas_tabung(r, t):
    return 2 * math.pi * r * (r + t)

def luas_kerucut(r, s):
    return math.pi * r * (r + s)