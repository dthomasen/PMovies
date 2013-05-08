#title           :pyscript.py
#description     :This will move video files and remove original directories
#author          :dth
#date            :20130324
#version         :1.0
#usage           :python PMovies.py
#notes           :Tested with Win8
#python_version  :3.3
#==============================================================================

import configparser
import os
import shutil
import ntpath

#Function to find the directory for the file, relative to the root directory
#Used for removing files directory after copy
def findRelativeFolder(rootDir, file):
    relativeDir = ntpath.split(file)[0]

    if(relativeDir.endswith(rootDir)):
        return relativeDir+"\\"+ntpath.basename(file)
    else:
        while not relativeDir.endswith(rootDir):
            relativeDirTuple = ntpath.split(relativeDir)
            relativeDir = relativeDirTuple[0]
            folderName = relativeDirTuple[1]
        try:
            return relativeDir+"\\"+folderName
        except UnboundLocalError:
            return relativeDir+"\\"+ntpath.basename(file) #If file is not in any folder

#Remove directory recursively - Doesn't fail if directory not found
def removeDir(path):
    if os.path.isdir(path):
        shutil.rmtree(path)


scriptDir = os.path.dirname(os.path.realpath(__file__))
config = configparser.ConfigParser()
print ("\nProperties: "+ config.read(scriptDir+'\\PMovies.properties')[0])
fromDir = config.get("Paths","OriginalDir")
toDir = config.get("Paths","MoveTo")
movieDir = config.get("Paths","MovieDir")
rootDir = ntpath.split(fromDir)[1]
moveSamples = config.get("Config","MoveSamples")
mp4Files = []
mkvFiles = []
movieFiles = []
aviFiles = []
wmvFiles = []
sampleFiles = []
dirsToRemove = []

# Locate files ------------------------------------------------------
for r,d,f in os.walk(fromDir):
    for files in f:
        if "sample" in files.lower():
           sampleFiles.append(os.path.join(r,files))
        elif (int(os.path.getsize(files)) > 2000000000):
            movieFiles.append(os.path.join(r,files))
        elif files.endswith(".mp4"):
           mp4Files.append(os.path.join(r,files))
        elif files.endswith(".mkv"):
           mkvFiles.append(os.path.join(r,files))
        elif files.endswith(".avi"):
           aviFiles.append(os.path.join(r,files))
        elif files.endswith(".wmv"):
           wmvFiles.append(os.path.join(r,files))

print("Found "+str(len(mp4Files))+" mp4 file(s).")
print("Found "+str(len(mkvFiles))+" mkv file(s).")
print("Found "+str(len(aviFiles))+" avi file(s).")
print("Found "+str(len(wmvFiles))+" wmv file(s).")
print("Found "+str(len(movieFiles))+" movie files")

if moveSamples is "Yes":
    print("Found "+str(len(sampleFiles))+" sample file(s)")
else:
    print("Skipping "+str(len(sampleFiles))+" sample file(s)")

# Moving files ------------------------------------------------------
if len(mp4Files) != 0:
    print("\nMoving mp4 files...")
    for file in mp4Files:
        try:
            print(" -Moving "+ntpath.basename(file)+"...")
            shutil.copy2(file,toDir)
            dirsToRemove.append(findRelativeFolder(rootDir,file))
            print(" -Done...")
        except IOError:
            print("File "+file+" already exists")
if len(mkvFiles) != 0:
    print("Moving mkv files...")
    for file in mkvFiles:
        try:
            print(" -Moving "+ntpath.basename(file)+"...")
            shutil.copy2(file,toDir)
            dirsToRemove.append(findRelativeFolder(rootDir,file))
            print(" -Done...")
        except IOError:
            print("File "+file+" already exists")
if len(aviFiles) != 0:
    print("Moving avi files...")
    for file in aviFiles:
        try:
            print(" -Moving "+ntpath.basename(file)+"...")
            shutil.copy2(file,toDir)
            dirsToRemove.append(findRelativeFolder(rootDir,file))
            print(" -Done...")
        except IOError:
            print("File "+file+" already exists")
if len(wmvFiles) != 0:
    print("Moving wmv files...")
    for file in wmvFiles:
        try:
            print(" -Moving "+ntpath.basename(file)+"...")
            shutil.copy2(file,toDir)
            dirsToRemove.append(findRelativeFolder(rootDir,file))
            print(" -Done...")
        except IOError:
            print("File "+file+" already exists")
if len(movieFiles) != 0:
    print("Moving movie files...")
    for file in movieFiles:
        try:
            print(" -Moving "+ntpath.basename(file)+"...")
            shutil.copy2(file,movieDir)
            dirsToRemove.append(findRelativeFolder(rootDir,file))
            print(" -Done...")
        except IOError:
            print("File "+file+" already exists")
if moveSamples is "Yes":
    print("Moving sample files...")
    for file in sampleFiles:
        try:
            print(" -Moving "+ntpath.basename(file)+"...")
            shutil.copy2(file,toDir)
            dirsToRemove.append(findRelativeFolder(rootDir,file))
            print(" -Done...")
        except IOError:
            print("File "+file+" already exists")

# Deleting files ----------------------------------------------------
print("\nRemoving "+str(len(dirsToRemove))+" directories")
for directory in dirsToRemove:
    print("Removing "+directory+"...")
    removeDir(directory)
    print("Done...")