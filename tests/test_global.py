# -----------------------------------------------------------------------------
# Autor: Matheus Henrique Marques da Silva
# RA: 252509
# Universidade Estadual de Campinas - Unicamp
# Ano: 2023
# -----------------------------------------------------------------------------
import os
import sys

from utils import test_an_image
# Get the absolute path to the parent directory of the current file
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))

# Add the parent directory to the Python module search path
sys.path.insert(0, parent_dir)
from src.thresholding import global_thresholding
from src.utils import open_pgm, process_folder
import numpy as np
################### TEST 1 ###################
#Parameters
thr = 30

#Input and output paths
file_path = "images/retina.pgm"
out_dir_path = f"output/test_global/"

test_an_image(file_path, out_dir_path,  sufix = f"_t{thr}",func={'func':global_thresholding, 'args':[thr]})

thr = 128
test_an_image(file_path, out_dir_path,  sufix = f"_t{thr}",func={'func':global_thresholding, 'args':[thr]})

thr = 200
test_an_image(file_path, out_dir_path,  sufix = f"_t{thr}",func={'func':global_thresholding, 'args':[thr]})

################### TEST 2 ###################

#Parameters
thr = 200

#Input and output paths
file_path = "images/fiducial.pgm"
out_dir_path = f"output/test_global/"

test_an_image(file_path, out_dir_path,  sufix = f"_t{thr}",func={'func':global_thresholding, 'args':[thr]})

thr = 50
test_an_image(file_path, out_dir_path,  sufix = f"_t{thr}",func={'func':global_thresholding, 'args':[thr]})

thr = 150
test_an_image(file_path, out_dir_path,  sufix = f"_t{thr}",func={'func':global_thresholding, 'args':[thr]})

################### TEST 3 ###################

#Parameters
thr = 100

#Input and output paths
file_path = "images/sonnet.pgm"
out_dir_path = f"output/test_global/"

test_an_image(file_path, out_dir_path,  sufix = f"_t{thr}",func={'func':global_thresholding, 'args':[thr]})

thr = 150
test_an_image(file_path, out_dir_path,  sufix = f"_t{thr}",func={'func':global_thresholding, 'args':[thr]})

thr = 200
test_an_image(file_path, out_dir_path,  sufix = f"_t{thr}",func={'func':global_thresholding, 'args':[thr]})

################### TEST 4 ###################

#Parameters
thr = 90

#Input and output paths
file_path = "images/monarch.pgm"
out_dir_path = f"output/test_global/"

test_an_image(file_path, out_dir_path,  sufix = f"_t{thr}",func={'func':global_thresholding, 'args':[thr]})

thr = 150
test_an_image(file_path, out_dir_path,  sufix = f"_t{thr}",func={'func':global_thresholding, 'args':[thr]})

thr = 200
test_an_image(file_path, out_dir_path,  sufix = f"_t{thr}",func={'func':global_thresholding, 'args':[thr]})

################### TEST 5 ###################

#Parameters
thr = 90

#Input and output paths
file_path = "images/wedge.pgm"
out_dir_path = f"output/test_global/"

test_an_image(file_path, out_dir_path,  sufix = f"_t{thr}",func={'func':global_thresholding, 'args':[thr]})

thr = 150
test_an_image(file_path, out_dir_path,  sufix = f"_t{thr}",func={'func':global_thresholding, 'args':[thr]})

thr = 200
test_an_image(file_path, out_dir_path,  sufix = f"_t{thr}",func={'func':global_thresholding, 'args':[thr]})

################### TEST 6 ###################

#Parameters
thr = 50

#Input and output paths
file_path = "images/peppers.pgm"
out_dir_path = f"output/test_global/"

test_an_image(file_path, out_dir_path,  sufix = f"_t{thr}",func={'func':global_thresholding, 'args':[thr]})

thr = 120
test_an_image(file_path, out_dir_path,  sufix = f"_t{thr}",func={'func':global_thresholding, 'args':[thr]})

thr = 170
test_an_image(file_path, out_dir_path,  sufix = f"_t{thr}",func={'func':global_thresholding, 'args':[thr]})
