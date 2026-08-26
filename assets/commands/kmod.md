# TAGLINE

管理 Linux 内核模块的核心工具

# TLDR

**列出**当前已加载的内核模块

```kmod list```

显示**静态设备节点**信息

```kmod static-nodes```

# SYNOPSIS

**kmod** [_options_] _command_

# PARAMETERS

**list**
> 列出当前已加载的内核模块（类似 lsmod）

**static-nodes**
> 显示内核模块提供的静态设备节点

# DESCRIPTION

**kmod** 是管理 Linux 内核模块的核心工具。它提供统一接口，通常通过带有更常见名称的符号链接访问。

以下命令都是指向 kmod 的符号链接：
- **lsmod** - 列出已加载的模块
- **insmod** - 插入模块
- **rmmod** - 移除模块
- **modprobe** - 连同依赖一起加载模块
- **modinfo** - 显示模块信息
- **depmod** - 生成模块依赖关系

# CAVEATS

直接使用 kmod 的情况很少见；更常用的是符号链接形式的命令。加载/卸载模块需要相应权限。模块操作会影响整个系统。

# HISTORY

kmod 从 **2011 年**前后开始取代旧的 module-init-tools 软件包。它由 Lucas De Marchi 开发，旨在提供更易维护、更高效的内核模块管理体系。

# INSTALL

```apt: sudo apt install kmod```

```dnf: sudo dnf install kmod```

```pacman: sudo pacman -S kmod```

```apk: sudo apk add kmod```

```zypper: sudo zypper install kmod```

```brew: brew install kmod```

```nix: nix profile install nixpkgs#kmod```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lsmod](/man/lsmod)(8), [modprobe](/man/modprobe)(8), [insmod](/man/insmod)(8), [rmmod](/man/rmmod)(8), [modinfo](/man/modinfo)(8)
