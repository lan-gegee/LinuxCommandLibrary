# TAGLINE

构建 PlatformIO 项目

# TLDR

**构建项目**

```pio run```

**构建并上传到设备**

```pio run --target upload```

**构建特定环境**

```pio run -e [uno]```

**清理构建文件**

```pio run --target clean```

**构建特定环境**并上传

```pio run -e [esp32dev] --target upload```

**从指定的**项目目录构建

```pio run -d [/path/to/project]```

**以详细模式构建**以便调试

```pio run -v```

**使用并行任务构建**以加快编译速度

```pio run -j [4]```

# SYNOPSIS

**pio run** [_options_]

# PARAMETERS

**-e**, **--environment** _name_
> 处理 platformio.ini 中定义的特定环境。

**-t**, **--target** _target_
> 处理目标（upload、clean、program、uploadfs 等）。

**-d**, **--project-dir** _dir_
> 项目目录（默认：当前目录）。

**--upload-port** _port_
> 上传端口（例如 /dev/ttyUSB0 或 COM3）。

**-j**, **--jobs** _num_
> 并行构建任务数。

**-v**, **--verbose**
> 详细输出，显示完整的编译器命令。

**-s**, **--silent**
> 抑制除错误之外的所有输出。

**--disable-auto-clean**
> 禁用环境配置变更后的自动清理。

**--list-targets**
> 列出可用的项目目标。

# DESCRIPTION

**pio run** 用于构建 PlatformIO 项目。它会编译源代码、链接库，并可选择将固件上传到目标设备。该命令读取 `platformio.ini` 配置文件来确定构建环境、开发板设置和库依赖。这是 PlatformIO 嵌入式开发工作流的核心命令。

可以在 platformio.ini 中定义多个环境，并使用 **-e** 标志进行选择性构建。常见目标包括 **upload**（烧录固件）、**clean**（清除构建产物）和 **uploadfs**（上传文件系统映像）。

# INSTALL

```aur: yay -S pio```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pio-init](/man/pio-init)(1), [pio-device](/man/pio-device)(1), [pio-test](/man/pio-test)(1), [pio-check](/man/pio-check)(1), [pio-debug](/man/pio-debug)(1), [pio-boards](/man/pio-boards)(1)
