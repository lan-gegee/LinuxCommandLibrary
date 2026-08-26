# TAGLINE

管理 Poetry 的软件包下载缓存

# TLDR

**显示缓存目录路径**

```poetry cache list```

**清除特定软件包的缓存**

```poetry cache clear [cache_name] --all```

**清除 PyPI 缓存**

```poetry cache clear pypi --all```

# SYNOPSIS

**poetry** **cache** _command_ [_options_]

# PARAMETERS

**list**
> 显示每个仓库缓存的软件包。

**clear** _cache_
> 清除特定的缓存。

**--all**
> 清除缓存中的所有条目。

# DESCRIPTION

**poetry cache** 管理 Poetry 的软件包缓存。Poetry 会缓存下载的软件包以加快后续安装。用它来查看缓存内容或清理空间。

# INSTALL

```dnf: sudo dnf install poetry```

```apk: sudo apk add poetry```

```brew: brew install poetry```

```nix: nix profile install nixpkgs#poetry```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[poetry](/man/poetry)(1), [poetry-install](/man/poetry-install)(1)
