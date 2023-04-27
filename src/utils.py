# -----------------------------------------------------------------------------
# Autor: Matheus Henrique Marques da Silva
# RA: 252509
# Universidade Estadual de Campinas - Unicamp
# Ano: 2023
# -----------------------------------------------------------------------------

from PIL import Image
import numpy as np
import os
import cv2

def open_image(path):

    image = Image.open(path, mode = 'r')

    return np.asarray(image)

def save_image(path, image):
    dir_path = os.path.dirname(path)
    os.makedirs(dir_path,exist_ok=True)

    image = Image.fromarray(image)
    image = image.convert("RGB")
    image.save(path)


def calculate_mean_hist(hist, bins):
        return hist*bins/np.sum(hist)
    
def calculate_var_hist(hist, bins):
    mean = calculate_mean_hist(hist, bins)

    return ((bins - mean) ** 2) * hist / sum(hist)

def open_pgm(path):
    return cv2.imread(path, -1)

def padding(image, pad_type, pad_shape = [(1,1),(1,1)]):
    h,w = image.shape[:2]
    buffer = np.zeros((h+int(sum(pad_shape[0])), w+int(sum(pad_shape[1]))))

    if pad_type == "REFLECTION":
        pass
        
    elif pad_type == "ZEROS":
        buffer[pad_shape[0][0]:h + pad_shape[0][0], pad_shape[1][0]:w + pad_shape[1][0]] = image
 
    elif pad_type == "VALID":
        return image
    
    else:
        raise Exception("Incorrect padding type...")
    
    return buffer

def local_analysis(image, func, window_size = 3, padding_type = 'ZEROS', pad_shape = None):
    func_args = func['args']
    func = func['func']
    h, w = image.shape[:2]
    h_f, w_f = window_size, window_size

    # calculate the size of the padding
    offset_h, offset_w = int(np.floor(h_f/2)), int(np.floor(w_f/2))

    if pad_shape == None:
        pad_shape = [(offset_h,offset_h),(offset_w,offset_w)]


    # padding of the image to keep the original size
    img_pad = padding(image/255., pad_type=padding_type, pad_shape=pad_shape)

    # where the processed pixels will be stored
    buffer = np.empty((img_pad.shape[0]-offset_h*2, img_pad.shape[1]-offset_w*2))

    for r in range(0, h):

        # define the rows interval of the window
        start_r = r
        end_r = r + offset_h*2 + 1

        for c in range(0, w):
            # define the columns interval of the window
            start_c = c 
            end_c = c + offset_w*2 +1
            
            # define window
            window = img_pad[start_r:end_r, start_c:end_c]
            t = func(window, *func_args)
            # multiply the window with the filter and store the result in the buffer
            buffer[r][c] = img_pad[r+offset_h][c+offset_w] > t
            
    return buffer

import matplotlib.pyplot as plt
if __name__ == "__main__":
    # img = open_pgm("images/baboon.pgm")
    img = cv2.imread('images/retina.pgm', -1)
    plt.imshow(img)
    plt.show()
    hist, bins = np.histogram(img, bins=list(range(256)), range=(0,255))
    print(np.sum(hist))
    print(hist.shape, bins.shape)
    print(img.shape[0]*img.shape[1])
    print(calculate_mean_hist(hist, bins))
    print(calculate_var_hist(hist, bins))


