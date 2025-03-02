
## FFmpeg Windows

```sh
#  Set-ExecutionPolicy Bypass -Scope Process -Force; `
# [System.Net.ServicePointManager]::SecurityProtocol = `
# [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; `
# iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

choco --version #2.3.0

choco install ffmpeg -y #with PS as ADMIN!
ffmpeg -version # 7.1-essentials_build
```

Create the **txt list**: all withing POWERSHELL

```sh
Get-ChildItem -Filter "*.MP4" | ForEach-Object { "file '$($_.Name)'" } | Set-Content file_list.txt
```

And just **use ffmpeg**:

```sh
ffmpeg -f concat -safe 0 -i file_list.txt -c copy output.mp4 #simple join
#ffmpeg -f concat -safe 0 -i file_list.txt -c:v copy -an output_video.mp4 #silenced video

### 🎵 Music by
#silence & music
#ffmpeg -f concat -safe 0 -i file_list.txt -c:v copy -an silenced_output_video.mp4 #silenced video
#ffmpeg -stream_loop -1 -i "TRAVELATOR - Density & Time.mp3" -i silenced_output_video.mp4 -c:v copy -c:a aac -shortest output_with_song.mp 
```

You can do this remotely thanks to **a**

> HEVC must be installed

---

### More mp4 video details

```sh
choco install mediainfo
choco install mediainfo-cli

Get-ChildItem -Filter "*.MP4" | ForEach-Object { Write-Output "File: $($_.Name)"; mediainfo "$($_.FullName)" | Select-String 'Rotation|Width|Height|Format|Duration'; ffprobe -v error -select_streams v:0 -show_entries stream=width,height,duration,codec_name,r_frame_rate -show_entries stream_tags=rotate "$($_.FullName)" | Select-String "TAG:rotate|width|height|duration|codec_name|r_frame_rate"; Write-Output "-----------------------" }
```