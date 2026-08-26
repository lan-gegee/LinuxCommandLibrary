# TAGLINE

Graphviz 的简易图形编辑器与查看器

# TLDR

**打开 gvedit**

```gvedit```

**打开图文件**

```gvedit [graph.gv]```

**打开多个图文件**

```gvedit [file1.gv] [file2.gv]```

**以详细输出模式打开**

```gvedit -v [graph.gv]```

# SYNOPSIS

**gvedit** [**-v**] [**-s**] [**-?**] [_file_ ...]

# PARAMETERS

**-s**
> 将节点位置坐标从点缩放为英寸。当布局算法（fdp、neato）接收的输入坐标以点为单位时很有用。

**-v**
> 启用详细模式以输出更多信息。

**-?**
> 显示用法信息并退出。

# DESCRIPTION

**gvedit** 是 Graphviz 软件包中的一个简易图形编辑器和查看器。它提供图形界面，用于创建、查看、编辑和处理 DOT 语言的图文件。可以同时打开多个图，每个显示在自己的文本窗口中。功能包括即时预览、通过对话框编辑属性，以及保存图的设置以备将来使用。

# SEE ALSO

[dot](/man/dot)(1), [neato](/man/neato)(1), [fdp](/man/fdp)(1), [dotty](/man/dotty)(1), [xdot](/man/xdot)(1)
