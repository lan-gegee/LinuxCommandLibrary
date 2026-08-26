# TAGLINE

极简的 suckless WebKit 网页浏览器

# TLDR

**打开 URL**

```surf [https://example.com]```

**嵌入 tabbed** 以支持标签页

```tabbed surf -e```

**以指定窗口几何尺寸打开**

```surf -g [800x600] [https://example.com]```

**以全屏模式打开**

```surf -F [https://example.com]```

**禁用 JavaScript**

```surf -s [https://example.com]```

**禁用图像和 Cookie**

```surf -i -k [https://example.com]```

按窗口 ID 将 surf **嵌入另一个窗口**

```surf -e [window_id] [https://example.com]```

将 X 窗口 ID **打印到标准输出**（便于脚本化）

```surf -x [https://example.com]```

# SYNOPSIS

**surf** [_options_] [_URI_]

# PARAMETERS

**-b**
> 禁用滚动条。

**-c** _file_
> 指定 cookie 文件。

**-d**
> 禁用磁盘缓存。

**-e** _winid_
> 嵌入到给定 ID 的窗口中。

**-f**
> 以窗口模式启动（非全屏）。

**-F**
> 以全屏模式启动。

**-g** _geometry_
> 设置窗口几何尺寸（WIDTHxHEIGHT）。

**-i**
> 禁用图像。

**-I**
> 启用图像（默认）。

**-k**
> 禁用 Cookie。

**-K**
> 启用 Cookie（默认）。

**-m**
> 禁止从指定文件应用样式。

**-M**
> 允许从指定文件应用样式。

**-n**
> 禁用 Web Inspector（开发者工具）。

**-N**
> 启用 Web Inspector（开发者工具）。

**-p**
> 禁用插件。

**-P**
> 启用插件（默认）。

**-r** _file_
> 指定脚本文件。

**-s**
> 禁用 JavaScript。

**-S**
> 启用 JavaScript（默认）。

**-t** _file_
> 指定样式文件。

**-v**
> 显示版本信息。

**-x**
> 将 X 窗口 ID 打印到标准输出。

# DESCRIPTION

**surf** 是来自 suckless 项目的极简网页浏览器。它基于 WebKit/GTK+，遵循 suckless 的简洁、清晰、节俭哲学。

该浏览器没有工具栏或地址栏等图形界面元素。导航完全通过键盘快捷键和 **dmenu** 等外部工具完成。使用 Ctrl+g 输入新 URL，Ctrl+y 复制当前 URL，Ctrl+p 打开剪贴板中的 URL。

按照 suckless 的方式，配置需要编辑 config.h 源文件并重新编译。要使用标签页浏览，可配合随附的 surf.sh 脚本使用 **tabbed** 工具。

源代码刻意控制在 2000 行以内，以保证可读性和可审计性。

# CAVEATS

需要 GTK+ 和 WebKit 库。没有内置标签页支持；标签页需配合 tabbed 使用。配置需要修改源码并重新编译。安装 dmenu 才能获得地址栏功能。与主流浏览器相比功能有限。

# HISTORY

**surf** 是 suckless 项目的产物之一，该项目出品的软件强调极简与清晰。它体现了"把一件事做好"的 Unix 哲学：显示网页。对于偏好键盘驱动界面和最小资源占用的用户来说，它是一个轻量级选择。

# INSTALL

```apt: sudo apt install surf```

```dnf: sudo dnf install surf```

```apk: sudo apk add sxmo-surf```

```nix: nix profile install nixpkgs#surf```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dmenu](/man/dmenu)(1), [st](/man/st)(1), [dwm](/man/dwm)(1), [firefox](/man/firefox)(1), [chromium](/man/chromium)(1), [xprop](/man/xprop)(1)
