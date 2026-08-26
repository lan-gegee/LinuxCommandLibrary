# TAGLINE

输出系统和内核信息

# TLDR

**显示所有系统信息**

```uname -a```

**显示内核名称**

```uname -s```

**显示主机名**

```uname -n```

**显示内核发行版本**

```uname -r```

**显示内核版本**

```uname -v```

**显示机器硬件名称**（架构）

```uname -m```

**显示操作系统**

```uname -o```

# SYNOPSIS

**uname** [_options_]

# PARAMETERS

**-a**, **--all**
> 输出所有信息

**-s**, **--kernel-name**
> 输出内核名称（如 Linux）

**-n**, **--nodename**
> 输出网络主机名

**-r**, **--kernel-release**
> 输出内核发行版本（如 5.15.0-generic）

**-v**, **--kernel-version**
> 输出内核版本

**-m**, **--machine**
> 输出机器硬件名称（如 x86_64、arm64）

**-p**, **--processor**
> 输出处理器类型

**-i**, **--hardware-platform**
> 输出硬件平台

**-o**, **--operating-system**
> 输出操作系统

# DESCRIPTION

**uname** 输出关于机器和操作系统的系统信息。它常用于脚本中检测平台并相应地调整行为。

最常见的用法是 **uname -a** 查看所有信息，以及 **uname -m** 确定系统架构（便于下载正确的二进制文件）。

不同的 Unix 系统可能支持不同的选项。**-s**、**-n**、**-r**、**-v** 和 **-m** 选项在各种 Unix 变体之间的可移植性最好。

# CAVEATS

在某些系统上，如果信息不可用，**-p** 和 **-i** 可能返回 "unknown"。

**uname -m** 的输出因系统而异：x86_64、amd64、arm64、aarch64 在不同系统上可能表示相似的架构。

在 Linux 上查看详细的发行版信息，请检查 **/etc/os-release** 或使用 **lsb_release**。

# HISTORY

**uname** 起源于 20 世纪 70 年代末的 **PWB/UNIX**。它属于 POSIX 标准，在 Linux 上是 GNU coreutils 的一部分。

# INSTALL

```apt: sudo apt install coreutils```

```dnf: sudo dnf install coreutils```

```pacman: sudo pacman -S coreutils```

```apk: sudo apk add coreutils```

```zypper: sudo zypper install coreutils```

```brew: brew install coreutils```

```nix: nix profile install nixpkgs#coreutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[hostname](/man/hostname)(1), [arch](/man/arch)(1), [hostnamectl](/man/hostnamectl)(1), [lsb_release](/man/lsb_release)(1)
