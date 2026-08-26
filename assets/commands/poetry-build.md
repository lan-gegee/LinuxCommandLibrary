# TAGLINE

构建 Python 发行包

# TLDR

**构建软件包**

```poetry build```

**仅构建 wheel**

```poetry build -f wheel```

**仅构建 sdist**

```poetry build -f sdist```

# SYNOPSIS

**poetry build** [_options_]

# PARAMETERS

**-f**, **--format** _FORMAT_
> 构建格式（wheel、sdist）。

# DESCRIPTION

**poetry build** 从当前项目创建可分发的 Python 软件包。默认情况下，它会在 **dist/** 目录中同时生成 wheel（.whl）和源代码发行版（sdist/tar 包）。

使用 **-f wheel** 仅构建 wheel 格式，或用 **-f sdist** 仅构建源代码发行版。构建过程使用来自 **pyproject.toml** 的项目元数据，包括名称、版本、依赖和入口点。

# CAVEATS

输出到 dist/ 目录。需要有效的 pyproject.toml。

# HISTORY

poetry build 提供 **Python 软件包**构建功能。

# INSTALL

```dnf: sudo dnf install poetry```

```apk: sudo apk add poetry```

```brew: brew install poetry```

```nix: nix profile install nixpkgs#poetry```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[poetry](/man/poetry)(1), [poetry-publish](/man/poetry-publish)(1)
