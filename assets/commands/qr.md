# TAGLINE

在命令行生成二维码

# TLDR

**生成二维码**

```qr "[text]"```

**从标准输入生成**

```echo "[text]" | qr```

**输出为图像**

```qr --output=[qr.png] "[text]"```

# SYNOPSIS

**qr** [_options_] [_text_]

# PARAMETERS

_TEXT_
> 要编码的文本。

**--output** _FILE_
> 输出文件。

**-o** _FILE_
> 输出文件。

# DESCRIPTION

**qr** 是一款简单的命令行工具，用于根据文本输入生成二维码。它可以使用 Unicode 方块字符直接在终端显示二维码，或将其保存为图像文件，适合快速通过可扫描的码分享 URL、WiFi 凭据或其他短文本。

该工具接受文本作为命令行参数或从标准输入读取，因此可以在 Shell 管道中使用。不同的软件包中存在多种 **qr** 命令的实现。

# CAVEATS

存在多种实现。请检查已安装的版本。

# HISTORY

qr 提供从命令行**快速生成二维码**的能力。

# INSTALL

```apk: sudo apk add py3-qrcode```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[qrencode](/man/qrencode)(1), [zbarimg](/man/zbarimg)(1)
