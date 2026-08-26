# TAGLINE

配置动态链接器的运行时绑定

# TLDR

**更新符号链接并重建共享库缓存**

```sudo ldconfig```

**仅为特定目录更新符号链接**

```sudo ldconfig -n [path/to/directory]```

**打印缓存中的库并搜索特定库**

```ldconfig -p | grep [library_name]```

**以详细输出重建缓存**

```sudo ldconfig -v```

**使用备用配置文件**

```sudo ldconfig -f [path/to/ld.so.conf]```

# SYNOPSIS

**ldconfig** [_options_] [_directory_...]

# PARAMETERS

**-n**
> 仅处理指定的目录（不更新缓存）

**-p**, **--print-cache**
> 打印缓存中存储的库

**-v**, **--verbose**
> 详细模式

**-N**
> 不重建缓存

**-X**
> 不更新符号链接

**-f** _FILE_
> 使用指定的配置文件代替 /etc/ld.so.conf

**-C** _FILE_
> 使用指定的缓存文件代替 /etc/ld.so.cache。

**-r** _ROOT_
> 切换到并将 _ROOT_ 用作根目录。

**-l**
> 库模式。手动链接单个库。

# DESCRIPTION

**ldconfig** 配置动态链接器的运行时绑定。它会为在 /etc/ld.so.conf 所列目录、受信任目录（/lib 和 /usr/lib）以及命令行指定目录中找到的最新共享库创建必要的符号链接和缓存（存储在 /etc/ld.so.cache 中）。

运行时链接器（ld.so 或 ld-linux.so）使用该缓存快速解析共享库依赖，无需在加载时扫描目录。安装新的共享库或修改 /etc/ld.so.conf 之后，通常需要运行 ldconfig。

# CAVEATS

修改系统缓存需要 root 权限。安装新的共享库后必须运行它，动态链接器才能找到这些库。非标准路径中的库必须在 /etc/ld.so.conf 中列出或通过命令行传入。软件包管理器通常会在安装库软件包后自动运行 ldconfig。

# HISTORY

ldconfig 是 GNU C 库（glibc）的一部分，自共享库问世以来一直是 Linux 系统上动态链接的关键环节。

# INSTALL

```apt: sudo apt install libc-bin```

```apk: sudo apk add musl-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ldd](/man/ldd)(1), [ld.so](/man/ld.so)(8)
