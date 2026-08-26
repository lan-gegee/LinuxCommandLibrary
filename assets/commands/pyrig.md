# TAGLINE

Python 项目脚手架与维护工具

# TLDR

**初始化**新项目（先将 pyrig 添加为开发依赖）

```uv add pyrig --dev && uv run pyrig init```

**同步**所有受管的配置文件和测试骨架

```uv run pyrig sync```

**为项目生成新的 CLI 命令**

```uv run pyrig mk cmd [command_name]```

**生成共享 CLI 命令**（在所有 pyrig-runtime 项目中可用）

```uv run pyrig mk cmd [command_name] --shared```

**以交互方式创建子类**以覆盖 pyrig 行为

```uv run pyrig mk subcls```

**创建缺失的** `__init__.py` 文件

```uv run pyrig mk inits```

**删除所有** `__pycache__` 目录

```uv run pyrig rm pyc```

**从项目中移除 pyrig** 及其痕迹

```uv run pyrig rm pyrig```

# SYNOPSIS

**pyrig** _command_ [_options_] [_arguments_]

# DESCRIPTION

**pyrig** 是一个带有强烈预设立场的命令行工具，用于为 Python 项目"装配骨架"：它搭建完整可用的项目布局，并在项目演进过程中保持配置、CLI 入口、测试和 CI/CD 同步。它被设计为架在 **uv** 之上作为包管理器和构建工具，要求 **Python 3.12+** 和 **Git**。

典型工作流：用 **uv init** 创建项目，将 pyrig 添加为开发依赖（**uv add pyrig --dev**），然后运行 **pyrig init**。该命令会重新生成受管的项目文件（保留 **pyproject.toml**），配置 linter、格式化工具、类型检查器、git 钩子、GitHub Actions 工作流、可用的 CLI 以及相关工具，最后创建初始提交。此后，**pyrig sync** 让配置文件和镜像测试骨架与源码树保持一致，**pyrig mk** 辅助命令则用来生成新的命令、子类和本地忽略文件。

自定义基于继承：每个受管的配置和工具都对应一个 Python 类。继承并重写方法（或用 **pyrig mk subcls** 生成存根）；pyrig 会自动发现自定义类。可选插件（例如 PyPI 发布、Codecov、独立可执行文件）就是作为依赖添加的普通包，会被 **init** 和 **sync** 自动识别。

CLI 入口是控制台脚本 **pyrig**（通过 **pyproject.toml** 注册）。在 uv 管理的项目中通常用 **uv run pyrig** 调用。由 pyrig 生成的项目还会获得自己的项目 CLI（例如 **my-project version**）。

# COMMANDS

**init**
> 完整的项目初始化：删除现有的受管配置文件（**pyproject.toml** 除外），重新生成脚手架并创建初始提交。集成远程 CI/CD 时建议使用空的 GitHub 仓库（不要先提交 README/许可证）。

**sync**
> 创建或更新所有受管项目文件和镜像测试骨架，使其匹配当前源码树和已安装的插件。

**scratch**
> 运行项目的 **.scratch.py** 文件。

**rm pyc**
> 删除项目下所有 **__pycache__** 目录。

**rm pyrig**
> 将 pyrig 及其受管产物从项目中彻底移除。

**mk cmd** _name_
> 在项目的子命令模块中生成新的 CLI 命令存根。使用 **--shared** 可注册一个在该环境中所有基于 pyrig-runtime 的项目中都可用的命令。

**mk inits**
> 在包目录树中创建所有缺失的 **__init__.py** 文件。

**mk local**
> 创建或更新被版本控制忽略的本地配置文件。

**mk subcls**
> 以交互方式为任意 pyrig 类生成子类以便覆盖行为。

# PARAMETERS

**-h**, **--help**
> 显示 pyrig 或子命令的帮助（**pyrig** _command_ **--help**）。

**--shared**
> 配合 **mk cmd** 使用：把存根放入共享子命令中，使其能被同一环境中使用 pyrig-runtime 的所有项目发现。

# CAVEATS

需要 **Python 3.12+**、**Git** 和 **uv**。通常通过 **uv add pyrig --dev** 安装（全局 CLI 可用 **pip install pyrig** / **uv tool** / **pipx**）；发行版软件包可能不提供它。

**pyrig init** 立场鲜明且具有破坏性——会删除 **pyproject.toml** 以外的受管文件（包括 **uv init** 生成的占位文件）。撤销脚手架比移除依赖复杂得多；如需完整的退出路径，请使用 **pyrig rm pyrig** 并查阅上游的缺点文档。

要使用完整的 GitHub CI/CD，远程仓库应从空仓库开始，并且在首次推送前必须配置细粒度的 **REPO_TOKEN**（以及插件所需的密钥）。空项目在尚无测试时可能无法通过健康检查工作流。

# SEE ALSO

[uv](/man/uv)(1), [poetry](/man/poetry)(1), [cookiecutter](/man/cookiecutter)(1), [copier](/man/copier)(1), [git](/man/git)(1), [python](/man/python)(1)

# RESOURCES

```[Source code](https://github.com/Winipedia/pyrig)```

```[Documentation](https://Winipedia.github.io/pyrig)```

<!-- verified: 2026-08-11 -->
