# TAGLINE

初始化新的 PlatformIO 项目

# TLDR

**在当前目录初始化项目**

```pio init```

**使用指定开发板初始化**

```pio init --board [uno]```

**附带 IDE 支持初始化**

```pio init --ide [vscode]```

**在指定目录初始化**

```pio init -d [project_dir]```

# SYNOPSIS

**pio init** [_options_]

# PARAMETERS

**-b**, **--board** _id_
> 要为其初始化的开发板 ID。

**-d**, **--project-dir** _dir_
> 项目目录。

**--ide** _ide_
> 生成 IDE 项目文件（vscode、atom 等）。

**-O** _option_
> 格式为 section.option=value 的项目选项。

**-e**, **--environment** _name_
> 默认环境名称。

# DESCRIPTION

**pio init** 初始化新的 PlatformIO 项目。创建包含 platformio.ini 配置文件的项目结构。支持多块开发板和多种 IDE 集成，便于嵌入式开发。

# INSTALL

```aur: yay -S pio```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pio-run](/man/pio-run)(1), [pio-boards](/man/pio-boards)(1), [pio-lib](/man/pio-lib)(1)
