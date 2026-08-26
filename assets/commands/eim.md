# TAGLINE

ESP-IDF 安装管理器

# TLDR

**安装特定的 ESP-IDF 版本**

```eim install -i [v5.3.2]```

**以交互方式安装**（带提示）

```eim install -i [v5.3.2] -n false```

**列出已安装的 ESP-IDF 版本**

```eim list```

**选择一个版本设为活动版本**供 IDE 使用

```eim select [version]```

**重命名已安装的版本**

```eim rename [old_name] [new_name]```

**移除特定的 ESP-IDF 版本**

```eim remove [version]```

# SYNOPSIS

**eim** _command_ [_options_]

# PARAMETERS

_COMMAND_
> 操作：install、list、select、rename、remove、run、purge。

**install** [**-i** _version_]
> 安装 ESP-IDF 版本。默认以非交互（无头）方式运行。

**list**
> 列出已安装的 ESP-IDF 版本。

**select** _version_
> 设置活动的 ESP-IDF 版本（更新 eim_idf.json 以供 IDE 集成）。

**rename** _old_ _new_
> 重命名已安装的 ESP-IDF 版本。

**remove** _version_
> 移除特定的 ESP-IDF 版本。

**run** _version_ _command_
> 在特定 ESP-IDF 版本的环境下运行命令。

**purge**
> 移除所有 ESP-IDF 安装。

**-n** _bool_
> 设置交互模式（true/false，无头安装时默认：true）。

**--help**
> 显示帮助信息。

# DESCRIPTION

**eim**（ESP-IDF Installation Manager）是乐鑫（Espressif）推出的跨平台工具，用于管理 ESP-IDF（Espressif IoT Development Framework）安装。它负责下载、安装以及在多个 ESP-IDF 版本之间切换，服务于 ESP32 开发。

该工具同时支持交互式和非交互式（无头）安装模式，既适合手动配置也适合 CI/CD 自动化。它通过 eim_idf.json 配置文件与 IDE 集成。

# CAVEATS

需要 ESP-IDF 工具链的构建依赖。安装可能耗费大量时间和磁盘空间。**purge** 命令会不可逆地移除所有已安装的版本。

# HISTORY

**eim** 由 **Espressif Systems** 开发，作为 ESP-IDF 开发框架的精简安装器，取代了手动配置流程。

# SEE ALSO

[asdf](/man/asdf)(1)
