# TAGLINE

管理轻量级 microVM

# TLDR

**创建 microVM**

```krunvm create [image] --name [myvm]```

**启动 microVM**

```krunvm start [myvm]```

**列出 microVM**

```krunvm list```

**删除 microVM**

```krunvm delete [myvm]```

**带端口映射创建**

```krunvm create [image] --name [vm] -p [8080:80]```

**设置 CPU 和内存**

```krunvm create [image] --cpus [2] --mem [1024]```

# SYNOPSIS

**krunvm** _command_ [_options_]

# PARAMETERS

**create** _IMAGE_
> 从镜像创建 microVM。

**start** _NAME_
> 启动 microVM。

**delete** _NAME_
> 删除 microVM。

**list**
> 列出 microVM。

**--name** _NAME_
> VM 名称。

**--cpus** _N_
> CPU 数量。

**--mem** _MB_
> 内存大小（MB）。

**-p** _MAPPING_
> 端口映射。

# DESCRIPTION

**krunvm** 是一款从 OCI 容器镜像构建和管理轻量级 microVM 的工具。它使用 libkrun——一个利用 KVM 虚拟化将每个工作负载运行在各自最小虚拟机中的库——提供比容器更强的隔离性，同时保持类容器的使用体验：启动快、内存开销低。

microVM 从镜像仓库拉取的标准容器镜像创建，因此现有的容器工作流和镜像都可以直接复用。每个 VM 可以配置特定的 CPU 数量、内存分配和端口映射，与容器运行时的选项类似。其结果是一种用起来像管理容器、却拥有硬件虚拟化安全边界的工作流，使 krunvm 非常适合多租户环境或需要更强隔离保证的工作负载。

# CAVEATS

需要支持 KVM 的 Linux。以容器镜像为基础。轻量级隔离。

# HISTORY

krunvm 由 **Red Hat** 创建，是一款使用 libkrun 虚拟化技术管理 microVM 的简单工具。

# INSTALL

```dnf: sudo dnf install krunvm```

```pacman: sudo pacman -S krunvm```

```zypper: sudo zypper install krunvm```

```nix: nix profile install nixpkgs#krunvm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[podman](/man/podman)(1), [docker](/man/docker)(1)
