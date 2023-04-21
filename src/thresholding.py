# -----------------------------------------------------------------------------
# Autor: Matheus Henrique Marques da Silva
# RA: 252509
# Universidade Estadual de Campinas - Unicamp
# Ano: 2023
# -----------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
from utils import open_image

def global_thresholding(img, thr):
    """
    Extracts a specific bit-plane from a given grayscale image.

    Parameters
    ----------
    img : np.ndarray
        Input image as a NumPy array of shape and data type uint8.
    thr : int
        The threshould of global method.
    Returns
    -------
    np.ndarray
        Binarized image.

    """
    return (img > thr)

def otsu(img):
    """
    Extracts a specific bit-plane from a given grayscale image.

    Parameters
    ----------
    img : np.ndarray
        Input image as a NumPy array of shape and data type uint8.
    thr : int
        The threshould of global method.
    Returns
    -------
    np.ndarray
        Binarized image.
        
    """
    
    def calculate_mean_hist(hist, bins):
        return hist*bins/len(bins)
    
    n = 0
    thr = 0
    hist, bins = np.histogram(img, bins=list(range(256)))
    
    for i in range(255):
        pass

    return img > thr

def bernsen(img):
    """
    Extracts a specific bit-plane from a given grayscale image.

    Parameters
    ----------
    img : np.ndarray
        Input image as a NumPy array of shape and data type uint8.
    thr : int
        The threshould of global method.
    Returns
    -------
    np.ndarray
        Binarized image.
        
    """
    pass

def niblack(img, k):
    """
    Extracts a specific bit-plane from a given grayscale image.

    Parameters
    ----------
    img : np.ndarray
        Input image as a NumPy array of shape and data type uint8.
    thr : int
        The threshould of global method.
    Returns
    -------
    np.ndarray
        Binarized image.
        
    """
    pass

def sauvola(img, n):
    """
    Extracts a specific bit-plane from a given grayscale image.

    Parameters
    ----------
    img : np.ndarray
        Input image as a NumPy array of shape and data type uint8.
    thr : int
        The threshould of global method.
    Returns
    -------
    np.ndarray
        Binarized image.
        
    """
    pass

def phansalskar(img, k, R, p, q):
    """
    Extracts a specific bit-plane from a given grayscale image.

    Parameters
    ----------
    img : np.ndarray
        Input image as a NumPy array of shape and data type uint8.
    thr : int
        The threshould of global method.
    Returns
    -------
    np.ndarray
        Binarized image.
        
    """
    pass

def contrast_thresholding(img):
    """
    Extracts a specific bit-plane from a given grayscale image.

    Parameters
    ----------
    img : np.ndarray
        Input image as a NumPy array of shape and data type uint8.
    thr : int
        The threshould of global method.
    Returns
    -------
    np.ndarray
        Binarized image.
        
    """
    pass

def mean_method(img, C):
    """
    Extracts a specific bit-plane from a given grayscale image.

    Parameters
    ----------
    img : np.ndarray
        Input image as a NumPy array of shape and data type uint8.
    thr : int
        The threshould of global method.
    Returns
    -------
    np.ndarray
        Binarized image.
        
    """
    pass

def median_method(img):
    """
    Extracts a specific bit-plane from a given grayscale image.

    Parameters
    ----------
    img : np.ndarray
        Input image as a NumPy array of shape and data type uint8.
    thr : int
        The threshould of global method.
    Returns
    -------
    np.ndarray
        Binarized image.
        
    """
    pass

if __name__ == "__main__":
    img = open_image("images/baboon.png")

    result_img = global_thresholding(img,200)
    result_img = global_thresholding(img,200)
    hist, bins = np.histogram(img, bins=list(range(256)))
    print(len(bins))
    plt.plot(hist)
    # plt.imshow(result_img, cmap='gray')
    plt.show()