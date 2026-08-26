# TAGLINE

Go 版本管理器

# TLDR

**列出可用的 Go 版本**

```goenv install -l```

**安装一个 Go 版本**

```goenv install [1.21.0]```

**安装最新稳定版本**

```goenv install latest```

**列出已安装的版本**

```goenv versions```

**设置全局 Go 版本**

```goenv global [1.21.0]```

**为目录设置局部版本**

```goenv local [1.21.0]```

**显示当前版本**

```goenv version```

**卸载某个版本**

```goenv uninstall [1.21.0]```

# SYNOPSIS

**goenv** _command_ [_args_]

# SUBCOMMANDS

**install** _version_
> 安装一个 Go 版本。

**uninstall** _version_
> 卸载一个 Go 版本。

**versions**
> 列出已安装的版本。

**version**
> 显示当前激活的版本。

**global** _version_
> 设置全局默认版本。

**local** _version_
> 设置目录级版本（会写入 `.go-version` 文件）。

**shell** _version_
> 通过 `GOENV_VERSION` 变量设置 shell 级版本。

**which** _command_
> 显示 goenv 将调用的可执行文件的完整路径。

**rehash**
> 重建 shim 可执行文件。

**init**
> 配置 shell 环境。

# PARAMETERS

**-l**, **--list**
> 列出可安装的版本。

# DESCRIPTION

**goenv** 是一个受 rbenv 和 pyenv 启发的 Go 版本管理器。它可以并行安装多个 Go 版本，并按项目或全局切换使用。

版本选择通过 **.go-version** 文件和 shim 来管理：shim 会拦截 Go 命令，并将其路由到相应的版本。

# CONFIGURATION

**~/.goenv/version**
> 全局 Go 版本设置。

**.go-version**
> 目录级的 Go 版本覆盖文件。

**GOENV_ROOT**
> 指定 goenv 安装目录的环境变量（默认 ~/.goenv）。

# INSTALL

```brew: brew install goenv```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[go](/man/go)(1), [pyenv](/man/pyenv)(1), [rbenv](/man/rbenv)(1)
