# TAGLINE

可视化并分析性能剖析数据

# TLDR

**启动 Web 界面**

```pprof -http=[localhost:8080] [profile.pb.gz]```

**显示排名靠前的函数**

```pprof -top [profile.pb.gz]```

**以文本形式显示调用图**

```pprof -text [profile.pb.gz]```

**以 PDF 形式显示调用图**

```pprof -pdf [profile.pb.gz] > [profile.pdf]```

**剖析运行中的服务器**

```pprof -http=[localhost:8080] [http://localhost:6060/debug/pprof/profile]```

**对比两个剖析文件**

```pprof -base [baseline.pb.gz] [current.pb.gz]```

**聚焦特定函数**

```pprof -focus=[FunctionName] [profile.pb.gz]```

# SYNOPSIS

**pprof** [_-http addr_] [_-top_] [_-text_] [_-pdf_] [_-focus pattern_] [_options_] _source_

# PARAMETERS

**-http** _ADDR_
> 启动 Web 服务器。

**-top**
> 显示排名靠前的函数。

**-text**
> 文本报告。

**-pdf**
> PDF 输出。

**-svg**
> SVG 输出。

**-png**
> PNG 输出。

**-web**
> 在浏览器中打开。

**-focus** _REGEX_
> 聚焦于匹配的函数。

**-ignore** _REGEX_
> 忽略匹配的函数。

**-base** _PROFILE_
> 与基线进行对比。

**-seconds** _N_
> 剖析时长。

**-sample_index** _IDX_
> 样本类型（cpu、alloc 等）。

**-lines**
> 显示行级信息。

# DESCRIPTION

**pprof** 分析并可视化来自 Go 程序及其他来源的性能剖析数据。它展示程序在时间和内存上的消耗位置。

Web 界面提供交互式探索。火焰图展示调用层次结构。图形视图显示调用者/被调用者关系。

剖析文件捕获 CPU 使用情况、内存分配、goroutine 数量以及自定义指标。Go 的 runtime/pprof 包负责生成这些剖析文件。

实时剖析通过 HTTP 端点连接到运行中的服务器。标准路径 /debug/pprof/ 提供各种剖析类型。

对比模式突出剖析文件之间的变化，用于识别代码更改后的性能退化或改进。

聚焦和忽略过滤器将分析范围缩小到特定区域。正则表达式匹配函数名，便于有针对性地调查。

# CAVEATS

生成图形需要 graphviz。CPU 剖析需要足够的采样时间。内存剖析可能需要多次采集。剖析文件大小随采样增长。

# HISTORY

**pprof** 由 **Google** 开发，用于剖析生产系统。Go 版本作为 Go 项目的一部分维护。它源自 Google 内部的剖析工具和 gperftools。

# INSTALL

```zypper: sudo zypper install pprof```

```nix: nix profile install nixpkgs#pprof```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[perf](/man/perf)(1), [flamegraph](/man/flamegraph)(1)
