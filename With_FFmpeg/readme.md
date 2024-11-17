* All started at [this post](https://jalcocert.github.io/JAlcocerT/dji-osmo-action-5-pro/)
    * And continued in the [x300 post](https://jalcocert.github.io/JAlcocerT/asrock-x300-home-server/#video-editing-101)

## Linux

```sh
sudo apt install ffmpeg
ffmpeg -version #

```



## Windows

```sh
#  Set-ExecutionPolicy Bypass -Scope Process -Force; `
# [System.Net.ServicePointManager]::SecurityProtocol = `
# [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; `
# iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

choco --version #2.3.0


choco install ffmpeg -y #with PS as ADMIN!
ffmpeg -version # 7.1-essentials_build
```