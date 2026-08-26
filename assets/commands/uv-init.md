# TAGLINE

用 uv 初始化新的 Python 项目

# TLDR

**初始化新项目**

```uv init```

**以指定名称初始化**

```uv init [project_name]```

**初始化库项目**

```uv init --lib```

**在目录中初始化**

```uv init [path]```

# SYNOPSIS

**uv** **init** [_options_] [_path_]

# PARAMETERS

**--name** _name_
> 项目名称。

**--lib**
> 创建库结构。

**--app**
> 创建应用程序结构。

**--no-workspace**
> 不添加到工作区。

**--python** _version_
> Python 版本要求。

# DESCRIPTION

**uv init** 用于初始化新的 Python 项目。它会创建包含项目元数据的 pyproject.toml，并为应用程序或库搭建项目结构。

# INSTALL

```dnf: sudo dnf install uv```

```pacman: sudo pacman -S uv```

```apk: sudo apk add uv```

```brew: brew install uv```

```nix: nix profile install nixpkgs#uv```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[uv](/man/uv)(1), [uv-add](/man/uv-add)(1), [uv-sync](/man/uv-sync)(1)
