# pip install demucs
import subprocess
# import demucs.separate

# input_audio_path = input("Please specify the input file: ")

# if input_audio_path == "":
#     input_audio_path = input("Please specify the input file: ")

input_audio_path = "insideOut.wav"
output_dir = "/stem-output"

# !python -m demucs.separate /content/stay_qUgdaiNx.wav <-- google colab

# Construct the command as a list of arguments
command = ["python", "-m", "demucs.separate", input_audio_path]
# Use subprocess to run the command
subprocess.run(command, check=True)