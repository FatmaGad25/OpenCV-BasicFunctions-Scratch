from matplotlib import pyplot as plt
import numpy as np
from ConvertToGrayscale import ConvertToGaryscale

def Convolve(Image,Gx,Gy):
    if len(Image.shape) == 3:
        Image = ConvertToGaryscale(Image)
    # print(len(Gx[0]))
    # print(len(Gy[0]))

    ImageNumberOfRows,ImageNumberOfColumns=Image.shape
    
    KernalNumberOfRows, KernalNumberOfColumns = Gx.shape
    PaddedHight = int((KernalNumberOfRows - 1) / 2)
    PaddedWidth = int((KernalNumberOfColumns - 1) / 2)
    PaddedImage = np.zeros((ImageNumberOfRows + (2 * PaddedHight), ImageNumberOfColumns + (2 * PaddedWidth)))

    PaddedImage[ PaddedHight : PaddedImage.shape[0] - PaddedHight,PaddedWidth : PaddedImage.shape[1] - PaddedWidth,] = Image
    ResultantImage = np.ones([ImageNumberOfRows,ImageNumberOfColumns]) 
    for row in range(ImageNumberOfRows):
        for column in range(ImageNumberOfColumns):

            if(Gy.any() == 0):
                ResultantImage[row,column]=np.sum(np.multiply(Gx,PaddedImage[row:row+KernalNumberOfRows,column:column+KernalNumberOfColumns]))  
            else: 
                PixelValueX=np.sum(np.multiply(Gx,PaddedImage[row:row+KernalNumberOfRows,column:column+KernalNumberOfColumns])) 
                PixelValueY=np.sum(np.multiply(Gy,PaddedImage[row:row+KernalNumberOfRows,column:column+KernalNumberOfColumns]))
                ResultantImage[row,column]=np.sqrt(PixelValueX**2+PixelValueY**2)

              
    return ResultantImage
