# TAGLINE

PHP 代码自动化重构与升级

# TLDR

**运行 rector**

```vendor/bin/rector process [src/]```

**试运行**

```vendor/bin/rector process [src/] --dry-run```

**使用特定配置文件**

```vendor/bin/rector process [src/] --config [rector.php]```

**只运行单个规则**

```vendor/bin/rector process [src/] --only [TypedPropertyFromAssignsRector]```

**显示所有已加载和已跳过的规则**

```vendor/bin/rector list-rules```

**初始化 rector.php 配置文件**

```vendor/bin/rector init```

**处理前清空缓存**

```vendor/bin/rector process --clear-cache```

**处理单个文件**

```vendor/bin/rector process [src/File.php]```

**为 GitHub Actions 或 GitLab CI 生成 CI 工作流**

```vendor/bin/rector setup-ci```

**用样板代码生成自定义规则**

```vendor/bin/rector custom-rule```

# SYNOPSIS

**rector** _command_ [_--dry-run_] [_--config file_] [_options_] [_paths_]

# PARAMETERS

**process**
> 对指定路径执行重构。

**init**
> 创建入门级 **rector.php** 配置文件。

**list-rules**
> 显示所有已加载和已跳过的规则。接受 **--config** 和 **--output-format json**。

**setup-ci**
> 生成用于自动运行 Rector 的 CI 工作流文件（GitHub Actions 或 GitLab CI）。

**custom-rule**
> 用样板结构和 PSR-4 自动加载路径生成自定义规则。

**--dry-run**
> 预览变更而不实际应用。

**--config** _FILE_
> 配置文件。

**--clear-cache**
> 处理前清空缓存。

**--only** _RULE_
> 只运行指定的单个规则类。

**--output-format** _FORMAT_
> 输出格式（如 **json**），便于将结果通过管道传给其他工具。

**-v**, **--verbose**
> 详细输出。

**--debug**
> 打印嵌套异常堆栈跟踪。

# DESCRIPTION

**Rector** 对 PHP 代码库执行自动化重构，应用基于规则的转换来升级语法、现代化框架用法并强化代码质量标准。它将 PHP 文件解析为抽象语法树，并应用配置的规则将旧结构转换为其现代等价物，自动处理 PHP 版本升级（例如 PHP 7.4 到 8.2）和框架迁移（Symfony、Laravel、PHPUnit）。

**--dry-run** 标志可预览所有变更而不修改文件，因此在应用之前可以安全地审查转换效果。规则按常见升级路径组织成集合，也可以针对项目特定的重构模式编写自定义规则。该工具通常通过 **rector.php** 文件配置，其中指明要应用的规则集和单个规则。

# CONFIGURATION

**rector.php**
> 主配置文件，定义规则集、单个规则、要处理的路径以及跳过模式。由 **rector init** 生成。

# CAVEATS

请仔细审查试运行的输出。复杂代码可能需要手动修复。运行前先提交到 Git。

# HISTORY

**Rector** 由 **Tomas Votruba** 创建，用于 PHP 代码自动化重构。它支持安全的大规模代码库现代化改造。

# SEE ALSO

[phpstan](/man/phpstan)(1), [php-cs-fixer](/man/php-cs-fixer)(1), [phpcs](/man/phpcs)(1), [composer](/man/composer)(1)
