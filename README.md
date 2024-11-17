# YT-Video-Edition

* This repository - https://github.com/JAlcocerT/YT-Video-Edition
* **More Description** about the topic on these **posts**
    * https://jalcocert.github.io/JAlcocerT/dji-osmo-action-5-pro/#my-workflow-with-the-dji-oa5-pro
    * https://jalcocert.github.io/JAlcocerT/asrock-x300-home-server/#video-editing-101
    * https://jalcocert.github.io/JAlcocerT/my-youtube-ai-workflow/

```sh
sudo apt install ffmpeg #
```


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

## Youtube Readme


```
Testing the DJi OA5Pro [2.7k/60fps/RS/W]in Netherlands during Autumn.

https://jalcocert.github.io/JAlcocerT/dji-osmo-action-5-pro/
```

And **with timestamps**:

```

```

---

## Venv Setup


```sh
python3 -m venv videoediting_venv #create the venv
#python -m venv videoediting_venv #create the venv


videoediting_venv\Scripts\activate #activate venv (windows)
source videoediting_venv/bin/activate #(linux)
```

```sh
pip install -r requirements.txt #all at once
#pip install moviepy==1.0.3 #https://pypi.org/project/firecrawl-py/
```