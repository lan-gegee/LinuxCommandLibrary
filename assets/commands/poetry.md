# TAGLINE

Python 依赖管理与打包工具

# TLDR

**创建新项目**

```poetry new [project-name]```

**在现有目录中初始化**

```poetry init```

**安装依赖**

```poetry install```

**添加软件包**

```poetry add [package]```

**移除软件包**

```poetry remove [package]```

**运行命令**

```poetry run [command]```

**激活虚拟环境**

```poetry shell```

# SYNOPSIS

**poetry** [_command_] [_options_]

# PARAMETERS

**new** _NAME_
> 创建新项目。

**init**
> 以交互方式初始化。

**install**
> 安装依赖。

**add** _PKG_
> 添加依赖。

**remove** _PKG_
> 移除依赖。

**run** _CMD_
> 在虚拟环境中运行命令。

**shell**
> 在虚拟环境中启动 shell。

**update**
> 更新依赖。

# DESCRIPTION

**poetry** 是一个 Python 依赖管理与打包工具，使用 **pyproject.toml** 作为唯一的配置文件。它负责依赖解析、虚拟环境管理、构建以及向 PyPI 发布软件包。

Poetry 为每个项目创建相互隔离的虚拟环境，并使用 lock 文件（**poetry.lock**）确保在不同机器上安装结果可复现。主要命令包括 **install**（安装依赖）、**add**/**remove**（管理依赖）、**run**（在虚拟环境中执行）和 **shell**（激活虚拟环境）。

# CONFIGURATION

**pyproject.toml**
> 项目配置文件，包含依赖、元数据、构建设置以及 `[tool.poetry]` 下的 Poetry 专属设置。

**poetry.lock**
> lock 文件，确保每次安装的依赖解析结果可复现。

**~/.config/pypoetry/config.toml**
> Poetry 全局配置，包括虚拟环境设置、仓库凭据和缓存路径。

# CAVEATS

需要 Python 3.8 及以上版本。使用自己的虚拟环境。

# HISTORY

Poetry 作为**现代 Python** 依赖管理方案而诞生。

# INSTALL

```dnf: sudo dnf install poetry```

```apk: sudo apk add poetry```

```brew: brew install poetry```

```nix: nix profile install nixpkgs#poetry```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pip](/man/pip)(1), [pipenv](/man/pipenv)(1), [python](/man/python)(1)
