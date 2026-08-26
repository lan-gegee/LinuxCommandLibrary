# TAGLINE

显示 PostgreSQL 安装配置

# TLDR

**显示所有配置**

```pg_config```

**显示客户端头文件的 include 目录**

```pg_config --includedir```

**显示库目录**

```pg_config --libdir```

**显示服务器端 include 目录**（用于扩展开发）

```pg_config --includedir-server```

**显示模块（pkglib）目录**

```pg_config --pkglibdir```

**显示版本**

```pg_config --version```

# SYNOPSIS

**pg_config** [_option_...]

# PARAMETERS

**--bindir**
> 用户可执行文件的位置。

**--docdir**
> 文档文件的位置。

**--htmldir**
> HTML 文档文件的位置。

**--includedir**
> 客户端接口所用 C 头文件的位置。

**--pkgincludedir**
> 其他 C 头文件的位置。

**--includedir-server**
> 服务器编程用 C 头文件的位置（构建扩展时需要）。

**--libdir**
> 目标代码库的位置。

**--pkglibdir**
> 可动态加载模块的位置。

**--localedir**
> 区域设置支持文件的位置。

**--mandir**
> 手册页的位置。

**--sharedir**
> 与架构无关的支持文件的位置。

**--sysconfdir**
> 全系统配置文件的位置。

**--pgxs**
> 扩展 makefile（pgxs.mk）的位置。

**--configure**
> 构建时传给 configure 脚本的选项。

**--cc**
> 构建 PostgreSQL 所用的 C 编译器。

**--cppflags**
> 构建 PostgreSQL 时使用的 CPPFLAGS 值。

**--cflags**
> 构建 PostgreSQL 时使用的 CFLAGS 值。

**--cflags_sl**
> 构建 PostgreSQL 时使用的 CFLAGS_SL 值。

**--ldflags**
> 构建 PostgreSQL 时使用的 LDFLAGS 值。

**--ldflags_ex**
> 构建 PostgreSQL 时使用的 LDFLAGS_EX 值。

**--ldflags_sl**
> 构建 PostgreSQL 时使用的 LDFLAGS_SL 值。

**--libs**
> 构建 PostgreSQL 时使用的 LIBS 值。

**--version**
> PostgreSQL 的版本。

**-?**, **--help**
> 显示关于 pg_config 命令行参数的帮助。

# DESCRIPTION

**pg_config** 打印当前安装的 PostgreSQL 版本的配置参数。它的设计用途之一，是供希望对接 PostgreSQL 的软件包快速定位所需的头文件和库。它显示安装路径和构建选项。对编译扩展（经由 PGXS）和定位 PostgreSQL 各组件来说必不可少。

不带任何参数调用时，**pg_config** 会打印所有已知设置。指定一个或多个选项则会把输出限定为这些值。

# INSTALL

```apt: sudo apt install libpq-dev```

```apk: sudo apk add libpq-dev```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[postgres](/man/postgres)(1), [psql](/man/psql)(1)
