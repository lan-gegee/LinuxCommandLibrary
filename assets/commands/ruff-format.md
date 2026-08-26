# TAGLINE

使用 Ruff 格式化 Python 代码

# TLDR

**格式化当前目录**

```ruff format```

**格式化特定文件**

```ruff format [file.py]```

**只检查格式而不修改**

```ruff format --check```

**显示差异**

```ruff format --diff```

# SYNOPSIS

**ruff** **format** [_options_] [_files_...]

# PARAMETERS

**--check**
> 检查但不修改。

**--diff**
> 显示格式化差异。

**--config** _file_
> 配置文件。

**--line-length** _n_
> 最大行长度。

# DESCRIPTION

**ruff format** 是 Ruff 的代码格式化子命令，提供用 Rust 编写的、与 Black 兼容的 Python 格式化工具。它通过强制执行一套有明确倾向的规则来统一代码风格，涵盖缩进、行长、字符串引号和空白等约定。

**--check** 标志在不修改文件的情况下校验格式，如果需要做出更改则返回非零退出码，这对 CI 流水线很有用。**--diff** 标志会显示将要应用的具体更改。诸如 **--line-length** 之类的配置选项可以在每个项目的 pyproject.toml 或 ruff.toml 中设置。

# INSTALL

```dnf: sudo dnf install ruff```

```pacman: sudo pacman -S ruff```

```apk: sudo apk add ruff```

```brew: brew install ruff```

```nix: nix profile install nixpkgs#ruff```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ruff](/man/ruff)(1), [ruff-check](/man/ruff-check)(1), [black](/man/black)(1)
