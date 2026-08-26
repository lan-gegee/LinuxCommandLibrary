# TAGLINE

管理 Python 版本安装

# TLDR

**列出可用的 Python 版本**

```uv python list```

**安装 Python 版本**

```uv python install [version]```

**卸载 Python 版本**

```uv python uninstall [version]```

**查找 Python 可执行文件**

```uv python find [version]```

**固定 Python 版本**

```uv python pin [version]```

# SYNOPSIS

**uv** **python** _command_ [_options_]

# PARAMETERS

**list**
> 显示可用的版本。

**install** _version_
> 安装 Python 版本。

**uninstall** _version_
> 移除 Python 版本。

**find** _version_
> 查找 Python 可执行文件。

**pin** _version_
> 设置项目的 Python 版本。

**dir**
> 显示 Python 安装目录。

# DESCRIPTION

**uv python** 管理 Python 安装。可以下载、安装并在不同 Python 版本之间切换。无需系统 Python 即可提供封闭式（hermetic）的 Python 管理。

# INSTALL

```dnf: sudo dnf install uv```

```pacman: sudo pacman -S uv```

```apk: sudo apk add uv```

```brew: brew install uv```

```nix: nix profile install nixpkgs#uv```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[uv](/man/uv)(1), [pyenv](/man/pyenv)(1)
