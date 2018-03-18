#Step 1 - import library
from pocketsphinx import LiveSpeech
#Step 2 - Print it out
for phrase in LiveSpeech():
    print(phrase)
