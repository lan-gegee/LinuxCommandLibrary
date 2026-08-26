# TAGLINE

显示媒体文件的技术信息

# TLDR

**显示媒体信息**

```mediainfo [video.mp4]```

**完整信息**

```mediainfo -f [video.mp4]```

以 JSON 格式**输出**

```mediainfo --Output=JSON [video.mp4]```

以 XML 格式**输出**

```mediainfo --Output=XML [video.mp4]```

**显示特定参数**

```mediainfo --Inform="Video;%Width%x%Height%" [video.mp4]```

**比较文件**

```mediainfo [file1.mp4] [file2.mp4]```

# SYNOPSIS

**mediainfo** [_options_] _file_

# PARAMETERS

_FILE_
> 要分析的媒体文件。

**-f**
> 完整信息。

**--Output** _FORMAT_
> 输出格式（XML、JSON、CSV）。

**--Inform** _TEMPLATE_
> 自定义输出模板。

**--Version**
> 显示版本。

**--help**
> 显示帮助信息。

# DESCRIPTION

**mediainfo** 用于显示媒体文件的技术信息，包括编解码器、码率、分辨率和元数据。

该工具支持视频、音频和图像格式，是媒体文件分析的必备工具。

# CAVEATS

只读。大文件支持因情况而异。某些格式需要额外的库。

# HISTORY

MediaInfo 由 **Jerome Martinez** 创建，旨在提供关于音频/视频文件的详细技术信息。

# INSTALL

```apt: sudo apt install mediainfo```

```dnf: sudo dnf install mediainfo```

```pacman: sudo pacman -S mediainfo```

```apk: sudo apk add mediainfo```

```zypper: sudo zypper install mediainfo```

```brew: brew install mediainfo```

```nix: nix profile install nixpkgs#mediainfo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ffprobe](/man/ffprobe)(1), [file](/man/file)(1), [exiftool](/man/exiftool)(1)
