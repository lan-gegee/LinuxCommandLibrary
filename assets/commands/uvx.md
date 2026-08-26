# TAGLINE

在临时环境中运行 Python 工具

# TLDR

**运行 Python 工具**

```uvx [ruff] [check] [.]```

**运行指定版本**

```uvx [package]@[version] [args]```

**附带可选依赖运行**

```uvx --with [extra] [package]```

**从 git 运行**

```uvx [git+https://github.com/repo/tool]```

# SYNOPSIS

**uvx** [_--with extras_] _package_[@_version_] [_args_]

# PARAMETERS

_package_
> 要运行的软件包。

**--with** _EXTRA_
> 包含指定的可选依赖。

**--from** _SOURCE_
> 安装来源。

**--python** _VER_
> Python 版本。

# DESCRIPTION

**uvx** 是 **uv tool run** 的简写形式，它在临时的隔离环境中执行 Python 命令行工具，而无需永久安装。它类似于 **pipx run**，但借助 uv 基于 Rust 的解析器，执行速度大幅提升。

每次调用都会创建一个临时的虚拟环境，安装所请求的工具及其依赖，运行命令，然后丢弃该环境。这确保了工具之间以及与项目依赖之间不会发生冲突。可以使用 **@version** 语法固定特定版本。

uvx 是 uv Python 软件包管理器生态的一部分，适合运行 linter、格式化工具、代码生成器等一次性工具，而不会因永久安装弄乱系统。

# CAVEATS

需要 uv。属于 Python 生态。可能会下载软件包。

# HISTORY

**uvx** 是快速 Python 软件包管理器 **uv** 的一部分，提供类似 pipx 的临时工具执行方式。

# INSTALL

```dnf: sudo dnf install uv```

```pacman: sudo pacman -S uv```

```apk: sudo apk add uv```

```brew: brew install uv```

```nix: nix profile install nixpkgs#uv```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[uv](/man/uv)(1), [pipx](/man/pipx)(1), [python](/man/python)(1)
