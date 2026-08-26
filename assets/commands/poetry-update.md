# TAGLINE

更新项目依赖

# TLDR

**更新所有依赖**

```poetry update```

**更新特定软件包**

```poetry update [package1] [package2]```

**预览更新但不安装**

```poetry update --dry-run```

**更新时不包含开发依赖**

```poetry update --without dev```

**只更新 lock 文件，不安装**

```poetry update --lock```

# SYNOPSIS

**poetry** **update** [_packages_...] [_options_]

# PARAMETERS

**--dry-run**
> 预览更新但不安装。

**--no-dev**
> 跳过开发依赖（已弃用，请使用 **--without dev**）。

**--with** _groups_
> 包含可选的依赖分组。

**--without** _groups_
> 排除依赖分组。

**--only** _groups_
> 只更新指定的依赖分组。

**--lock**
> 只更新 lock 文件，不安装软件包。

**--sync**
> 通过移除不在 lock 文件中的软件包来同步环境。

**-v**, **-vv**, **-vvv**
> 提高输出详细程度。

# DESCRIPTION

**poetry update** 会将依赖解析为 pyproject.toml 中约束所允许的最新版本，更新 poetry.lock 文件并安装新版本。如果指定了具体的软件包，则只更新这些软件包及其依赖。不带参数时，会更新所有依赖。

# INSTALL

```dnf: sudo dnf install poetry```

```apk: sudo apk add poetry```

```brew: brew install poetry```

```nix: nix profile install nixpkgs#poetry```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[poetry](/man/poetry)(1), [poetry-install](/man/poetry-install)(1), [poetry-lock](/man/poetry-lock)(1), [poetry-add](/man/poetry-add)(1), [poetry-show](/man/poetry-show)(1)
