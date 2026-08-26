# TAGLINE

在 PyPI 上搜索软件包

# TLDR

**搜索软件包**

```poetry search [query]```

**用特定关键词搜索**

```poetry search requests```

# SYNOPSIS

**poetry** **search** _query_

# DESCRIPTION

**poetry search** 在 PyPI 上搜索软件包。返回匹配的软件包名称和描述。注意：由于 PyPI XML-RPC API 的限制，该命令在 Poetry 1.6.0 中已被弃用。建议直接在 pypi.org 上搜索。

# CAVEATS

该命令已在 Poetry 1.6.0 中弃用，在新版本中可能无法使用。请直接在 pypi.org 上搜索软件包。

# INSTALL

```dnf: sudo dnf install poetry```

```apk: sudo apk add poetry```

```brew: brew install poetry```

```nix: nix profile install nixpkgs#poetry```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[poetry](/man/poetry)(1), [poetry-add](/man/poetry-add)(1)
