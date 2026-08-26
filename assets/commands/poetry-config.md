# TAGLINE

管理 Poetry 配置设置

# TLDR

**列出配置**

```poetry config --list```

**设置配置**

```poetry config [key] [value]```

**设置仓库 URL**

```poetry config repositories.[name] [https://repo.example.com]```

**设置 PyPI 令牌**

```poetry config pypi-token.pypi [token]```

**取消配置**

```poetry config --unset [key]```

# SYNOPSIS

**poetry config** [_options_] [_key_] [_value_]

# PARAMETERS

_KEY_
> 配置键。

_VALUE_
> 配置值。

**--list**
> 显示所有配置。

**--unset**
> 移除配置。

**--local**
> 项目专属配置。

# DESCRIPTION

**poetry config** 读写 Poetry 的配置设置，包括虚拟环境偏好、仓库 URL 和身份验证令牌。使用 **--list** 查看当前所有设置。

默认情况下，设置全局存储。**--local** 标志会在项目目录中创建 **poetry.toml** 文件，用于项目专属覆盖。常见设置包括 `virtualenvs.in-project`、`repositories` 和 `pypi-token`。使用 **--unset** 移除某个配置键。

# CAVEATS

令牌存储在配置中。项目级设置请使用 --local。

# HISTORY

poetry config 为 Poetry 设置提供**配置管理**功能。

# INSTALL

```dnf: sudo dnf install poetry```

```apk: sudo apk add poetry```

```brew: brew install poetry```

```nix: nix profile install nixpkgs#poetry```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[poetry](/man/poetry)(1), [poetry-publish](/man/poetry-publish)(1)
