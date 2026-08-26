# TAGLINE

用于 Go pprof 剖析数据的交互式终端 UI

# TLDR

**分析 CPU 剖析文件**

```pproftui [cpu.prof]```

**聚焦你模块的代码**

```pproftui --module-path=[github.com/your/project] [cpu.prof]```

**从运行中的服务器实时获取 CPU 剖析文件**

```pproftui -live=[http://localhost:6060/debug/pprof/profile?seconds=5] -refresh=[10s]```

# SYNOPSIS

**pproftui** [_options_] [_profile_file_]

# PARAMETERS

**--module-path** _PATH_
> 聚焦于指定 Go module 路径下的代码。

**-live** _URL_
> 从运行中的 HTTP pprof 端点获取剖析文件。

**-refresh** _DURATION_
> 实时剖析的刷新间隔。

# DESCRIPTION

**pproftui** 是一个基于终端的 Go pprof UI，让性能剖析变得交互且直观。它提供集成的源代码视图和调用图视图，并可选择隐藏 Go 运行时函数。它的对比功能使用颜色编码指示器突出剖析文件之间资源使用的变化。

# CAVEATS

仅适用于 Go pprof 剖析数据。

# HISTORY

**pproftui** 由 **Oloruntobi1** 创建，使用 **Go** 编写。

# SEE ALSO

[go](/man/go)(1), [pprof](/man/pprof)(1)
