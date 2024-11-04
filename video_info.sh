for video in *.MP4; do
    echo "File: $video"
    ffprobe "$video"
done


####

for video in *.MP4; do
    echo "File: $video"
    mediainfo "$video" | grep -E 'Rotation|Width|Height|Format|Duration'
done

####

#check .MP$ info recursively
find . -type f -iname "*.mp4" -exec bash -c '
  for file; do
    name=$(basename "$file")
    duration=$(ffprobe -v error -select_streams v:0 -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "$file")
    size=$(stat --format="%s" "$file")
    resolution=$(ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=s=x:p=0 "$file")
    
    # FPS extraction
    fps_raw=$(ffprobe -v error -select_streams v:0 -show_entries stream=r_frame_rate -of csv=p=0 "$file")
    fps=$(echo "$fps_raw" | awk -F "/" '"'"'{ if ($2) print $1/$2; else print $1 }'"'"')

    # Bitrate extraction in kbps
    bitrate_bps=$(ffprobe -v error -show_entries format=bit_rate -of default=noprint_wrappers=1:nokey=1 "$file")
    bitrate_kbps=$(echo "scale=2; $bitrate_bps / 1000" | bc -l)
    
    # Average MB/s calculation
    avg_mbps=$(echo "scale=2; $bitrate_bps / 1000000000" | bc -l)

    echo "Name: $name - Duration: ${duration}s - Size: ${size} GB - Resolution: $resolution - FPS: $fps - Bitrate: ${bitrate_kbps}kbps - Avg MB/s: ${avg_mbps}MB/s"
  done
' bash {} +