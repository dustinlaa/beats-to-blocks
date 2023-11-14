from pretty_midi import PrettyMIDI

bass = PrettyMIDI('./output/bass.mid')
drums = PrettyMIDI('./output/drums.mid')
piano = PrettyMIDI('./output/piano.mid')
other = PrettyMIDI('./output/other.mid')
vocals = PrettyMIDI('./output/vocals.mid')

bass.instruments[0].program = 33
bass.instruments[0].is_drum = False
bass.instruments[0].name = 'Electric Bass'

drums.instruments[0].name = 'Steel Drums'
drums.instruments[0].is_drum = True 
drums.instruments[0].program = 114

piano.instruments[0].program = 2
piano.instruments[0].is_drum = False
piano.instruments[0].name = 'Electric Grand Piano'

vocals.instruments[0].program = 78
vocals.instruments[0].is_drum = False
vocals.instruments[0].name = 'Whistle'

other.instruments[0].program = 88
other.instruments[0].is_drum = False
other.instruments[0].name = 'Pad 1'



bass.write('./output/bass.mid')
drums.write('./output/drums.mid')
piano.write('./output/piano.mid')
vocals.write('./output/vocals.mid')
other.write('./output/other.mid')

bass = PrettyMIDI('./output/bass.mid')
drums = PrettyMIDI('./output/drums.mid')
piano = PrettyMIDI('./output/piano.mid')
other = PrettyMIDI('./output/other.mid')
vocals = PrettyMIDI('./output/vocals.mid')

midis = [bass, drums, piano, other, vocals]

print(drums.instruments[0].notes)