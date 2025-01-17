ls *.MP4 | sed "s/^/file '/; s/$/'/" > file_list.txt #add .mp4 of current folder to a list

#du -sh ./* #check their size

#generate a video from few parts
#ffmpeg -f concat -safe 0 -i file_list.txt -c copy output_video.mp4
ffmpeg -f concat -safe 0 -i file_list.txt -c:v copy -an silenced_output_video.mp4 #silenced video
#ffmpeg -i output_video.mp4 -filter:v "setpts=PTS/4" -an fast_output_video.mp4 #

##cut a video (trim)
ffmpeg -i DJI_20250117120043_0014_D.MP4 -t 00:05:05 -c copy -avoid_negative_ts make_zero output.mp4
#trim and add song
ffmpeg -i DJI_20250117120043_0014_D.MP4 -i Cumulus\ Nimbus\ -\ Quincas\ Moreira.mp3 -t 00:05:05 -c:v copy -c:a aac -strict experimental -avoid_negative_ts make_zero output_with_audio.mp4


#ffmpeg -stream_loop -1 -i "AETHER - Density & Time.mp3" -i silenced_output_video.mp4 -c:v copy -c:a aac -shortest output_with_song.mp4
ffmpeg -stream_loop -1 -i "TRAVELATOR - Density & Time.mp3" -i silenced_output_video.mp4 -c:v copy -c:a aac -shortest output_with_song.mp4