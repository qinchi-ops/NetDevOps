#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import turtle


def hexagon(t, L, layer):
    if not layer: return
    for n in range(6):
        hexagon(t, L, layer - 1)
        t.forward(L)
        (t.left if (layer % 2 == 0) else t.right)(60)

t = turtle.Turtle()
t.speed(100)


if __name__ == '__main__':
    hexagon(t, 10, 4)
