# TAGLINE

为 PlatformIO 项目运行持续集成构建

# TLDR

**在 CI 中构建库**

```pio ci --lib [.] --board [uno] [examples/Blink]```

**针对多块开发板构建**

```pio ci --board [uno] --board [esp32dev] [src/]```

**使用项目配置构建**

```pio ci --project-conf [platformio.ini] [src/]```

从构建中**排除文件**

```pio ci --exclude [src/examples] --board [esp32dev] [src/]```

内联**传递项目选项**

```pio ci --board [uno] -O "lib_deps=[ArduinoJSON]" [src/]```

**带详细输出构建**

```pio ci --board [uno] --verbose [src/]```

# SYNOPSIS

**pio ci** [_OPTIONS_] [_SRC_]

# PARAMETERS

**-l**, **--lib** _path_
> 将被复制到构建目录 lib 文件夹的源代码。可多次指定。

**-b**, **--board** _id_
> 基于开发板设置自动预生成的环境来构建项目。可多次指定。

**--exclude** _path_
> 从构建目录中排除目录和/或文件。路径必须相对于构建目录内的 PlatformIO 项目。支持 glob 模式。

**-c**, **--project-conf** _file_
> 使用预配置的 platformio.ini 文件构建项目。

**-O**, **--project-option** _option_
> 传递额外的项目配置选项。可为不同选项多次指定。

**-e**, **--environment** _name_
> 处理项目配置中声明的指定环境。可多次指定。

**--build-dir** _path_
> PlatformIO 初始化新项目的目录路径。默认为临时目录。

**--keep-build-dir**
> 构建过程结束后不删除构建目录。

**-v**, **--verbose**
> 处理环境时显示详细信息。

# DESCRIPTION

**pio ci** 为 PlatformIO 项目运行持续集成构建。它无需现有的项目结构即可针对指定开发板构建源文件。PlatformIO 利用提供的源代码和库内容，在构建目录中初始化一个新项目，并通过 **pio run** 命令处理它。常用于 CI/CD 流水线。

# INSTALL

```aur: yay -S pio```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pio-run](/man/pio-run)(1), [pio-test](/man/pio-test)(1), [pio](/man/pio)(1)
