# TAGLINE

并行运行命令并提供实时反馈

# TLDR

对每一行输入**运行一条命令**

```find . -name '*.png' | machma convert {} {.}.jpg```

带替换标记的**并行任务**

```cat [hosts.txt] | machma ssh {} uptime```

**显示帮助**

```machma -h```

# SYNOPSIS

**machma** [*options*] *command* [*args*...]

# DESCRIPTION

**machma** 对 stdin 的每一行（或每组参数）执行一次命令模板，以并行方式运行，并通过实时终端界面展示进度和结果。**{}** 等占位符会展开为当前条目（设计意图类似于 **xargs** / **GNU parallel**，但带有交互式反馈）。由 fd0 编写。

# PARAMETERS

*command* [*args*...]

> 命令模板；**{}** 会被替换为每个输入值。

stdin 的各行提供要处理的条目。并发数与失败处理相关的标志可通过 **machma -h** 查看。

# CAVEATS

不加限制的并行可能压垮远程主机或磁盘——必要时请限制任务数量。模板中含有 shell 元字符时务必小心加引号。

# SEE ALSO

[xargs](/man/xargs)(1), [parallel](/man/parallel)(1), [rush](/man/rush)(1)

# RESOURCES

```[Source code](https://github.com/fd0/machma)```

<!-- verified: 2026-07-19 -->
