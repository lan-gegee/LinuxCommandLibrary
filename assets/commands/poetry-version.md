# TAGLINE

管理项目版本号

# TLDR

**显示当前版本**

```poetry version```

**递增主版本号**

```poetry version major```

**递增次版本号**

```poetry version minor```

**递增修订号**

```poetry version patch```

**设置为特定版本**

```poetry version [1.2.3]```

# SYNOPSIS

**poetry version** [_options_] [_version_]

# PARAMETERS

_VERSION_
> 版本号或递增规则。

**major**
> 递增主版本号。

**minor**
> 递增次版本号。

**patch**
> 递增修订号。

**--short**
> 只输出版本号。

**--dry-run**
> 不修改文件。

# DESCRIPTION

**poetry version** 用于显示或更新 **pyproject.toml** 中的项目版本。不带参数时显示当前版本。给定递增规则（**major**、**minor**、**patch**、**premajor**、**preminor**、**prepatch**、**prerelease**）或明确的版本号字符串时，会相应地更新版本。

**--short** 标志只输出版本号而不带项目名称。使用 **--dry-run** 可在不修改文件的情况下预览版本变更。

# CAVEATS

只更新 pyproject.toml。不会创建 git 标签。

# HISTORY

poetry version 为 Poetry 项目提供**版本管理**功能。

# INSTALL

```dnf: sudo dnf install poetry```

```apk: sudo apk add poetry```

```brew: brew install poetry```

```nix: nix profile install nixpkgs#poetry```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[poetry](/man/poetry)(1), [semver](/man/semver)(1)
