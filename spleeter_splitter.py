# pip install spleeter
from spleeter.separator import Separator
import sys
# import os

separator = Separator('spleeter:5stems')

input_file = sys.argv[1]
output_folder = sys.argv[2]

separator.separate_to_file(input_file, output_folder)