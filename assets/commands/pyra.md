# TAGLINE

用 Rust 构建的现代 Python 软件包与项目管理器

# TLDR

**安装指定的 Python** 解释器版本

```pyra python install [3.12]```

**初始化**锁定特定 Python 版本的新项目

```pyra init --python [3.12]```

**向当前项目添加依赖**

```pyra add [requests]```

**从当前项目移除依赖**

```pyra remove [requests]```

**按 lockfile 同步环境**

```pyra sync```

**通过受管环境运行脚本或命令**

```pyra run [script.py]```

**显示依赖树**

```pyra tree```

**更新 Pyra 自身**

```pyra self update```

# SYNOPSIS

**pyra** _command_ [_subcommand_] [_options_] [_args_]

# PARAMETERS

**python install** _version_
> 安装由 Pyra 管理的指定 Python 解释器版本。

**init** [**--python** _version_]
> 初始化新项目，生成 _pyproject.toml_ 和 _pylock.toml_。

**add** _package_ [_package ..._]
> 向 _pyproject.toml_ 添加一个或多个依赖并更新 lockfile。

**remove** _package_ [_package ..._]
> 从 _pyproject.toml_ 移除依赖并更新 lockfile。

**sync**
> 将本地虚拟环境与 _pylock.toml_ 对齐。

**lock**
> 解析依赖并把精确状态写入 _pylock.toml_。

**run** _command_
> 在已同步的环境中执行脚本或命令。

**tree**
> 显示当前项目解析后的依赖树。

**info**
> 显示项目元数据、Python 版本和环境详情。

**cache**
> 查看或管理 Pyra 的磁盘缓存。

**self update**
> 将 Pyra 自身更新到最新版本。

# DESCRIPTION

**pyra** 是一个用 **Rust** 编写的现代 Python 软件包与项目管理器。它把 Python 版本管理、项目初始化、依赖解析、环境同步和脚本执行统一到一条确定性的流水线中。

项目在 _pyproject.toml_ 中声明意图，Pyra 把完全解析后的状态写入 _pylock.toml_。之后运行 **pyra sync** 即可将本地虚拟环境精确对齐到 lockfile，因此同一份 lockfile 在不同机器上总能得到相同的环境。

与 _pip_ 和 _venv_ 等传统工具相比，Pyra 用一个二进制文件取代了 _pyenv_ + _virtualenv_ + _pip_ + _pip-tools_ 的工具链，覆盖完整生命周期——install、add、lock、sync、run——除获取已声明软件包所需的网络调用外，运行时不再有其他网络请求。

# CONFIGURATION

项目配置位于 **pyproject.toml**（声明的意图）。精确的安装状态写入 **pylock.toml**。两个文件都应纳入版本控制。

# CAVEATS

Pyra 仍在积极开发中；命令名和标志在稳定版发布前可能变化。其 lockfile 格式（**pylock.toml**）为 Pyra 专属，尚不能与其他 Python 工具互换。

# HISTORY

**pyra** 为改变碎片化的 Python 工具生态而创建，借鉴了 **uv**、**poetry** 和 **pdm** 等工具的设计理念，专注于通过专用 lockfile 实现确定性的环境复现。

# SEE ALSO

[uv](/man/uv)(1), [pip](/man/pip)(1), [poetry](/man/poetry)(1), [pdm](/man/pdm)(1), [python](/man/python)(1)
