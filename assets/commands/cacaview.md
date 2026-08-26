# TAGLINE

在终端中将图片显示为 ASCII 艺术

# TLDR

将**图片**显示为 ASCII 艺术

```cacaview [path/to/image]```

# SYNOPSIS

**cacaview** [_options_] _image_

# DESCRIPTION

**cacaview** 使用 libcaca 库在终端中以 ASCII 艺术形式显示图片。它将图像文件转换为彩色文本字符，以便在文本模式环境中查看。

该查看器支持在显示的图像内导航和缩放。

# KEY BINDINGS

**n** / **p** 或 **PageDown** / **PageUp**
> 下一张 / 上一张图片。

**+** / **-**
> 放大 / 缩小。

**x**
> 重置视图。

**f**
> 切换全屏。

**d**
> 切换抖动（dithering）模式。

**a**
> 切换抗锯齿模式。

**q** 或 **Esc**
> 退出。

# INSTALL

```apt: sudo apt install caca-utils```

```dnf: sudo dnf install caca-utils```

```apk: sudo apk add libcaca-apps```

```zypper: sudo zypper install caca-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cacaclock](/man/cacaclock)(1), [cacademo](/man/cacademo)(1), [cacafire](/man/cacafire)(1), [img2txt](/man/img2txt)(1)
