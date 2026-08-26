# TAGLINE

从模板生成 configure 脚本

# TLDR

**生成** configure 脚本

```autoconf```

使用**指定模板**生成

```autoconf -o [configure] [configure.ac]```

**追踪** configure.ac 中的特定宏

```autoconf --trace=[AC_CHECK_LIB]```

显示**版本**

```autoconf --version```

# SYNOPSIS

**autoconf** [_-o output_] [_input_]

# DESCRIPTION

**autoconf** 从模板（configure.ac 或 configure.in）生成 configure 脚本。这些脚本会探测系统的可用特性、库和工具，生成适配构建环境的 Makefile。

Autoconf 是 GNU 构建系统（autotools）的一部分，被成千上万的开源项目使用。

# PARAMETERS

**-o** _file_
> 输出文件（默认：configure）

**-W** _category_
> 警告类别

**-I** _dir_
> 向搜索路径添加目录

**-f**, **--force**
> 强制重新生成

**-v**, **--verbose**
> 详细输出

**--trace=**_macro_
> 追踪 configure.ac 中的宏调用

**-B** _dir_
> 将目录添加到搜索路径最前面

# WORKFLOW

1. 编写 configure.ac
2. 运行 **autoconf** 生成 configure
3. 随源码一起分发 configure
4. 用户运行 ./configure 生成 Makefile

# CAVEATS

依赖 M4 宏处理器。语法基于 M4，较为复杂。生成的 configure 脚本体量很大。学习曲线陡峭。

# HISTORY

**Autoconf** 由 David MacKenzie 于 **1991 年**创建，用于解决 Unix 软件的可移植性问题。后来成为 GNU 及众多其他项目的标准构建系统。

# INSTALL

```dnf: sudo dnf install autoconf```

```pacman: sudo pacman -S autoconf```

```apk: sudo apk add autoconf```

```zypper: sudo zypper install autoconf```

```brew: brew install autoconf```

```nix: nix profile install nixpkgs#autoconf```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[automake](/man/automake)(1), [autoreconf](/man/autoreconf)(1), [configure](/man/configure)(1), [m4](/man/m4)(1), [libtool](/man/libtool)(1)
