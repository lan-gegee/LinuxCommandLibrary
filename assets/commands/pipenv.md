# TAGLINE

结合虚拟环境的 Python 依赖管理工具

# TLDR

**创建虚拟环境并安装软件包**

```pipenv install [requests]```

**安装开发依赖**

```pipenv install --dev [pytest]```

**从 Pipfile 安装**

```pipenv install```

**激活虚拟环境**

```pipenv shell```

**在虚拟环境中运行命令**

```pipenv run [python script.py]```

**生成 requirements.txt**

```pipenv requirements > requirements.txt```

**显示依赖图**

```pipenv graph```

**移除虚拟环境**

```pipenv --rm```

# SYNOPSIS

**pipenv** _command_ [_options_] [_packages_]

# PARAMETERS

**install** [_packages_]
> 安装软件包并添加到 Pipfile。

**uninstall** _packages_
> 从环境中移除软件包。

**lock**
> 生成 Pipfile.lock。

**sync**
> 从 Pipfile.lock 安装软件包。

**shell**
> 在虚拟环境中启动 Shell。

**run** _command_
> 在虚拟环境中运行命令。

**graph**
> 显示依赖图。

**check**
> 检查安全漏洞。

**requirements**
> 生成 requirements.txt 输出。

**update** [_packages_]
> 更新软件包。

**clean**
> 移除不在 Pipfile.lock 中的软件包。

**--dev**, **-d**
> 包含开发依赖。

**--python** _VERSION_
> 指定 Python 版本。

**--venv**
> 显示虚拟环境路径。

**--rm**
> 移除虚拟环境。

**--where**
> 显示项目主目录。

**--three** / **--two**
> 使用 Python 3 / Python 2。

**--site-packages**
> 启用系统 site-packages。

# DESCRIPTION

**pipenv** 将 pip 和 virtualenv 组合为单一工作流。它通过 Pipfile/Pipfile.lock 文件管理项目依赖，类似于 npm 的 package.json 或 Ruby 的 Bundler。

Pipfile 以更结构化的格式取代了 requirements.txt，并将生产依赖与开发依赖分开。Pipfile.lock 通过锁定确切的版本和哈希来确保构建的确定性。

虚拟环境会按项目自动创建。shell 命令用于激活环境，而 run 则无需手动激活即可在其中执行命令。环境的位置由项目目录决定。

安全特性包括软件包哈希校验以及通过 check 命令进行漏洞扫描。graph 命令可视化依赖树，帮助理解传递依赖。

Pipenv 集成了 .env 文件支持，会自动加载环境变量。这使机密信息与代码分离，同时在开发期间保持可用。

# CONFIGURATION

**Pipfile**
> 位于项目根目录的项目依赖规范文件。

**Pipfile.lock**
> 包含锁定版本和哈希的锁文件，用于可复现安装。

**.env**
> 由 pipenv 自动加载的环境变量文件。

**PIPENV_VENV_IN_PROJECT**
> 设置后在项目目录内创建虚拟环境。

**PIPENV_NO_INHERIT**
> 不继承父 Shell 的环境变量。

**PIPENV_CACHE_DIR**
> 覆盖默认的 pip 缓存目录位置。

# CAVEATS

对于复杂的依赖，锁解析可能较慢。不如 Poetry 或 uv 等较新工具快。哈希校验要求软件包已发布哈希值。依赖解析存在一些边缘情况。可能与系统级 pip 软件包冲突。

# HISTORY

**pipenv** 由 **Kenneth Reitz**（requests 的作者）于 **2017 年**前后创建，旨在将 npm/Bundler 的开发者体验带给 Python。它获得了 PyPA 的认可并被列为推荐工具。虽然 Poetry 等更新的替代品已经出现，pipenv 凭借其简洁性以及与 pip 的集成仍被广泛使用。

# INSTALL

```brew: brew install pipenv```

```nix: nix profile install nixpkgs#pipenv```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pip](/man/pip)(1), [poetry](/man/poetry)(1), [virtualenv](/man/virtualenv)(1), [uv](/man/uv)(1)
