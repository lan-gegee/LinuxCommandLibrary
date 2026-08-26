# TAGLINE

校验 pyproject.toml 配置

# TLDR

**检查 pyproject.toml 的有效性**

```poetry check```

**同时校验锁文件**

```poetry check --lock```

# SYNOPSIS

**poetry check** [_options_]

# PARAMETERS

**--lock**
> 同时校验 poetry.lock 文件。

# DESCRIPTION

**poetry check** 校验 **pyproject.toml** 文件的结构和内容，确保必需字段存在且格式正确。它能在配置错误于安装或构建操作中引发问题之前将其捕获。

**--lock** 选项还会验证 **poetry.lock** 文件与 pyproject.toml 是否一致并保持最新。这在 CI 流水线中很有用，可确保锁文件未发生漂移。

# CAVEATS

仅检查语法和结构。不验证依赖是否存在。

# HISTORY

poetry check 为 Poetry 项目提供**配置校验**功能。

# INSTALL

```dnf: sudo dnf install poetry```

```apk: sudo apk add poetry```

```brew: brew install poetry```

```nix: nix profile install nixpkgs#poetry```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[poetry](/man/poetry)(1), [poetry-lock](/man/poetry-lock)(1)
