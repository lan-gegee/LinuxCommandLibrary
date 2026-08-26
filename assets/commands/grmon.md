# TAGLINE

基于 pprof 的 Go 进程 goroutine 终端监视器

# TLDR

**连接**到默认的本地 pprof 端点

```grmon```

**连接**到特定的主机和端口

```grmon -host [localhost:6060]```

**设置刷新间隔**（秒，0 表示禁用自动刷新）

```grmon -i [2]```

**使用自定义 pprof 路径**

```grmon -endpoint [/debug/pprof]```

# SYNOPSIS

**grmon** [**-i** *seconds*] [**-host** *host:port*] [**-endpoint** *path*]

# DESCRIPTION

**grmon** 是一个交互式终端 UI，用于观察运行中的 Go 程序里的 goroutine。目标进程必须暴露 Go 的 **net/http/pprof** 端点（或启动小型 **grmon** 代理）。**grmon** 轮询 profile 端点并显示 goroutine 数量和堆栈；你可以暂停刷新、过滤、排序以及展开单个调用轨迹。

默认目标为 **localhost:1234**，路径为 **/debug/pprof**。在目标应用中，可以调用代理包中的 **grmon.Start()**，也可以自行提供 pprof 服务（例如在导入 **_ "net/http/pprof"** 后执行 **http.ListenAndServe(":6060", nil)**）。

# PARAMETERS

**-i** *seconds*

> 刷新间隔（默认：5）。**0** 表示禁用自动刷新。

**-host** *host:port*

> 目标主机（默认：**localhost:1234**）。

**-endpoint** *path*

> pprof 基础路径（默认：**/debug/pprof**）。

交互按键包括 **r** 刷新、**p** 暂停、**s** 排序、**f** 过滤、方向键/**j**/**k** 移动、Enter 展开、**t** 全屏查看轨迹、**q** 退出。

# CAVEATS

目标必须暴露 pprof；将 pprof 绑定到公网接口存在安全风险。收集堆栈有运行时开销。不同 Go module 模式下 **go get** 的安装路径可能不同——请以仓库中最新的模块安装说明为准。

# INSTALL

```nix: nix profile install nixpkgs#grmon```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[go](/man/go)(1), [pprof](/man/pprof)(1), [top](/man/top)(1)

# RESOURCES

```[Source code](https://github.com/bcicen/grmon)```

<!-- verified: 2026-07-19 -->
