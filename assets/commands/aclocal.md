# TAGLINE

GNU 构建系统的 autoconf 宏收集器

# TLDR

从 configure.ac **生成** aclocal.m4

```aclocal```

在**额外目录**中查找宏

```aclocal -I [m4/]```

**打印**宏搜索目录

```aclocal --print-ac-dir```

生成时对过时宏给出**警告**

```aclocal --warnings=obsolete```

将第三方宏**安装**到本地 m4 目录

```aclocal -I [m4/] --install```

# SYNOPSIS

**aclocal** [_-I dir_] [_--output=file_] [_--warnings=category_] [_options_]

# DESCRIPTION

**aclocal** 是 GNU Automake 构建系统的一部分。它通过扫描 configure.ac（或 configure.in）中的宏调用，并从已安装的 .m4 文件中收集所需的宏定义，生成 aclocal.m4 文件。

生成的 aclocal.m4 文件包含 autoconf 处理 configure.ac 所需的全部 M4 宏。对于使用 GNU 构建系统（autotools）的项目而言，这个工具是连接 Automake 与 Autoconf 的桥梁，不可或缺。

# PARAMETERS

**-I** _dir_
> 将目录加入 .m4 文件的搜索路径

**--output=**_file_
> 将输出写入指定文件而非 aclocal.m4

**--print-ac-dir**
> 打印存放系统 .m4 文件的目录

**--warnings=**_category_
> 启用警告：syntax、unsupported、obsolete、all、none、error

**--install**
> 将第三方宏复制到本地 m4 目录（需配合 -I）

**--force**
> 总是重新生成输出文件

**--dry-run**
> 不实际创建或修改任何文件

**--verbose**
> 打印正在处理的文件的名称

**--version**
> 打印版本信息

**--help**
> 显示帮助信息

# CAVEATS

从源码构建时必须在 autoconf 之前运行。.m4 文件的搜索顺序很重要；用 -I 指定的本地目录会先于系统目录被搜索。configure.ac 发生更改后需要重新运行 aclocal。

# HISTORY

**aclocal** 作为 GNU Automake 的一部分由 David MacKenzie 和 Tom Tromey 创建，首次发布于 **1994** 年。它的设计目标是简化基于 Autoconf 的构建系统收集 M4 宏的过程。

# INSTALL

```dnf: sudo dnf install automake```

```pacman: sudo pacman -S automake```

```apk: sudo apk add automake```

```zypper: sudo zypper install automake```

```brew: brew install automake```

```nix: nix profile install nixpkgs#automake```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[autoconf](/man/autoconf)(1), [automake](/man/automake)(1), [autoreconf](/man/autoreconf)(1), [libtoolize](/man/libtoolize)(1), [make](/man/make)(1)
