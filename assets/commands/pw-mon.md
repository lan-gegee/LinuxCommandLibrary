# TAGLINE

实时监控 PipeWire 对象

# TLDR

**监控**默认的 PipeWire 实例

```pw-mon```

监控特定的**远程实例**

```pw-mon -r remote_name```

以特定的**颜色配置**监控

```pw-mon -N never```

显示**帮助**

```pw-mon -h```

# SYNOPSIS

**pw-mon** [_options_]

# PARAMETERS

**-r**, **--remote** _name_
> 连接到特定的远程 PipeWire 实例

**-N**, **--color** _mode_
> 彩色输出模式：never、always 或 auto

**-h**, **--help**
> 显示帮助信息

# DESCRIPTION

**pw-mon** 实时监控 PipeWire 实例上的对象。它显示节点、端口、链接和其他图对象在创建、修改或销毁时的信息。

该工具适合调试音频路由、观察设备连接以及了解 PipeWire 运行时的内部状态。

# CAVEATS

在音频设备和应用众多的系统上，输出可能非常冗长。对于特定的监控任务，可考虑将输出通过过滤工具处理。

# HISTORY

**PipeWire**（Linux 上的现代多媒体框架）的一部分。为调试和监控提供对 PipeWire 图的实时可见性。

# INSTALL

```apt: sudo apt install pipewire-bin```

```apk: sudo apk add pipewire-tools```

```zypper: sudo zypper install pipewire-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pipewire](/man/pipewire)(1), [pw-metadata](/man/pw-metadata)(1), [pw-cli](/man/pw-cli)(1), [pw-top](/man/pw-top)(1)
