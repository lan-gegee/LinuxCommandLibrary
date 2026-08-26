# TAGLINE

创建新的 Python 项目结构

# TLDR

**创建新项目**

```poetry new [project-name]```

**以指定的源码目录创建**

```poetry new --src [project-name]```

**以自定义名称创建**

```poetry new --name [package-name] [directory]```

# SYNOPSIS

**poetry new** [_options_] _path_

# PARAMETERS

_PATH_
> 项目目录路径。

**--name** _NAME_
> 软件包名称。

**--src**
> 使用 src 布局。

**--readme** _FORMAT_
> Readme 格式（md、rst）。

# DESCRIPTION

**poetry new** 搭建一个具有标准结构的新 Python 项目目录，包括 **pyproject.toml**、软件包目录和 tests 目录。这提供了一个开箱即用的项目布局。

**--src** 标志使用 `src/` 布局模式，软件包位于 `src/` 子目录之下。**--name** 选项允许软件包名与目录名不同。若要向已有项目添加 Poetry，请改用 **poetry init**。

# CAVEATS

会创建新目录。已有项目请使用 poetry init。

# HISTORY

poetry new 为新的 Python 软件包提供**项目脚手架**功能。

# INSTALL

```dnf: sudo dnf install poetry```

```apk: sudo apk add poetry```

```brew: brew install poetry```

```nix: nix profile install nixpkgs#poetry```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[poetry](/man/poetry)(1), [poetry-init](/man/poetry-init)(1)
