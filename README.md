Pmovies
=======

3 phase movie reordering

<h3>1. Find relevant files</h3>
The script will recursively locate mkv, avi, mp4 and wmv files in the directory specified in the properties file (OriginalDir) and determine if they are movie files or TV Shows (Based on their size)

<h3>2. Move files</h3>
This phase will move the files found in step 1 to the location specified in the properties file (MoveTo)

<h3>3. Delete original folders (If specified in properties)</h3>
Lastly the script will recursively delete the original folders for the files (Relative to the basedir)

<h2>Prerequisites</h2>
<ul>
<li>Python 3 or greater</li>
</ul>
