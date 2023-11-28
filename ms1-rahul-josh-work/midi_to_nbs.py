import pynbs
from pretty_midi import PrettyMIDI

midi_to_nbs_instrs = {
    0: 0, # piano
    2: 0, # piano
    114: 3, # drums
    33: 1, # bass
    78: 6, # vocals 
    88: 9 # other
}

nbs_instr_files = {
    0: 'harp.ogg',
    3: 'sdrum.ogg',
    1: 'bdrum.ogg',
    6: 'flute.ogg',
    9: 'iron_xylophone.ogg'
}

nbs_instr_names = {
    0: 'harp',
    3: 'snare drum',
    1: 'bass drum',
    6: 'flute',
    9: 'iron xylophone'
}


# get midi input from /content/song_files/combined_midi/combined_midi.mid

midi_file = PrettyMIDI('/content/song_files/combined_midi/combined_midi.mid')

# in many songs (and thus midi files), notes are played at the same time (same onset time)
# in nbs, layers are used when multiple notes are played at the same time
# so:
    # for each instrument
        # and for each note in that instrument
            # get the first note and its onset time
            # get all other notes with the same onset time
            # for each of those notes  
                # create an nbs note and append it to the list of notes
                # each note should be put in a different layer (since they are played at the same time)
            # update the maximum number of layers
            # remove the notes we just converted from the midi instrument notes list
        # update layer offset (as to not override notes we just did for the previous instrument)

list_of_notes = []
layer_offsets = [0]
nbs_instrument_set = set()
max_num_ticks = 0
for i, instrument in enumerate(midi_file.instruments):
    max_num_layers = 0
    while(len(instrument.notes) > 0):
        curr_note = instrument.notes[0]
        time = curr_note.start
        # Filter midi notes according to nearly similar start time
        notes_at_time = list(filter(lambda n: n.start < time + 0.05, instrument.notes))
        # Convert all filtered notes to NBS notes and store all layers of instrument i's notes 
        # in layer_offsets 
        for j in range(len(notes_at_time)):
            max_num_ticks = int(round(time / 0.05)) if max_num_ticks < int(round(time / 0.05)) else max_num_ticks
            n = notes_at_time[j]
            pynbs_instrument_id = midi_to_nbs_instrs[instrument.program]
            list_of_notes.append(
                pynbs.Note(
                    tick=int(round(time / 0.05)),
                    layer=j + layer_offsets[i],
                    instrument=pynbs_instrument_id,
                    key=n.pitch - 21,
                    velocity=n.velocity,
                    pitch=0
                )
            )
            nbs_instrument_set.add(pynbs_instrument_id)
        max_num_layers = len(notes_at_time) if len(notes_at_time) > max_num_layers else max_num_layers
        # Get the leftover midi notes of instrument i and then sort them into layers in the next iteration; 
        # keep at it until we run out of midi notes
        instrument.notes = [note for note in instrument.notes if note not in notes_at_time]
    # Once done with a single instrument, add offset for what layer instrument (i+1)'s notes will
    # start to be inserted
    layer_offsets.append(layer_offsets[i] + max_num_layers)

# Testing for conflicting notes in same layer
for tick in range(max_num_ticks + 1):
    notes_at_tick = [note for note in list_of_notes if note.tick == tick]
    for i in range(len(notes_at_tick)):
        for j in range(len(notes_at_tick)):
            if j != i:
                note_i_layer = notes_at_tick[i].layer
                note_j_layer = notes_at_tick[j].layer
                if note_i_layer == note_j_layer:
                    print(str(notes_at_tick[i]), str(notes_at_tick[j], 'have the same layer and tick'))
                    exit(-1)

nbs_file = pynbs.new_file(
    song_name='song', 
    tempo=20.00,
    song_layers=layer_offsets[-1],
    song_length=max_num_ticks    
)
nbs_file.layers = [pynbs.Layer(id=i, name='', lock=False, volume=100, panning=0) for i in range(layer_offsets[-1])]
nbs_file.instruments = [pynbs.Instrument(id=i, name=nbs_instr_names[i], file=nbs_instr_files[i], pitch=45, press_key=True) for i in nbs_instrument_set]
nbs_file.notes.extend(list_of_notes)
# write to nbs_output.nbs in /content/song_files/nbs_output/combined_nbs.nbs
nbs_file.save("/content/song_files/nbs_output/combined_nbs.nbs", version=5)


