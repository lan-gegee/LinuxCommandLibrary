# TAGLINE

管理沙箱化的 snap 软件包

# TLDR

**搜索软件包**

```snap find [query]```

**安装软件包**

```snap install [package]```

以 classic 沙箱模式**安装**（完全系统访问权限）

```snap install --classic [package]```

**更新所有软件包**

```snap refresh```

**列出已安装的 snap**

```snap list```

**显示某个 snap 的详细信息**

```snap info [package]```

**移除软件包**

```snap remove [package]```

**回退到之前的版本**

```snap revert [package]```

# SYNOPSIS

**snap** _command_ [_OPTIONS_]

# DESCRIPTION

**snap** 是用于管理 snap 软件包的命令行界面。Snap 是包含全部依赖的自包含软件包，运行在沙箱中，自动更新，并可在众多 Linux 发行版上使用。

# PARAMETERS

**find** _query_
> 搜索与查询匹配的 snap

**install** _snap_
> 安装一个 snap 软件包

**remove** _snap_
> 移除已安装的 snap

**refresh** [_snap_]
> 更新指定的 snap 或所有 snap

**list**
> 列出已安装的 snap

**info** _snap_
> 显示某个 snap 的详细信息

**changes**
> 显示最近的更改和操作

**connections** [_snap_]
> 显示接口连接

**--channel** _channel_
> 为 install 或 refresh 指定通道（track/risk/branch）

**revert** _snap_
> 将 snap 回退到之前的版本

**disable** _snap_
> 禁用 snap 但不删除它

**enable** _snap_
> 重新启用被禁用的 snap

**--channel** _channel_
> 为 install 或 refresh 指定通道（track/risk/branch）

**--classic**
> 以 classic 沙箱模式安装（完全系统访问权限）

**--devmode**
> 以开发模式安装（无沙箱）

**--dangerous**
> 安装本地 snap 文件而不进行签名验证

# CAVEATS

Snap 在沙箱中运行，对系统资源的访问受限。接口连接决定 snap 可以访问哪些资源。某些 snap 需要 **--classic** 模式才能访问完整系统。

# HISTORY

**snap** 是 **snapd** 的一部分，由 Canonical 开发，旨在提供通用 Linux 打包方案。它提供自动更新、回滚能力，并可在大多数 Linux 发行版上运行。

# INSTALL

```apt: sudo apt install snapd```

```dnf: sudo dnf install snapd```

```brew: brew install snap```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[snapd](/man/snapd)(8), [apt](/man/apt)(8), [flatpak](/man/flatpak)(1)
