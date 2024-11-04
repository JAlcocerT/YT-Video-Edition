# YT-Video-Edition

```sh
sudo apt install ffmpeg
```

* All started at [this post](https://jalcocert.github.io/JAlcocerT/dji-osmo-action-5-pro/)

```sh
du -h --max-depth=1 #check space
find . -name "*.LRF" -type f -delete #cleaning .LRF
```

---

## Tweak Photos

```sh
#mediainfo PXL_20241031_124037774.jpg
#exiftool PXL_20241031_124037774.jpg
#identify -verbose PXL_20241031_124037774.jpg

ffmpeg -i PXL_20241030_115355466.jpg -q:v 3 compressed_PXL_20241030_115355466.jpg
#convert PXL_20241031_124037774.jpg -quality 85 compressed_PXL_20241031_124037774.jpg
```
