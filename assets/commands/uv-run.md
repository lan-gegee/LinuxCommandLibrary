# TAGLINE

在项目虚拟环境中执行命令

# TLDR

**在项目中运行命令**

```uv run [command]```

**运行 Python 脚本**

```uv run python [script.py]```

**附带额外依赖运行**

```uv run --with [package] [command]```

**运行带内联依赖的独立脚本**

```uv run [script.py]```

**不同步环境直接运行**

```uv run --frozen [command]```

**使用指定的 Python 版本运行**

```uv run --python [3.12] python [script.py]```

**运行已安装的工具**（如 pytest、ruff）

```uv run pytest [tests/]```

# SYNOPSIS

**uv** **run** [_options_] _command_ [_args_...]

# PARAMETERS

**--with** _package_
> 仅在本次调用中包含一个额外依赖。

**--frozen**
> 运行时不更新锁文件。若锁文件缺失或过时则失败。

**--no-sync**
> 运行前跳过环境同步。

**--isolated**
> 在隔离的临时环境中运行，忽略项目。

**--python** _version_
> 使用特定的 Python 版本或解释器。

**--no-project**
> 不查找项目或工作区。

**--package** _name_
> 在工作区内的特定软件包中运行命令。

**--extra** _name_
> 包含可选依赖组。

**--all-extras**
> 包含所有可选依赖组。

# DESCRIPTION

**uv run** 在项目的虚拟环境中执行命令。它会根据需要自动创建虚拟环境并同步依赖，是在 uv 管理的项目中运行脚本和工具的主要方式。

运行带有内联脚本元数据（PEP 723）的 `.py` 文件时，uv 会自动解析并安装所声明的依赖。**--with** 标志允许添加临时依赖而无需修改项目配置。

# CAVEATS

如果找不到 `pyproject.toml`，**uv run** 将在没有项目上下文的情况下运行。**--frozen** 标志要求已存在锁文件，否则会失败。

# INSTALL

```dnf: sudo dnf install uv```

```pacman: sudo pacman -S uv```

```apk: sudo apk add uv```

```brew: brew install uv```

```nix: nix profile install nixpkgs#uv```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[uv](/man/uv)(1), [uv-sync](/man/uv-sync)(1), [uv-lock](/man/uv-lock)(1), [python](/man/python)(1), [pip](/man/pip)(1)
