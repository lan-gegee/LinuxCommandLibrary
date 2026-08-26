# TAGLINE

同步项目虚拟环境

# TLDR

**同步环境**

```uv sync```

**同步时不包含开发依赖**

```uv sync --no-dev```

**同步指定的可选组**

```uv sync --extra [name]```

**从冻结的锁文件同步**

```uv sync --frozen```

# SYNOPSIS

**uv** **sync** [_options_]

# PARAMETERS

**--frozen**
> 若锁文件需要更新则报错。

**--locked**
> 断言锁文件是最新的。

**--no-dev**
> 跳过开发依赖。

**--extra** _name_
> 包含指定的可选组。

**--all-extras**
> 包含所有可选组。

# DESCRIPTION

**uv sync** 将虚拟环境与项目依赖同步。按需创建 venv，并安装/移除软件包以匹配锁文件。是环境管理的核心命令。

# INSTALL

```dnf: sudo dnf install uv```

```pacman: sudo pacman -S uv```

```apk: sudo apk add uv```

```brew: brew install uv```

```nix: nix profile install nixpkgs#uv```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[uv](/man/uv)(1), [uv-lock](/man/uv-lock)(1), [uv-add](/man/uv-add)(1)
