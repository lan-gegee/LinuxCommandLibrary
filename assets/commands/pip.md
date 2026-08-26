# TAGLINE

Python 软件包安装器和管理器

# TLDR

**安装软件包**

```pip install [package]```

**安装特定版本**

```pip install [package]==[1.0.0]```

**从 requirements 文件安装软件包**

```pip install -r [requirements.txt]```

**升级软件包**

```pip install --upgrade [package]```

**卸载软件包**

```pip uninstall [package]```

**列出已安装的软件包**

```pip list```

**显示软件包信息**

```pip show [package]```

**生成 requirements 文件**

```pip freeze > [requirements.txt]```

**仅为当前用户安装**

```pip install --user [package]```

# SYNOPSIS

**pip** _command_ [_options_] [_package_...]

**pip** install [_options_] _package_

**python -m pip** _command_ [_options_]

# COMMANDS

**install**
> 安装软件包

**uninstall**
> 移除软件包

**list**
> 列出已安装的软件包

**show**
> 显示软件包信息

**freeze**
> 以 requirements 格式输出已安装的软件包

**search**
> 在 PyPI 中搜索软件包（自 pip 23.1 起已移除）

**index**
> 查看索引上可用的软件包版本

**download**
> 下载软件包而不安装

**wheel**
> 构建 wheel 软件包

**check**
> 验证已安装的软件包是否具有兼容的依赖

**config**
> 管理配置

**cache**
> 管理 pip 的缓存

# PARAMETERS

**-U**, **--upgrade**
> 将软件包升级到最新版本

**--user**
> 安装到用户目录（~/.local）

**-r**, **--requirement** _FILE_
> 从 requirements 文件安装

**--no-deps**
> 不安装依赖

**-c**, **--constraint** _FILE_
> 使用给定的约束文件限制软件包版本

**--force-reinstall**
> 即使已是最新版本也重新安装

**-I**, **--ignore-installed**
> 忽略已安装的软件包

**--pre**
> 包含预发布版本

**-i**, **--index-url** _URL_
> 软件包索引的基础 URL

**--extra-index-url** _URL_
> 额外的软件包索引 URL

**-e**, **--editable** _PATH_
> 以可编辑/开发模式安装

**--target** _DIR_
> 安装到指定目录

**-y**, **--yes**
> 不请求确认

**-q**, **--quiet**
> 最少输出

**-v**, **--verbose**
> 详细输出

**-V**, **--version**
> 显示版本

**-h**, **--help**
> 显示帮助

# DESCRIPTION

**pip** 是 Python 的软件包安装器，用于从 Python Package Index（PyPI）和其他仓库安装和管理软件包。它负责 Python 软件包的依赖解析、下载和安装。

软件包可以全局安装（需要 root）、通过 **--user** 按用户安装，或在虚拟环境中安装（推荐）。版本说明符允许精确控制：**==** 表示精确匹配，**>=** 表示最低版本，**~=** 表示兼容版本。

由 **pip freeze** 生成的 **requirements.txt** 格式记录确切版本，以实现可复现的安装。现代 Python 建议使用 **python -m pip** 而非裸的 **pip** 命令，以确保使用正确的 Python 解释器。

# CONFIGURATION

**~/.config/pip/pip.conf**（Linux）、**~/Library/Application Support/pip/pip.conf**（macOS）、**%APPDATA%\pip\pip.ini**（Windows）
> 用户级配置文件，用于设置默认选项。

**/etc/pip.conf**（Linux/macOS）、**C:\ProgramData\pip\pip.ini**（Windows）
> 全局系统级配置文件。

**$VIRTUAL_ENV/pip.conf**
> 虚拟环境内的 site 级配置文件。

**PIP_INDEX_URL**
> 用于设置默认软件包索引 URL 的环境变量。

**PIP_EXTRA_INDEX_URL**
> 用于设置额外软件包索引 URL 的环境变量。

**PIP_CONFIG_FILE**
> 用于覆盖配置文件位置的环境变量。

**PIP_NO_CACHE_DIR**
> 用于禁用 pip 缓存的环境变量。

# CAVEATS

在 Linux 系统上，避免使用 sudo 运行 pip 全局安装软件包，因为这可能与系统软件包冲突。请改用虚拟环境或 **--user**。某些发行版为 Python 3 将 pip 重命名为 **pip3**。由于滥用行为，search 命令已在 PyPI 上被禁用。软件包安装可能需要编译工具和构建依赖。

# HISTORY

pip 由 **Ian Bicking** 创建，于 **2008 年**首次发布，作为 easy_install 的替代品。其名称是一个递归缩写："**p**ip **i**nstalls **p**ackages"。它成为标准的 Python 软件包管理器，自 Python 3.4 起默认内置。现在 pip 由 Python Packaging Authority（PyPA）维护，在依赖解析、安全性和性能方面持续改进。

# INSTALL

```apk: sudo apk add py3-pip```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[python](/man/python)(1), [pip-freeze](/man/pip-freeze)(1), [virtualenv](/man/virtualenv)(1), [pipx](/man/pipx)(1), [uv](/man/uv)(1), [pipenv](/man/pipenv)(1), [conda](/man/conda)(1)
