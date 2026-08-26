# TAGLINE

用首选应用程序打开文件

# TLDR

在文件管理器中打开**当前目录**

```xdg-open .```

在默认浏览器中打开 **URL**

```xdg-open https://example.com```

在默认查看器中打开**图像**

```xdg-open path/to/image.png```

在默认查看器中打开 **PDF**

```xdg-open path/to/document.pdf```

在默认播放器中打开**视频**

```xdg-open path/to/video.mp4```

# SYNOPSIS

**xdg-open** _file_|_URL_

# DESCRIPTION

**xdg-open** 用用户的首选应用程序打开文件或 URL。它是 xdg-utils 软件包的一部分，通过检测当前运行的桌面环境并使用相应的方法，从而在不同桌面环境之间通用。

# PARAMETERS

**--help**
> 显示帮助信息

**--version**
> 显示版本信息

# SUPPORTED DESKTOP ENVIRONMENTS

xdg-open 会检测并使用以下桌面环境的适当方法：
- GNOME（gio open 或 gnome-open）
- KDE（kde-open 或 kfmclient）
- Xfce（exo-open）
- MATE（mate-open）
- Enlightenment（enlightenment_open）
- 通用回退方案（mimeopen）

# CAVEATS

文件或 URL 是异步打开的；xdg-open 会立即返回。所选应用程序取决于桌面的 MIME 类型关联。在没有桌面环境的系统上，它可能回退到基于文本的替代方案。

# HISTORY

**xdg-open** 是 **xdg-utils** 的一部分，后者是由 freedesktop.org 项目开发的一组桌面集成脚本，旨在为不同的 Linux 桌面环境提供一致的行为。

# INSTALL

```dnf: sudo dnf install xdg-utils```

```pacman: sudo pacman -S xdg-utils```

```apk: sudo apk add xdg-utils```

```zypper: sudo zypper install xdg-utils```

```nix: nix profile install nixpkgs#xdg-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xdg-mime](/man/xdg-mime)(1), [xdg-settings](/man/xdg-settings)(1), [gio](/man/gio)(1)
