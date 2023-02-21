import numpy as np
import cv2
from matplotlib.image import imread
from matplotlib import pyplot as plt
import basicfuncs

def normalization(img):
    m,n,c = img.shape
    norm_img=np.zeros(img.shape,dtype='uint8')
    print(norm_img.shape)
    for k in range(c):
        max_c=np.max(img[:,:,k])
        min_c=np.min(img[:,:,k])
        for i in range(m):
            for j in range(n):
                norm_img[i,j,k]=((img[i,j,k]-min_c)/(max_c-min_c))*255
    return norm_img


def normalization_eq(img):
    m,n,c = img.shape
    norm_img=np.zeros(img.shape,dtype='uint8')
    print(norm_img.shape)
    mean= basicfuncs.get_mean(img)
    stddev= basicfuncs.get_stdev(img)
    for k in range(c):
        mean_c= mean[k]
        stddev_c=stddev[k]
        for i in range(m):
            for j in range(n):
                norm_img[i,j,k]=(img[i,j,k]-mean_c)/stddev_c
           
    return norm_img


