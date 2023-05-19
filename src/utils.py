# -----------------------------------------------------------------------------
# Autor: Matheus Henrique Marques da Silva
# RA: 252509
# Universidade Estadual de Campinas - Unicamp
# Ano: 2023
# -----------------------------------------------------------------------------

from PIL import Image
import numpy as np
import os
from os import listdir
from os.path import isfile, join
import matplotlib
matplotlib.use('TkAgg')
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


def process_folder(dir_path, out_dir_path, func={'func':None, 'args':None}, ext_out = ".png"):
    func_args = func['args']
    func = func['func']
    all_files_path = [f for f in listdir(dir_path) if isfile(join(dir_path, f))]

    os.makedirs(out_dir_path, exist_ok=True)

    for file_path in all_files_path:
        file_path = os.path.join(dir_path,file_path)
        img = open_pgm(file_path)

        result_img, str_result = func(img, *func_args)
        result_img = result_img.astype(np.uint8)*255

        num_px_b = np.sum(result_img==0)
        fp = int(num_px_b *100 / (result_img.shape[0] * result_img.shape[1]))

        filename = os.path.basename(file_path)
        filename = os.path.splitext(filename)[0]
        out_file_path = os.path.join(out_dir_path, filename + f"_fp{fp}_{str_result}")+ext_out
        cv2.imwrite(out_file_path, result_img)

def convert_to_png(dir_path, out_dir_path,  ext_out = ".png"):
    all_files_path = [f for f in listdir(dir_path) if isfile(join(dir_path, f))]

    os.makedirs(out_dir_path, exist_ok=True)

    for file_path in all_files_path:
        file_path = os.path.join(dir_path,file_path)
        img = open_pgm(file_path)
        filename = os.path.basename(file_path)
        filename = os.path.splitext(filename)[0]
        out_file_path = os.path.join(out_dir_path, filename)+ext_out
        cv2.imwrite(out_file_path, img)

def histogram_plot(img, out_path):
    hist, bins = np.histogram(img, bins=list(range(257)),range = (0,256))
    plt.figure()
    plt.title("Grayscale Histogram")
    plt.xlabel("Bins")
    plt.ylabel("# of Pixels")
    plt.plot(hist)
    plt.xlim([0, 256])
    plt.savefig(out_path)



def generate_histograms(dir_path, out_dir_path,  ext_out = ".png"):
    all_files_path = [f for f in listdir(dir_path) if isfile(join(dir_path, f))]

    os.makedirs(out_dir_path, exist_ok=True)

    for file_path in all_files_path:
        file_path = os.path.join(dir_path,file_path)
        img = open_pgm(file_path)
        
        filename = "histo_"+os.path.basename(file_path)
        filename = os.path.splitext(filename)[0]
        out_file_path = os.path.join(out_dir_path, filename)+ext_out
        histogram_plot(img,out_file_path)



import matplotlib.pyplot as plt
if __name__ == "__main__":
    # convert_to_png("images", "images_png",  ext_out = ".png")
    generate_histograms("images", "images_png",  ext_out = ".png")
    # img = open_pgm("images/baboon.pgm")
    img = cv2.imread('images/retina.pgm', -1)
    histogram_plot(img, "hist.png")
    plt.imshow(img)
    plt.show()
    hist, bins = np.histogram(img, bins=list(range(256)), range=(0,255))
    print(np.sum(hist))
    print(hist.shape, bins.shape)
    print(img.shape[0]*img.shape[1])
    print(calculate_mean_hist(hist, bins))
    print(calculate_var_hist(hist, bins))


