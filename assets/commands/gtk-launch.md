# TAGLINE

通过 desktop 文件启动应用程序

# TLDR

**启动**应用程序

```gtk-launch [Application_name]```

显示**帮助**

```gtk-launch -h```

# SYNOPSIS

**gtk-launch** _application_ [_URI_...]

# PARAMETERS

_application_
> Desktop 文件名（不含 .desktop 扩展名）

_URI..._
> 供应用程序打开的可选 URI/文件

**-h**, **--help**
> 显示帮助信息

# DESCRIPTION

**gtk-launch** 使用来自标准 XDG 位置（/usr/share/applications、~/.local/share/applications 等）的 .desktop 文件启动应用程序。这相当于以编程方式点击应用程序图标。

application 参数是 desktop 文件 ID（去掉 .desktop 扩展名的文件名）。例如，**gtk-launch firefox** 启动 firefox.desktop 中定义的应用程序。

这对于在脚本中以与桌面环境无关的方式启动应用程序很有用，会遵循应用程序的 StartupNotify、exec 参数及其他 desktop 文件设置。

# CAVEATS

仅适用于有 .desktop 文件的应用程序。应用程序名称区分大小写，必须与 desktop 文件名完全一致（不含扩展名）。需要已安装 GTK 库。

# HISTORY

gtk-launch 是 GTK 命令行工具的一部分，提供了启动桌面应用程序的标准方式。它支持 XDG Desktop Entry 规范以实现跨桌面兼容性。

# INSTALL

```apt: sudo apt install libgtk-3-bin```

```apk: sudo apk add gtk+3.0```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xdg-open](/man/xdg-open)(1), [gio](/man/gio)(1), [desktop-file-validate](/man/desktop-file-validate)(1)
