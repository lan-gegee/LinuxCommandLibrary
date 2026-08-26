# TAGLINE

提取机器硬件配置的详细信息

# TLDR

**以紧凑表格列出所有硬件**

```sudo lshw -short```

**显示 CPU 信息**

```sudo lshw -class processor```

**显示磁盘和存储设备**

```sudo lshw -class disk -class storage -short```

**显示网络硬件**

```sudo lshw -class network```

**以 JSON 输出**

```sudo lshw -json```

**将网络信息保存为 HTML**

```sudo lshw -class network -html > network.html```

**去除敏感信息**（序列号、IP）

```sudo lshw -sanitize```

# SYNOPSIS

**lshw** [_-format_] [_-class class_] [_options_]

# DESCRIPTION

**lshw**（Hardware Lister）提取机器硬件配置的详细信息，可以报告内存、固件、CPU、总线、磁盘、网络等硬件配置。

# PARAMETERS

**-class CLASS**
> 只显示指定的硬件类别（可重复使用）

**-short**
> 以紧凑的表格格式输出硬件路径

**-businfo**
> 输出总线信息

**-X**
> 启动图形界面（如可用）

**-html**
> 以 HTML 输出

**-xml**
> 以 XML 输出

**-json**
> 以 JSON 输出

**-sanitize**
> 移除敏感信息（IP、序列号）

**-numeric**
> 输出数字 ID

**-quiet**
> 抑制状态消息

**-notime**
> 在输出中排除时间信息

**-enable TEST**
> 启用特定测试

**-disable TEST**
> 禁用特定测试

# HARDWARE CLASSES

system, bridge, memory, processor, address, storage, disk, tape, bus, network, display, input, printer, multimedia, communication, power, volume, generic

# CAVEATS

完整的硬件信息需要 root 权限。没有 root 时，部分细节可能缺失或不准确。

# HISTORY

**lshw** 由 Lyonel Vincent 开发，是 Linux 上的综合硬件信息工具，比基础工具提供更多细节。

# INSTALL

```apt: sudo apt install lshw```

```dnf: sudo dnf install lshw```

```pacman: sudo pacman -S lshw```

```apk: sudo apk add lshw```

```zypper: sudo zypper install lshw```

```nix: nix profile install nixpkgs#lshw```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dmidecode](/man/dmidecode)(8), [hwinfo](/man/hwinfo)(8), [inxi](/man/inxi)(1), [lscpu](/man/lscpu)(1)
