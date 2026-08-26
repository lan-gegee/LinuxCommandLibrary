# TAGLINE

在 X11 上把程序运行为桌面背景

# TLDR

将**视频**作为背景运行

```xwinwrap -b -nf -ov -- mpv --wid WID --loop --no-audio --no-resume-playback --panscan=1.0 [path/to/video.mp4]```

**全屏**运行视频

```xwinwrap -b -nf -fs -ov -- mpv --wid WID --loop --no-audio --no-resume-playback --panscan=1.0 [path/to/video.mp4]```

带**透明度**运行

```xwinwrap -b -nf -ov -o 0.8 -- mpv --wid WID --loop --no-audio --no-resume-playback --panscan=1.0 [path/to/video.mp4]```

在**指定**显示器上运行

```xwinwrap -g 1600x900+1920+0 -b -nf -ov -- mpv --wid WID --loop --no-audio --no-resume-playback --panscan=1.0 [path/to/video.mkv]```

# SYNOPSIS

**xwinwrap** [_OPTIONS_] -- _COMMAND_

# PARAMETERS

**-b**
> 置于其他窗口之下

**-nf**
> 不获取焦点

**-fs**
> 全屏

**-ov**
> 设置 override redirect

**-o** _OPACITY_
> 设置透明度（0.0 到 1.0）

**-g** _GEOMETRY_
> 窗口几何描述（WxH+X+Y）

**WID**
> 窗口 ID 占位符，传给子进程时会被替换为实际的窗口 ID

**-s**
> 粘性窗口（出现在所有桌面/工作区）

**-st**
> 不显示在任务栏

# DESCRIPTION

**xwinwrap** 将程序作为桌面背景窗口运行。它会创建一个位于所有窗口之后的窗口，并把它的窗口 ID 传给子程序，从而实现视频壁纸和动态背景。

常与 mpv 搭配，将视频播放为桌面背景。

# CAVEATS

仅支持 X11。可能无法在所有窗口管理器或合成器下工作。子进程必须支持窗口 ID 参数。

# INSTALL

```nix: nix profile install nixpkgs#xwinwrap```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mpv](/man/mpv)(1), [feh](/man/feh)(1), [xdotool](/man/xdotool)(1), [xsetroot](/man/xsetroot)(1)
