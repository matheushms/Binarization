# -----------------------------------------------------------------------------
# Autor: Matheus Henrique Marques da Silva
# RA: 252509
# Universidade Estadual de Campinas - Unicamp
# Ano: 2023
# -----------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
from utils import open_image, open_pgm, local_analysis

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
    
    def calculate_mean_hist(hist, bins, density = False):
        if not density:
            return np.sum(hist*bins)/len(bins)
        
        return np.sum(hist*bins)
    
    def calculate_var_hist(hist, bins, mean=None):
        if mean==None:
            mean = calculate_mean_hist(hist, bins)
        return np.sum((bins - mean) ** 2 * hist)
    
    n = 0
    thr = 0
    density = True
    hist, bins = np.histogram(img, bins=list(range(257)),range = (0,256), density=density)
    #hist, bins = np.histogram(np.arange(4), bins=list(range(5)),range=(0,4), density=density)
    bins = bins[:-1]
    mean_t = calculate_mean_hist(hist, bins, density)
    var_t = calculate_var_hist(hist, bins, mean_t)

    for i in range(1,len(bins)):
        w1 = np.sum(hist[:i])
        w2 = 1 - w1
        mean_s = calculate_mean_hist(hist[:i], bins[:i],density)
        mean_1 = mean_s / w1
        mean_2 = (mean_t - mean_s)/ (w2 + 10 ** (-20))

        var_b = w1*w2*(mean_1*mean_2)**2
        
        n_T = var_b / var_t

        if n_T > n:
            n = n_T
            thr = i
    print(thr)
    return img > thr




def bernsen(image, window_size = 3):
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
    def func(window):
        zmin = np.min(window)
        zmax = np.max(window)
        t = (zmin + zmax)/2
        return t
    
    return local_analysis(image, {'func':func, 'args':[]}, window_size, padding_type = 'ZEROS', pad_shape = None)

def niblack(image, window_size = 15, k=-0.2, padding_type = 'ZEROS', pad_shape = None):
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
    def func(window, k):
        mean = np.mean(window)
        std = np.std(window)
        t = mean + k*std
        return t
    
    return local_analysis(image,  {'func':func, 'args':[k]}, window_size, padding_type = 'ZEROS', pad_shape = None)



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
    img = open_pgm("images/monarch.pgm")
    #result_img = global_thresholding(img,200)
    result_img = otsu(img)
    #result_img = bernsen(img, window_size=5)
    result_img = niblack(img)
    hist, bins = np.histogram(img, bins=list(range(257)),range = (0,256))
    bins = bins[:-1]
    #hist,bins = np.histogram(np.array([1,1,2,3,3,0]), bins = np.arange(5))

    plt.plot(hist)
    plt.show()
    plt.imshow(result_img, cmap='gray')
    # plt.imshow(result_img, cmap='gray')
    plt.show()

    