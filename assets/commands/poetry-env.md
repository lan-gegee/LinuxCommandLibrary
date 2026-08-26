# TAGLINE

管理 Poetry 虚拟环境

# TLDR

**列出环境**

```poetry env list```

**显示环境信息**

```poetry env info```

**使用特定 Python**

```poetry env use [python3.11]```

**移除环境**

```poetry env remove [python3.11]```

**显示环境路径**

```poetry env info --path```

# SYNOPSIS

**poetry env** _command_ [_options_]

# COMMANDS

**info**
> 显示环境信息。

**list**
> 列出所有环境。

**use** _python_
> 激活 Python 版本。

**remove** _envs_
> 移除环境。

# PARAMETERS

**--path**
> 仅显示环境路径。

**--executable**
> 仅显示 Python 可执行文件。

# DESCRIPTION

**poetry env** 管理 Poetry 项目的虚拟环境。它可以创建、列出和移除环境，还能在不同 Python 版本之间切换。

# EXAMPLES

```bash
# Show current environment
poetry env info

# Get environment path
poetry env info --path

# List all environments
poetry env list

# Switch to Python 3.11
poetry env use python3.11

# Use specific path
poetry env use /usr/bin/python3.10

# Remove environment
poetry env remove python3.9

# Remove all environments
poetry env remove --all
```

# ENVIRONMENT LOCATION

By default, environments are in:
```
~/.cache/pypoetry/virtualenvs/
```

Or project-local with:
```
poetry config virtualenvs.in-project true
```

# CAVEATS

Python 版本须单独安装。Poetry 管理的是环境，而非 Python 本身的安装。

# HISTORY

poetry env 是 **Sébastien Eustace** 的 **Poetry** 的一部分，为 Python 项目提供虚拟环境管理。

# INSTALL

```dnf: sudo dnf install poetry```

```apk: sudo apk add poetry```

```brew: brew install poetry```

```nix: nix profile install nixpkgs#poetry```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[poetry](/man/poetry)(1), [poetry-install](/man/poetry-install)(1), [pyenv](/man/pyenv)(1)
