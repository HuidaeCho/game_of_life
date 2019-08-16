#!/usr/bin/env python3
################################################################################
# Name:    Conway's Game of Life
# Purpose: This script plays Conway's Game of Life.
# Author:  Huidae Cho
# Since:   August 16, 2019
#
# Copyright (C) 2019, Huidae Cho <https://idea.isnew.info>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
################################################################################

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

gen = np.random.randint(2, size=(100,100))

next_gen = gen.copy()

fig, ax = plt.subplots()
plt.axis('off')
im = plt.imshow(gen, cmap='gray_r')

def init():
    return im,

def update(tick):
    global gen, next_gen
    [nrows,ncols] = gen.shape
    for i in range(nrows):
        for j in range(ncols):
            n = 0
            n += i > 0 and gen[i-1,j]
            n += i > 0 and j > 0 and gen[i-1,j-1]
            n += i > 0 and j < ncols-1 and gen[i-1,j+1]
            n += i < nrows-1 and gen[i+1,j]
            n += i < nrows-1 and j > 0 and gen[i+1,j-1]
            n += i < nrows-1 and j < ncols-1 and gen[i+1,j+1]
            n += j > 0 and gen[i,j-1]
            n += j < ncols-1 and gen[i,j+1]
            next_gen[i,j] = (gen[i,j] and (n == 2 or n == 3)) or \
                            (not gen[i,j] and n == 3)
    im.set_data(next_gen)
    tmp = gen
    gen = next_gen
    next_gen = tmp
    return im,

ani = FuncAnimation(fig, update, frames=range(10), init_func=init, blit=True)
plt.show()
