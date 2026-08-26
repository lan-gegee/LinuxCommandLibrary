# TAGLINE

管理 CubeSandbox 模板与沙箱的 CLI

# TLDR

从容器镜像**创建沙箱模板**

```cubemastercli tpl create-from-image --image [registry/image:tag]```

创建模板时**暴露端口**并设置探测端口

```cubemastercli tpl create-from-image --image [image] --expose-port [49999] --probe [49999]```

为模板**配置可写层大小**

```cubemastercli tpl create-from-image --image [image] --writable-layer-size [1G]```

**跟踪模板构建任务的进度**

```cubemastercli tpl watch --job-id [job_id]```

显示子命令的**帮助**

```cubemastercli tpl --help```

# SYNOPSIS

**cubemastercli** _subcommand_ _action_ [_options_]

# DESCRIPTION

**cubemastercli** 是 **CubeSandbox** 的命令行接口。CubeSandbox 是构建在 **RustVMM** 和 **KVM** 之上的高性能安全沙箱服务，运维人员用它来创建、构建和监控沙箱模板，这些模板为 AI 代理的隔离执行环境提供支撑。

模板由 OCI 容器镜像生成，封装了启动基于 microVM 的沙箱所需的全部内容，包括根文件系统、可写层、暴露的端口以及就绪探测。模板构建完成后，CubeSandbox 可以在 60 毫秒内以硬件级隔离的方式从中启动沙箱。

该工具通常面向 CubeMaster 控制平面运行，由其编排 RustVMM/KVM 宿主机上的底层 microVM。

# PARAMETERS

**tpl create-from-image**
> 从容器镜像构建新的沙箱模板，并向 CubeMaster 提交一个构建任务。

**tpl watch**
> 跟踪正在运行的模板构建任务的进度。

**--image** _registry/image:tag_
> 用作模板基础的容器镜像。

**--writable-layer-size** _size_
> 可写 overlay 层的大小（如 _1G_）。从此模板启动的沙箱会获得该大小的新可写层。

**--expose-port** _port_
> 从沙箱暴露一个 TCP 端口。可以多次指定。

**--probe** _port_
> 用于就绪探测的端口；一旦该端口接受连接，模板即被视为就绪。

**--job-id** _id_
> 要跟踪的构建任务标识符，由 **tpl create-from-image** 返回。

**--help**
> 显示命令或子命令的帮助。

# EXAMPLES

用腾讯云镜像构建代码解释器模板并跟踪生成的任务：

```
cubemastercli tpl create-from-image \
    --image ccr.ccs.tencentyun.com/ags-image/sandbox-code:latest \
    --writable-layer-size 1G \
    --expose-port 49999 \
    --expose-port 49983 \
    --probe 49999

cubemastercli tpl watch --job-id <job_id>
```

# CAVEATS

**cubemastercli** 需要可达的 CubeMaster 控制平面以及一台启用 KVM 的宿主机。它属于 CubeSandbox 项目，不由 Linux 发行版提供；各版本之间的选项和子命令可能变化。

# HISTORY

**CubeSandbox** 由**腾讯云**开源，是一个为 AI 代理打造的即时、并发、安全且轻量的沙箱，构建于 **RustVMM** 和 **KVM** 之上。**cubemastercli** 作为其 CubeMaster 控制平面的管理客户端发布。

# SEE ALSO

[docker](/man/docker)(1), [kvm](/man/kvm)(4), [qemu](/man/qemu)(1)
