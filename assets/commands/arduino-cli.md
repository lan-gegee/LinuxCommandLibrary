# TAGLINE

Arduino 开发的官方命令行工具

# TLDR

**列出已连接的板卡**

```arduino-cli board list```

为指定板卡**编译 sketch**

```arduino-cli compile --fqbn [arduino:avr:uno] [path/to/sketch]```

将编译好的 sketch **上传**到板卡

```arduino-cli upload --port [/dev/ttyACM0] --fqbn [arduino:avr:uno] [path/to/sketch]```

一条命令完成**编译并上传**

```arduino-cli compile --fqbn [arduino:avr:uno] --port [/dev/ttyACM0] -u [path/to/sketch]```

**创建新的 sketch**

```arduino-cli sketch new [MySketch]```

**安装板卡平台**

```arduino-cli core install [arduino:avr]```

**搜索库**

```arduino-cli lib search [servo]```

**安装库**

```arduino-cli lib install "[Servo]"```

在端口上**打开串口监视器**

```arduino-cli monitor --port [/dev/ttyACM0]```

**更新平台索引**并升级所有已安装的平台

```arduino-cli core update-index && arduino-cli core upgrade```

# SYNOPSIS

**arduino-cli** _command_ [_flags_]

# PARAMETERS

**board list**
> 列出已连接的 Arduino 板卡及其端口和 FQBN

**board listall**
> 列出所有已知的板卡类型

**compile**
> 编译 Arduino sketch

**upload**
> 将编译好的二进制文件上传到板卡

**sketch new** _name_
> 在 sketchbook 中创建新 sketch

**core install** _platform_
> 安装板卡平台（如 arduino:avr）

**core update-index**
> 更新平台索引

**lib install** _name_
> 从库管理器安装库

**lib search** _query_
> 搜索库

**lib list**
> 列出已安装的库

**monitor**
> 打开串口监视器与板卡通信

**config init**
> 创建默认配置文件

**core upgrade**
> 将所有已安装的板卡平台升级到最新版本

**-b**, **--fqbn** _string_
> 完全限定板卡名称（如 arduino:avr:uno）

**-p**, **--port** _string_
> 端口地址（如 /dev/ttyACM0 或 COM3）

**-u**, **--upload**
> 编译后上传二进制文件（配合 compile 使用）

**-e**, **--export-binaries**
> 将编译产物导出到 sketch 文件夹

**--output-dir** _path_
> 编译产物目录

**-t**, **--verify**
> 上传后校验上传的二进制文件

**-v**, **--verbose**
> 编译或上传时启用详细输出

**-P**, **--programmer** _name_
> 上传时使用指定的编程器

# DESCRIPTION

**arduino-cli** 是 Arduino 开发的官方命令行工具。它无需 Arduino IDE 即可进行板卡和库管理、sketch 编译、上传以及串口监视。

该工具使用完全限定板卡名称（FQBN）标识目标板卡，格式为 **vendor:architecture:board**（如 arduino:avr:uno）。编译前必须先安装对应的板卡平台。

典型工作流：用 **core install** 安装目标平台，用 **compile** 编译 sketch，再用 **upload** 上传。给 compile 加上 **--upload** 标志可一步完成两个步骤。

该工具支持通过 **--libraries** 标志使用自定义库，通过 **--build-property** 配置板卡参数，并能很好地集成到 VS Code 等 IDE 的 Arduino 开发工作流中。

# CONFIGURATION

**~/.arduino15/arduino-cli.yaml**
> 主配置文件，控制板卡管理器 URL、库路径、日志记录和构建默认值。

# CAVEATS

上传需要串口有相应权限；在 Linux 上用户通常需要加入 **dialout** 或 **uucp** 组。**upload** 命令不会自动编译；要合并两步请使用 **compile --upload**。首次使用前必须安装板卡平台。

# HISTORY

**arduino-cli** 由 **Arduino** 开发并于 **2018** 年发布，作为旧版 Arduino 命令行工具的现代替代品。它的目标是支持无界面的 Arduino 开发、支撑 CI/CD 流水线，并为第三方 IDE 集成奠定基础。该工具与 Arduino IDE 2.0 共享同一核心，目前仍在积极维护。

# INSTALL

```pacman: sudo pacman -S arduino-cli```

```brew: brew install arduino-cli```

```nix: nix profile install nixpkgs#arduino-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[avrdude](/man/avrdude)(1), [platformio](/man/platformio)(1), [screen](/man/screen)(1), [minicom](/man/minicom)(1)
