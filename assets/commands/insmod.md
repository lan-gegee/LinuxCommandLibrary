# TAGLINE

向 Linux 内核插入模块的简单程序

# TLDR

**插入**内核模块

```sudo insmod path/to/module.ko```

插入带**参数**的模块

```sudo insmod path/to/module.ko param=value```

# SYNOPSIS

**insmod** [_filename_] [_module options_...]

# DESCRIPTION

**insmod** 是一个向 Linux 内核插入模块的简单程序。它要求提供模块文件的完整路径。与 modprobe 不同，insmod 不会自动处理依赖关系。

# PARAMETERS

_filename_
> 内核模块文件（**.ko**）的路径。使用 **-** 可从标准输入读取模块。

_module options_
> 加载时传给模块的 key=value 参数。

**-f**, **--force**
> 禁用内核版本和 vermagic 检查。危险：可能导致内存损坏或崩溃。

**--force-modversion**
> 忽略模块版本符号不匹配。

**--force-vermagic**
> 忽略 vermagic 字符串不匹配。

**-s**, **--syslog**
> 将错误消息发送到 syslog 而非 stderr。

**-v**, **--verbose**
> 打印 insmod 正在执行操作的详细信息。

**-V**, **--version**
> 显示程序版本并退出。

**-h**, **--help**
> 显示帮助并退出。

# CAVEATS

insmod 是底层工具，不会解析依赖，且要求提供 **.ko** 文件的完整路径。大多数情况下请改用 **modprobe**，因为它能处理依赖并使用模块名而非文件路径。详细的错误诊断通常出现在 **dmesg** 中而非 stderr 上。加载模块需要 root 权限。

# HISTORY

**insmod** 是 **kmod** 的一部分。它直接插入模块而不具备 modprobe 的智能处理能力，适用于测试或加载不在标准模块路径中的模块。

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

[modprobe](/man/modprobe)(8), [rmmod](/man/rmmod)(8), [lsmod](/man/lsmod)(8), [modinfo](/man/modinfo)(8), [depmod](/man/depmod)(8), [kmod](/man/kmod)(8), [dmesg](/man/dmesg)(1)
