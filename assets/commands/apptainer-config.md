# TAGLINE

管理 Apptainer 容器平台的配置

# TLDR

**为用户添加 fakeroot 映射**

```sudo apptainer config fakeroot --add [username]```

**移除用户的 fakeroot 映射**

```sudo apptainer config fakeroot --remove [username]```

**设置全局配置指令**

```sudo apptainer config global --set "[directive]" [value]```

**获取全局指令的当前值**

```sudo apptainer config global --get "[directive]"```

**将全局指令重置**为默认值

```sudo apptainer config global --reset "[directive]"```

**预览更改**而不写入配置文件

```sudo apptainer config global --dry-run --set "[directive]" [value]```

# SYNOPSIS

**apptainer config** _subcommand_ [_options_]

# DESCRIPTION

**apptainer config** 管理 Apptainer 容器平台的配置。它提供管理命令，用于管理 fakeroot 用户映射，以及从命令行编辑全局 **apptainer.conf** 配置文件。大多数操作需要 root 权限或非特权安装。

该命令通过两个子命令工作：**fakeroot** 用于管理用户命名空间映射（允许非特权用户以表面上的 root 权限构建和运行容器）；**global** 用于修改系统级配置指令，这些指令控制容器行为、绑定路径、安全设置和资源限制。

# SUBCOMMANDS

**fakeroot**
> 管理 fakeroot 用户映射条目（仅限 root 用户）。控制哪些用户可以使用 fakeroot 功能，以模拟 root 权限构建和运行容器。

**global**
> 从命令行编辑 apptainer.conf 配置指令（仅限 root 用户或非特权安装）。支持对配置值进行 set、unset、get 和 reset 操作。

# PARAMETERS

**-a**, **--add**
> 为用户添加 fakeroot 映射条目（fakeroot 子命令）

**-r**, **--remove**
> 移除用户的 fakeroot 映射条目（fakeroot 子命令）

**-e**, **--enable**
> 启用已有的 fakeroot 映射条目（fakeroot 子命令）

**-d**, **--disable**
> 禁用已有的 fakeroot 映射条目（fakeroot 子命令）

**--set**
> 设置配置指令的值（global 子命令）

**--unset**
> 从配置指令中移除一个值（global 子命令）

**--get**
> 获取配置指令的当前值（global 子命令）

**--reset**
> 将配置指令重置为默认值（global 子命令）

**--dry-run**
> 显示生成的配置但不写入文件（global 子命令）

**-h**, **--help**
> 显示 config 命令的帮助信息

# CONFIGURATION

global 子命令修改 **/etc/apptainer/apptainer.conf**（或非特权安装中的对应路径）。常见指令包括：

**bind path**
> 自动绑定进容器的路径

**max loop devices**
> SIF 镜像可用的回环设备最大数量

**allow setuid**
> 是否允许以 setuid-root 模式执行容器

**allow net users / allow net groups / allow net networks**
> 控制哪些用户和网络可以进行容器网络通信

# CAVEATS

大多数 config 操作需要 root 权限。fakeroot 子命令管理 **/etc/subuid** 和 **/etc/subgid** 条目，会影响整个系统的用户命名空间映射。修改全局配置可能影响系统上的所有用户。在采用非特权安装的系统上，global 子命令可以在没有 root 的情况下运行，但只影响该安装自身的配置。

# HISTORY

Apptainer 源自 **Singularity**，由 **Gregory Kurtzer** 于 **2015** 年在 **劳伦斯伯克利国家实验室** 创建，目的是将容器技术引入高性能计算（HPC）领域。**2021** 年 **11 月**，该项目加入 **Linux 基金会**并更名为 **Apptainer**。config 子命令提供的管理工具随平台在全球科学计算和 HPC 环境中的应用不断扩大而逐步演进。

# INSTALL

```dnf: sudo dnf install apptainer```

```pacman: sudo pacman -S apptainer```

```apk: sudo apk add apptainer```

```zypper: sudo zypper install apptainer```

```brew: brew install apptainer```

```nix: nix profile install nixpkgs#apptainer```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[apptainer](/man/apptainer)(1), [singularity](/man/singularity)(1), [docker](/man/docker)(1), [podman](/man/podman)(1)
