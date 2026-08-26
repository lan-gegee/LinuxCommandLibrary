# TAGLINE

设置 KDE Plasma 桌面壁纸

# TLDR

**应用**壁纸

```plasma-apply-wallpaperimage [/path/to/image]```

以**填充模式**应用

```plasma-apply-wallpaperimage --fill-mode [preserveAspectCrop] [/path/to/image]```

显示**帮助**

```plasma-apply-wallpaperimage --help```

# SYNOPSIS

**plasma-apply-wallpaperimage** [**--fill-mode** _mode_] _image_path_

# PARAMETERS

**--fill-mode _mode_**
> 图像适配方式：stretch、preserveAspectFit、preserveAspectCrop、tile、tileVertically、tileHorizontally、pad

**image_path**
> 壁纸图像文件的路径

**--help**
> 显示帮助信息

# DESCRIPTION

**plasma-apply-wallpaperimage** 通过命令行设置 KDE Plasma 的桌面壁纸。它支持多种填充模式，控制图像如何缩放或平铺以适配屏幕。

该工具适合编写根据时间、天气或其他条件更换壁纸的脚本。

# CAVEATS

需要正在运行的 Plasma 会话。图像必须为受支持的格式（PNG、JPG 等）。默认应用到所有桌面/显示器。

# HISTORY

**plasma-apply-wallpaperimage** 是 **KDE Plasma Workspace** 的一部分，与其他 plasma-apply 工具一起提供可脚本化的壁纸控制。

# INSTALL

```apt: sudo apt install plasma-workspace```

```dnf: sudo dnf install plasma-workspace```

```pacman: sudo pacman -S plasma-workspace```

```apk: sudo apk add plasma-workspace```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[plasma-apply-colorscheme](/man/plasma-apply-colorscheme)(1), [feh](/man/feh)(1), [nitrogen](/man/nitrogen)(1)
