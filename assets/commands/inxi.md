# TAGLINE

系统信息脚本，提供详细的硬件信息

# TLDR

打印**基础**系统摘要

```inxi```

打印**完整**系统描述并过滤敏感信息

```inxi -ez```

打印 **CPU** 信息

```inxi -C```

打印**显卡**信息

```inxi -G```

打印**内存/RAM** 信息

```inxi -m```

打印**音频**系统信息

```inxi -A```

打印**传感器**数据（温度、风扇）

```inxi -s```

打印**软件仓库**信息

```inxi -r```

# SYNOPSIS

**inxi** [_options_]

# PARAMETERS

**-C**, **--cpu**
> CPU 信息

**-G**, **--graphics**
> 显卡和显示信息

**-m**, **--memory**
> RAM 内存信息

**-A**, **--audio**
> 音频/声卡信息

**-s**, **--sensors**
> 传感器数据（温度、风扇、电压）

**-r**, **--repos**
> 发行版软件仓库信息

**-e**, **--expanded**
> 显示更多细节

**-z**, **--filter**
> 过滤敏感信息（IP、MAC 地址等）

**-F**, **--full**
> 输出完整系统信息

# DESCRIPTION

**inxi** 是一个系统信息脚本，提供关于硬件和软件配置的详细信息。它被设计为一款快速调试和支持工具，输出整洁、人类易读。

该工具从 /proc、/sys 以及各种实用命令等多个系统来源聚合信息，并以一致的格式呈现，适合粘贴到论坛或支持工单中分享。

# CAVEATS

部分信息需要 root 权限。准确性取决于可用的系统工具和内核接口。不同版本之间的输出格式可能有差异。

# HISTORY

inxi 由 locsmif 从 infobash 分支而来，由 inxi 项目团队维护。它已成为许多 Linux 发行版中快速收集系统信息进行调试的标准工具。

# INSTALL

```dnf: sudo dnf install inxi```

```pacman: sudo pacman -S inxi```

```apk: sudo apk add inxi```

```zypper: sudo zypper install inxi```

```brew: brew install inxi```

```nix: nix profile install nixpkgs#inxi```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lshw](/man/lshw)(1), [hwinfo](/man/hwinfo)(8), [lscpu](/man/lscpu)(1)
