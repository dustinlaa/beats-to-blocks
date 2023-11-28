from basic_pitch.inference import predict
from basic_pitch import ICASSP_2022_MODEL_PATH
from enum import Enum
import basic_pitch.inference

class InstrumentIndex(Enum):
    ACOUSTIC_BASS = 32
    SYNTH_DRUM = 118
    ACOUSTIC_GRAND_PIANO = 0

input_paths = [
    './assets/bass.wav',
    './assets/drums.wav',
    './assets/other.wav',
    './assets/piano.wav',
    './assets/vocals.wav'
]

output_paths = [
    '/content/song_files/basic_pitch/bass.mid',
    '/content/song_files/basic_pitch/drums.mid',
    '/content/song_files/basic_pitch/other.mid',
    '/content/song_files/basic_pitch/piano.mid',
    '/content/song_files/basic_pitch/vocals.mid'
]

try:
    for i, o in zip(input_paths, output_paths):
        model_output, midi_data, note_events = predict(
            i,
            model_or_model_path=str(ICASSP_2022_MODEL_PATH)
        )
        midi_data.write(o)
except Exception as e:
    print(e)
