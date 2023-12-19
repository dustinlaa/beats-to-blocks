# Beats to Blocks - https://beatstoblocks.github.io/
## Peter Akdemir (pja4@njit.edu), Dustin La (drl3@njit.edu), Joshua Quizon (jbq2@njit.edu), Rahul Shah (rns22@njit.edu)
- CS 485 - Machine Listening
- New Jersey Institute of Technology
- Dr. Mark Cartwright

#  Instructions
- To run, create a folder in Drive titled "beats-to-blocks"
- Mount drive and upload a .wav file in the second cell which is titled "Upload Audio (only if file has not been previously uploaded)"
  - If you have already previously uploaded a .wav file, instead run the third cell which is titled "Choose output folder" and type in exactly the same name as your .wav file
- Run all the following cells up to "Pipeline #5 NBS to Audio" to activate the Demucs and Spleeter Stem Splitting, MT3 and Spotify Basic Pitch MIDI Transcription, Combine MIDI functions, MIDI to NBS Transcriptions, and finally NBS to Audio output to obtain the final .wav files.
  - Note: This can be a very long process (over an hour for a minute .wav file)

- All files created are stored in your mounted drive under "beats-to-blocks/(your song name)".

# To import into Minecraft:
  - Must have ran all previous cells and successfully finished
  - For Pipeline 1, use the cell that specifies its for Pipeline 1
  - For Pipelines #2-5, use the other cell and type in the wanted pipeline
  - Download the created .nbs file and import into Open Note Block Studio
  - Export as Schematic
  - Put in the desired world's folder in the world/generated/minecraft/structures
  - Use a structure block to load the schematic into the world
