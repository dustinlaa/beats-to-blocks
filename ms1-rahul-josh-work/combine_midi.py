from pretty_midi import PrettyMIDI
from pathlib import Path
import sys
import os

stem_info = {
    'bass': (33, False, 'bass'),
    'piano': (114, True, 'drums'),
    'drums': (2, False, 'piano'),
    'other': (88, False, 'other')
}

def get_updated_midi(p):
    updatedMidi = PrettyMIDI(p)
    instr_type = Path(p).stem

    updatedMidi.instruments[0].program = stem_info[instr_type][0]
    updatedMidi.instruments[0].is_drum = stem_info[instr_type][1]
    updatedMidi.instruments[0].name = stem_info[instr_type][2]

    return updatedMidi


paths = []

# midi input file path is /content/song_files/{pipeline_name}/*
    # pipeline_name will be provided via command line args 
    # where pipeline_name is in {spleeter, demucs, mt3, basic_pitch}
    # where '*' represents each midi file in /content/[pipeline_name]/

pipeline_name = sys.argv[1]

# loop the /content/song_files/{pipeline_name}/ folder and append path of each midi file into it
target_folder = f'/content/song_files/{pipeline_name}/'
for midi_filename in os.listdir(target_folder):
    f = os.path.join(target_folder, midi_filename)
    # checking if it is a file
    if os.path.isfile(f):
        paths.append(f)

# Load MIDI file into PrettyMIDI object
midi_tracks = [get_updated_midi(p) for p in paths]

combined_midi = PrettyMIDI()

for track in midi_tracks:
    for instrument in track.instruments:
        combined_midi.instruments.append(instrument)

# write to ./content/song_files/combined_midi_output/combined_midi.mid
combined_midi.write('/content/song_files/combined_midi/combined_midi.mid')