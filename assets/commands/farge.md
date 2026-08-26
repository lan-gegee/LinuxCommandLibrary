# TAGLINE

X11 和 Wayland 屏幕取色器

# TLDR

显示**预览**并复制十六进制颜色值

```farge```

复制十六进制颜色值，**不显示**预览

```farge --no-preview```

将十六进制颜色值**输出**到 stdout

```farge --stdout```

输出 **RGB** 值到 stdout

```farge --rgb --stdout```

以**通知**形式显示并指定过期时间

```farge --notify --expire-time [5000]```

# SYNOPSIS

**farge** [_options_]

# DESCRIPTION

**farge** 选取并显示屏幕上特定像素的颜色。它可以以十六进制或 RGB 格式输出颜色，并将值复制到剪贴板。

适合设计者和开发者快速从屏幕任意位置采样颜色。

# PARAMETERS

**--no-preview**
> 不显示预览窗口

**--stdout**
> 输出到 stdout

**--rgb**
> 以 RGB 格式输出

**--notify**
> 以通知形式显示

**--expire-time** _ms_
> 通知过期时间（毫秒）

# CAVEATS

需要剪贴板和通知工具。借助相应的后端可在 X11 和 Wayland 上工作。

# INSTALL

```nix: nix profile install nixpkgs#farge```

<!-- packages: 2026-07-22 -->

# SEE ALSO
