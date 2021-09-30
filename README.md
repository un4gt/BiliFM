# BiliFM
## Intro
An script to download all videos of the Bilibili uploader you love.  
使用 Bilili 库的脚本，用于下载指定up主全部或指定数量的视频，并转换为音乐格式（是否转换可选）
## Usage
使用实例：
```Bash
python __main__.py 261485584 --save=0 --music=1 
```
```python
uid = 261485584 # uid 为up主的uid
--save=0 # 选择是否保存已下载的视频
--music=0 # 选择是否将下载的视频转换为音频格式
```
## Status quo
* python 版本应不低于3.8（Bilili 库的要求）
* 需要安装 ffmpeg 并加入 path
## Issues
* Linux 下 FFmpeg 缺少 mp3 编码器
  * 可以依赖 libmp3lame 但会使使用成本上升不少
* WIndows 下，安装合理的第三方编译版可以避开这个问题（大概）
* requirement.txt 对依赖库的描述不准确
## Licence
Bilili 采用 GPLv3，ffmpy 采用 MIT  
依照 GPLv3 的要求，本项目采用 GPLv3.
