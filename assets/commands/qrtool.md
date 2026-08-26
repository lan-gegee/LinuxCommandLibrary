# TAGLINE

用于编码和解码二维码的命令行工具

# TLDR

**将文本编码为二维码 PNG**

```qrtool encode "[text]" -o [output.png]```

**将文本编码为终端 ASCII 字符画**

```qrtool encode "[text]" -t ansi```

**从图像中解码二维码**

```qrtool decode [image.png]```

**编码为自定义颜色的 SVG**

```qrtool encode "[text]" -t svg --foreground "#000000" --background "#ffffff" -o [output.svg]```

**生成 Micro 二维码**

```qrtool encode "[text]" --variant micro -o [output.png]```

**从标准输入读取并输出二维码**

```echo "[text]" | qrtool encode -o [output.png]```

# SYNOPSIS

**qrtool** _command_ [_options_]

# PARAMETERS

**encode** _TEXT_
> 将文本编码为二维码。省略 TEXT 时从标准输入读取。

**decode** _FILE_
> 从图像文件中解码二维码。

**-t**, **--type** _FORMAT_
> 输出格式：png（默认）、svg、eps、pic、ansi、ascii、unicode 及其彩色变体。

**-o**, **--output** _FILE_
> 输出文件路径（省略时写入标准输出）。

**-r**, **--read-from** _FILE_
> 从文件而非命令行读取输入数据。

**--variant** _TYPE_
> 二维码类型：`normal`（默认）、`micro` 或 `rmqr`。

**--foreground** _COLOR_
> CSS 格式的前景色（默认：黑色）。

**--background** _COLOR_
> CSS 格式的背景色（默认：白色）。

**-v**, **--symbol-version** _N_
> 符号版本：normal 为 1-40，micro 为 1-4。省略时自动选择。

**-l**, **--error-correction-level** _LEVEL_
> 纠错级别：`l`、`m`、`q` 或 `h`。

**--mode** _MODE_
> 编码模式：`numeric`、`alphanumeric`、`byte` 或 `kanji`。

**--mask** _N_
> 掩模图案 0-7。省略时自动选择。

**-s**, **--size** _N_
> 光栅/矢量输出的模块像素大小。

**-m**, **--margin** _N_
> 边距宽度，单位为模块数（默认：normal 为 4，其他为 2）。

**--verbose**
> 将二维码元数据打印到标准错误。

# DESCRIPTION

**qrtool** 是一款命令行工具，用于将文本编码为二维码以及从图像中解码二维码。它支持多种输出格式，包括 PNG、SVG、EPS、ANSI 终端字符画和 Unicode，并支持标准二维码、Micro QR 和 rMQR 等变体。它从标准输入读取并向标准输出写入，便于集成到 Unix 管道中。

# HISTORY

**qrtool** 由 **sorairolake** 创建，使用 **Rust** 编写。

# INSTALL

```pacman: sudo pacman -S qrtool```

```zypper: sudo zypper install qrtool```

```brew: brew install qrtool```

```nix: nix profile install nixpkgs#qrtool```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[qrc](/man/qrc)(1), [qrencode](/man/qrencode)(1), [zbarimg](/man/zbarimg)(1)
