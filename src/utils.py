# -----------------------------------------------------------------------------
# Autor: Matheus Henrique Marques da Silva
# RA: 252509
# Universidade Estadual de Campinas - Unicamp
# Ano: 2023
# -----------------------------------------------------------------------------

from PIL import Image
import numpy as np
import os

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
    
if __name__ == "__main__":
    img = open_image("images/baboon.png")
    hist, bins = np.histogram(img, bins=list(range(256)), range=(0,255))
    print(np.sum(hist))
    print(hist.shape, bins.shape)
    print(img.shape[0]*img.shape[1])
    print(calculate_mean_hist(hist, bins))
    print(calculate_var_hist(hist, bins))


