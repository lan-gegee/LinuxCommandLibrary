# TAGLINE

为 groff 输入处理转换编码

# TLDR

**为 groff 转换编码**

```preconv [file]```

**指定输入编码**

```preconv -e [utf-8] [file]```

**调试模式**

```preconv -d [file]```

# SYNOPSIS

**preconv** [_options_] [_files_]

# PARAMETERS

_FILES_
> 输入文件。

**-e** _ENCODING_
> 输入编码。

**-d**
> 调试输出。

**-r**
> 不添加 .lf 行。

# DESCRIPTION

**preconv** 是一个 groff 预处理器，用于将各种字符编码（UTF-8、Latin-1 等）的输入文件转换为 groff 可处理的格式。它将非 ASCII 字符翻译为 groff 转义序列，使 groff 能够处理 Unicode 及其他多字节编码。

该工具通常在需要时由 groff 自动调用，但也可以在预处理管道中显式使用。它通过 BOM 标记、coding 标签或区域设置来检测输入编码。

# CAVEATS

groff 预处理器。通常自动调用。

# HISTORY

preconv 是作为 **groff 预处理器**创建的，用于编码转换。

# INSTALL

```apt: sudo apt install groff-base```

```dnf: sudo dnf install groff-base```

```pacman: sudo pacman -S groff```

```apk: sudo apk add groff```

```zypper: sudo zypper install groff```

```brew: brew install groff```

```nix: nix profile install nixpkgs#groff```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[groff](/man/groff)(1), [troff](/man/troff)(1), [iconv](/man/iconv)(1)
