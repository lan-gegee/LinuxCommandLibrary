# TAGLINE

DJ 混音软件

# TLDR

**启动 Mixxx**

```mixxx```

**打开指定文件**

```mixxx [music.mp3]```

**全屏模式**

```mixxx --fullScreen```

**指定设置路径**

```mixxx --settingsPath [/path/to/config]```

**调试模式**

```mixxx --debugAssertBreak```

# SYNOPSIS

**mixxx** [_options_] [_file_]

# PARAMETERS

_FILE_
> 要加载的音乐文件。

**--fullScreen**
> 全屏启动。

**--settingsPath** _DIR_
> 配置目录。

**--midiDebug**
> 启用 MIDI 调试。

**--resourcePath** _DIR_
> 资源路径。

**--help**
> 显示帮助信息。

# DESCRIPTION

**mixxx** 是 DJ 混音软件。它提供带控制器支持的数字 DJ 功能。

该工具提供节拍检测、效果器和媒体库管理。支持 MIDI 控制器。

# CAVEATS

音频延迟各异。需要控制器映射。资源消耗较高。

# HISTORY

Mixxx 始于 2001 年，作为 Traktor 等商业 **DJ 软件**的开源替代品。

# INSTALL

```apt: sudo apt install mixxx```

```dnf: sudo dnf install mixxx```

```pacman: sudo pacman -S mixxx```

```apk: sudo apk add mixxx```

```zypper: sudo zypper install mixxx```

```nix: nix profile install nixpkgs#mixxx```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[audacity](/man/audacity)(1), [ardour](/man/ardour)(1)
