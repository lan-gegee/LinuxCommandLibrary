# TAGLINE

KDE 的非线性视频编辑器

# TLDR

**启动 Kdenlive**

```kdenlive```

**打开项目**

```kdenlive [project.kdenlive]```

**从命令行渲染**

```kdenlive_render [project.kdenlive]```

# SYNOPSIS

**kdenlive** [_options_] [_file_]

# PARAMETERS

_file_
> 要打开的项目文件。

**--config** _file_
> 使用备用配置。

**--mlt-log**
> MLT 调试输出。

**--help**
> 显示帮助。

# DESCRIPTION

**Kdenlive** 是 KDE 的非线性视频编辑器。它提供多轨编辑、特效、转场，并通过 FFmpeg 和 MLT 支持广泛的视频格式。

Kdenlive 提供关键帧、色彩校正、音频混音和字幕等专业功能。它既适合业余爱好者也适合专业视频制作。

# FEATURES

- 多轨时间线编辑
- 视频和音频特效
- 转场与合成
- 关键帧动画
- 为提升性能的代理剪辑
- 色彩校正工具
- 音频混音
- 字幕制作器

# KEYBOARD SHORTCUTS

```
Space       Play/Pause
J/K/L       Shuttle control
I/O         Set in/out points
V           Selection tool
X           Razor tool
S           Split clip
```

# CAVEATS

需要 KDE 库。4K 编辑对资源消耗较大。为提升性能建议使用代理剪辑。稳定性因版本而异。

# HISTORY

Kdenlive 由 **Jason Wood** 于 **2002** 年发起，此后一直由 KDE 社区持续开发。它已成为 Linux 上功能最强大的开源视频编辑器之一。

# INSTALL

```apt: sudo apt install kdenlive```

```dnf: sudo dnf install kdenlive```

```pacman: sudo pacman -S kdenlive```

```apk: sudo apk add kdenlive```

```zypper: sudo zypper install kdenlive```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ffmpeg](/man/ffmpeg)(1), [melt](/man/melt)(1), [openshot](/man/openshot)(1)
