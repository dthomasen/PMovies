import configparser
import os

scriptDir = os.path.dirname(os.path.realpath(__file__))
config = configparser.ConfigParser()
print ("\nProperties: "+ config.read(scriptDir+'\\PMovies.properties')[0])
fromDir = config.get("Paths","OriginalDir")
toDir = config.get("Paths","MoveTo")
moveSamples = config.get("Config","MoveSamples")
mp4Files = []
mkvFiles = []
aviFiles = []
wmvFiles = []
sampleFiles = []

for r,d,f in os.walk(fromDir):
    for files in f:
        if "sample" in files.lower():
           sampleFiles.append(os.path.join(r,files))
        elif files.endswith(".mp4"):
           mp4Files.append(os.path.join(r,files))
        if files.endswith(".mkv"):
           mkvFiles.append(os.path.join(r,files))
        if files.endswith(".avi"):
           aviFiles.append(os.path.join(r,files))
        if files.endswith(".wmv"):
           wmvFiles.append(os.path.join(r,files))

print("Found "+str(len(mp4Files))+" mp4 file(s).")
print("Found "+str(len(mkvFiles))+" mkv file(s).")
print("Found "+str(len(aviFiles))+" avi file(s).")
print("Found "+str(len(wmvFiles))+" wmv file(s).")

if moveSamples is "Yes":
    print("Found "+str(len(sampleFiles))+" sample file(s)")
else:
    print("Skipping "+str(len(sampleFiles))+" sample file(s)")

