# TAGLINE

生成和更新依赖锁文件

# TLDR

**生成锁文件**

```poetry lock```

**更新锁文件但不安装**

```poetry lock --no-update```

**检查锁文件是否最新**

```poetry lock --check```

# SYNOPSIS

**poetry lock** [_options_]

# PARAMETERS

**--no-update**
> 不更新依赖。

**--check**
> 校验锁文件是否为最新。

# DESCRIPTION

**poetry lock** 解析 **pyproject.toml** 中定义的所有依赖，并将解析出的确切版本写入 **poetry.lock**。该锁文件确保每次安装都使用完全相同的软件包版本，从而实现可复现的构建。

**--no-update** 标志重新生成锁文件的格式而不更新依赖版本。**--check** 标志验证现有锁文件与 pyproject.toml 是否一致，不修改任何内容。注意此命令只更新锁文件；请在其后运行 **poetry install** 来实际安装软件包。

# CAVEATS

不安装软件包。之后请运行 poetry install。

# HISTORY

poetry lock 为可复现环境提供**依赖锁定**功能。

# INSTALL

```dnf: sudo dnf install poetry```

```apk: sudo apk add poetry```

```brew: brew install poetry```

```nix: nix profile install nixpkgs#poetry```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[poetry](/man/poetry)(1), [poetry-install](/man/poetry-install)(1)
