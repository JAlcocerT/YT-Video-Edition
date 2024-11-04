for video in *.MP4; do
    echo "File: $video"
    mediainfo "$video" | grep -E 'Rotation|Width|Height|Format|Duration'
    ffprobe -v error -select_streams v:0 -show_entries stream=width,height,duration,codec_name,r_frame_rate -show_entries stream_tags=rotate "$video" | grep -E "TAG:rotate|width|height|duration|codec_name|r_frame_rate"
    echo "-----------------------"
done