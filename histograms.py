import numpy as np
import cv2
from matplotlib.image import imread
from matplotlib import pyplot as plt
#draw histogram for each intenisty discrete or cont.
#takes too much time
def hist_plot(img):

    m, n = img.shape[:2]
      
    # empty list to store the count 
    # of each intensity value
    count =[]
    # empty list to store intensity 
    # value
    r = []
    # loop to traverse each intensity 
    # value
    for k in range(0, 256):
        r.append(k)
        count1 = 0
          
        # loops to traverse each pixel in 
        # the image 
        for i in range(m):
            for j in range(n):
                if img[i, j]== k:
                    count1+= 1
        count.append(count1)
          
    return (r, count)

#another method to draw histogram for each intenisty discrete or cont.
def Histo(image,bins):
    H = np.zeros(shape = (bins,1))
    s = image.shape
    for i in range (s[0]):
        for j in range(s[1]):
            k=image[i,j]##get each intensity
            H[k,0]+=1
    return H


#cumulative curve
def cumulative_distrubution(count):
    hist= iter(count)
    b = [next(hist)]
    for i in hist:
        b.append(b[-1] + i)
    
    b = np.array(b)
    curve= ((b - b.min()) * 255)/(b.max() - b.min())

    return curve

# #method to draw continuous histogram
# def con_histogram(image_input,bins):
#         # array with size of bins(intensities of image), set to zeros
#         histogram = np.zeros(bins)
        
#         # count the pixels
#         for pixel in image_input:
#             histogram[pixel] += 1
        
#         y=np.linspace(0,np.max(histogram))
        
#         return histogram

def draw_histogram(hist_1,hist_2,hist_3,bins):
    l_int=[]
    for i in range(0,bins):
        l_int.append(i)
    plt.plot(l_int,hist_1,color="blue")
    plt.plot(l_int,hist_2,color="green")
    plt.plot(l_int,hist_3,color="red")
    

    

def draw_histogram_bars(hist_1,hist_2,hist_3,bins):
    l_int=[]
    for i in range(0,bins):
        l_int.append(i)
    
    figure, axis = plt.subplots(3, 1, figsize = (35,35))
  
    # For blue channel
    axis[0].bar(l_int,hist_1.ravel(),width=5,color='Blue',edgecolor='black', align='center')
    axis[0].set_title("Blue Channel")

    # For green channel
    axis[1].bar(l_int,hist_2.ravel(),width=5,color='Green',edgecolor='black', align='center')
    axis[1].set_title("Green Channel")

    # For red channel
    axis[2].bar(l_int,hist_3.ravel(),width=5,color='Red',edgecolor='black', align='center')
    axis[2].set_title("Red Channel")

def draw_lines(hist_1,hist_2,hist_3,bins):
    l_int=[]
    for i in range(0,bins):
        l_int.append(i)
    
    figure, axis = plt.subplots(3, 1, figsize = (35, 35))

    axis[0].stem(l_int, hist_1)
    axis[0].set_title("Blue Channel")

    axis[1].stem(l_int, hist_2)
    axis[1].set_title("Green Channel")

    axis[2].stem(l_int, hist_3)
    axis[2].set_title("Red Channel")

    

def draw_cumulative(hist_1,hist_2,hist_3):
    figure, axis = plt.subplots(3, 1, figsize = (35, 35))

    curve1=cumulative_distrubution(hist_1)
    curve2=cumulative_distrubution(hist_2)
    curve3= cumulative_distrubution(hist_3)

    axis[0].plot(curve1)
    axis[0].set_title("Blue Channel")

    axis[1].plot(curve2)
    axis[1].set_title("Green Channel")

    axis[2].plot(curve3)
    axis[2].set_title("Red Channel")

def equalization(image):
        n,m,c = image.shape
        for o in range(c):
            H = Histo(image[:,:,o],256)
            x = H.reshape(1,256)
            y = np.array([])
            y=np.append(y,x[0,0])
            for i in range (255):
                k = x[0,i+1]+y[i]
                y = np.append(y,k)
            y = np.round((y/(n*m))*255)
            for i in range(n):
                for j in range (m):
                    k = image[i,j,o]
                    image[i,j,o] = y[k]

        return image
    


