# TAGLINE

显示音频文件的格式信息

# TLDR

**显示文件信息**

```soxi [audio.wav]```

**显示时长**

```soxi -D [audio.wav]```

**显示采样率**

```soxi -r [audio.wav]```

**显示通道数**

```soxi -c [audio.wav]```

**显示位深**

```soxi -b [audio.wav]```

**显示编码**

```soxi -e [audio.wav]```

**显示文件类型**

```soxi -t [audio.wav]```

**显示多个文件的总时长**

```soxi -T [file1.wav] [file2.wav]```

# SYNOPSIS

**soxi** [_-D_] [_-r_] [_-c_] [_-b_] [_options_] _files_

# PARAMETERS

**-D**
> 以秒为单位的时长。

**-d**
> 时间格式的时长。

**-r**
> 采样率。

**-c**
> 通道数。

**-b**
> 每采样位数。

**-e**
> 编码类型。

**-t**
> 文件类型。

**-s**
> 采样数。

**-V**[_level_]
> 设置详细程度。

**-T**
> 给定多个文件时输出总时长。

# DESCRIPTION

**soxi** 显示音频文件信息。它是 SoX（Sound eXchange）的一部分。

时长显示文件长度。可用秒或时间格式表示。

技术参数展示格式细节：采样率、位深、通道数。

可以查询多个文件。支持汇总总计。

输出可脚本化处理。返回单个值便于解析。

# CAVEATS

属于 SoX 套件的一部分。并非所有格式都受支持。元数据仅限于音频属性。

# HISTORY

**soxi** 是 **SoX**（Sound eXchange）——音频处理的"瑞士军刀"——的信息查询工具。由 Chris Bagwell 等人创建。

# INSTALL

```apt: sudo apt install sox```

```dnf: sudo dnf install sox```

```pacman: sudo pacman -S sox```

```apk: sudo apk add sox```

```zypper: sudo zypper install sox```

```brew: brew install sox```

```nix: nix profile install nixpkgs#sox```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sox](/man/sox)(1), [ffprobe](/man/ffprobe)(1), [mediainfo](/man/mediainfo)(1)
