# Generate the file list
ls *.MP4 | sed "s/^/file '/; s/$/'/" > file_list.txt

# Concatenate videos and add watermark to the bottom right
ffmpeg -f concat -safe 0 -i file_list.txt -i watermark.jpg -filter_complex "overlay=W-w-10:H-h-10" -c:v libx264 -crf 18 -preset veryfast -c:a copy output_video.mp4


# ls *.MP4 | sed "s/^/file '/; s/$/'/" > file_list.txt #add .mp4 of current folder to a list

# #du -sh ./* #check their size

# #generate a video with them (IT PRESERVES THE ORIGINAL BITRATE)
# ffmpeg -f concat -safe 0 -i file_list.txt -c copy output_video.mp4
# #ffmpeg -f concat -safe 0 -i file_list.txt -c:v copy -an output_video.mp4 #silenced video
# #ffmpeg -i output_video.mp4 -filter:v "setpts=PTS/4" -an fast_output_video.mp4 #