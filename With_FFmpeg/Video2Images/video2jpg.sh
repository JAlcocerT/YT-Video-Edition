#apparently with lower resolution in practice
ffmpeg -i "your_video.MP4" -vsync vfr "./extractedframes/frame%04d.jpg"
##rm *.jpg #clean if needed


#This one seems to work better
ffmpeg -i input_video.mp4 -vf "select='gte(t\,120)',fps=1" -vsync vfr frame_%03d.png
ffmpeg -i DJI_20250116072852_0036_D.MP4 -vf "select='gte(t\,90)',fps=1" -vsync vfr frame_%03d.png
#ffmpeg -i DJI_20250116072852_0036_D.MP4 -vf "select='gte(t\,90)',fps=1" -vsync vfr frame_%03d.jpg


#between 2 seconds, 1fps extracts and creates a folder
#ffmpeg -i DJI_20250116072528_0035_D.MP4 -vf "select='between(t,90,105)',fps=1" -vsync vfr frame_%03d.png
mkdir -p "./$(basename DJI_20250116072528_0035_D.MP4 .MP4)" && ffmpeg -i DJI_20250116072528_0035_D.MP4 -vf "select='between(t,0,18)',fps=1" -vsync vfr "./$(basename DJI_20250116072528_0035_D.MP4 .MP4)/frame_%03d.png"
