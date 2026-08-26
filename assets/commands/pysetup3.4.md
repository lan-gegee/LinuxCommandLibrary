# TAGLINE

已弃用的 Python 3.4 软件包安装器

# TLDR

**安装软件包（已弃用）**

```pysetup3.4 install [package]```

**运行 setup 命令**

```pysetup3.4 run [command]```

# SYNOPSIS

**pysetup3.4** [_command_] [_options_]

# PARAMETERS

_COMMAND_
> setup 命令。

**install**
> 安装软件包。

**run**
> 运行命令。

# DESCRIPTION

**pysetup3.4** 是随 Python 3.4 附带的软件包安装与管理工具，属于 distutils2 打包计划的一部分。它在 pip 成为标准包管理器之前，提供安装、卸载和管理 Python 软件包的命令。

该工具已被弃用，完全由 **pip** 取代。新项目不应使用它；仍在依赖它的遗留系统应迁移到 pip 进行包管理。

# CAVEATS

已弃用。请改用 pip。

# HISTORY

pysetup3.4 是**已弃用的 distutils2** 打包计划的一部分。

# SEE ALSO

[pip](/man/pip)(1), [python3.4](/man/python3.4)(1)
