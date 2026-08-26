# TAGLINE

终端中的交互式火焰图查看器

# TLDR

**查看**折叠栈文件

```flamelens [folded-stacks.txt]```

直接**管道传入**性能剖析数据

```[profiler] | flamelens```

在火焰图中**搜索**

```flamelens [file] -s [pattern]```

# SYNOPSIS

**flamelens** [_options_] [_file_]

# PARAMETERS

**-s, --search** _PATTERN_
> 在调用栈中搜索指定模式

**--no-unicode**
> 使用 ASCII 字符而非 Unicode 字符

**--no-color**
> 禁用彩色输出

**-h, --help**
> 显示帮助并退出

**-V, --version**
> 显示版本并退出

# DESCRIPTION

**flamelens** 是一个运行在终端中的交互式火焰图查看器。它让用户能够以可视化、可导航的格式浏览性能剖析数据，无需网页浏览器或图形界面。

该工具支持折叠栈格式（由 perf、dtrace 或 Brendan Gregg 的栈合并脚本等工具生成），并提供 vim 风格的导航、搜索和缩放功能。

# KEYBINDINGS

**↑/↓** 或 **k/j**
> 在帧之间上下导航

**←/→** 或 **h/l**
> 缩小/放大所选帧

**/**
> 搜索模式

**n/N**
> 下一个/上一个搜索结果

**Enter**
> 聚焦所选帧

**Esc**
> 退出缩放/返回完整视图

**q**
> 退出

# CAVEATS

需要折叠栈格式的输入。非常大的性能剖析文件可能影响性能。终端必须支持 Unicode 才能获得最佳显示效果。某些性能分析器需要额外的脚本才能生成兼容的输出。

# HISTORY

**flamelens** 作为基于网页的火焰图查看器的替代方案而创建，可在没有浏览器访问能力的服务器环境中进行性能剖析分析。

# INSTALL

```pacman: sudo pacman -S flamelens```

```nix: nix profile install nixpkgs#flamelens```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[inferno](https://github.com/jonhoo/inferno), [flamegraph](https://github.com/brendangregg/FlameGraph), [cargo-flamegraph](https://github.com/flamegraph-rs/flamegraph)
