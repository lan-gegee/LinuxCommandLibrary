# TAGLINE

面向终端的 Mach-O 和 Objective-C 分析工具包

# TLDR

**转储 Mach-O 头信息**

```ktool dump [path/to/binary]```

**列出段和节**

```ktool list [path/to/binary]```

**显示二进制文件中的符号**

```ktool symbols [path/to/binary]```

**以 JSON 输出分析结果**

```ktool json [path/to/binary]```

**显示文件类型信息**

```ktool file [path/to/binary]```

# SYNOPSIS

**ktool** _command_ [_options_] [_file_]

# DESCRIPTION

**ktool** 是一个用于检查和编辑 Mach-O 二进制文件及 Objective-C 元数据的 CLI 和 TUI 工具包。它提供 MachO 分析命令（dump、json、list、symbols、info）、MachO 编辑命令（insert、edit、lipo），以及其他实用工具（file、img4）。

该工具无需外部编译依赖，只要有 Python 解释器即可在任何地方运行。它可以分析 Apple mach-o 和 dyld_shared_cache 文件。

# CAVEATS

专为 Apple Mach-O 二进制格式设计。不适用于 ELF 或 PE 二进制文件。

# HISTORY

**ktool** 由 **0cyn** 创建，使用 **Python** 编写。可通过 pip 安装：`pip install k2l`。

# SEE ALSO

[nm](/man/nm)(1)
