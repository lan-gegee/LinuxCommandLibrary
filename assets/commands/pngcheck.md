# TAGLINE

校验 PNG 文件的完整性与结构

# TLDR

**检查 PNG 文件**完整性

```pngcheck [image.png]```

**详细**输出（逐个数据块的细节）

```pngcheck -v [image.png]```

**检查多个文件**

```pngcheck [*.png]```

**彩色**输出

```pngcheck -c [image.png]```

**打印文本数据块**（标题、注释等）

```pngcheck -t [image.png]```

**安静模式** - 仅显示错误

```pngcheck -q [image.png]```

在文件中**搜索内嵌的 PNG**

```pngcheck -s [file]```

# SYNOPSIS

**pngcheck** [**-cfpqstvx7**] _file_...

# PARAMETERS

_FILE_
> 要检查的 PNG、JNG 或 MNG 文件。

**-v**
> 详细模式；显示每个数据块的信息。

**-c**
> 对文本输出着色。

**-f**
> 遇到重大错误后仍强制继续。

**-p**
> 打印 PLTE、tRNS、hIST、sPLT 和 PPLT 数据块的内容。

**-q**
> 安静模式；仅显示错误和警告。

**-s**
> 在文件中搜索子图像（内嵌的 PNG/MNG）。

**-t**
> 打印 tEXt、zTXt 和 iTXt 文本数据块的内容。

**-x**
> 搜索并提取子图像（与 **-s** 搭配使用）。

**-7**
> 以 7 位纯 ASCII 打印 tEXt 数据块（转义高位字节）。

**--help**
> 显示帮助信息。

# DESCRIPTION

**pngcheck** 校验 PNG、JNG 和 MNG 图像文件的完整性与结构。它会验证 CRC 校验和、检查数据块的排列顺序，并报告结构性错误或损坏。

在详细模式下，它会列出每个数据块的尺寸、颜色类型、位深、压缩方法和滤波类型。配合 **-t** 可打印内嵌的文本元数据（tEXt、zTXt、iTXt）。配合 **-s** 可以定位其他文件中内嵌的 PNG/MNG 图像，**-x** 则能将其提取出来。

# CAVEATS

支持 PNG/JNG/MNG 格式。只读分析工具。

# HISTORY

pngcheck 是为 **PNG 文件验证**和检查而创建的工具。

# INSTALL

```apt: sudo apt install pngcheck```

```dnf: sudo dnf install pngcheck```

```zypper: sudo zypper install pngcheck```

```brew: brew install pngcheck```

```nix: nix profile install nixpkgs#pngcheck```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pngcrush](/man/pngcrush)(1), [optipng](/man/optipng)(1), [file](/man/file)(1)
