# TAGLINE

Drupal 代码弃用检查器

# TLDR

**检查模块的**弃用项

```drupal-check [modules/custom/mymodule]```

以**分析级别**检查

```drupal-check -a [modules/custom/mymodule]```

**检查 Drupal 10** 兼容性

```drupal-check --drupal-root=[.] [modules/custom/mymodule]```

按指定格式输出

```drupal-check --format=[json] [path]```

**检查多个路径**

```drupal-check [path1] [path2]```

# SYNOPSIS

**drupal-check** [_options_] _paths_...

# PARAMETERS

_PATH_...
> 一个或多个要分析的目录或文件。

**-d**, **--deprecations**
> 检查弃用 API 的使用（默认行为）。

**-a**, **--analysis**
> 运行一般性静态分析检查。

**-s**, **--style**
> 运行代码风格检查。

**--php8**
> 使用 PHPStan phpVersion 8.1（Drupal 10 要求）。

**--drupal-root** _PATH_
> Drupal 根目录路径。

**--format** _FORMAT_
> 输出格式：raw、table、checkstyle、json 或 junit（默认：table）。

**--memory-limit** _LIMIT_
> 分析的内存限制（如 1G）。

**-e**, **--exclude-dir** _DIRS_
> 要排除的目录，以逗号分隔。

**--no-progress**
> 不显示进度条。

**-v**, **-vv**, **-vvv**
> 提高输出详细程度。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**drupal-check** 是一款静态分析工具，用于检查 Drupal 代码中的弃用 API 用法及其他问题。它通过识别需要更新的代码，帮助模块为 Drupal 版本升级做好准备。

该工具使用 PHPStan 进行静态分析，并应用 Drupal 专属规则。它能检测到未来 Drupal 版本中将被移除的已弃用函数、类和服务的用法。

drupal-check 是维护 Drupal 模块、确保与后续版本兼容的必备工具。

# CAVEATS

需要 PHP 和 Composer。可能出现误报。复杂的动态代码可能无法正确分析。结果取决于弃用数据库的更新程度。

# HISTORY

drupal-check 由 **Matt Glaman** 创建，旨在帮助 Drupal 社区为 Drupal 9 迁移做准备。它解决了在庞大 Drupal 代码库中识别弃用代码这一难题。

# INSTALL

```pacman: sudo pacman -S drupal```

```nix: nix profile install nixpkgs#drupal```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[drupal](/man/drupal)(1), [drush](/man/drush)(1), [phpstan](/man/phpstan)(1)
