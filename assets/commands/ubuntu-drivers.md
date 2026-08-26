# TAGLINE

管理 Ubuntu 硬件驱动软件包

# TLDR

**列出**当前硬件的可用驱动

```sudo ubuntu-drivers list```

**安装**所有推荐的驱动

```sudo ubuntu-drivers install```

安装**指定驱动**

```sudo ubuntu-drivers install nvidia-driver-535```

显示**帮助**

```ubuntu-drivers --help```

显示**设备**及可用驱动

```ubuntu-drivers devices```

**只列出推荐的**驱动

```ubuntu-drivers list --recommended```

**列出 GPGPU（服务器）**驱动

```ubuntu-drivers list --gpgpu```

**只安装自由**驱动

```sudo ubuntu-drivers install --free-only```

# SYNOPSIS

**ubuntu-drivers** [_options_] _command_

# DESCRIPTION

**ubuntu-drivers** 是一个用于管理 Ubuntu 系统上驱动软件包的工具。它能检测需要专有驱动或额外驱动的硬件，并可以自动安装推荐的驱动。

# PARAMETERS

**list**
> 列出检测到的硬件所对应的推荐驱动软件包

**install**
> 为所有检测到的硬件安装推荐驱动

**install DRIVER**
> 安装指定的驱动软件包

**devices**
> 显示设备及可用驱动

**autoinstall**
> 自动安装驱动（在系统安装过程中使用）。

**debug**
> 打印调试信息以便排障。

**--gpgpu**
> 针对 GPGPU/服务器驱动进行操作（面向计算负载而非显示）。与 list 或 install 搭配使用。

**--recommended**
> 将 list/install 限制为仅推荐驱动。

**--free-only**
> 只考虑自由（非专有）软件包。

**--package-list** _FILE_
> 将选中的软件包列表写入 FILE（供安装器使用）。

# CAVEATS

安装需要 root 权限。安装驱动后通常需要重启系统。对于 NVIDIA 驱动，该工具是 Ubuntu 系统上的推荐方法。

# HISTORY

**ubuntu-drivers** 由 Canonical 开发，是 Ubuntu 设备驱动管理体系的一部分，用于简化查找和安装硬件驱动的流程。

# SEE ALSO

[apt](/man/apt)(8), [dpkg](/man/dpkg)(1), [nvidia-smi](/man/nvidia-smi)(1)
