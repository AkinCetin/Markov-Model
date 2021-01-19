#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 14:29:28 2021

@author: akincetin
"""
transitionDictionary = {'ss': 0.9, 'sr': 0.1, 'rs': 0.3, 'rr': 0.7}


def ps(n):
    if n == 1:
        return 1.0

    px = transitionDictionary.get("ss") * ps(n - 1) + transitionDictionary.get("rs") * pr(n - 1)

    return px


def pr(n):
    if n == 1:
        return 0.0

    px = transitionDictionary.get("rr") * pr(n - 1) + transitionDictionary.get("sr") * ps(n - 1)

    return px


day = "s"
n = 17
if day == "s":
    print(ps(n))
elif day == "r":
    print(pr(n))
else:
    print("please select day")
