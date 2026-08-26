# TAGLINE

管理 Sailfish OS 模拟器实例

# TLDR

**启动模拟器**

```sfdk emulator start```

**停止模拟器**

```sfdk emulator stop```

**列出模拟器**

```sfdk emulator list```

**显示模拟器**属性

```sfdk emulator show```

**设置模拟器** CPU 数量

```sfdk emulator set vm.cpuCount=[4]```

**设置模拟器**内存大小

```sfdk emulator set vm.memorySize=[2048]```

# SYNOPSIS

**sfdk emulator** _command_ [_options_]

# PARAMETERS

**start**
> 启动模拟器虚拟机。

**stop**
> 停止模拟器虚拟机。

**list**
> 列出可用的模拟器实例。

**show**
> 显示模拟器虚拟机的属性。

**set** _property=value_
> 设置模拟器虚拟机属性（例如 vm.cpuCount、vm.memorySize）。

**status**
> 显示模拟器的当前状态。

# DESCRIPTION

**sfdk emulator** 管理用于测试应用程序的 Sailfish OS 模拟器实例。它提供启动、停止和配置模拟器虚拟机的命令。可以使用 **set** 子命令调整 CPU 数量和内存大小等 VM 属性。属于 Sailfish SDK 的一部分。

# SEE ALSO

[sfdk](/man/sfdk)(1), [sfdk-device](/man/sfdk-device)(1)
