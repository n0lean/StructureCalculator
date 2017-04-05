import cv2
import qimage2ndarray as qn
import numpy as np

def np2q(frame):
    if frame.shape[-1] == 3:
        subarray = np.dsplit(frame,3)
        frame = np.dstack((subarray[2],subarray[1],subarray[0]))
    qimage = qn.array2qimage(frame)
    return qimage