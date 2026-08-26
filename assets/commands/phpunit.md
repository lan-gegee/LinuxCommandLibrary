# TAGLINE

PHP 测试框架

# TLDR

**运行所有测试**

```phpunit```

**运行特定测试文件**

```phpunit [tests/ExampleTest.php]```

**运行目录中的测试**

```phpunit [tests/]```

**运行特定测试**

```phpunit --filter [testMethodName]```

**生成覆盖率报告**

```phpunit --coverage-html [coverage/]```

**使用配置文件**

```phpunit -c [phpunit.xml]```

# SYNOPSIS

**phpunit** [_options_] [_files_...]

# PARAMETERS

_FILES_
> 测试文件或目录。

**--filter** _PATTERN_
> 过滤测试。

**--coverage-html** _DIR_
> HTML 覆盖率报告。

**-c** _FILE_
> 配置文件。

**--testdox**
> TestDox 输出。

**--help**
> 显示帮助。

# DESCRIPTION

**phpunit** 是 PHP 事实上的单元和集成测试框架，源自 xUnit 家族。它发现并运行继承自 `PHPUnit\Framework\TestCase` 的测试类，提供丰富的断言、数据供给器、测试替身以及代码覆盖率报告。

测试通常组织在 `tests/` 目录下，并通过项目根目录中的 `phpunit.xml` 文件进行配置，该文件定义测试套件、引导文件和覆盖率过滤器。结果可以输出为 TestDox、JUnit XML 及其他格式，便于 CI 集成。

# CONFIGURATION

**phpunit.xml**, **phpunit.xml.dist**
> 项目配置：测试套件、引导文件、覆盖率过滤器和 PHP 设置。

# CAVEATS

通过 phpunit.xml 进行配置。代码覆盖率需要安装 Xdebug 或 PCOV。主要版本（9、10、11）移除了已弃用的 API，因此升级时测试代码可能需要更新。

# HISTORY

PHPUnit 由 **Sebastian Bergmann** 创建，是标准的 **PHP 测试框架**。

# INSTALL

```apk: sudo apk add phpunit```

```brew: brew install phpunit```

```nix: nix profile install nixpkgs#phpunit```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[phpspec](/man/phpspec)(1), [pest](/man/pest)(1), [php](/man/php)(1)
