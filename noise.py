import numpy as np
import random
import cv2
from matplotlib import pyplot as plt
# %matplotlib inline
import os


def rgb2gray(rgb):

    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b

    return gray

def bgr2gray(rgb):

    r, g, b = rgb[:,:,2], rgb[:,:,1], rgb[:,:,0]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b

    return gray



def sap(image, probability):

    '''
    Assign zeros and ones(salt and pepper) to some 
    random pixels with specific probability
    '''
    #create an empty array with the same shape to carry the output
    noisy_img = np.zeros(image.shape,np.uint8)  
    
    black = 0
    
    #8 for 8-bits
    white = 2 ** 8 -1
    
    #top of probability
    threshold = 1 - probability 
    
    # for row, column in enumerate(np.subtract(image.shape,(1,1))):

    for row in range(image.shape[0]):
        for column in range(image.shape[1]):
            
            #generate random number between 0 and 1
            rand = random.random()

            #assign zero(black-pepper) if the number is less that the noise probability(minimum)
            if rand < probability:
                noisy_img[row][column] = black

            #assign one(white-salt) if the number is more than the thresold probability(maximum)
            elif rand > threshold:
                noisy_img[row][column] = white

            #keep the pixel's original value if the number is within the accepted range
            else:
                noisy_img[row][column] = image[row][column]
            
    return noisy_img




def gauss(image, variance):
    '''
    Adds a normally(Gaussian) distributed noise to some image
    '''
    
    #centered bell-shaped distribuation
    mean = 0
    
    #sqrt(variance)
    sigma = variance ** 0.5
    
    #PDF of mean and segma, creates random number with a normally distributed probability
    gaussian_noise = np.random.normal(mean, sigma, image.shape)
    
    #create a copy with the same size to carry the noise
    noisy_img = np.zeros(image.shape, np.float32)
    
    #add the noise to the original image
    noisy_img = image + gaussian_noise
    
    return noisy_img


def uniform(image, snr):
    
    '''
    Adds a uniformally distributed noise to some image
    '''
    #Create the noise(uniformally distributed between 0 and 255)
    noise = np.random.uniform(0, 255, size=image.shape)  
    
    #create a copy with the same size to carry the noise
    noisy_img = np.zeros(image.shape, np.float32)

    #add the noise to the original image with a signal to noise ratio(to keep within range)
    noisy_img = (image * snr + noise * (1 - snr)).astype(int)
    
    print((np.amax(noisy_img)))
    
    return noisy_img


