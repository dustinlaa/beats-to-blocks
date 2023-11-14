from pretty_midi import PrettyMIDI

paths = [
    './output/bass.mid',
    './output/drums.mid',
    './output/other.mid',
    './output/piano.mid',
]

# midi input file path is /content/song_files/{pipeline_name}/*
    # pipeline_name will be provided via command line args 
    # where pipeline_name is in {spleeter, demucs, mt3, basic_pitch}
    # where '*' represents each midi file in /content/[pipeline_name]/

# Load MIDI file into PrettyMIDI object
midi_tracks = [PrettyMIDI(p) for p in paths]

combined_midi = PrettyMIDI()

for track in midi_tracks:
    for instrument in track.instruments:
        combined_midi.instruments.append(instrument)

combined_midi.write('./output/combined_no_piano_vocals.mid')

# write to midi file in /content/song_files/combined_midi_output/
