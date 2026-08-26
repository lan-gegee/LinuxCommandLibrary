# TAGLINE

从 Poetry 项目移除依赖

# TLDR

**移除依赖**

```poetry remove [package]```

**移除开发依赖**

```poetry remove --group dev [package]```

**移除多个软件包**

```poetry remove [package1] [package2]```

**试运行**

```poetry remove --dry-run [package]```

# SYNOPSIS

**poetry remove** [_options_] _packages_

# PARAMETERS

_PACKAGES_
> 要移除的软件包。

**-G**, **--group** _GROUP_
> 从特定组中移除。

**-D**, **--dev**
> 从开发依赖中移除（已弃用，请改用 **-G dev**）。

**--dry-run**
> 模拟移除而不做更改。

**--lock**
> 仅更新锁文件，不卸载软件包。

# DESCRIPTION

**poetry remove** 从项目中移除一个或多个依赖，同时更新 **pyproject.toml** 和锁文件。它还会从虚拟环境中卸载这些软件包以及任何孤立的传递依赖。

使用 **-G** 从特定依赖组（如 dev、test）中移除。**--dry-run** 标志显示将要移除的内容而不做更改。

# CAVEATS

会更新锁文件。可能连带移除依赖它的软件包。

# HISTORY

poetry remove 为 Poetry 项目提供**依赖移除**功能。

# INSTALL

```dnf: sudo dnf install poetry```

```apk: sudo apk add poetry```

```brew: brew install poetry```

```nix: nix profile install nixpkgs#poetry```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[poetry](/man/poetry)(1), [poetry-add](/man/poetry-add)(1)
