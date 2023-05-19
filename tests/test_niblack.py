# -----------------------------------------------------------------------------
# Autor: Matheus Henrique Marques da Silva
# RA: 252509
# Universidade Estadual de Campinas - Unicamp
# Ano: 2023
# -----------------------------------------------------------------------------
import os
import sys
# Get the absolute path to the parent directory of the current file
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))

# Add the parent directory to the Python module search path
sys.path.insert(0, parent_dir)
from src.thresholding import niblack
from src.utils import open_pgm, process_folder

################### TEST 2 ###################
#Parameters
window_size = 45
k=-0.5
#Input and output paths
dir_path = "images"
out_dir_path = f"output/test_niblack/w{window_size}+k{k}"

process_folder(dir_path, out_dir_path, func={'func':niblack, 'args':[window_size,k]}, ext_out = ".png")



################### TEST 2 ###################
#Parameters
window_size = 45
k=0.5
#Input and output paths
dir_path = "images"
out_dir_path = f"output/test_niblack/w{window_size}+k{k}"

process_folder(dir_path, out_dir_path, func={'func':niblack, 'args':[window_size,k]}, ext_out = ".png")


# ################### TEST 1 ###################
# #Parameters
# window_size=5
# k=-0.2
# #Input and output paths
# dir_path = "images"
# out_dir_path = f"output/test_niblack/w{window_size}+k{k}"

# process_folder(dir_path, out_dir_path, func={'func':niblack, 'args':[window_size,k]}, ext_out = ".png")


# ################### TEST 2 ###################
# #Parameters
# window_size = 45
# k=-0.2
# #Input and output paths
# dir_path = "images"
# out_dir_path = f"output/test_niblack/w{window_size}+k{k}"

# process_folder(dir_path, out_dir_path, func={'func':niblack, 'args':[window_size,k]}, ext_out = ".png")


# ################### TEST 3 ###################
# #Parameters
# window_size = 30
# k=-0.5
# #Input and output paths
# dir_path = "images"
# out_dir_path = f"output/test_niblack/w{window_size}+k{k}"
# process_folder(dir_path, out_dir_path, func={'func':niblack, 'args':[window_size,k]}, ext_out = ".png")

