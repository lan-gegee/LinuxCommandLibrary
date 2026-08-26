# TAGLINE

将环境与 lock 文件同步

# TLDR

**根据 lock 文件同步依赖**

```poetry sync```

**同步时不包含开发依赖**

```poetry sync --no-dev```

**同步特定分组**

```poetry sync --with [group]```

**试运行**

```poetry sync --dry-run```

# SYNOPSIS

**poetry sync** [_options_]

# PARAMETERS

**--no-dev**
> 排除开发依赖。

**--with** _GROUPS_
> 包含特定分组。

**--without** _GROUPS_
> 排除特定分组。

**--dry-run**
> 模拟同步过程。

# DESCRIPTION

**poetry sync** 会严格地将虚拟环境同步到与 **poetry.lock** 文件完全一致的状态。与 **poetry install** 不同，它还会移除环境中存在但未列入 lock 文件的软件包。

这适用于在 CI/CD 流水线或生产部署中确保环境干净且可复现。可在实际应用之前使用 **--dry-run** 预览变更。

# CAVEATS

会移除未被锁定的软件包。比 install 更严格。

# HISTORY

poetry sync 提供与 lock 文件的**严格同步**功能。

# INSTALL

```dnf: sudo dnf install poetry```

```apk: sudo apk add poetry```

```brew: brew install poetry```

```nix: nix profile install nixpkgs#poetry```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[poetry](/man/poetry)(1), [poetry-install](/man/poetry-install)(1), [poetry-lock](/man/poetry-lock)(1)
