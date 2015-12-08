#! /usr/bin/env python3.4
#
#########################
#      $Author: ee364f03 $
#      $Date: 2015-11-23 02:32:41 -0500 (Mon, 23 Nov 2015) $
#      $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F15/students/ee364f03/Lab11/MoreHomography.py $
#      $Revision: 83522 $
#
#########################


import string
import re
import copy
import math
from pprint import pprint as pp
import numpy as np
import scipy
from scipy import interpolate
from PIL import Image
from scipy.misc import *
from enum import Enum
import os
from Homography import *


class Effect(Enum):
    rotate90 = 1
    rotate180 = 2
    rotate270 = 3
    flipHorizontally = 4
    flipVertically = 5
    transpose = 6


class AdvancedTransformation(ColorTransformation):
    def __init__(self, sourceImage, v, h1, h2):
        ColorTransformation.__init__(self, sourceImage)
        if not sourceImage.ndim == 3:
            raise ValueError("Must have 3 dimensions")
        if not sourceImage.shape[1] % 2 == 0:
            raise ValueError("Number of columns must be even")
        self.v = v
        self.h1 = h1
        self.h2 = h2

    def applyEffectV(self):
        return 1

    def applyEffectA(self):
        return 1


if __name__ == '__main__':
    print("In main")


    #source[...,0]
