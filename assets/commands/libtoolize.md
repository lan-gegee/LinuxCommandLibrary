# TAGLINE

通过复制必要的辅助文件为软件包使用 libtool 做准备

# TLDR

使用复制和强制模式为项目初始化 **libtool**

```libtoolize --copy --force```

# SYNOPSIS

**libtoolize** [_options_]

# DESCRIPTION

**libtoolize** 通过将必要的辅助文件（ltmain.sh、config.guess 等）复制到项目目录中，为软件包使用 libtool 做好准备。它将 libtool 无缝集成到基于 autotools 的构建系统中。

# PARAMETERS

**-c, --copy**
> 复制文件而不是创建符号链接

**-f, --force**
> 覆盖已有文件

**-i, --install**
> 安装 libtool 支持文件

**-n, --dry-run**
> 显示将要执行的操作但不实际执行

**--automake**
> 与 automake 配合时静默工作

**--ltdl**
> 安装 libltdl 支持文件

# CAVEATS

在设置 autotools 项目时应先于 autoreconf 或 aclocal 运行。它会创建或修改 m4 宏文件。

# INSTALL

```dnf: sudo dnf install libtool```

```pacman: sudo pacman -S libtool```

```apk: sudo apk add libtool```

```zypper: sudo zypper install libtool```

```brew: brew install libtool```

```nix: nix profile install nixpkgs#libtool```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[libtool](/man/libtool)(1), [autoreconf](/man/autoreconf)(1), [automake](/man/automake)(1)
