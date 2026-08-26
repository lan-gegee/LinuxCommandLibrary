# TAGLINE

系统错误编号查询工具

# TLDR

**按编号查找**错误

```errno [22]```

**按名称查找**错误

```errno [EINVAL]```

**列出所有错误**

```errno -l```

**搜索**错误描述

```errno -s [permission]```

# SYNOPSIS

**errno** [_options_] [_error_...]

# PARAMETERS

_ERROR_
> 要查询的错误编号或名称。

**-l**, **--list**
> 列出所有错误。

**-s**, **--search** _TEXT_
> 在描述中搜索匹配的词（不区分大小写）。

**-S**, **--search-all-locales** _TEXT_
> 跨所有可用语言区域搜索描述。

**--help**
> 显示帮助信息。

# DESCRIPTION

**errno** 查询 errno 值及其描述。它在错误编号与系统调用中使用的符号名（如 EINVAL、ENOENT）之间进行转换。

该工具在调试时非常有用，可帮助理解系统调用失败的原因。strace 输出或程序报错中的错误编号可以被快速转换为有意义的描述。

errno 还提供搜索和列表功能，便于浏览全部已定义的错误。

# CAVEATS

错误编号在不同架构间可能不同。部分错误是特定系统才有的。描述可能很简短。并非所有 errno 值都有标准含义。

# HISTORY

errno 是 **moreutils** 软件包的一部分。errno 机制可追溯到早期 Unix，为系统调用提供了一种标准化的错误报告方式。

# INSTALL

```apt: sudo apt install moreutils```

```dnf: sudo dnf install moreutils```

```pacman: sudo pacman -S moreutils```

```apk: sudo apk add moreutils```

```zypper: sudo zypper install moreutils```

```brew: brew install moreutils```

```nix: nix profile install nixpkgs#moreutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[strace](/man/strace)(1)
