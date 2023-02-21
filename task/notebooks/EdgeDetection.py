
from matplotlib import pyplot as plt
import numpy as np
from CannyBasicFunctions import Gradient, Hysteresis, NonMaxSuppression
from Thresholding import Threshold
# from Convolution import Convolve
import import_ipynb
from filters import *
from basicfuncs_nb import *
from Convolution import *


def Sobel(image):
    SobelKernalX=np.array([[-1,0,1],
                           [-2,0,2],
                           [-1,0,1]])                           
    SobelKernalY=np.flip(SobelKernalX.transpose())
    SobelImage=Convolve(image,SobelKernalX,SobelKernalY)
    return SobelImage

def Prewitt(image):
    PerwittKernalX=np.array([[-1,0,1],
                             [-1,0,1],
                             [-1,0,1]])  
    PerwittKernalY=PerwittKernalX.transpose()
    PrewittImage=Convolve(image,PerwittKernalX,PerwittKernalY)
    return PrewittImage                        

def Roberts(image):
    RobertsKernalX=np.array([[-1,0],
                             [0,1]])
    RobertsKernalY=np.array([[0,1],
                             [-1,0]])                         
    RobertsImage=Convolve(image,RobertsKernalX,RobertsKernalY)
    return RobertsImage 
    
def Canny(image):
    Weak=50
    GaussianImage=gaussian_filter(image,1)
    Magnitude , Theta = Gradient(GaussianImage)
    Suppression=NonMaxSuppression(Magnitude,Theta)
    Thresholding=Threshold(Suppression,50,5,Weak)
    FinalImage=Hysteresis(Thresholding,Weak)  
    return FinalImage
 
