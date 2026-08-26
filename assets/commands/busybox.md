# TAGLINE

嵌入式 Linux 实用工具的瑞士军刀

# TLDR

**列出**可用的 applet

```busybox --list```

**运行**特定命令

```busybox ls [-la]```

**创建**符号链接

```busybox --install -s```

**显示**帮助和版本

```busybox --help```

# SYNOPSIS

**busybox** [_applet_] [_arguments_]

# DESCRIPTION

**busybox** 将许多常用的 Unix 实用工具组合成一个单一的小型可执行文件。它实现了 300 多个命令的轻量版本，非常适合嵌入式系统、容器和最小化安装。

该工具在嵌入式 Linux、Android 以及 Alpine Linux 之类的容器镜像中无处不在。

# PARAMETERS

**--list**
> 列出可用的 applet

**--install** [**-s**]
> 创建 applet 符号链接

**--help** [_applet_]
> 显示 applet 的帮助信息

# COMMON APPLETS

核心实用工具：
- **ls, cp, mv, rm** - 文件操作
- **cat, grep, sed, awk** - 文本处理
- **sh** - Shell
- **tar, gzip** - 归档
- **wget** - 下载
- **ping, ifconfig** - 网络

# USAGE MODES

**直接调用**
```bash
busybox ls -la
busybox grep pattern file
```

**符号链接**（最常见）
```bash
# After busybox --install -s
ls -la  # Actually runs busybox ls
grep pattern file  # Actually runs busybox grep
```

**Applet 模式**
```bash
# When busybox is symlinked as command name
/bin/ls -> busybox
```

# FEATURES

- 单一二进制文件（约 1-2 MB）
- 300 多个 Unix 实用工具
- 兼容 POSIX
- 编译时可配置
- 最小依赖
- 嵌入式友好

# CAVEATS

功能简化版（特性少于 GNU 工具）。缺少某些高级选项。行为可能与完整版本略有不同。配置在编译时固定。并非所有构建都提供所有 applet。

# HISTORY

**BusyBox** 由 Bruce Perens 于 **1996 年**为 Debian 安装程序创建，后来成为嵌入式 Linux 系统的标准多合一二进制文件。

# INSTALL

```apt: sudo apt install busybox```

```dnf: sudo dnf install busybox```

```pacman: sudo pacman -S busybox```

```apk: sudo apk add busybox```

```zypper: sudo zypper install busybox```

```nix: nix profile install nixpkgs#busybox```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[alpine](/man/alpine)(1), [toybox](/man/toybox)(1), [coreutils](/man/coreutils)(7)

# RESOURCES

```[Homepage](https://busybox.net)```

<!-- verified: 2026-06-22 -->
