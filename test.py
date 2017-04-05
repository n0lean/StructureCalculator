from MplMainWindow import *
from PyQt4.QtGui import *
import sys
import cv2
import numpy as np
from beam import *
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from frame_type import *
import matplotlib
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas



t = np.arange(0.0, 3.0, 0.01)
s = np.sin(2 * np.pi * t)

