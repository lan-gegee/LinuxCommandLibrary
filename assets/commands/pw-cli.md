# TAGLINE

从命令行管理 PipeWire 对象

# TLDR

按类型**列出**对象

```pw-cli ls [Node|Link|Port|Device]```

显示特定对象的**信息**

```pw-cli info [4]```

显示**所有**对象的信息

```pw-cli info all```

**监控**变更

```pw-cli -m```

显示**帮助**

```pw-cli help```

# SYNOPSIS

**pw-cli** [**-m**|**--monitor**] [_command_] [_args_...]

# COMMANDS

**ls, list-objects _type_**
> 列出指定类型的对象

**i, info _id_|_all_**
> 显示某个对象或所有对象的信息

**create-node _factory_ _props_**
> 创建新节点

**destroy _id_**
> 销毁一个对象

**enum-params _id_ _param_**
> 枚举对象参数

**set-param _id_ _param_ _value_**
> 设置对象参数

# PARAMETERS

**-m, --monitor**
> 监控对象变化

**-r, --remote _name_**
> 连接到远程 PipeWire 实例

**-h, --help**
> 显示帮助信息

# DESCRIPTION

**pw-cli** 是用于管理 PipeWire 的命令行界面。它可以列出、查看、创建和销毁 PipeWire 对象，包括节点、链接、端口和设备。

该工具提供对 PipeWire 对象模型的底层访问，适合调试、编写脚本以及理解音频图。

# CAVEATS

需要正在运行的 PipeWire 守护进程。对象 ID 在不同会话之间可能变化。更简单的管理可使用 wpctl。某些操作需要了解 PipeWire 内部机制。

# HISTORY

**pw-cli** 是 **PipeWire**（Linux 上的现代多媒体框架）的一部分。它提供与 PulseAudio 的 pactl 类似的管理能力。

# INSTALL

```apt: sudo apt install pipewire-bin```

```apk: sudo apk add pipewire-tools```

```zypper: sudo zypper install pipewire-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pw-top](/man/pw-top)(1), [pw-dump](/man/pw-dump)(1), [wpctl](/man/wpctl)(1), [pipewire](/man/pipewire)(1)
