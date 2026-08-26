# TAGLINE

全屏显示文本消息

# TLDR

**全屏显示一条消息**

```sm "Hello World!"```

以**反色**显示

```sm -i "Hello World!"```

自定义**前景色**

```sm -f blue "Hello World!"```

自定义**背景色**

```sm -b "#008888" "Hello World!"```

**旋转**显示（90 度的倍数）

```sm -r 3 "Hello World!"```

从**管道**输入显示

```echo "Hello World!" | sm -```

**信息亭模式**（非交互）

```sm -k "Message"```

# SYNOPSIS

**sm** [_OPTIONS_] [_text_|-]

# PARAMETERS

**-f, --foreground** _color_
> 设置文字颜色（颜色名或 #RRGGBB 之类的十六进制码）

**-b, --background** _color_
> 设置背景色

**-i, --invert**
> 交换前景色和背景色

**-r, --rotate** _n_
> 旋转显示（n * 90 度，逆时针）

**-k, --kiosk**
> 非交互模式（忽略除 Ctrl-Q 外的所有输入）

**-n, --font** _fontspec_
> 指定字体族

**-a, --align** _alignment_
> 文本对齐：0=居中、1=左对齐、2=右对齐

**-m, --markup**
> 启用 Pango markup XML 格式

**-**
> 从标准输入读取文本

**-h, --help**
> 显示帮助

**-V, --version**
> 显示版本

# DESCRIPTION

**sm**（screen-message）将文字尽可能大地显示在屏幕上，并自动缩放以填满可用空间。它会创建一个全屏窗口来展示消息，适用于演示、标牌或在活动现场展示信息。

在交互模式下，用户可以直接输入来编辑所显示的文字。按 **Escape** 清空文字，按 **Ctrl-I** 反转颜色，按 **Ctrl-Q** 或双击 Escape 退出。通过 **-** 从 stdin 读取时，显示会在换页符（\f）处更新。

# CAVEATS

需要图形显示（X11 或 Wayland）。文字大小自动调整；很长的消息会导致字体变小。信息亭模式下禁用交互式编辑。字体的可用性取决于系统安装情况。

# HISTORY

**sm**（screen-message）由 **Joachim Breitner**（nomeata）创建，是一个简单的显示工具。它曾被用于 Debian 会议和其他活动上的照片展示与标牌。该工具可用于 Linux、Windows，也有 Web 应用版本。以 GPL-2.0 许可证发布。

# INSTALL

```apt: sudo apt install sm```

```apk: sudo apk add screen-message```

```zypper: sudo zypper install screen-message```

```nix: nix profile install nixpkgs#screen-message```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[figlet](/man/figlet)(6), [toilet](/man/toilet)(1), [banner](/man/banner)(1)
