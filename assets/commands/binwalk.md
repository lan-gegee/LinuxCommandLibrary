# TAGLINE

分析并提取固件镜像

# TLDR

**扫描**固件中的签名

```binwalk [firmware.bin]```

**提取**内嵌文件

```binwalk -e [firmware.bin]```

**熵**分析

```binwalk -E [firmware.bin]```

**递归**提取

```binwalk -Me [firmware.bin]```

**将**已知和未知内容**提取到磁盘**

```binwalk -c [firmware.bin]```

**列出**受支持的签名和提取器

```binwalk -L```

# SYNOPSIS

**binwalk** [_options_] _file_...

# DESCRIPTION

**binwalk** 是一款固件分析工具，用于在二进制镜像中搜索内嵌文件和可执行代码。它可以识别文件签名、压缩数据、文件系统以及固件镜像中常见的其他模式。

该工具是逆向工程、安全研究和固件修改的必备工具。

自版本 3（2024 年发布）起，binwalk 已完全用 Rust 重写，扫描速度大幅提升、误报更少，内置的提取器也更多。旧 Python 实现的一些选项（如 **--dd**、**--hexdump**、**--raw** 和 **--disasm**）已被移除或替换。

# PARAMETERS

**-e**, **--extract**
> 自动提取已识别的文件类型

**-M**, **--matryoshka**
> 递归扫描提取出的文件

**-c**, **--carve**
> 将已知和未知的文件内容都提取到磁盘

**-E**, **--entropy**
> 生成熵曲线图（使用 Plotly 渲染）

**-p**, **--png**
> 将熵曲线图保存为 PNG 文件

**-a**, **--search-all**
> 在所有偏移量处搜索所有签名

**-d**, **--directory** _path_
> 将文件和文件夹提取到自定义目录

**-t**, **--threads** _count_
> 手动指定使用的线程数

**-y**, **--include** _signatures_
> 只扫描给定的签名

**-x**, **--exclude** _signatures_
> 不扫描给定的签名

**-l**, **--log** _file_
> 将 JSON 结果记录到文件（'-' 表示 stdout）

**-L**, **--list**
> 列出受支持的签名和提取器

**-s**, **--stdin**
> 从标准输入读取数据

**-q**, **--quiet**
> 抑制常规 stdout 输出

**-v**, **--verbose**
> 递归提取时显示所有结果

# FEATURES

- 文件签名识别
- 内嵌文件系统检测
- 压缩数据检测
- 熵可视化
- 自动提取
- 自定义签名支持
- 插件系统

# WORKFLOW

```bash
# Scan firmware
binwalk firmware.bin

# Extract all files
binwalk -e firmware.bin

# Recursive extraction
binwalk -Me firmware.bin

# Entropy analysis (finds compressed/encrypted regions)
binwalk -E firmware.bin

# Extract into a custom directory
binwalk -e -d extracted/ firmware.bin
```

# COMMON FINDINGS

- **文件系统镜像**（squashfs、cramfs、jffs2）
- **引导加载程序**（U-Boot、LILO）
- **内核**（Linux、VxWorks）
- **压缩数据**（gzip、lzma、zlib）
- **证书与密钥**

# CAVEATS

对自定义格式的提取可能不奏效。加密区段表现为高熵。某些签名会产生误报。需要相应的提取工具（sasquatch、jefferson 等）。大型固件镜像处理较慢。

# HISTORY

**binwalk** 由 Craig Heffner 于约 **2010 年**创建，用于逆向工程和分析嵌入式设备的固件镜像，现由 ReFirmLabs 维护。版本 3 于 2024 年首次亮相，是一次基于 Rust 的完全重写。

# INSTALL

```dnf: sudo dnf install binwalk```

```pacman: sudo pacman -S binwalk```

```zypper: sudo zypper install binwalk```

```brew: brew install binwalk```

```nix: nix profile install nixpkgs#binwalk```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[foremost](/man/foremost)(1), [strings](/man/strings)(1), [file](/man/file)(1), [dd](/man/dd)(1), [hexdump](/man/hexdump)(1)

# RESOURCES

```[Source code](https://github.com/ReFirmLabs/binwalk)```

```[Homepage](https://github.com/ReFirmLabs/binwalk)```

<!-- verified: 2026-06-19 -->
