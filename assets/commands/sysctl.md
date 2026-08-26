# TAGLINE

查看和修改内核参数

# TLDR

**显示**所有可用变量及其值

```sysctl -a```

**设置**一个可写的内核状态变量

```sysctl -w [section.tunable]=[value]```

**获取**当前打开的文件句柄数

```sysctl fs.file-nr```

**获取**同时打开文件的上限

```sysctl fs.file-max```

**应用** /etc/sysctl.conf 中的更改

```sysctl -p```

# SYNOPSIS

**sysctl** [_options_] [_variable_[=_value_]] ...

# PARAMETERS

**-a, --all**
> 显示所有可用变量

**-w, --write**
> 向变量写入值

**-p, --load [_file_]**
> 从文件加载设置（默认：/etc/sysctl.conf）

**-n, --values**
> 只打印值，不打印变量名

**-e, --ignore**
> 忽略未知变量

**-q, --quiet**
> 抑制错误消息

**--system**
> 从所有系统配置文件加载设置

# DESCRIPTION

**sysctl** 用于在运行时检查和修改内核参数。可用参数列在 **/proc/sys/** 下，可使用该工具读取或写入。

常见类别包括 **kernel.**（核心内核设置）、**net.**（网络）、**vm.**（虚拟内存）和 **fs.**（文件系统）。用 sysctl 所做的更改是临时的，除非持久化到配置文件。

# CONFIGURATION

**/etc/sysctl.conf**
> 持久化内核参数设置的主配置文件，在启动时加载。

**/etc/sysctl.d/*.conf**
> 用于模块化内核参数配置文件的 drop-in 目录。

# CAVEATS

除非保存到 **/etc/sysctl.conf** 或 **/etc/sysctl.d/** 下的文件，否则重启后更改会丢失。部分参数是只读的。错误的值可能导致系统不稳定。修改值需要 root 权限。

# HISTORY

**sysctl** 是 **procps**（现 procps-ng）的一部分。它为 /proc/sys 虚拟文件系统提供了便捷接口，可在运行时读写内核参数。

# INSTALL

```apt: sudo apt install procps```

```dnf: sudo dnf install procps-ng```

```pacman: sudo pacman -S procps-ng```

```apk: sudo apk add procps-ng```

```zypper: sudo zypper install procps```

```brew: brew install procps```

```nix: nix profile install nixpkgs#procps```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[proc](/man/proc)(5)
