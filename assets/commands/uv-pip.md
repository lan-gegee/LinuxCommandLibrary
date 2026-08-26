# TAGLINE

快速且兼容 pip 的软件包管理接口

# TLDR

向当前环境**安装软件包**

```uv pip install [package]```

从 requirements 文件**安装**

```uv pip install -r requirements.txt```

**安装到系统 Python**（不使用 virtualenv）

```uv pip install --system [package]```

**卸载**软件包

```uv pip uninstall [package]```

**列出已安装的**软件包

```uv pip list```

将环境**冻结**为 requirements 格式

```uv pip freeze```

将 `pyproject.toml` 或 `requirements.in` **编译**为固定版本的 `requirements.txt`

```uv pip compile [requirements.in] -o requirements.txt```

将环境**同步**到与 requirements 文件完全一致

```uv pip sync requirements.txt```

# SYNOPSIS

**uv pip** _subcommand_ [_options_] [_arguments_]

# SUBCOMMANDS

**install** _packages_
> 向环境中安装软件包。

**uninstall** _packages_
> 从环境中移除软件包。

**list**
> 列出已安装的软件包。

**freeze**
> 以 requirements 格式输出已安装的软件包。

**show** _package_
> 显示软件包的元数据和位置。

**check**
> 验证环境中的依赖是否兼容。

**compile** _input_
> 解析依赖并固定版本，生成锁文件风格的 requirements.txt。

**sync** _requirements_
> 安装/卸载软件包，使环境与文件完全一致。

**tree**
> 显示已安装软件包的依赖树。

# PARAMETERS

**-r**, **--requirement** _FILE_
> 从给定的 requirements 文件安装（可重复使用）。

**-e**, **--editable** _PATH_
> 以可编辑模式安装项目。

**-U**, **--upgrade**
> 允许升级已安装的软件包。

**--system**
> 操作系统 Python 而不是虚拟环境。

**--python** _PATH_
> 使用指定的 Python 解释器。

**--index-url** _URL_
> 覆盖软件包索引 URL。

**--no-deps**
> 跳过依赖的安装。

**--reinstall**
> 重新安装所有软件包，即使已经安装过。

**--dry-run**
> 只解析依赖而不修改环境。

# DESCRIPTION

**uv pip** 提供与 pip 兼容的命令，由 **uv** 基于 Rust 的解析器和安装器驱动。它是 `pip`、`pip-tools` 和 `virtualenv` 在非项目工作流中的即插即用替代品，通常快 10-100 倍。

与 `pip` 不同，`uv pip` 不会自动创建或激活虚拟环境。它要么使用当前活动的 `.venv` / `VIRTUAL_ENV`，要么需要 `--system` 来操作系统 Python。

# CAVEATS

`uv pip` 用于临时性的软件包管理。对于带锁文件的项目工作流，建议使用直接管理 `pyproject.toml` 和 `uv.lock` 的 `uv add`/`uv sync`/`uv lock`。

# INSTALL

```dnf: sudo dnf install uv```

```pacman: sudo pacman -S uv```

```apk: sudo apk add uv```

```brew: brew install uv```

```nix: nix profile install nixpkgs#uv```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[uv](/man/uv)(1), [pip](/man/pip)(1), [pipx](/man/pipx)(1), [poetry](/man/poetry)(1)
