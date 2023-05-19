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
from src.thresholding import phansalskar
from src.utils import open_pgm, process_folder


#################### TEST 2 ###################
# #Parameters
# k=0.25 
# R=128
# p=3
# q=10
# window_size = 30

# #Input and output paths
# dir_path = "images"
# out_dir_path = f"output/test_phansalskar/w{window_size}_k{k}_R{R}_p{p}_{q}"

# process_folder(dir_path, out_dir_path, func={'func':phansalskar, 'args':[window_size, k, R, p, q]}, ext_out = ".png")

# ################### TEST 2 ###################
# #Parameters
# k=0.25 
# R=128
# p=3
# q=10
# window_size = 45

# #Input and output paths
# dir_path = "images"
# out_dir_path = f"output/test_phansalskar/w{window_size}_k{k}_R{R}_p{p}_{q}"

# process_folder(dir_path, out_dir_path, func={'func':phansalskar, 'args':[window_size, k, R, p, q]}, ext_out = ".png")

# ################### TEST 2 ###################
# #Parameters
# k=0.25 
# R=128
# p=5
# q=10
# window_size = 45

# #Input and output paths
# dir_path = "images"
# out_dir_path = f"output/test_phansalskar/w{window_size}_k{k}_R{R}_p{p}_{q}"

# process_folder(dir_path, out_dir_path, func={'func':phansalskar, 'args':[window_size, k, R, p, q]}, ext_out = ".png")

################### TEST 2 ###################
#Parameters
k=0.3 
R=128
p=10
q=10
window_size = 15

#Input and output paths
dir_path = "images"
out_dir_path = f"output/test_phansalskar/w{window_size}_k{k}_R{R}_p{p}_{q}"

process_folder(dir_path, out_dir_path, func={'func':phansalskar, 'args':[window_size, k, R, p, q]}, ext_out = ".png")
