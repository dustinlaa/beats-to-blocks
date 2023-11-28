import nbswave
from pathlib import Path

# ffmpeg and ffprobe are required to use nbswave
# sound data from note block studio is also required

# get input from /content/song_files/nbs_output/combined_nbs.nbs

# Sounds data from Minecraft
song_name = input("Name your song: ")
nbs_sounds_folder = Path('Sounds')

# write to /content/song_files/final_output/output.wav
nbswave.render_audio(
    '/content/song_files/nbs_output/combined_nbs.nbs', 
    f'/content/song_files/final_output/{song_name}.wav', 
    format='wav',
    custom_sound_path=nbs_sounds_folder,
    ignore_missing_instruments=True
)
