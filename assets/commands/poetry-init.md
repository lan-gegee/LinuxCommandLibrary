# TAGLINE

初始化新的 pyproject.toml 文件

# TLDR

**在当前目录交互式初始化**

```poetry init```

**以默认值非交互式初始化**

```poetry init -n```

**指定名称和描述**

```poetry init --name [myproject] --description "[A cool project]"```

**初始化期间添加依赖**

```poetry init --dependency [requests] --dev-dependency [pytest]```

**固定 Python 版本**

```poetry init -n --python "[^3.11]"```

# SYNOPSIS

**poetry init** [_options_]

# PARAMETERS

**-n**, **--no-interaction**
> 跳过交互式提示；未提供的值一律使用默认值。

**--name** _name_
> 软件包名称（默认取当前目录名）。

**--description** _text_
> 软件包描述。

**--author** _author_
> 作者，格式为 **"Name <email>"**。可重复。

**--license** _spdx_
> SPDX 许可证标识符（如 **MIT**、**Apache-2.0**）。

**--python** _constraint_
> Python 版本约束（如 **^3.11**、**>=3.10,<4**）。

**--dependency** _name[@version]_
> 添加运行时依赖。可重复。

**--dev-dependency** _name[@version]_
> 添加开发依赖。可重复。

**--directory** _path_
> 在其他目录中运行 init。

**--help**
> 显示帮助。

# DESCRIPTION

**poetry init** 在目标目录中创建新的 **pyproject.toml**，描述项目的元数据和依赖。交互式流程会依次询问项目名称、版本、作者、许可证、Python 约束以及初始的运行时/开发依赖，并在此过程中对照 PyPI 校验软件包名。

它不会创建虚拟环境、安装依赖或写入锁文件 —— 这些请之后运行 **poetry install** 完成。

# CAVEATS

Poetry 2.0（2025）按照 PEP 621 使用标准的 **[project]** 表写入 pyproject.toml，而旧版本使用旧式的 **[tool.poetry]** 表。具体布局取决于你安装的 Poetry 版本。运行 **poetry --version** 查看。

# HISTORY

**poetry** 由 **Sébastien Eustace** 于 **2018 年**创建，是 Python 项目的依赖管理器和打包工具。**init** 子命令自早期版本起就是 Poetry 的一部分。

# INSTALL

```dnf: sudo dnf install poetry```

```apk: sudo apk add poetry```

```brew: brew install poetry```

```nix: nix profile install nixpkgs#poetry```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[poetry-install](/man/poetry-install)(1), [poetry-new](/man/poetry-new)(1), [poetry](/man/poetry)(1), [pip](/man/pip)(1)
