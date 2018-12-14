import os

#point this at your directory
target = r"C:\mkvs\"

#tools, move to suit
mkvExtract = r'"C:\Program Files\MKVToolNix\mkvextract.exe"'
mkvMerge = r'"C:\Program Files\MKVToolNix\mkvmerge.exe"'
mkvInfo = r'"C:\Program Files\MKVToolNix\mkvinfo.exe"'
eac3to = r'C:\tools\eac3to.exe'
lame = r'C:\tools\lame.exe'

files = list()

def createAndMerge(inputFile):
    outFile = inputFile + "_out.mkv"
    audioFileDts = inputFile + ".dts"
    audioFileMp3 = inputFile + ".mp3"

    print("Extracting dts file...")
    os.system(mkvInfo + " " + inputFile)

	#Assumes the 2nd track is the audio track
    retVal = os.system(mkvExtract + " tracks " + inputFile + " 1:" + inputFile + ".dts")
    if retVal != 0:
        os.exit("Fail!")

    print("Converting to mp3...")
    retVal = os.system(eac3to + " " + audioFileDts + " stdout.wav -normalize -down2 | " + lame + " -V2 - " + audioFileMp3)
    if retVal != 0:
        os.exit("Fail!")

    print("Merging to output...")
    mkvMergeCmd = mkvMerge + " --ui-language en --output " + outFile + " --no-audio --language 0:und --sub-charset 1:UTF-8 --language 1:eng --sub-charset 2:UTF-8 --language 2:eng --track-name 2:SDH ( " + inputFile + " ) --language 0:und ( " + audioFileMp3 + " ) --track-order 0:0,0:1,0:2,1:0 "
    retval = os.system(mkvMergeCmd)
    if retVal != 0:
        os.exit("Fail!")

    print("Cleaning up...")
    os.system("del " + audioFileMp3)
    os.system("del " + audioFileDts)
    #rename the input and output files
    os.system("move " + inputFile + " " + inputFile.rsplit( ".", 1 )[ 0 ] + ".old")
    os.system("move " + outFile + " " + inputFile.rsplit(".", 1)[0] + ".mkv" )

for file in os.listdir(target):
    if file.endswith(".mkv"):
        files.append(target + "\\" + file)
        print("Processing " + file + "...")
        createAndMerge(target + "\\" + file)

print("All Done!")

