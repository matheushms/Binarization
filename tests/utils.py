import os
import sys
import numpy as np
# Get the absolute path to the parent directory of the current file
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))

# Add the parent directory to the Python module search path
sys.path.insert(0, parent_dir)
from src.utils import open_pgm
import cv2

def test_an_image(file_path, output_dir, prefix="",sufix="", func=None):
    os.makedirs(output_dir,exist_ok=True)
    args = func["args"]
    func = func["func"]
    
    img = open_pgm(file_path)
    result_img, str_result = func(img, *args)
    result_img = result_img.astype(np.uint8)*255
    filename = os.path.basename(file_path)
    filename = os.path.splitext(filename)[0]
    num_px_b = np.sum(result_img==0)
    fp = int(num_px_b *100 / (result_img.shape[0] * result_img.shape[1]))

    out_file_path = os.path.join(output_dir, prefix + filename + f"_fp{fp}_{str_result}_"+ sufix)+".png"
    cv2.imwrite(out_file_path, result_img)