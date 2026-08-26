# TAGLINE

管理软件仓库源

# TLDR

**添加软件包源**

```poetry source add [name] [url]```

**移除软件包源**

```poetry source remove [name]```

**显示已配置的源**

```poetry source show```

**添加私有仓库**

```poetry source add --priority=supplemental [name] [url]```

# SYNOPSIS

**poetry source** _command_ [_options_]

# PARAMETERS

**add** _NAME_ _URL_
> 添加软件包源。

**remove** _NAME_
> 移除源。

**show**
> 列出源。

**--priority** _LEVEL_
> 源的优先级（primary、supplemental、explicit）。

# DESCRIPTION

**poetry source** 用于管理 **pyproject.toml** 中的软件仓库源。它允许在默认的 PyPI 之外添加私有或替代的软件包索引，或取代 PyPI。

**--priority** 选项控制源的使用方式：**primary** 源会被优先查询，**supplemental** 源只在 primary 源中找不到某个软件包时才会查询，而 **explicit** 源仅在软件包明确引用它们时才使用。使用 **show** 可列出已配置的源。

# CAVEATS

会修改 pyproject.toml。优先级会影响解析顺序。

# HISTORY

poetry source 为软件包源提供**软件仓库管理**功能。

# INSTALL

```dnf: sudo dnf install poetry```

```apk: sudo apk add poetry```

```brew: brew install poetry```

```nix: nix profile install nixpkgs#poetry```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[poetry](/man/poetry)(1), [poetry-config](/man/poetry-config)(1)
