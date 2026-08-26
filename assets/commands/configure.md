# TAGLINE

Autotools 构建配置脚本

# TLDR

**以默认选项运行**

```./configure```

**设置安装前缀**

```./configure --prefix=[/usr/local]```

**启用或禁用特性**

```./configure --enable-[feature] --disable-[other]```

**指定依赖的路径**

```./configure --with-[lib]=[/path/to/lib]```

**显示所有选项**

```./configure --help```

**面向不同主机构建**

```./configure --host=[x86_64-linux-gnu]```

**设置编译器和旗标**

```CC=[gcc] CFLAGS="[-O2]" ./configure```

# SYNOPSIS

**./configure** [_options_] [_VAR=VALUE_...]

# DESCRIPTION

**configure** 是由 GNU Autotools 生成的 shell 脚本，用于让软件准备好在当前系统上构建。它会检测系统能力、检查依赖，并生成针对当前环境定制的 Makefile。

该脚本探测编译器、库、头文件和系统特性，把结果存入 config.h 并替换进 Makefile.in 模板。这使软件能够在不同的类 Unix 系统上便携地构建。

# PARAMETERS

**--prefix=** _path_
> 安装的根目录。

**--exec-prefix=** _path_
> 与架构相关的文件的存放位置。

**--bindir=** _path_
> 用户可执行文件目录。

**--libdir=** _path_
> 库目录。

**--includedir=** _path_
> 头文件目录。

**--enable-** _feature_
> 启用可选特性。

**--disable-** _feature_
> 禁用特性。

**--with-** _package_
> 使用外部软件包。

**--without-** _package_
> 不使用该软件包。

**--host=** _triplet_
> 面向目标平台交叉编译。

**--build=** _triplet_
> 构建系统类型。

**--help**
> 显示可用选项。

# ENVIRONMENT VARIABLES

**CC**: C 编译器命令
**CXX**: C++ 编译器命令
**CFLAGS**: C 编译器旗标
**LDFLAGS**: 链接器旗标
**PKG_CONFIG_PATH**: pkg-config 搜索路径

# CAVEATS

autoconf 文件变动后必须重新生成脚本。交叉编译需要仔细配置。某些软件包选项繁多，难以逐一排查。缺少依赖时构建可能失败。

# HISTORY

**configure** 脚本由 **GNU Autoconf** 生成，后者由 **David MacKenzie** 自 **1991** 年起开发。Autoconf 解决了软件在多样 Unix 系统间的可移植性难题。configure/make/make install 模式成为 Unix 软件分发的标准。虽然出现了更新的构建系统，Autotools 仍被广泛使用。

# SEE ALSO

[make](/man/make)(1), [autoconf](/man/autoconf)(1), [automake](/man/automake)(1), [pkg-config](/man/pkg-config)(1)

# RESOURCES

```[Source code](https://git.savannah.gnu.org/cgit/autoconf.git)```

```[Homepage](https://www.gnu.org/software/autoconf/)```

```[Documentation](https://www.gnu.org/software/autoconf/manual/)```

<!-- verified: 2026-06-23 -->
