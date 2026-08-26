# TAGLINE

极快的 Python 软件包与项目管理器

# TLDR

**创建新的 Python 项目**

```uv init [project_name]```

**添加依赖**

```uv add [package]```

**移除依赖**

```uv remove [package]```

从 pyproject.toml **同步依赖**

```uv sync```

在项目环境中**运行命令**

```uv run [command]```

**安装 Python 版本**

```uv python install [3.12]```

**创建虚拟环境**

```uv venv```

**全局安装工具**

```uv tool install [ruff]```

# SYNOPSIS

**uv** _command_ [_options_] [_arguments_]

# PARAMETERS

**init** [_name_]
> 创建新的 Python 项目

**add** _package_
> 向 pyproject.toml 添加依赖

**remove** _package_
> 移除依赖

**sync**
> 依据锁文件同步依赖

**lock**
> 生成/更新 uv.lock 文件

**run** _command_
> 在项目环境中运行命令

**python install** _version_
> 安装 Python 版本

**python list**
> 列出已安装的 Python 版本

**venv** [_path_]
> 创建虚拟环境

**pip install** _package_
> 安装软件包（兼容 pip 的接口）

**tool install** _tool_
> 全局安装 CLI 工具

**tool run** _tool_
> 不安装直接运行工具

**--help**, **-h**
> 显示帮助

**--version**, **-V**
> 显示版本

# DESCRIPTION

**uv** 是一个用 Rust 编写、速度极快的 Python 软件包与项目管理器。它用一个统一的工具取代了 pip、pip-tools、pipx、poetry、pyenv 和 virtualenv。

项目通过 **pyproject.toml** 管理，依赖锁定在 **uv.lock** 中。**uv sync** 命令按锁文件中的精确版本进行安装，确保环境可复现。

UV 直接管理 Python 版本，无需 pyenv。使用 **uv python install** 下载并管理多个 Python 版本。

该工具提供与 pip 兼容的接口（**uv pip**），可以在现有工作流中即插即用，同时为新项目提供基于项目的工作流。

# CAVEATS

UV 相对较新（2024 年）且发展迅速。某些边缘情况的行为可能与 pip 不同。

锁文件应提交到版本控制以保证可复现性。修改依赖后请运行 **uv lock**。

对于 CI/CD，使用 **uv sync --frozen**，在锁文件过时时直接失败而不是重新生成。

# HISTORY

UV 由 **Astral**（Ruff 的开发者）创建并于 **2024 年**发布。它借助 Rust 和并行下载实现了比 pip 快 10-100 倍的性能。该工具迅速被广泛采用，成为现代 Python 工具链的替代品。

# INSTALL

```dnf: sudo dnf install uv```

```pacman: sudo pacman -S uv```

```apk: sudo apk add uv```

```brew: brew install uv```

```nix: nix profile install nixpkgs#uv```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pip](/man/pip)(1), [poetry](/man/poetry)(1), [pipx](/man/pipx)(1), [python](/man/python)(1)
