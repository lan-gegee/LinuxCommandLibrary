# TAGLINE

对 Python 代码运行 Ruff linter

# TLDR

**检查当前目录**

```ruff check```

**检查特定文件**

```ruff check [file.py]```

**检查并修复**

```ruff check --fix```

**使用指定规则检查**

```ruff check --select [E,F]```

**监视文件变化**

```ruff check --watch```

# SYNOPSIS

**ruff** **check** [_options_] [_files_...]

# PARAMETERS

**--fix**
> 自动修复违规项。

**--select** _rules_
> 启用特定规则。

**--ignore** _rules_
> 忽略特定规则。

**--watch**
> 监视文件变化。

**--config** _file_
> 配置文件。

**--output-format** _format_
> 输出格式（text、json、github）。

# DESCRIPTION

**ruff check** 是 Ruff 的 lint 子命令，Ruff 是一个用 Rust 编写、速度极快的 Python linter。它分析 Python 源文件中的风格违规、潜在缺陷和代码质量问题，在单一统一接口中实现了来自 Flake8、isort、pyupgrade 以及众多其他成熟 Python 工具的规则集。

**--fix** 标志会自动就地修复可修复的违规项，而 **--select** 和 **--ignore** 则控制哪些规则类别生效。监视模式会在每次保存文件时重新检查，在开发过程中提供实时反馈。输出格式包括纯文本、JSON 以及用于 CI 集成的 GitHub Actions 注解。

# INSTALL

```dnf: sudo dnf install ruff```

```pacman: sudo pacman -S ruff```

```apk: sudo apk add ruff```

```brew: brew install ruff```

```nix: nix profile install nixpkgs#ruff```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ruff](/man/ruff)(1), [ruff-format](/man/ruff-format)(1), [flake8](/man/flake8)(1)
