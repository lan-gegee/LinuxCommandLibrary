# TAGLINE

显示项目依赖树

# TLDR

**显示依赖树**

```uv tree```

**显示限制深度的依赖树**

```uv tree --depth [n]```

**显示反向依赖树**

```uv tree --invert```

**显示特定软件包的依赖树**

```uv tree --package [name]```

# SYNOPSIS

**uv** **tree** [_options_]

# PARAMETERS

**--depth** _n_
> 限制树的深度。

**--invert**
> 显示反向依赖。

**--package** _name_
> 显示特定软件包。

**--no-dev**
> 排除开发依赖。

# DESCRIPTION

**uv tree** 显示项目的依赖树。以分层格式展示软件包及其依赖关系。有助于理解和调试依赖关系。

# INSTALL

```dnf: sudo dnf install uv```

```pacman: sudo pacman -S uv```

```apk: sudo apk add uv```

```brew: brew install uv```

```nix: nix profile install nixpkgs#uv```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[uv](/man/uv)(1)
