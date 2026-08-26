# TAGLINE

在虚拟环境中执行命令

# TLDR

**在虚拟环境中运行命令**

```poetry run [command]```

**运行 Python 脚本**

```poetry run python [script.py]```

**运行已安装的工具**

```poetry run pytest```

**带参数运行**

```poetry run python -m [module] [args]```

# SYNOPSIS

**poetry run** _command_ [_args_]

# PARAMETERS

_COMMAND_
> 要执行的命令。

_ARGS_
> 要传递的参数。

# DESCRIPTION

**poetry run** 在项目的虚拟环境中执行命令，无需手动激活。它会自动定位并使用当前项目对应的正确虚拟环境。

这是运行项目脚本、测试套件和已安装工具的推荐方式。例如 `poetry run pytest` 使用项目的依赖运行测试，`poetry run python script.py` 用项目的 Python 解释器执行脚本。交互式会话可改用 **poetry shell**。

# CAVEATS

venv 不存在时会创建。是 poetry shell 的替代方案。

# HISTORY

poetry run 提供**虚拟环境**内的命令执行功能。

# INSTALL

```dnf: sudo dnf install poetry```

```apk: sudo apk add poetry```

```brew: brew install poetry```

```nix: nix profile install nixpkgs#poetry```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[poetry](/man/poetry)(1), [poetry-shell](/man/poetry-shell)(1)
