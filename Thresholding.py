import numpy as np

def Threshold(image,High,Low , Weak):
    ResultantImage = np.zeros(image.shape)
    HighNumbersRow, HighNumbersColumn = np.where(image >= High)
    LowNumbersRow, LowNumbersColumn = np.where((image <= High) & (image >= Low))
    ResultantImage[HighNumbersRow, HighNumbersColumn] = 255
    ResultantImage[LowNumbersRow, LowNumbersColumn] =Weak 
    return ResultantImage  

def local_thresh(input_img,threshold):

    h, w = input_img.shape

    S = w/8
    s2 = S/2
    

    #integral img
    int_img = np.zeros_like(input_img, dtype=np.uint32)
    for col in range(w):
        for row in range(h):
            int_img[row,col] = input_img[0:row,0:col].sum()

    #output img
    out_img = np.zeros_like(input_img)    

    for col in range(w):
        for row in range(h):
            #SxS region
            y0 = int(max(row-s2, 0))
            y1 = int(min(row+s2, h-1))
            x0 = int(max(col-s2, 0))
            x1 = int(min(col+s2, w-1))

            count = int((y1-y0)*(x1-x0))

            sum_ = int_img[y1, x1]-int_img[y0, x1]-int_img[y1, x0]+int_img[y0, x0]

            if input_img[row, col]*count < sum_*(100.-threshold)/100.:
                out_img[row,col] = 0
            else:
                out_img[row,col] = 255

    return out_img
  