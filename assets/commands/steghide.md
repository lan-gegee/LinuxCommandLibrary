# TAGLINE

在图像和音频文件中隐藏数据

# TLDR

将数据**嵌入**图像

```steghide embed -cf [path/to/image.jpg] -ef [path/to/data.txt]```

从文件中**提取**数据

```steghide extract -sf [path/to/image.jpg]```

显示**文件信息**

```steghide info [path/to/file.jpg]```

以**最大压缩率**嵌入

```steghide embed -cf [path/to/image.jpg] -ef [path/to/data.txt] -z 9```

列出**加密算法**

```steghide encinfo```

以**指定的加密方式**嵌入

```steghide embed -cf [path/to/image.jpg] -ef [path/to/data.txt] -e blowfish cbc```

提取到**指定文件**

```steghide extract -sf [path/to/image.jpg] -xf [path/to/output.txt]```

# SYNOPSIS

**steghide** _command_ [_arguments_]

# COMMANDS

**embed**
> 将数据隐藏到载体文件（cover file）中

**extract**
> 从隐写文件（stego file）中取回隐藏数据

**info**
> 显示文件信息并检测嵌入的数据

**encinfo**
> 列出可用的加密算法和模式

# PARAMETERS

**-cf, --coverfile** _file_
> 用于嵌入的载体文件

**-ef, --embedfile** _file_
> 要嵌入的文件（省略时使用 stdin）

**-sf, --stegofile** _file_
> 隐写文件（extract 的输入，embed 的输出）

**-xf, --extractfile** _file_
> 提取数据的输出文件名

**-e, --encryption** _algo_ [_mode_]
> 加密算法和模式（默认：rijndael-128 cbc）

**-z, --compress** _level_
> 压缩级别 1-9

**-Z, --dontcompress**
> 跳过压缩

**-p, --passphrase** _pass_
> 提供口令

**-K, --nochecksum**
> 省略 CRC32 校验和

**-N, --dontembedname**
> 不嵌入原始文件名

**-f, --force**
> 覆盖现有文件

**-v, --verbose**
> 详细输出

**-q, --quiet**
> 抑制消息

# DESCRIPTION

**steghide** 是一款隐写工具，可将数据隐藏在 JPEG、BMP、WAV 和 AU 文件中。它会先压缩并加密秘密数据，然后将其嵌入到能保持载体文件统计特性的位置，从而增加检测难度。

该工具使用图论方法寻找最优嵌入位置。默认加密为 CBC 模式的 AES-128，配合用户提供的口令。嵌入数据的完整性通过 CRC32 校验和验证。

# CAVEATS

载体文件的容量取决于文件大小与内容；**info** 命令可显示可用空间。仅支持 JPEG、BMP、WAV 和 AU 格式作为载体文件。高度压缩的图像嵌入容量更小。强口令对安全至关重要。除非用 **-sf** 指定单独的输出文件，否则载体文件会被就地修改。

# HISTORY

**steghide** 由 **Stefan Hetzl** 创建，于 **2003 年**首次发布。它至今仍是最广泛使用的开源隐写工具之一，常用于 CTF 竞赛、安全研究和隐私保护场景。大多数 Linux 发行版的软件仓库中都提供该工具。

# INSTALL

```apt: sudo apt install steghide```

```dnf: sudo dnf install steghide```

```nix: nix profile install nixpkgs#steghide```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[stegsnow](/man/stegsnow)(1), [outguess](/man/outguess)(1), [openstego](/man/openstego)(1)
