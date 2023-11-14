import nbswave
from pathlib import Path

# ffmpeg and ffprobe are required to use nbswave
# sound data from note block studio is also required

# get input from /content/song_files/nbs_output/nbs_output.nbs

nbs_sounds_folder = Path('Sounds')
nbswave.render_audio(
    'winter_wind_nbs.nbs', 
    'winter_wind_nbs.wav', 
    format='wav',
    custom_sound_path=nbs_sounds_folder,
    ignore_missing_instruments=True
)

# write to /content/song_files/final_output/output.wav
