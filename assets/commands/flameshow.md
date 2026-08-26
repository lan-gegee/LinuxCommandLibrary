# TAGLINE

基于终端的火焰图查看器

# TLDR

**查看**火焰图文件

```flameshow [profile.json]```

**查看**折叠栈

```flameshow [stacks.folded]```

从标准输入**查看**

```cat [profile] | flameshow```

# SYNOPSIS

**flameshow** [_options_] [_file_]

# PARAMETERS

**-h, --help**
> 显示帮助并退出

**--version**
> 显示版本并退出

**--theme** _THEME_
> 配色主题：dark、light

# DESCRIPTION

**flameshow** 是一个基于 Python 的终端火焰图查看器。它让用户可以直接在终端中可视化性能剖析数据，无需离开命令行即可轻松分析性能数据。

该工具支持多种剖析文件格式，并提供交互式 TUI 用于浏览火焰图、定位热点以及了解应用程序的性能表现。

# KEYBINDINGS

**↑/↓**
> 在帧之间导航

**Enter**
> 展开/折叠帧

**q**
> 退出

**?**
> 显示帮助

# CAVEATS

需要 Python 环境。可能不支持所有性能分析器的输出格式。性能取决于终端的能力。较大的剖析文件可能影响渲染速度。

# HISTORY

**flameshow** 的开发目标是作为浏览器火焰图查看器的替代品，专注于终端原生显示和快速检查剖析文件。

# SEE ALSO

[flamelens](https://github.com/YS-L/flamelens), [flamegraph](https://github.com/brendangregg/FlameGraph), [py-spy](https://github.com/benfred/py-spy)
