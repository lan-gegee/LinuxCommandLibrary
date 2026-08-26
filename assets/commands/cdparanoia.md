# TAGLINE

带纠错功能的 CD 音频抓轨工具

# TLDR

**将整张 CD 抓取为 WAV 文件**

```cdparanoia -B```

**抓取指定音轨**

```cdparanoia [5] [track05.wav]```

**抓取音轨范围**

```cdparanoia [1-5]```

**查询 CD 目录表**

```cdparanoia -Q```

**输出原始 PCM 数据**

```cdparanoia -r [1] [track.raw]```

**详细输出**

```cdparanoia -v [1]```

# SYNOPSIS

**cdparanoia** [_options_] _span_ [_outfile_]

# DESCRIPTION

**cdparanoia** 是一款具备高级纠错和抖动（jitter）处理能力的 CD 数字音频提取工具。它从支持 CDDA 的光驱中读取音频轨道，并执行校验、同步和划痕重建，尽可能产生逐位精确（bit-perfect）的抓取结果。

与简单的 CD 抓轨器不同，cdparanoia 通过多次读取并对数据做互相关分析，来检测并纠正由划痕、污渍或光驱缺陷造成的错误。进度显示用笑脸表示读取质量，从正常运行到划痕检测乃至纠正失败都有对应符号。

输出格式包括 WAV（默认）、AIFF、AIFF-C 以及原始 16 位 PCM。批量模式（`-B`）会自动按音轨边界把输出拆分为多个文件。

# PARAMETERS

**-B**, **--batch**
> 批量模式，在音轨边界处拆分输出

**-Q**, **--query**
> 查询并打印 CD 目录表

**-d** _device_, **--force-cdrom-device** _device_
> 指定 CD-ROM 设备

**-v**, **--verbose**
> 详细输出，用于调试

**-q**, **--quiet**
> 安静模式运行

**-w**, **--output-wav**
> 输出 WAV 格式（默认）

**-a**, **--output-aiff**
> 输出 AIFF 格式

**-r**, **--output-raw**
> 输出原始 16 位 PCM

**-R**, **--output-raw-big-endian**
> 输出大端序原始 PCM

**-c**, **--output-aifc**
> 输出 AIFF-C 格式

**-f**, **--force-cdrom-little-endian**
> 强制将光驱视为小端序。

**-F**, **--force-cdrom-big-endian**
> 强制将光驱视为大端序。

**-g** _device_, **--force-generic-device** _device_
> 强制对指定设备使用旧的通用 SCSI（sg）接口。

**-S** _speed_, **--force-read-speed** _speed_
> 设置光驱的读取速度（在支持的情况下）。

**-A**, **--analyze-drive**
> 对光驱的缓存、时序和读取行为进行完整分析并记录日志。

**-z**, **--never-skip**
> 从不跳过读取失败的区块，无限重试。

**-Z**, **--disable-paranoia**
> 禁用所有数据校验和纠错功能。

**-X**, **--abort-on-skip**
> 若因数据不完美而跳过读取，则中止该音轨的读取。

# SPAN FORMAT

**N**: 第 N 条音轨

**N-M**: 第 N 到第 M 条音轨

**N-**: 第 N 条音轨到最后

**-M**: 开头到第 M 条音轨

# PROGRESS SYMBOLS

**:-)** 正常运行，抖动较小

**:-|** 抖动明显

**:-(** 检测到划痕

**;-(** 放弃纠正

**:^D** 完成

# CAVEATS

需要支持 CDDA 的光驱。对不缓存音频、支持 Accurate Stream 的光驱效果最佳。有划痕的光盘可能导致读取时间过长。

# INSTALL

```apt: sudo apt install cdparanoia```

```dnf: sudo dnf install cdparanoia```

```pacman: sudo pacman -S cdparanoia```

```apk: sudo apk add cdparanoia```

```zypper: sudo zypper install cdparanoia```

```nix: nix profile install nixpkgs#cdparanoia```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[abcde](/man/abcde)(1), [lame](/man/lame)(1), [flac](/man/flac)(1), [sox](/man/sox)(1)
