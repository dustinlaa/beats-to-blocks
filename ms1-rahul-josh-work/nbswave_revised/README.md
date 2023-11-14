# Notes

## nbs_to_audio.py and related packages
- installation of nbswave requires extra binaries and `Sounds/` data to work
    - `ffmpeg.exe` is required in the root of project directory
    - `ffprobe.exe` is required in the root of project directory
    - `Sounds/*/**` is required in the root of the project directory
        - `*.ogg` should be in root level of `Sounds/` 
- changed `nbswave/main.py` to **NOT** use `headroom` and `ignore_missing_instruments` arguments
    - this version of `nbswave` is in `nbswave.zip`
