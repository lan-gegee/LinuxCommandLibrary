# TAGLINE

移除已加载的内核模块

# TLDR

**移除**内核模块

```sudo rmmod module_name```

以**详细输出**方式移除

```sudo rmmod --verbose module_name```

移除并记录到 **syslog**

```sudo rmmod --syslog module_name```

**强制**移除

```sudo rmmod --force module_name```

# SYNOPSIS

**rmmod** [_-f_] [_-s_] [_-v_] _modulename_...

# DESCRIPTION

**rmmod** 是一个用于从 Linux 内核中移除模块的简单程序。它只移除指定的模块，不会处理依赖该模块的其他模块。

# PARAMETERS

**-f, --force**
> 强制移除，即使模块正在使用中（危险）。

**-s, --syslog**
> 将错误发送到 syslog 而不是 stderr。

**-v, --verbose**
> 打印详细信息。

**-V, --version**
> 显示版本。

**-h, --help**
> 显示帮助。

# CAVEATS

如果模块正被其他模块或进程使用，则无法移除。大多数情况下请改用 **modprobe -r**，因为它会处理依赖关系。**--force** 选项很危险，可能导致系统崩溃。

# HISTORY

**rmmod** 是 **kmod** 的一部分。它提供直接的模块移除功能，不具备 modprobe -r 的智能依赖处理能力。

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

[modprobe](/man/modprobe)(8), [insmod](/man/insmod)(8), [lsmod](/man/lsmod)(8)
