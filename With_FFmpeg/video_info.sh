for video in *.MP4; do
    echo "File: $video"
    ffprobe "$video"
done

####

for file in *.MP4; do
    echo "Information for $file:"
    ffprobe -v error -show_format -show_streams "$file"
    echo "-----------------------"
done

####

for file in *.MP4; do
    echo "Rotation information for $file:"
    ffprobe -v error -select_streams v:0 -show_entries stream_tags=rotate "$file" | grep "TAG:rotate"
    echo "-----------------------"
done

####

for video in *.MP4; do
    echo "File: $video"
    mediainfo "$video" | grep -E 'Rotation|Width|Height|Format|Duration'
done

for video in *.MP4; do
    echo "File: $video"
    mediainfo "$video" | grep -E 'Rotation|Width|Height|Format|Duration'
    ffprobe -v error -select_streams v:0 -show_entries stream=width,height,duration,codec_name -show_entries stream_tags=rotate "$video" | grep -E "TAG:rotate|width|height|duration|codec_name"
    echo "-----------------------"
done


### Just seconds and MB
for file in *.MP4 *.mp4; do  # Handles both uppercase and lowercase extensions
  if [[ -f "$file" ]]; then  # Check if it's a regular file (not a directory)
    duration=$(ffmpeg -i "$file" 2>&1 | grep Duration | awk '{print $2}' | sed s/,//)
    size=$(stat -c '%s' "$file") # Size in bytes
    size_mb=$((size / (1024 * 1024))) # Size in MB

    echo "File: $file"
    echo "Duration: $duration seconds"
    echo "Size: $size bytes ($size_mb MB)"
    echo "--------------------"
  fi
done


### And with the average mb/s then!
for file in *.MP4 *.mp4; do
  if [[ -f "$file" ]]; then
    duration=$(ffmpeg -i "$file" 2>&1 | grep Duration | awk '{print $2}' | sed s/,//)
    size=$(stat -c '%s' "$file")
    size_mb=$((size / (1024 * 1024)))

    # Calculate duration in seconds
    hours=$(echo "$duration" | awk -F: '{print $1}')
    minutes=$(echo "$duration" | awk -F: '{print $2}')
    seconds=$(echo "$duration" | awk -F: '{print $3}' | cut -d. -f1)
    total_seconds=$((hours * 3600 + minutes * 60 + seconds))

    # Calculate average MB per second
    if ((total_seconds > 0)); then
      avg_mbps=$(echo "scale=2; $size_mb / $total_seconds" | bc)
    else
      avg_mbps="N/A (duration is zero)"
    fi

    echo "File: $file"
    echo "Duration: $duration seconds"
    echo "Size: $size bytes ($size_mb MB)"
    echo "Average MB/s: $avg_mbps"
    echo "--------------------"
  fi
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