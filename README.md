Pmovies
=======

3 phase movie reordering

<h3>1. Find relevant files</h3>
The script will locate mkv, avi, mp4 and wmv files in the directory specified in the properties file (OriginalDir)

<h3>2. Move files</h3>
This phase will move the files found in step 1 to the location specified in the properties file (MoveTo)

<h3>3. Delete original folders (If specified in properties)</h3>
Lastly the script will recursively delete the original folder for the files (Relative to the basedir)