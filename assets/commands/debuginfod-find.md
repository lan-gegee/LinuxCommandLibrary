# TAGLINE

从 debuginfod 服务器请求调试信息的客户端

# TLDR

基于 **build ID** 请求 debuginfo

```debuginfod-find -v debuginfo [build_id]```

获取 build ID 对应的**可执行文件**

```debuginfod-find executable [build_id]```

获取 build ID 对应的**源码文件**

```debuginfod-find source [build_id] [/path/to/source.c]```

直接为某个 **ELF 文件**获取 debuginfo

```debuginfod-find debuginfo [/path/to/binary]```

# SYNOPSIS

**debuginfod-find** [_options_] _type_ _build-id_

# DESCRIPTION

**debuginfod-find** 从 debuginfod 服务器请求调试信息。它可以基于 ELF 二进制文件的 build ID 检索 debuginfo、可执行文件或源码文件。

它是 elfutils 软件包的一部分，可为 gdb 等调试工具按需下载调试符号。

# PARAMETERS

**debuginfo** _build-id_
> 获取调试信息文件

**executable** _build-id_
> 获取可执行文件

**source** _build-id_ _path_
> 获取源码文件

**-v**
> 详细输出

# CONFIGURATION

**DEBUGINFOD_URLS**（环境变量）
> 用于查询调试信息的 debuginfod 服务器 URL 列表，以空格分隔。

**DEBUGINFOD_CACHE_PATH**（环境变量）
> 缓存已下载调试文件的目录（默认：$HOME/.debuginfod_client_cache）。

# CAVEATS

需要网络连接以及配置好的 debuginfod 服务器。Build ID 可通过 `readelf -n` 或 `eu-readelf -n` 查看。

# INSTALL

```apt: sudo apt install debuginfod```

```pacman: sudo pacman -S debuginfod```

```apk: sudo apk add libdebuginfod```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[debuginfod](/man/debuginfod)(8), [gdb](/man/gdb)(1), [readelf](/man/readelf)(1)

# RESOURCES

```[Homepage](https://sourceware.org/elfutils/)```

```[Documentation](https://sourceware.org/elfutils/Debuginfod.html)```

<!-- verified: 2026-07-11 -->
