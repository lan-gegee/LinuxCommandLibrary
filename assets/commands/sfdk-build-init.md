# TAGLINE

初始化 Sailfish OS 构建环境

# TLDR

**初始化构建环境**

```sfdk build-init```

为特定构建目标**初始化**

```sfdk -c target=[SailfishOS-4.5.0.24-armv7hl] build-init```

**持久保存目标**供后续命令使用

```sfdk config --push target [SailfishOS-4.5.0.24-armv7hl]; sfdk build-init```

# SYNOPSIS

**sfdk** [_-c target=name_] **build-init** [_options_]

# PARAMETERS

**-c** _target=name_
> 选择构建目标的全局 sfdk 配置选项。该目标并非 build-init 专有；它通过 **-c** 选项设置（或用 **sfdk config --push target** _name_ 持久保存），并由其他构建子命令复用。

# DESCRIPTION

**sfdk build-init** 针对配置的构建目标，为 Sailfish OS 项目准备（初始化）构建目录。它会设置构建引擎快照和构建时依赖，之后即可运行 **sfdk build-shell**、**sfdk build** 或 **sfdk make** 等命令。属于 Sailfish SDK 命令行工具 **sfdk** 的一部分。

# SEE ALSO

[sfdk](/man/sfdk)(1), [sfdk-build-requires](/man/sfdk-build-requires)(1)
