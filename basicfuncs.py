import numpy as np
import cv2
from matplotlib.image import imread
from matplotlib import pyplot as plt

 

def get_mean(img):
    l_channels=[]
    l_means=[]
    m,n,c=img.shape
    #to get mean for each channel
    for k in range(c):
        sum_val=0
        for i in range(m):
            for j in range(n):
                sum_val+=img[i, j,k]
        l_channels.append(sum_val)
    for channel in l_channels: 
        mean= channel/(m*n)
        l_means.append(mean)
        
    return l_means

def get_stdev(img): 
    m,n,c=img.shape
    l_sums=[]
    l_dev=[]
    #to get standard deviation for each channel
    for k in range(c):
        mean= get_mean(img)[k]
        sum_val=0
        for i in range(m):
            for j in range(n):
                sum_val+=((img[i,j,k]-mean)**2)
        l_sums.append(sum_val)
        
    for l_sum in l_sums:
        dev=np.sqrt(l_sum/(m*n))
        l_dev.append(dev)
        
    return l_dev

