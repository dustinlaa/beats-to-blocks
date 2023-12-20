# Beats to Blocks - https://beatstoblocks.github.io/
## Peter Akdemir (pja4@njit.edu), Dustin La (drl3@njit.edu), Joshua Quizon (jbq2@njit.edu), Rahul Shah (rns22@njit.edu)
- CS 485 - Machine Listening
- New Jersey Institute of Technology
- Dr. Mark Cartwright

#  Instructions
## Beats-To-Blocks
- To run, create a folder in Google Drive titled "beats-to-blocks".
   - Also download the files [here](https://drive.google.com/drive/folders/1eooU0Jh0WGtWmmeTF6kklcrCYdIagK3a?usp=sharing) and place in the "beats-to-blocks" directory. 
- Create a copy of the file titled "beats-to-blocks_v1_0.ipynb" and use it for the following. 
- Mount Drive and upload a .wav file in the second cell titled "Upload Audio (only if file has not been previously uploaded)".
  - If you have already uploaded a .wav file, instead run the third cell titled "Choose output folder" and type in the same name as your .wav file. ex. song.wav
- Run all the following cells up to "Pipeline #5 NBS to Audio" to activate the Demucs and Spleeter Stem Splitting, MT3 and Spotify Basic Pitch MIDI Transcription, Combine MIDI functions, MIDI to NBS Transcriptions, and finally NBS to Audio output to obtain the final .wav files.
  - Note: This can be a very long process (over an hour for a minute .wav file).

- All files created are stored in your mounted drive under "beats-to-blocks/(your song name)".

## Evaluation
- Requires a number of different file paths for
  - Pipeline predictions
  - Datasets
- Once all paths are satisfied and contain the correct files, run all cells to preprocess the data and evaluate the performance of each pipeline.


## To import into Minecraft (1.20.2):
  - Must have run all previous cells and successfully finished.
     - If all cells are finished and are coming back to a session, use the "Choose output folder" cell and type in the same name as your .wav file. 
  - For Pipeline 1, use the cell that specifies it for Pipeline 1.
  - For Pipelines #2-5, use the other cell and type in the wanted pipeline.
  - Download the created .nbs file and import it into Open Note Block Studio.
  - Export as Schematic.
  - Put in the desired world's folder in the (world)/generated/minecraft/structures.
    - Create these directories if they do not already exist
  - Use a structure block to load the schematic into the world.
