# TAGLINE

遵循 PEP 标准的 Python 软件包管理器

# TLDR

**初始化新项目**

```pdm init```

**添加依赖**

```pdm add [requests]```

**添加开发依赖**

```pdm add -d [pytest]```

**安装所有依赖**

```pdm install```

**更新依赖**

```pdm update```

**在环境中运行命令**

```pdm run [python] [script.py]```

**列出已安装的软件包**

```pdm list```

**构建软件包**

```pdm build```

# SYNOPSIS

**pdm** _command_ [_options_] [_args_...]

# COMMANDS

**init**
> 创建带 pyproject.toml 的新项目。

**add** _packages_
> 添加依赖。

**remove** _packages_
> 移除依赖。

**install**
> 从锁文件安装依赖。

**update** [_packages_]
> 更新依赖。

**lock**
> 生成或更新锁文件。

**sync**
> 将软件包与锁文件同步。

**run** _command_
> 在项目环境中运行命令。

**list**
> 列出已安装的软件包。

**build**
> 构建分发包。

**publish**
> 发布到 PyPI。

**use** _python_
> 切换项目的 Python 解释器。

**venv** create|list|remove|activate
> 管理项目的虚拟环境。

**info**
> 显示项目、环境和 Python 解释器信息。

**cache** clear|list|info
> 查看或清除软件包缓存。

**config** _key_ [_value_]
> 获取或设置 PDM 配置项。

# PARAMETERS

**-d**, **--dev**
> 开发依赖。

**-G**, **--group** _name_
> 依赖组。

**-L**, **--lockfile** _file_
> 自定义锁文件路径。

**--no-sync**
> 添加后不同步。

**--no-lock**
> 跳过锁文件更新。

**--prod**, **--production**
> 排除开发依赖。

**-p**, **--project** _path_
> 项目目录。

**-v**, **--verbose**
> 增加详细输出。

**-q**, **--quiet**
> 抑制输出。

# DESCRIPTION

**pdm** 是一个遵循 PEP 标准的 Python 软件包管理器。它使用 pyproject.toml 来管理依赖、虚拟环境和构建。

**pdm init** 创建带 pyproject.toml 的新项目。它会检测或创建 Python 解释器，并可选择初始化虚拟环境。

依赖在 pyproject.toml 中声明，并锁定到 pdm.lock。**add** 同时修改两者；**install** 读取锁文件。依赖组用于区分开发、测试和可选依赖。

PDM 曾支持以 PEP 582（__pypackages__）作为虚拟环境的替代方案，但 PEP 582 已于 2023 年被否决；现代的 PDM 默认使用 virtualenv。偏好该方式的用户仍可通过 **pdm config python.use_venv false** 启用本地包模式。

**pdm run** 会在项目环境激活的状态下执行命令。pyproject.toml 中 [tool.pdm.scripts] 下定义的脚本提供快捷方式。

构建和发布遵循 PEP 517/518。**pdm build** 创建 wheel 和 sdist；**pdm publish** 上传到 PyPI。

# CAVEATS

PEP 582 支持情况因 Python 版本和工具而异。某些较旧的软件包可能无法兼容新标准。锁文件格式是 PDM 特有的。需要 Python 3.8+。

# HISTORY

PDM 由 **Frost Ming** 创建，首次发布于 **2019 年**。它率先支持 PEP 582 和现代 Python 打包标准。该项目强调遵循标准（PEP 517、518、621）而非自定义格式。凭借对 PEP 标准和性能的专注，PDM 作为 pip、Poetry 和 pipenv 之外的替代方案而广受欢迎。

# INSTALL

```brew: brew install pdm```

```nix: nix profile install nixpkgs#pdm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pip](/man/pip)(1), [poetry](/man/poetry)(1), [pipenv](/man/pipenv)(1), [uv](/man/uv)(1)
