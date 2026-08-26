# TAGLINE

查看 PlatformIO 项目配置和元数据

# TLDR

**显示项目配置**

```pio project config```

**显示项目元数据**

```pio project metadata -e [uno]```

**初始化项目数据**

```pio project init```

# SYNOPSIS

**pio project** _command_ [_options_]

# PARAMETERS

**config**
> 显示项目配置。

**metadata**
> 显示项目元数据。

**init**
> 初始化项目。

**-e**, **--environment** _name_
> 目标环境。

**-d**, **--project-dir** _dir_
> 项目目录。

**--json-output**
> 以 JSON 格式输出。

# DESCRIPTION

**pio project** 用于检查 PlatformIO 项目的配置和元数据，可显示解析后的 platformio.ini 设置、解析后的依赖以及构建信息。

# INSTALL

```aur: yay -S pio```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pio-init](/man/pio-init)(1), [pio-run](/man/pio-run)(1)
