import noise
import histograms
import normalizaion
import numpy as np
import random
import cv2
from matplotlib import pyplot as plt
# %matplotlib inline
import os



image = cv2.imread('lena.jpg',0) # Only for grayscale image
path="E:/cv_tasks/our_repo/CV_Task1/apple.jpeg"
img_1=cv2.imread(path)
plt.imshow(cv2.cvtColor(img_1, cv2.COLOR_BGR2RGB))
plt.show()
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()
hist_1=histograms.Histo(img_1[:,:,0],256)
hist_2=histograms.Histo(img_1[:,:,1],256)
hist_3=histograms.Histo(img_1[:,:,2],256)

#draw histograms continuously
histograms.draw_histogram(hist_1,hist_2,hist_3,256)
plt.show()
histograms.draw_histogram_bars(hist_1,hist_2,hist_3,256)
plt.show()
histograms.draw_cumulative(hist_1,hist_2,hist_3)
plt.show()
histograms.draw_lines(hist_1,hist_2,hist_3,256)
plt.show()

equalized_image=histograms.equalization(img_1)
plt.imshow(cv2.cvtColor(equalized_image, cv2.COLOR_BGR2RGB))
plt.show()
eq_1=histograms.Histo(equalized_image[:,:,0],256)
eq_2=histograms.Histo(equalized_image[:,:,1],256)
eq_3=histograms.Histo(equalized_image[:,:,2],256)
##draw equalized image histogram
histograms.draw_histogram_bars(eq_1,eq_2,eq_3,256)
plt.show()
plt.imshow(image,cmap='gray')
plt.show()
noise_img = noise.sap(image, 0.05)
noise_img2 = noise.gauss(image, 2500)
noise_img3 = noise.uniform(image,0.8)
# noise_img4 = uniform2(image,0.8)
plt.imshow(noise_img,cmap='gray')
plt.show()
plt.close()
plt.imshow(noise_img2,cmap='gray')
plt.show()
plt.imshow(noise_img3,cmap='gray')
plt.show()