# 视频与音频

## 截图
桌面环境工具（**gnome-screenshot**、**spectacle**、**flameshot**）随桌面自带；**scrot** 和 **maim** 在任何 X11 环境下都可用，**grim** 用于 Wayland。
```[flameshot](/man/flameshot) gui```
```[gnome-screenshot](/man/gnome-screenshot)```
```[spectacle](/man/spectacle)```
```[scrot](/man/scrot)```
```[maim](/man/maim) [fileName].png```
```[grim](/man/grim) [fileName].png```
```[import](/man/import) -window root [fileName].png```

## 屏幕录制
在 X11 上用 ffmpeg 录制屏幕，Wayland 上用 **wf-recorder**。对于终端会话，**asciinema** 记录的是文本而非像素。
```[ffmpeg](/man/ffmpeg) -f x11grab -i :0.0 recording.mp4```
```[wf-recorder](/man/wf-recorder) -f recording.mp4```
```[recordmydesktop](/man/recordmydesktop)```
```[asciinema](/man/asciinema) rec session.cast```

## 摄像头
用摄像头拍摄照片。
```[fswebcam](/man/fswebcam) [fileName].jpg```
```[ffmpeg](/man/ffmpeg) -f v4l2 -i /dev/video0 -frames:v 1 [fileName].jpg```
```[uvccapture](/man/uvccapture) -d/dev/video0 -o[fileName].jpg```

## 播放音频与视频
**mpv** 和 **vlc** 几乎能播放任何格式。**ffplay** 是 ffmpeg 自带的简易播放器；**aplay** 和 **play** 处理简单的声音文件。
```[mpv](/man/mpv) [file]```
```[vlc](/man/vlc) [file]```
```[ffplay](/man/ffplay) [file]```
```[aplay](/man/aplay) sound.wav```
```[play](/man/play) sound.wav```

## 音量
**alsamixer** 和 **pavucontrol** 是交互式混音器。在脚本中，**pactl** 控制 PulseAudio/PipeWire 的默认输出设备。
```[alsamixer](/man/alsamixer)```
```[pavucontrol](/man/pavucontrol)```
```[pactl](/man/pactl) set-sink-volume @DEFAULT_SINK@ +5%```
```[pactl](/man/pactl) set-sink-mute @DEFAULT_SINK@ toggle```
```[amixer](/man/amixer) set Master mute```
```[amixer](/man/amixer) set Master unmute```

## 录制音频
从默认麦克风录音。
```[arecord](/man/arecord) -f cd [fileName].wav```
```[ffmpeg](/man/ffmpeg) -f alsa -i default [fileName].wav```

## 语音与蜂鸣
让电脑说话，或播放经典的 PC 扬声器蜂鸣声。
```[spd-say](/man/spd-say) "I am a robot"```
```[espeak](/man/espeak) "I am a robot"```
```[beep](/man/beep)```

## 检查媒体文件
显示编解码器、分辨率、时长和码率。
```[ffprobe](/man/ffprobe) [file]```
```[mediainfo](/man/mediainfo) [file]```

## 用 ffmpeg 转换
ffmpeg 根据文件扩展名确定输出格式，因此简单转换不需要任何参数。
```[ffmpeg](/man/ffmpeg) -i input.avi output.mp4```
```[ffmpeg](/man/ffmpeg) -i input.mp4 output.webm```

提取音轨并保存为 MP3（**-vn** 去掉视频，**-b:a** 设置音频码率；**-q:a 0** 则使用最佳可变质量）。
```[ffmpeg](/man/ffmpeg) -i video.mp4 -vn -b:a 192k audio.mp3```
```[ffmpeg](/man/ffmpeg) -i video.mp4 -vn -q:a 0 audio.mp3```

调整视频尺寸；**-1** 表示保持宽高比。
```[ffmpeg](/man/ffmpeg) -i input.mp4 -vf scale=1280:-1 output.mp4```

## 剪切视频
**-ss** 设置起点，**-t** 设置时长。**-c copy** 剪切时不重新编码：瞬间完成且无损，但只能精确到最近的关键帧。
```[ffmpeg](/man/ffmpeg) -ss 00:01:30 -i input.mp4 -t 00:00:20 -c copy clip.mp4```
```[ffmpeg](/man/ffmpeg) -ss 00:01:30 -i input.mp4 -t 00:00:20 clip.mp4```

## 图像与视频
把编号图像序列转成视频或反向转换，或制作动画 GIF。
```[ffmpeg](/man/ffmpeg) -framerate 24 -i image%d.jpg video.mp4```
```[ffmpeg](/man/ffmpeg) -i video.mp4 image%d.jpg```
```[ffmpeg](/man/ffmpeg) -i video.mp4 -vf "fps=10,scale=480:-1" animation.gif```

将图像转换为 WebP 格式。
```[gif2webp](/man/gif2webp) [inputFile] -o [outputFile]```
```[img2webp](/man/img2webp) [inputFile] -o [outputFile]```
