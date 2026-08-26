# TAGLINE

创建 Python 虚拟环境

# TLDR

**创建虚拟环境**

```uv venv```

**使用指定的 Python 创建**

```uv venv --python [3.11]```

**在指定目录中创建**

```uv venv [path]```

**创建时安装种子软件包**

```uv venv --seed```

# SYNOPSIS

**uv** **venv** [_options_] [_path_]

# PARAMETERS

**--python** _version_
> Python 版本。

**--seed**
> 安装 pip 和 setuptools。

**--system-site-packages**
> 访问系统软件包。

**--prompt** _name_
> 自定义提示符。

# DESCRIPTION

**uv venv** 用于创建 Python 虚拟环境。为软件包安装创建隔离的环境。比 python -m venv 或 virtualenv 快得多。

# INSTALL

```dnf: sudo dnf install uv```

```pacman: sudo pacman -S uv```

```apk: sudo apk add uv```

```brew: brew install uv```

```nix: nix profile install nixpkgs#uv```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[uv](/man/uv)(1), [virtualenv](/man/virtualenv)(1)
