import numpy as np
from ConvertToGrayscale import ConvertToGaryscale

def Convolve(Image,Gx,Gy):
    if len(Image.shape) == 3:
        Image = ConvertToGaryscale(Image)
    ImageNumberOfRows,ImageNumberOfColumns=Image.shape
    KernalNumberOfRows, KernalNumberOfColumns = Gx.shape	 
    ResultantImage = np.zeros([ImageNumberOfRows,ImageNumberOfColumns]) # The Resultant Image Shape is (rows-2,columns-2)
    for row in range(ImageNumberOfRows-KernalNumberOfRows+1):
        for column in range(ImageNumberOfColumns-KernalNumberOfColumns+1):

            if(Gy.any() == 0):
                ResultantImage[row+1,column+1]=np.sum(np.multiply(Gx,Image[row:row+KernalNumberOfRows,column:column+KernalNumberOfColumns]))  
            else: 
                PixelValueX=np.sum(np.multiply(Gx,Image[row:row+KernalNumberOfRows,column:column+KernalNumberOfColumns])) 
                PixelValueY=np.sum(np.multiply(Gy,Image[row:row+KernalNumberOfRows,column:column+KernalNumberOfColumns]))
                ResultantImage[row+1,column+1]=np.sqrt(PixelValueX**2+PixelValueY**2)

              
    return ResultantImage
 