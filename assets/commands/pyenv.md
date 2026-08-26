# TAGLINE

管理多个 Python 版本

# TLDR

**列出可用的 Python 版本**

```pyenv install --list```

**安装 Python 版本**

```pyenv install [3.12.0]```

**列出已安装的版本**

```pyenv versions```

**设置全局 Python 版本**

```pyenv global [3.12.0]```

**设置目录级 Python 版本**（仅对当前目录生效）

```pyenv local [3.11.0]```

**设置 shell 级版本**

```pyenv shell [3.10.0]```

**取消 shell 级版本**

```pyenv shell --unset```

**显示当前生效的版本**

```pyenv version```

**卸载某个版本**

```pyenv uninstall [3.9.0]```

**重建 shims**（在安装了带可执行文件的软件包之后）

```pyenv rehash```

# SYNOPSIS

**pyenv** _command_ [_args_]

# DESCRIPTION

**pyenv** 在单一系统上管理多个 Python 安装。它允许安装不同的 Python 版本，并按项目、按 shell 或全局切换。

pyenv 通过向 PATH 中插入一个 shims 目录来工作。这些 shim 会拦截 Python 命令，并根据配置层级将其重定向到相应的 Python 版本：shell > local > global。

对于需要在多个 Python 版本上测试代码，或参与需要不同 Python 版本项目的开发者来说，这个工具必不可少。

# PARAMETERS

**install** _version_
> 安装 Python 版本。

**uninstall** _version_
> 移除 Python 版本。

**versions**
> 列出已安装的版本。

**version**
> 显示当前生效的版本。

**global** _version_
> 设置默认版本。

**local** _version_
> 为当前目录设置版本。

**shell** _version_
> 为当前 shell 设置版本。

**rehash**
> 重建 shim 可执行文件。

**which** _command_
> 显示命令的完整路径。

**init**
> 配置 shell 以使用 pyenv。

**root**
> 显示 pyenv 安装根目录。

# CONFIGURATION

**~/.pyenv/**
> 根目录，包含已安装的 Python 版本、shims 和 pyenv 插件。

**.python-version**
> 目录级文件，指定该目录使用的 Python 版本，由 `pyenv local` 创建。

**~/.pyenv/version**
> 全局默认 Python 版本文件，由 `pyenv global` 设置。

**PYENV_ROOT**
> 环境变量，用于覆盖默认的 pyenv 安装目录。

# CAVEATS

需要在 profile（~/.bashrc 或 ~/.zshrc）中进行 shell 初始化。安装 Python 版本需要构建依赖。virtualenv 集成需要 pyenv-virtualenv 插件。部分软件包可能需要按版本单独编译。

# HISTORY

**pyenv** 由 **Yuu Yamashita**（yyuu）于 **2012 年**创建，灵感来自 Ruby 的 rbenv。它解决了在开发机上管理多个 Python 版本的常见问题。该项目逐步发展出管理 virtualenv 的插件，并成为 Python 生态中的标准工具。

# INSTALL

```pacman: sudo pacman -S pyenv```

```zypper: sudo zypper install pyenv```

```brew: brew install pyenv```

```nix: nix profile install nixpkgs#pyenv```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[python](/man/python)(1), [pip](/man/pip)(1), [virtualenv](/man/virtualenv)(1), [rbenv](/man/rbenv)(1)
