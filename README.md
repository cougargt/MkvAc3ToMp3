# MkvAc3ToMp3
Simple script to strip ac3 from mkv files, convert to two channel mp3 and re-merge in batch.

I created this script to fix an issue I had with my Roku Ultra/Plex.  For some reason it would not direct play ac3 audio channels.  This uses a variety of open source programs to extract the ac3, convert it to mp3 (the only format I could guarantee to work), and re-merge it into one mkv.  I found some evidence of others having the same issue and the Plex fixes didn't seem to resolve it. 

I found separate tools that could do each piece.  You'll need to install mkvToolsNix, eca3to, and the lame.exe converter.  I put all but mkvToolsNix into a tools folder.  

It does not recurse or delete the source files. It does clean-up intermediary files.  It will relabel the source mkv to .old. 
