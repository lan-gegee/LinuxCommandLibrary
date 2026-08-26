# TAGLINE

将 PPM 图像序列编码为 MPEG 视频

# TLDR

**使用参数文件将 PPM 帧编码为 MPEG**

```ppmtompeg [path/to/param_file]```

**编码并输出统计信息**

```ppmtompeg -stat [path/to/stats.txt] [path/to/param_file]```

**静默编码**只显示错误

```ppmtompeg -realquiet [path/to/param_file]```

**编码指定的帧范围**

```ppmtompeg -frames [0] [99] [path/to/param_file]```

# SYNOPSIS

**ppmtompeg** [_options_] _parameter_file_

# PARAMETERS

_parameter_file_
> 包含编码参数的文件。

**-stat** _file_
> 将编码统计信息追加到文件。

**-realquiet**
> 抑制除错误外的所有输出。

**-quiet** _n_
> 将剩余时间报告限制为每 n 秒一次。

**-no_frame_summary**
> 抑制每帧的摘要行。

**-float_dct**
> 使用更精确但更慢的浮点 DCT。

**-gop** _num_
> 只编码指定编号的 GOP。

**-combine_gops**
> 将分离的 GOP 文件合并为单个 MPEG 流。

**-frames** _first_ _last_
> 只编码指定的帧范围。

**-combine_frames**
> 将单独的 MPEG 帧合并为一个流。

**-nice**
> 以低优先级运行远程进程。

**-snr**
> 在统计信息中包含信噪比。

# DESCRIPTION

**ppmtompeg** 将 PPM 图像序列编码为 MPEG-1 视频比特流。所有编码设置（输入文件、输出文件、帧模式、GOP 大小、质量）都在参数文件中指定，而不是在命令行上。参数文件格式区分大小写，使用 INPUT_DIR、PATTERN、GOP_SIZE、BASE_FILE_FORMAT 等关键字。属于 Netpbm 工具集。-gop、-combine_gops、-frames 和 -combine_frames 选项互斥。

# CAVEATS

过时的编码器。现代视频编码请考虑使用 ffmpeg。

# INSTALL

```apt: sudo apt install netpbm```

```dnf: sudo dnf install netpbm```

```pacman: sudo pacman -S netpbm```

```apk: sudo apk add netpbm```

```zypper: sudo zypper install netpbm```

```brew: brew install netpbm```

```nix: nix profile install nixpkgs#netpbm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ffmpeg](/man/ffmpeg)(1)
