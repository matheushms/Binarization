# -----------------------------------------------------------------------------
# Autor: Matheus Henrique Marques da Silva
# RA: 252509
# Universidade Estadual de Campinas - Unicamp
# Ano: 2023
# -----------------------------------------------------------------------------

import argparse
from src.thresholding import *
import cv2
from src.utils import open_pgm

def main():
    # Create the main argument parser
    parser = argparse.ArgumentParser(description="Thresholding methods")

    parser.add_argument("--input", type=str)
    parser.add_argument("--output", type=str)
    # Create a subparsers object
    subparsers = parser.add_subparsers(dest="method", help="Choose a thresholding method")

    # Add subparsers for each thresholding method
    global_parser = subparsers.add_parser("global", help="Global method")
    global_parser.add_argument("--thr", type = int, default = 128, help="Threshould")

    otsu_parser = subparsers.add_parser("otsu", help="Otsu's method")

    bernsen_parser = subparsers.add_parser("bernsen", help="Bernsen's method")
    bernsen_parser.add_argument("--window_size", type=int, default=5, help="Window size")

    niblack_parser = subparsers.add_parser("niblack", help="Niblack's method")
    niblack_parser.add_argument("--k", type=float, default=-0.2, help="k parameter")
    niblack_parser.add_argument("--window_size", type=int, default=5, help="Window size")

    sauvola_parser = subparsers.add_parser("sauvola", help="Sauvola's method")
    sauvola_parser.add_argument("--k", type=float, default=-0.2, help="k parameter")
    sauvola_parser.add_argument("--R", type=int, default=128, help="R parameter")
    sauvola_parser.add_argument("--window_size", type=int, default=15, help="Window size")

    phansalskar_parser = subparsers.add_parser("phansalskar", help="Phansalskar's method")
    phansalskar_parser.add_argument("--k", type=float, default=-0.2, help="k parameter")
    phansalskar_parser.add_argument("--R", type=int, default=128, help="R parameter")
    phansalskar_parser.add_argument("--p", type=int, default=2, help="p parameter")
    phansalskar_parser.add_argument("--q", type=int, default=10, help="q parameter")
    phansalskar_parser.add_argument("--window_size", type=int, default=5, help="Window size")

    contrast_thresholding_parser = subparsers.add_parser("contrast_thresholding", help="Contrast thresholding")
    contrast_thresholding_parser.add_argument("--window_size", type=int, default=5, help="Window size")

    mean_method_parser = subparsers.add_parser("mean_method", help="Mean method")
    mean_method_parser.add_argument("--C", type=float, default=0, help="C parameter")
    mean_method_parser.add_argument("--window_size", type=int, default=5, help="Window size")

    median_method_parser = subparsers.add_parser("median_method", help="Median method")
    median_method_parser.add_argument("--window_size", type=int, default=5, help="Window size")

    # Parse the arguments
    args = parser.parse_args()

    # Process the arguments and perform the corresponding action
    result_img = None
    img = open_pgm(args.input)
    if args.method == "global" :
        result_img = global_thresholding(img, args.thr)

    elif args.method == "otsu" :
        result_img = otsu(img)

    elif args.method == "bersen" :
        result_img = bernsen(img, window_size=args.window_size)

    elif args.method == "niblack" :
        result_img = niblack(img, window_size=args.window_size)

    elif args.method == "sauvola" :
        result_img = sauvola(img, window_size=args.window_size, k=args.k, R=args.R)

    elif args.method == "phansalkar" :
        result_img = phansalskar(img, window_size=args.window_size, k=args.k, R=args.R, p=args.p, q=args.q)

    elif args.method == "local_contrast" :
        result_img = contrast_thresholding(img, window_size=args.window_size)

    elif args.method == "local_mean" :
        result_img = mean_method(img, window_size=args.window_size, C=args.size)
    
    elif args.method == "local_median" :
        result_img = median_method(img, window_size=args.window_size)

    else:
        print("No method specified. Use --help for more information.")
    

    result_img = result_img.astype(np.uint8)*255
    cv2.imwrite(args.output, result_img)

if __name__ == "__main__":
    main()