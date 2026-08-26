# TAGLINE

嵌入式开发平台与构建系统

# TLDR

**初始化项目**

```pio init --board [uno]```

**构建项目**

```pio run```

**上传到开发板**

```pio run --target upload```

**监视串口**

```pio device monitor```

**列出已连接的开发板**

```pio device list```

**安装库**

```pio pkg install --library "[library_name]"```

**搜索开发板**

```pio boards [pattern]```

**清理构建文件**

```pio run --target clean```

# SYNOPSIS

**pio** _command_ [_options_]

# DESCRIPTION

**platformio** 是一个嵌入式开发生态系统。它提供统一的工具，用于跨众多平台和框架构建、上传和调试嵌入式软件。

该工具支持 Arduino、ESP32、STM32 以及数百种其他开发板，并集成了库管理和调试功能。

# PARAMETERS

**init**
> 初始化项目。

**run**
> 构建项目。

**run --target upload**
> 上传固件。

**device monitor**
> 串口监视器。

**device list**
> 列出设备。

**pkg install**
> 安装软件包（库、平台、工具）。

**pkg install --library** _NAME_
> 安装一个库依赖。

**pkg search**
> 在 PlatformIO Registry 中搜索。

**boards**
> 列出受支持的开发板。

**check**
> 运行静态代码分析。

**debug**
> 启动调试器。

**test**
> 运行单元测试。

**home**
> 启动 PlatformIO Home 网页界面。

**-e**, **--environment** _env_
> 指定环境。

**-v**, **--verbose**
> 详细输出。

# CONFIGURATION

**platformio.ini**
> 项目配置文件，定义目标开发板、框架、库依赖和构建选项。

**~/.platformio/**
> PlatformIO 主目录，存放已安装的平台、软件包和全局设置。

**PLATFORMIO_CORE_DIR**
> 用于覆盖 PlatformIO 主目录位置的环境变量。

# CAVEATS

初始设置会下载大量依赖。某些开发板需要驱动程序。`pio lib` 命令族自 PlatformIO 6.0 起已弃用；请改用 `pio pkg`。

# HISTORY

**PlatformIO** 由 **Ivan Kravets** 于 **2014 年**创建，旨在统一嵌入式开发工具链。它解决了各厂商专用 IDE 和构建系统的碎片化问题，深受物联网和创客社区欢迎。

# INSTALL

```brew: brew install platformio```

```nix: nix profile install nixpkgs#platformio```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pio](/man/pio)(1), [arduino-cli](/man/arduino-cli)(1), [make](/man/make)(1), [cmake](/man/cmake)(1), [gdb](/man/gdb)(1)
