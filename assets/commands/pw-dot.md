# TAGLINE

将 PipeWire 图可视化为 Graphviz DOT

# TLDR

生成图到 **pw.dot** 文件

```pw-dot```

从 **pw-dump JSON** 文件读取对象

```pw-dot -j [path/to/file.json]```

指定**输出文件**并显示所有对象类型

```pw-dot -o [path/to/file.dot] -a```

将图打印到**标准输出**并包含对象属性

```pw-dot -o - -d```

从**远程实例**生成图，只显示有链接的对象

```pw-dot -r [remote_name] -s```

将图**从左到右**布局

```pw-dot -L```

在边上使用 **90 度直角**

```pw-dot -9```

生成图并**渲染为 PNG** 图像

```pw-dot && dot -Tpng pw.dot -o [pw-graph.png]```

# SYNOPSIS

**pw-dot** [_options_]

# PARAMETERS

**-o**, **--output** _file_
> 输出文件（默认：pw.dot；使用 - 表示标准输出）

**-a**, **--all**
> 显示所有对象类型

**-s**, **--smart**
> 只显示有链接的对象

**-d**, **--detail**
> 显示所有对象属性

**-r**, **--remote** _name_
> 连接到远程 PipeWire 实例

**-j**, **--json** _file_
> 从 pw-dump JSON 文件读取对象

**-L**, **--lr**
> 将图从左到右布局

**-9**, **--90**
> 边使用 90 度直角

**-h**, **--help**
> 显示帮助信息

# DESCRIPTION

**pw-dot** 从 PipeWire 图生成 Graphviz DOT 文件，将节点、端口和设备之间的连接可视化。输出可以用 Graphviz 的 **dot** 命令渲染成图像。

这有助于理解音频/视频路由、排查连接问题以及记录系统音频配置。

# CAVEATS

需要 Graphviz 才能将 DOT 文件渲染为图像。对象繁多的复杂图可能难以阅读；可使用 **--smart** 只显示有连接的对象。

# HISTORY

**PipeWire** 的一部分，提供多媒体图的可视化。对开发者、系统集成商以及排查音频路由问题的用户很有用。

# INSTALL

```apt: sudo apt install pipewire-bin```

```apk: sudo apk add pipewire-tools```

```zypper: sudo zypper install pipewire-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pw-dump](/man/pw-dump)(1), [pw-cli](/man/pw-cli)(1), [pw-top](/man/pw-top)(1), [pw-mon](/man/pw-mon)(1), [pipewire](/man/pipewire)(1), [dot](/man/dot)(1)
