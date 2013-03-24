import configparser
import os

scriptDir = os.path.dirname(os.path.realpath(__file__))
config = configparser.ConfigParser()
print ("\nProperties: "+ config.read(scriptDir+'\\PMovies.properties')[0])
fromDir = config.get("Paths","OriginalDir")
toDir = config.get("Paths","MoveTo")
mp4Files = []
mkvFiles = []

for r,d,f in os.walk(fromDir):
    for files in f:
        if files.endswith(".mp4"):
            mp4Files.append(os.path.join(r,files))
        if files.endswith(".mkv"):
            mkvFiles.append(os.path.join(r,files))

print("Found "+str(len(mp4Files))+" mp4 files.")
print("Found "+str(len(mkvFiles))+" mkv files.")