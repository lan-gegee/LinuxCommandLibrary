# TAGLINE

通过 git 钩子强制执行 PHP 代码质量检查

# TLDR

**生成初始配置文件**

```grumphp configure```

**运行所有已配置的任务**

```grumphp run```

**运行特定任务**

```grumphp run --tasks=[phpcs,phpunit]```

**运行特定的测试套件**

```grumphp run --testsuite=[mytestsuite]```

**注册 GrumPHP 的 git 钩子**

```grumphp git:init```

**注销 GrumPHP 的 git 钩子**

```grumphp git:deinit```

**手动运行 pre-commit 钩子的任务**

```grumphp git:pre-commit```

# SYNOPSIS

**grumphp** _command_ [_options_]

# PARAMETERS

_COMMAND_
> 要运行的命令。

**configure**
> 生成初始的 grumphp.yml 配置文件，并推测合理的默认值。

**run**
> 对代码库执行所有已配置的任务。

**git:init**
> 注册 GrumPHP 的 git 钩子（`composer install` 之后自动运行）。

**git:deinit**
> 注销 GrumPHP 的 git 钩子。

**git:pre-commit**
> 运行绑定到 pre-commit 钩子的任务。

**git:commit-msg**
> 运行校验提交信息的任务。

**--tasks** _TASK1,TASK2_
> 只运行给定的逗号分隔任务。

**--testsuite** _NAME_
> 只运行属于给定测试套件的任务。

**--help**
> 显示帮助信息。

# DESCRIPTION

**GrumPHP** 是一款 PHP 代码质量工具，会在 git 提交时运行检查。它通过在允许提交前运行 PHPStan、PHP_CodeSniffer 和 PHPUnit 等任务来强制执行编码规范。

该工具与 git 钩子集成，阻止未通过质量检查的提交。它可以通过项目根目录下的 grumphp.yml 文件进行配置。

# CONFIGURATION

**grumphp.yml**
> 项目级配置文件，定义任务、参数和 git 钩子设置。

# CAVEATS

仅适用于 PHP 项目。需要 Composer。任务较多时可能拖慢提交速度。

# HISTORY

GrumPHP 由 **phpro** 创建，旨在通过 git 钩子自动化 PHP 代码质量检查。

# SEE ALSO

[composer](/man/composer)(1), [phpcs](/man/phpcs)(1), [phpstan](/man/phpstan)(1)

# RESOURCES

```[Source code](https://github.com/phpro/grumphp)```

```[Documentation](https://github.com/phpro/grumphp/tree/v2.x/doc)```

<!-- verified: 2026-07-17 -->
