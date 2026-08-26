# TAGLINE

分发 ELF 调试信息的 HTTP 服务器

# TLDR

**扫描目录中的 ELF/DWARF 文件**

```debuginfod -F [/usr/lib/debug]```

**在指定端口启动**

```debuginfod -p [8002] -F [/usr/lib/debug]```

**索引目录中的 RPM 归档**

```debuginfod -R [/path/to/rpms]```

**索引目录中的 DEB 归档**

```debuginfod -U [/path/to/debs]```

**以详细模式和自定义数据库路径运行**

```debuginfod -v -d [/var/cache/debuginfod.sqlite] -F [/usr/lib/debug]```

**设置扫描间隔和并发线程数**

```debuginfod -t [600] -c [10] -F [/path/to/debug]```

# SYNOPSIS

**debuginfod** [_options_] [_paths_...]

# DESCRIPTION

**debuginfod** 是一个通过 HTTP 分发 ELF 调试信息的服务器。它索引可执行文件、共享库和调试信息，并按需提供给 gdb 和 systemtap 等客户端。

该服务实现了调试符号的自动解析，无需手动安装调试软件包。客户端按 build-id 查询以获取匹配的调试信息。

# PARAMETERS

**-p** _port_
> HTTP 服务器端口（默认 8002）。

**-F**
> 对指定路径启用 ELF/DWARF 文件扫描。

**-R**
> 扫描 RPM 归档。

**-U**
> 扫描 DEB/DDEB 归档。

**-Z** _ext_
> 为给定扩展名启用额外的归档模式扫描。

**-d** _file_
> SQLite 数据库文件位置（默认 ~/.debuginfod.sqlite）。

**-c** _num_
> 扫描器队列线程上限。

**-C** _num_
> Webapi 线程池大小。

**-t** _seconds_
> 目录重新扫描间隔（默认 300 秒）。

**-g** _seconds_
> 整理（grooming）间隔（默认 86400 秒）。

**-I** _regex_
> 只包含匹配 POSIX 扩展正则表达式的文件。

**-X** _regex_
> 排除匹配 POSIX 扩展正则表达式的文件。

**-L**
> 扫描时遍历符号链接。

**--passive**
> 只读模式；不进行扫描，仅提供现有索引。

**--cors**
> 添加 CORS 响应头，供第三方 Web 应用访问。

**-v**
> 提高详细程度（可重复使用）。

# CLIENT USAGE

设置 DEBUGINFOD_URLS 即可启用自动获取：
```
export DEBUGINFOD_URLS="https://debuginfod.example.com"
```

# CAVEATS

大型仓库的初次索引可能较慢。SQLite 数据库会随内容增长。客户端需要网络连接。该服务可能暴露已安装二进制文件的细节。客户端必须持有匹配的 build-id 才能获取调试信息。

# HISTORY

**debuginfod** 由 **Red Hat** 工程师作为 **elfutils** 项目的一部分于约 **2019 年**开发。它解决了 Linux 发行版分发调试符号的难题，实现按需获取，而不必安装庞大的调试软件包。

# INSTALL

```apt: sudo apt install debuginfod```

```pacman: sudo pacman -S debuginfod```

```apk: sudo apk add debuginfod```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[debuginfod-find](/man/debuginfod-find)(1), [gdb](/man/gdb)(1), [objdump](/man/objdump)(1), [readelf](/man/readelf)(1)
