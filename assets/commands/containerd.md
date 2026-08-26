# TAGLINE

工业级容器运行时守护进程

# TLDR

**启动 containerd** 守护进程

```sudo containerd```

**使用指定配置**文件启动

```sudo containerd --config [/etc/containerd/config.toml]```

**以调试日志启动**

```sudo containerd --log-level debug```

**生成默认配置**

```containerd config default > [/etc/containerd/config.toml]```

**查看 containerd 版本**

```containerd --version```

**以指定的根目录启动**

```sudo containerd --root [/var/lib/containerd]```

# SYNOPSIS

**containerd** [_options_]

# PARAMETERS

**--config** _FILE_
> 配置文件路径（默认：/etc/containerd/config.toml）。

**--root** _DIR_
> containerd 数据的根目录。

**--state** _DIR_
> containerd 的状态目录。

**--address** _SOCKET_
> containerd gRPC 套接字的地址。

**--log-level** _LEVEL_
> 日志级别：trace、debug、info、warn、error、fatal、panic。

**config default**
> 将默认配置输出到 stdout。

**config dump**
> 输出当前配置。

**--version**
> 显示版本信息。

**--help**
> 显示帮助信息。

# CONFIGURATION

**/etc/containerd/config.toml**
> containerd 守护进程设置、运行时选项和插件配置的主配置文件。

# DESCRIPTION

**containerd** 是一个工业标准的容器运行时，管理主机上完整的容器生命周期。它负责镜像传输与存储、容器执行与监督、底层存储以及网络挂载。

作为守护进程，containerd 提供 gRPC API 供 Docker、Kubernetes 和 nerdctl 等上层工具交互。它支持 OCI（Open Container Initiative）镜像和运行时规范，确保与整个容器生态的兼容性。

containerd 的设计目标是嵌入更大的系统而非供最终用户直接使用。Kubernetes 通过 CRI（Container Runtime Interface）将 containerd 用作容器运行时，Docker 也将其作为核心运行时引擎。

# CAVEATS

containerd 通常作为系统服务管理，而不是直接运行。直接交互需要 **ctr** 或 **nerdctl** 等工具。正确的配置对安全至关重要，尤其是运行时选项和命名空间隔离方面。大多数操作需要 root 权限。

# HISTORY

containerd 最初作为 Docker 的一部分开发，于 **2016 年 12 月**独立为一个项目。它在 **2017** 年捐赠给云原生计算基金会（CNCF），并于 **2019** 年从 CNCF 毕业，成为 Kubernetes 的标准容器运行时。

# INSTALL

```apt: sudo apt install containerd```

```dnf: sudo dnf install containerd```

```pacman: sudo pacman -S containerd```

```apk: sudo apk add containerd```

```zypper: sudo zypper install containerd```

```brew: brew install containerd```

```nix: nix profile install nixpkgs#containerd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ctr](/man/ctr)(1), [nerdctl](/man/nerdctl)(1), [docker](/man/docker)(1), [runc](/man/runc)(1)

# RESOURCES

```[Source code](https://github.com/containerd/containerd)```

```[Homepage](https://containerd.io)```

```[Documentation](https://containerd.io/docs/)```

<!-- verified: 2026-06-23 -->
