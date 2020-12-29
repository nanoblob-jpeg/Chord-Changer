# Chord Changer
This program changes chord sheets from letter to greek numbers. It has a gui that allows you to convert multiple chord charts very quickly.

__THIS DOES NOT WORK 100% OF THE TIME__: In the attempt to reduce the work for the user, this program tries to identify the lines which include the chord names. This is based on the ratio of spaces to characters, thus, sometimes it will try to translate lines with lyrics and fail to translate some lines with chords. To solve this, add more characters/spaces as appropriate to the respective lines.

### Prerequisites
You need to have Python 3.* installed before running this program.

### Installing
simply clone this repository and then run the magic.py file:
```
python magic.py
```

### Using
In the gui, you are prompted for the key that the song is in. Enter it and then copy paste the untranslated chart to the left side. Click the translate button and then copy the translated chart from the right side to wherever you need it.
