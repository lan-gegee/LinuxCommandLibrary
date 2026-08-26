# TAGLINE

面向嵌入式系统的开发平台

# TLDR

**初始化新项目**

```pio project init --board [uno]```

**构建项目**

```pio run```

**上传到开发板**

```pio run --target upload```

**监视串口**

```pio device monitor```

**列出开发板**

```pio boards [search_term]```

**安装库**

```pio pkg install --library "[library_name]"```

**运行测试**

```pio test```

**检查更新**

```pio pkg update```

# SYNOPSIS

**pio** [_project_] [_run_] [_device_] [_pkg_] [_boards_] [_options_] [_args_]

# PARAMETERS

**project init**
> 初始化项目。

**run**
> 构建项目。

**run -t upload**
> 上传固件。

**run -t clean**
> 清理构建产物。

**device monitor**
> 串口监视器。

**device list**
> 列出设备。

**boards** [_QUERY_]
> 搜索开发板。

**pkg install**
> 安装软件包。

**pkg update**
> 更新软件包。

**pkg list**
> 列出软件包。

**test**
> 运行单元测试。

**-e** _ENV_
> 目标环境。

**-d** _DIR_
> 项目目录。

**-v**
> 详细输出。

# DESCRIPTION

**pio**（PlatformIO Core CLI）是一个面向嵌入式系统的开发平台，支持数百种开发板，包括 Arduino、ESP32、STM32 等。

项目初始化会创建目录结构和配置。platformio.ini 文件定义了开发板、框架和依赖。

构建会针对目标平台编译代码。可以为不同的开发板或配置定义多个环境。

上传将固件传输到已连接的设备。串口监视器提供用于调试的交互式通信。

库管理负责处理依赖。库可以全局安装或按项目安装。注册表中包含数千个库。

单元测试可以在嵌入式设备或主机上运行，从而为固件实现测试驱动开发。

通过 PlatformIO IDE 扩展集成 VS Code 可提供完整的开发环境。

# CAVEATS

平台支持需要大量下载。首次构建会下载工具链。某些冷门开发板可能不受支持。高级用法的配置可能较为复杂。

# HISTORY

**PlatformIO** 由 **Ivan Kravets** 自 **2014 年**前后开始创建。它统一了碎片化的嵌入式开发工具，为物联网开发提供了跨平台、不依赖特定厂商的基础设施。

# INSTALL

```aur: yay -S pio```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[arduino-cli](/man/arduino-cli)(1), [esptool](/man/esptool)(1), [avrdude](/man/avrdude)(1), [openocd](/man/openocd)(1)
