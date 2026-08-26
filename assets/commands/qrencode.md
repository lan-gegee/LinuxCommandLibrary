# TAGLINE

将文本编码为二维码图像

# TLDR

**在终端生成二维码**

```qrencode -t ANSI "[text]"```

**生成 PNG 图像**

```qrencode -o [qr.png] "[text]"```

**生成 SVG 文件**

```qrencode -t SVG -o [qr.svg] "[text]"```

**设置模块像素大小**

```qrencode -s [10] -o [qr.png] "[text]"```

**设置自定义前景色和背景色**

```qrencode --foreground=[000000] --background=[FFFFFF] -o [qr.png] "[text]"```

**生成 Micro QR Code**

```qrencode -M -o [qr.png] "[text]"```

**从标准输入读取**

```echo "[text]" | qrencode -o [qr.png]```

# SYNOPSIS

**qrencode** [_options_] [_string_]

# PARAMETERS

_STRING_
> 要编码的文本。若省略则从标准输入读取。

**-o** _FILE_, **--output=**_FILE_
> 输出文件。使用 "-" 表示标准输出。

**-t** _TYPE_, **--type=**_TYPE_
> 输出类型：PNG、PNG32、SVG、EPS、XPM、ANSI、ANSI256、ASCII、ASCIIi、UTF8、UTF8i、ANSIUTF8、ANSIUTF8i、ANSI256UTF8。

**-s** _NUMBER_, **--size=**_NUMBER_
> 模块（点）大小，单位为像素（默认：3）。

**-l** {L|M|Q|H}, **--level=**{L|M|Q|H}
> 纠错级别，从 L（最低）到 H（最高）。默认：L。

**-v** _NUMBER_, **--symversion=**_NUMBER_
> 最小 QR 符号版本（默认：自动）。

**-m** _NUMBER_, **--margin=**_NUMBER_
> 边距宽度，单位为模块数（默认：4）。

**-d** _NUMBER_, **--dpi=**_NUMBER_
> PNG 输出的 DPI（默认：72）。

**-r** _FILE_, **--read-from=**_FILE_
> 从文件读取输入数据。

**-8**, **--8bit**
> 以 8 位模式编码全部数据。

**-M**, **--micro**
> 编码为 Micro QR Code。

**-i**, **--ignorecase**
> 忽略大小写，仅使用大写字符。

**--foreground=**_RRGGBB[AA]_
> 以十六进制设置前景色。

**--background=**_RRGGBB[AA]_
> 以十六进制设置背景色。

**--svg-path**
> 在 SVG 中使用单个 path 绘制模块。

**--inline**
> 生成不含 XML 声明的 SVG。

**--strict-version**
> 禁用自动版本调整。

**-V**, **--version**
> 显示版本号。

# DESCRIPTION

**qrencode** 是一款基于 libqrencode 库的命令行二维码生成器。它将文本编码为二维码，并以多种格式输出，包括 PNG、SVG、EPS、ANSI 终端字符画和 ASCII，既适合屏幕显示也适合打印用途。

选项可以控制纠错级别（L/M/Q/H）、QR 版本（决定容量和物理尺寸）以及光栅输出的模块大小。输入可以来自命令行参数或标准输入，便于集成到脚本和管道中。

# CAVEATS

最大数据容量取决于 QR 版本和纠错级别。纠错级别越高，容量越小。二进制数据可能需要 **-8** 标志启用 8 位模式。

# HISTORY

qrencode 由 **Kentaro Fukuchi** 编写，基于 **libqrencode** 库构建。它提供多种输出格式的命令行二维码生成能力。

# INSTALL

```apt: sudo apt install qrencode```

```dnf: sudo dnf install qrencode```

```pacman: sudo pacman -S qrencode```

```apk: sudo apk add libqrencode-tools```

```zypper: sudo zypper install qrencode```

```brew: brew install qrencode```

```nix: nix profile install nixpkgs#qrencode```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[zbarimg](/man/zbarimg)(1), [zbarcam](/man/zbarcam)(1), [qr](/man/qr)(1)
