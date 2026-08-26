# TAGLINE

管理开发工具版本

# TLDR

**安装工具**

```mise install [node@20]```

**使用工具版本**

```mise use [node@20]```

**列出已安装版本**

```mise list```

**设置全局版本**

```mise use -g [python@3.11]```

**以指定工具运行**

```mise exec [node@18] -- node [script.js]```

**激活 Shell**

```eval "$(mise activate bash)"```

# SYNOPSIS

**mise** _command_ [_options_]

# PARAMETERS

_COMMAND_
> Mise 操作。

**install** _TOOL_
> 安装工具版本。

**use** _TOOL_
> 设置工具版本。

**list**
> 列出已安装版本。

**exec**
> 以指定版本运行。

**activate**
> Shell 激活。

**--help**
> 显示帮助信息。

# DESCRIPTION

**mise** 管理开发工具版本。它是一个多语言运行时管理器（rtx 的继任者）。

该工具管理 Node.js、Python、Ruby 等。兼容 asdf 插件。

# CAVEATS

需要激活 Shell。rtx 的继任者。兼容 asdf。

# HISTORY

mise（原名 rtx）作为 asdf 的快速 **Rust 编写**替代品而创建，用于管理工具版本。

# INSTALL

```pacman: sudo pacman -S mise```

```apk: sudo apk add mise```

```brew: brew install mise```

```nix: nix profile install nixpkgs#mise```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[asdf](/man/asdf)(1), [nvm](/man/nvm)(1), [pyenv](/man/pyenv)(1)
