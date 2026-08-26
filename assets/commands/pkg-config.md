# TAGLINE

查询库的编译器和链接器标志

# TLDR

**获取编译器标志**

```pkg-config --cflags [library]```

**获取链接器标志**

```pkg-config --libs [library]```

**获取全部标志**

```pkg-config --cflags --libs [library]```

**检查库是否存在**

```pkg-config --exists [library] && echo "Found"```

**获取库版本**

```pkg-config --modversion [library]```

**列出所有软件包**

```pkg-config --list-all```

# SYNOPSIS

**pkg-config** [_options_] [_packages_]

# PARAMETERS

_PACKAGES_
> 软件包名称。

**--cflags**
> 编译器标志。

**--libs**
> 链接器标志。

**--exists**
> 检查是否存在。

**--modversion**
> 显示版本。

**--list-all**
> 列出软件包。

**--atleast-version** _VERSION_
> 版本不低于 VERSION 时成功退出。

**--exact-version** _VERSION_
> 版本完全匹配时成功退出。

**--max-version** _VERSION_
> 版本不高于 VERSION 时成功退出。

**--variable** _NAME_
> 打印 .pc 文件中定义的变量的值。

**--libs-only-L**
> 仅打印 -L/-R 库搜索路径标志。

**--libs-only-l**
> 仅打印 -l 库名称标志。

**--cflags-only-I**
> 仅打印 -I 头文件搜索路径标志。

**--static**
> 输出静态链接所需的标志（包含私有依赖）。

**--print-errors**
> 找不到软件包时显示错误。

**--silence-errors**
> 抑制错误输出。

# DESCRIPTION

**pkg-config** 用于获取针对已安装库构建软件所需的编译器和链接器标志。它读取各库安装的 **.pc** 元数据文件，提供正确的头文件路径、库路径和链接标志。

autotools、CMake 和 Meson 等构建系统使用 pkg-config 以可移植的方式定位库。**--cflags** 返回编译器标志（头文件路径），**--libs** 返回链接器标志，**--modversion** 显示已安装版本。版本约束可用 **--atleast-version** 检查。

# CONFIGURATION

**PKG_CONFIG_PATH**
> 以冒号分隔的额外 .pc 文件搜索目录列表。

**PKG_CONFIG_LIBDIR**
> 完全覆盖默认的 .pc 文件搜索路径。

# CAVEATS

依赖 .pc 文件。自定义位置请设置 PKG_CONFIG_PATH。

# HISTORY

pkg-config 由 **James Henstridge** 于 **2001 年前后**作为 freedesktop.org 项目的一部分创建，旨在简化库的编译和链接。它广泛应用于 autotools、CMake 和 Meson 构建系统。

# INSTALL

```apt: sudo apt install pkgconf```

```dnf: sudo dnf install pkgconf```

```pacman: sudo pacman -S pkgconf```

```apk: sudo apk add pkgconf```

```zypper: sudo zypper install pkgconf```

```brew: brew install pkgconf```

```nix: nix profile install nixpkgs#pkgconf```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[make](/man/make)(1), [gcc](/man/gcc)(1), [pkgconf](/man/pkgconf)(1)
