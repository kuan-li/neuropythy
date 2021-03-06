####################################################################################################
# neuropythy/test/optimize.py
# Code for testing the neuropythy.optimize package.

import os, gzip, types, six, abc, pimms
import numpy                 as np
import scipy                 as sp
import scipy.sparse          as sps
import scipy.optimize        as spopt
import pyrsistent            as pyr

import neuropythy.optimize   as opt

sqrt2_2 = np.sqrt(2.0)/2.0
tiny_mesh = {'coords': np.array([[0,0], [1,0], [-sqrt2_2, sqrt2_2], [-sqrt2_2, -sqrt2_2]]),
             'faces':  np.array([[0,1,2], [0,2,3], [0,3,1]])}
mesh = {'coords': np.array([[ 1.0000,  0.0000], [ 0.9888,  0.1490], [ 0.9556,  0.2948],
                            [ 0.9010,  0.4339], [ 0.8262,  0.5633], [ 0.7331,  0.6802],
                            [ 0.6235,  0.7818], [ 0.5000,  0.8660], [ 0.3653,  0.9309],
                            [ 0.2225,  0.9749], [ 0.0747,  0.9972], [-0.0747,  0.9972],
                            [-0.2225,  0.9749], [-0.3653,  0.9309], [-0.5000,  0.8660],
                            [-0.6235,  0.7818], [-0.7331,  0.6802], [-0.8262,  0.5633],
                            [-0.9010,  0.4339], [-0.9556,  0.2948], [-0.9888,  0.1490],
                            [-1.0000,  0.0000], [-0.9888, -0.1490], [-0.9556, -0.2948],
                            [-0.9010, -0.4339], [-0.8262, -0.5633], [-0.7331, -0.6802],
                            [-0.6235, -0.7818], [-0.5000, -0.8660], [-0.3653, -0.9309],
                            [-0.2225, -0.9749], [-0.0747, -0.9972], [ 0.0747, -0.9972],
                            [ 0.2225, -0.9749], [ 0.3653, -0.9309], [ 0.5000, -0.8660],
                            [ 0.6235, -0.7818], [ 0.7331, -0.6802], [ 0.8262, -0.5633],
                            [ 0.9010, -0.4339], [ 0.9556, -0.2948], [ 0.9888, -0.1490],
                            [-0.3968, -0.3165], [-0.2859,  0.4194], [-0.5921,  0.0444],
                            [-0.6746, -0.2648], [-0.4082, -0.5988], [ 0.1496, -0.4850],
                            [-0.2136,  0.6925], [-0.5666,  0.4519], [ 0.4396,  0.2538],
                            [-0.1028, -0.6819], [ 0.4082, -0.5988], [ 0.1756,  0.5694],
                            [ 0.4929,  0.5313], [ 0.5789, -0.1321], [ 0.7065,  0.1613],
                            [ 0.0000,  0.0000]]),
        'faces':  np.array([[  45,   26,   46], [  26,   45,   25], [  24,   45,   23],
                            [  24,   25,   45], [  33,   51,   32], [  51,   30,   31],
                            [  46,   42,   45], [  28,   46,   27], [  49,   15,   16],
                            [  46,   26,   27], [  21,   22,   44], [  20,   44,   19],
                            [  19,   44,   49], [  12,   13,   48], [  57,   42,   47],
                            [  22,   23,   45], [   8,   53,    7], [  49,   18,   19],
                            [  49,   16,   17], [  42,   44,   45], [  43,   48,   49],
                            [  48,   14,   49], [  21,   44,   20], [  51,   29,   30],
                            [  28,   29,   46], [  14,   15,   49], [  22,   45,   44],
                            [  14,   48,   13], [  57,   44,   42], [  47,   51,   33],
                            [  52,   33,   34], [  55,   57,   47], [  35,   36,   52],
                            [  50,   55,   56], [  55,   52,   38], [  35,   52,   34],
                            [   0,   56,   55], [  52,   47,   33], [  40,   41,   55],
                            [  53,   50,   54], [  56,    0,    1], [  50,   56,   54],
                            [  43,   53,   48], [  41,    0,   55], [   7,   54,    6],
                            [  46,   51,   42], [  55,   50,   57], [   1,    2,   56],
                            [  18,   49,   17], [   8,    9,   53], [   9,   10,   53],
                            [  10,   48,   53], [  57,   53,   43], [  39,   40,   55],
                            [  11,   12,   48], [  10,   11,   48], [   5,    6,   54],
                            [  56,    4,   54], [  36,   37,   52], [  42,   51,   47],
                            [   7,   53,   54], [  54,    4,    5], [  52,   55,   47],
                            [  57,   43,   44], [  32,   51,   31], [  56,    3,    4],
                            [  56,    2,    3], [  44,   43,   49], [  38,   52,   37],
                            [  46,   29,   51], [  53,   57,   50], [  55,   38,   39]])}
mesh_face_areas = np.array([0.0650852, 0.0227693, 0.0203633, 0.0209682, 0.0252780, 0.0229886, 
                            0.0395070, 0.0203633, 0.0209682, 0.0209682, 0.0306438, 0.0306438, 
                            0.0772443, 0.0203633, 0.1199090, 0.0209682, 0.0304909, 0.0227693, 
                            0.0203633, 0.0450694, 0.0395070, 0.0650852, 0.0301482, 0.0235642, 
                            0.0209682, 0.0227693, 0.0533419, 0.0209682, 0.1024960, 0.0689997, 
                            0.0227693, 0.1305020, 0.0203633, 0.0450694, 0.0945041, 0.0209682, 
                            0.0533419, 0.0592066, 0.0301482, 0.0450376, 0.0209682, 0.0395070, 
                            0.0576115, 0.0306438, 0.0209682, 0.0435943, 0.1024960, 0.0203633, 
                            0.0209682, 0.0299935, 0.0304909, 0.0770522, 0.1182260, 0.0306438, 
                            0.0209682, 0.0227693, 0.0203633, 0.0650852, 0.0209682, 0.0750569,
                            0.0532468, 0.0209682, 0.0700543, 0.1178150, 0.0235642, 0.0227693, 
                            0.0209682, 0.0575997, 0.0227693, 0.0489386, 0.1028530, 0.0321196])
