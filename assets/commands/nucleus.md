# TAGLINE

轻量级、强化安全的容器运行时

# TLDR

在隔离容器中**运行命令**

```nucleus run [image] [command]```

**带内存和 CPU 限制运行**

```nucleus run --memory [512m] --cpus [2] [image] [command]```

**后台分离运行**

```nucleus run --detach [image] [command]```

**列出正在运行的**容器

```nucleus ps```

**查看容器日志**

```nucleus logs [container]```

**停止**正在运行的容器

```nucleus stop [container]```

# SYNOPSIS

**nucleus** _subcommand_ [_options_] [_image_] [_command_]

# DESCRIPTION

**nucleus** 是一个轻量级的声明式容器运行时，面向临时性的 agent 沙箱和长期运行的生产服务。它不在上面叠加沉重的守护进程，而是直接驱动 Linux 内核原语（名称空间、cgroups、seccomp 和 Landlock），以极小的开销创建隔离的执行环境。

它以不同的模式运行。默认的 agent 模式以尽力而为的方式创建临时沙箱；而严格 agent 模式采用失败即关闭的策略：除非 cgroup 创建、seccomp 过滤和 Landlock 强制全部成功，否则拒绝启动。生产模式则面向长期运行的服务，提供声明式配置、可复现的根文件系统、出站策略、健康检查和 systemd 集成。子命令涵盖常见的生命周期操作（**run**、**create**、**ps**、**logs**、**stop**、**attach**），并通过 **compose** 支持多容器拓扑，还能从系统调用轨迹生成 seccomp 配置。

# PARAMETERS

**run**
> 从镜像或根文件系统创建并启动容器。

**create**
> 通过 JSON 或 TOML 配置定义容器但不启动它。

**ps**
> 列出容器。

**logs**
> 显示容器的输出。

**stop**
> 停止正在运行的容器。

**attach**
> 附加到正在运行的容器的标准流。

**compose**
> 启动多容器拓扑。

**--memory** _SIZE_
> 限制容器的内存。

**--cpus** _N_
> 限制 CPU 数量。

**--network** _MODE_
> 选择容器的网络模式。

**--rootfs** _PATH_
> 使用给定的根文件系统。

**--seccomp-profile** _FILE_
> 对容器应用 seccomp 配置。

**--landlock-policy** _SPEC_
> 应用 Landlock 文件系统访问策略。

**--detach**
> 在后台运行容器。

# CAVEATS

nucleus 依赖 cgroups v2、seccomp 和 Landlock 等现代 Linux 内核特性；严格 agent 模式在其中任何一项不可用时都会失败关闭，因此较旧的内核可能只支持降级的 agent 模式。它是 Linux 专属的，并不是完整 Docker 或 OCI 工具生态的直接替代品。

# INSTALL

```nix: nix profile install nixpkgs#nucleus```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[podman](/man/podman)(1), [docker](/man/docker)(1), [runc](/man/runc)(8), [bwrap](/man/bwrap)(1), [systemd-nspawn](/man/systemd-nspawn)(1)

# RESOURCES

```[Source code](https://github.com/sig-id/nucleus)```

<!-- verified: 2026-06-10 -->
