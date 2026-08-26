# TAGLINE

从 uv 项目中移除依赖

# TLDR

**移除依赖**

```uv remove [package]```

**移除开发依赖**

```uv remove --dev [package]```

**从可选组中移除**

```uv remove --optional [group] [package]```

# SYNOPSIS

**uv** **remove** [_options_] _packages_...

# PARAMETERS

**--dev**
> 从 **[tool.uv.dev-dependencies]** 组中移除该软件包。

**--optional** _GROUP_
> 从 **pyproject.toml** 中指定的可选依赖组中移除。

**--group** _GROUP_
> 从指定的 PEP 735 依赖组中移除。

**--script** _SCRIPT.PY_
> 操作单个 PEP 723 脚本文件的依赖块，而不是项目。

**--package** _PACKAGE_
> 在工作区中，以名为 _PACKAGE_ 的软件包成员为目标。

**--frozen**
> 更新 **pyproject.toml** 但保持 **uv.lock** 不变。

**--locked**
> 若 **uv.lock** 需要更改则失败（CI 保护）。

**--no-sync**
> 更改后跳过同步项目的虚拟环境。

# DESCRIPTION

**uv remove** 从 Python 项目中移除依赖。它会更新 pyproject.toml 和 uv.lock，并自动同步虚拟环境。

# INSTALL

```dnf: sudo dnf install uv```

```pacman: sudo pacman -S uv```

```apk: sudo apk add uv```

```brew: brew install uv```

```nix: nix profile install nixpkgs#uv```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[uv](/man/uv)(1), [uv-add](/man/uv-add)(1), [uv-sync](/man/uv-sync)(1)
