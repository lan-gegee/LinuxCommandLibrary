# TAGLINE

管理 pip 配置文件和设置

# TLDR

**列出配置**

```pip config list```

**获取特定设置**

```pip config get [key]```

**设置配置值**

```pip config set [key] [value]```

**编辑配置文件**

```pip config edit```

**删除设置**

```pip config unset [key]```

# SYNOPSIS

**pip** **config** _command_ [_options_]

# PARAMETERS

**list**
> 列出当前生效的配置。

**get** _key_
> 获取配置值。

**set** _key_ _value_
> 设置配置值。

**unset** _key_
> 移除配置值。

**edit**
> 在编辑器中编辑配置文件。

**debug**
> 显示配置文件及其取值。

**--global**
> 使用全局配置文件。

**--user**
> 使用用户配置文件。

**--site**
> 使用 site（虚拟环境级）配置文件。

# DESCRIPTION

**pip config** 用于管理不同作用域的 pip 配置文件。它提供命令行界面来读取、写入和编辑 pip 设置，无需手动查找并编辑 INI 格式的配置文件。

配置分为三个层级：global（系统级）、user（每用户）和 site（每虚拟环境）。设置按层级叠加，越具体的作用域优先级越高。常见设置包括自定义软件包索引 URL、私有仓库的可信主机以及默认安装选项。

使用 **pip config list** 可查看所有生效的设置及其来源，或使用 **pip config debug** 显示完整的搜索路径及存在的文件。**edit** 子命令会在默认编辑器中打开相应的配置文件。

# CONFIGURATION

**~/.config/pip/pip.conf**（Linux）、**~/Library/Application Support/pip/pip.conf**（macOS）、**%APPDATA%\pip\pip.ini**（Windows）
> 用户级配置文件。

**/etc/pip.conf**（Linux/macOS）、**C:\ProgramData\pip\pip.ini**（Windows）
> 全局系统级配置文件。

**$VIRTUAL_ENV/pip.conf**
> 虚拟环境内的 site 级配置文件。

**PIP_CONFIG_FILE**
> 用于覆盖默认配置文件位置的环境变量。

# INSTALL

```apk: sudo apk add py3-pip```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pip](/man/pip)(1)
