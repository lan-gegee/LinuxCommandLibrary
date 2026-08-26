# TAGLINE

GNOME 的简易光栅图像编辑器

# TLDR

**启动** Drawing

```drawing```

打开**指定文件**

```drawing [path/to/image1] [path/to/image2]```

在**新窗口**中打开

```drawing --new-window [path/to/image1] [path/to/image2]```

# SYNOPSIS

**drawing** [_options_] [_files_]

# DESCRIPTION

**drawing** 是一款为 GNOME 桌面环境设计的简易光栅图像编辑器。它提供基础的绘图和编辑工具，包括铅笔、橡皮、直线、弧线、形状、文本和选区工具，并支持裁剪、缩放和旋转。

这款应用填补了基础截图标注与 GIMP 等全功能图像编辑器之间的空白。它非常适合快速修改图片、给截图添加箭头和文字、绘制简单示意图，或对现有图片做基本调整。

Drawing 支持包括 PNG、JPEG 和 BMP 在内的常见图像格式，足以胜任日常图像编辑任务，又没有专业图形软件的复杂度。

# PARAMETERS

**--new-window**
> 在新窗口中打开文件

_files_
> 要打开的图像文件

# CAVEATS

Drawing 是一款**光栅**编辑器，放大图像会损失画质，也没有任何类似矢量对象的东西：需要在任意尺寸下保持清晰的内容请使用 Inkscape。它不支持图层——这是用户最想念的功能——也没有色彩管理、调节曲线或插件系统。这是刻意的功能取舍而非疏漏；超出快速修改范围的工作应交给 GIMP 或 Krita。

它是一款为 GNOME 构建的 GTK 应用。虽然也能在其他桌面上运行，但它主要以 **Flatpak** 形式分发，因此发行版自有仓库中的版本往往落后很多。

# HISTORY

Drawing 由 **Romain Vigier**（maoschanz）于 **2018 年**前后创建，是一款刻意保持简单的 GNOME 光栅编辑器。其公开宣称的灵感来自老式微软画图：一个能瞬间打开、让你往截图上涂个箭头、然后不碍事的应用。这个定位确有需求，因为 GNOME 此前没有同类工具，而用 GIMP 解决轻量问题实在是大材小用。它后来被适配到手机上运行，并在一些移动 Linux 发行版中作为默认图像编辑器随系统发布。

# INSTALL

```apt: sudo apt install drawing```

```dnf: sudo dnf install drawing```

```pacman: sudo pacman -S drawing```

```apk: sudo apk add drawing```

```zypper: sudo zypper install drawing```

```nix: nix profile install nixpkgs#drawing```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gimp](/man/gimp)(1), [inkscape](/man/inkscape)(1), [krita](/man/krita)(1), [pinta](/man/pinta)(1)

# RESOURCES

```[Source code](https://github.com/maoschanz/drawing)```

```[Homepage](https://apps.gnome.org/Drawing/)```

<!-- verified: 2026-07-14 -->
