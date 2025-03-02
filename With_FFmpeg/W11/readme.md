* Explained for yosua at <https://jalcocert.github.io/JAlcocerT/web-for-moto-blogger/>


## FFmpeg Windows

> HEVC must be installed

```sh
#  Set-ExecutionPolicy Bypass -Scope Process -Force; `
# [System.Net.ServicePointManager]::SecurityProtocol = `
# [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; `
# iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

choco --version #2.3.0

choco install ffmpeg -y #with PS as ADMIN!
ffmpeg -version # 7.1-essentials_build
```

**Copy the files**

```sh
Copy-Item -Path "E:\DCIM\DJI_001\*.MP4" -Destination "C:\Users\j--e-\OneDrive\Escritorio\cadiz" -Force
#Robocopy "E:\DCIM\DJI_001" "C:\Users\j--e-\OneDrive\Escritorio\cadiz" *.MP4 /MT:8 /R:3 /W:2 /ETA /TEE /LOG+:copy_log.txt
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

You can do this remotely thanks to **Rustdesk**

---

### More mp4 video details

See video files details:

```sh
choco install mediainfo
choco install mediainfo-cli

Get-ChildItem -Filter "*.MP4" | ForEach-Object { Write-Output "File: $($_.Name)"; mediainfo "$($_.FullName)" | Select-String 'Rotation|Width|Height|Format|Duration'; ffprobe -v error -select_streams v:0 -show_entries stream=width,height,duration,codec_name,r_frame_rate -show_entries stream_tags=rotate "$($_.FullName)" | Select-String "TAG:rotate|width|height|duration|codec_name|r_frame_rate"; Write-Output "-----------------------" }
```