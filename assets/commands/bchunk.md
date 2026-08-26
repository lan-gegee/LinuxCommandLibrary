# TAGLINE

将 BIN/CUE 光盘镜像转换为 ISO 和音轨

# TLDR

将二进制光盘镜像**转换**为 ISO

```bchunk [path/to/image.bin] [path/to/image.cue] [path/to/output]```

以**详细模式**转换

```bchunk -v [path/to/image.bin] [path/to/image.cue] [path/to/output]```

以 **WAV 格式**输出音频文件

```bchunk -w [path/to/image.bin] [path/to/image.cue] [path/to/output]```

# SYNOPSIS

**bchunk** [_options_] _image.bin_ _image.cue_ _output_

# DESCRIPTION

**bchunk** 将 BIN/CUE 格式的光盘镜像转换为标准 ISO 9660 镜像和音轨。它读取 CUE 索引表来确定轨道布局，并将每条轨道提取为单独的文件。

数据轨被转换为 ISO 格式，而音轨可以输出为原始 CDR 音频或 WAV 文件。输出文件以指定的前缀命名并顺序编号。

# PARAMETERS

**-v**
> 详细模式；显示详细的进度信息

**-w**
> 将音轨输出为 WAV 文件而非原始 CDR

**-r**
> 原始模式；不将数据轨转换为 ISO 格式

**-p**
> 对某些光盘类型使用 PSX（PlayStation）模式

**-s**
> 交换音轨中的字节序

# CAVEATS

BIN 文件必须与 CUE 索引表描述的布局完全一致。多区段光盘可能无法正确转换。某些受保护或非标准的光盘镜像可能转换失败。

# HISTORY

**bchunk**（BIN/CUE CHunK）的开发初衷是将专有的光盘镜像格式转换为刻录软件和模拟器可用的标准格式。

# INSTALL

```apt: sudo apt install bchunk```

```dnf: sudo dnf install bchunk```

```pacman: sudo pacman -S bchunk```

```zypper: sudo zypper install bchunk```

```brew: brew install bchunk```

```nix: nix profile install nixpkgs#bchunk```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[cdrdao](/man/cdrdao)(1), [wodim](/man/wodim)(1)
