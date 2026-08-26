# TAGLINE

快速且用户友好的构建系统

# TLDR

**设置构建目录**

```meson setup [builddir]```

**带选项进行配置**

```meson setup [builddir] -D[option=value]```

**编译项目**

```meson compile -C [builddir]```

**运行测试**

```meson test -C [builddir]```

**安装项目**

```meson install -C [builddir]```

**重新配置**

```meson configure [builddir] -D[option=value]```

**清空并重新配置构建目录**

```meson setup --wipe [builddir]```

**创建 release 构建**

```meson setup [builddir] --buildtype=release```

# SYNOPSIS

**meson** _command_ [_options_]

# PARAMETERS

_COMMAND_
> Meson 子命令（见下方列表）。

**init**
> 在当前目录为新项目创建一个最小化的 meson.build。

**setup** _DIR_
> 配置构建目录（规范的第一步）。

**compile** **-C** _DIR_
> 构建项目。

**test** **-C** _DIR_
> 运行项目的测试套件。

**install** **-C** _DIR_
> 将构建好的项目安装到配置的前缀路径。

**configure** _DIR_
> 在不删除构建目录的情况下修改现有构建目录的构建选项。

**dist**
> 创建带签名的源码发行包 tarball。

**introspect**
> 以 JSON 格式打印目标、测试、选项等信息的描述。

**subprojects**, **wrap**
> 管理 meson 子项目和 **.wrap** 依赖文件。

**devenv**
> 启动一个已预设构建环境变量（如 **PATH**、**PKG_CONFIG_PATH**）的 shell。

**rewrite**
> 以编程方式修改 **meson.build** 文件。

**env2mfile**
> 根据当前环境变量生成交叉编译或本地编译定义文件。

**format**
> 自动格式化 **meson.build** 文件（别名 **fmt**）。

**-D** _OPT=VAL_
> 设置构建选项（例如 **-Dbuildtype=release**、**-Dprefix=/usr**）。

**--buildtype** _TYPE_
> 构建类型：**plain**、**debug**、**debugoptimized**、**release**、**minsize**、**custom**。

**--prefix** _PATH_
> 安装前缀（默认 **/usr/local**）。

**--backend** _BACKEND_
> 要生成的后端：**ninja**（默认）、**vs**、**vs2017**、**xcode** 等。

**--default-library** _TYPE_
> 默认库类型：**static**、**shared** 或 **both**。

**--cross-file** _FILE_
> 使用交叉编译定义文件。

**--native-file** _FILE_
> 覆盖主机上的本机编译器/工具选择。

**--reconfigure**
> 使用已保存的选项重新运行配置，不删除构建目录。

**--wipe**
> 清空并重新配置现有的构建目录。

**--werror**, **--warnlevel** _N_
> 将警告视为错误，或设置编译器警告级别（0-3/everything）。

**--optimization** _LEVEL_
> 优化级别（**0**、**g**、**1**、**2**、**3**、**s**）。

**--vsenv**
> 在 Windows 上构建前激活 Visual Studio 环境。

**--help**
> 显示帮助信息。

# DESCRIPTION

**meson** 是一个追求快速和用户友好的构建系统。它读取 **meson.build** 项目定义，并生成后端构建文件（默认为 ninja）用于实际编译。

Meson 支持 C、C++、Rust、Java、Fortran 等语言。它具有自动依赖检测、交叉编译支持以及内置的单元测试和覆盖率基础设施。GNOME、systemd、X.Org 和 Mesa 等项目都在使用它。

# CAVEATS

默认需要 Python 3 和 ninja 后端。构建目录不能在不同源码目录之间复用。只支持源外构建（不能在源码树内构建）。--wipe 标志会销毁并重建构建目录。

# HISTORY

Meson 由 **Jussi Pakkanen** 于 2013 年创建，是一个快速且用户友好的构建系统。

# INSTALL

```dnf: sudo dnf install meson```

```pacman: sudo pacman -S meson```

```apk: sudo apk add meson```

```zypper: sudo zypper install meson```

```brew: brew install meson```

```nix: nix profile install nixpkgs#meson```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ninja](/man/ninja)(1), [cmake](/man/cmake)(1), [make](/man/make)(1)
