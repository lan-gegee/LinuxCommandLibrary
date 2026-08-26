# TAGLINE

向 uv Python 项目添加依赖

# TLDR

**添加依赖**

```uv add [package]```

**带版本约束添加**

```uv add [package]>=[version]```

**添加开发依赖**

```uv add --dev [package]```

**添加可选依赖**

```uv add --optional [group] [package]```

# SYNOPSIS

**uv** **add** [_options_] _packages_...

# PARAMETERS

**--dev**
> 添加为开发依赖。

**--optional** _group_
> 添加到可选组。

**--frozen**
> 不更新锁文件。

**--no-sync**
> 不同步环境。

# DESCRIPTION

**uv add** 向 Python 项目添加依赖。它会更新 pyproject.toml 和 uv.lock，并自动将新的依赖同步到虚拟环境中。属于 uv——一个速度极快的 Python 软件包管理器。

# INSTALL

```dnf: sudo dnf install uv```

```pacman: sudo pacman -S uv```

```apk: sudo apk add uv```

```brew: brew install uv```

```nix: nix profile install nixpkgs#uv```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[uv](/man/uv)(1), [uv-remove](/man/uv-remove)(1), [uv-sync](/man/uv-sync)(1)
