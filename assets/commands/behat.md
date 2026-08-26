# TAGLINE

PHP 的 BDD 测试框架

# TLDR

**初始化新的 Behat 项目**

```behat --init```

**运行所有功能测试**

```behat```

**运行特定功能文件的测试**

```behat [features/login.feature]```

按行号**运行特定场景**

```behat [features/login.feature:15]```

**运行带指定标签的测试**

```behat --tags [smoke]```

为未定义步骤**生成步骤定义**

```behat --snippets-for --append-snippets```

以详细输出**运行测试**

```behat -v```

以 JUnit 格式**输出结果**

```behat --format junit --out [reports/]```

# SYNOPSIS

**behat** [_options_] [_feature_file_]

# DESCRIPTION

**behat** 是一个面向 PHP 的 BDD（行为驱动开发）框架，通过人类可读的场景来测试业务预期。它是 Cucumber 的 PHP 实现，使用 Gherkin 语法定义测试场景。

Behat 让团队可以用开发人员、QA 和利益相关者都能理解的平实语言来描述应用行为。场景写在 feature 文件中，并针对用 PHP 实现的步骤定义执行。

# PARAMETERS

**--init**
> 初始化一个新的 Behat 项目并创建所需的目录结构

**--tags** _value_
> 只运行带有匹配标签的场景（如 @smoke、@regression）

**--name** _value_
> 只运行名称匹配给定字符串或正则表达式的 feature 元素

**-f, --format** _value_
> 输出格式化器：pretty（默认）、progress、junit

**--out** _value_
> 将输出写入文件或目录

**--snippets-for** _value_
> 为未定义的步骤生成步骤定义片段

**--append-snippets**
> 将生成的片段追加到上下文文件中

**-v, --verbose**
> 提高输出的详细程度

**--colors** / **--no-colors**
> 强制启用或禁用彩色输出

**-s, --suite** _value_
> 只运行指定的测试套件

**-p, --profile** _value_
> 使用特定的配置 profile

**-c, --config** _value_
> 使用特定的配置文件（默认：behat.yml 或 behat.yml.dist）

**--dry-run**
> 只调用格式化器而不实际执行测试或钩子

**--stop-on-failure**
> 在第一个失败的场景处停止处理

**--rerun**
> 只重新运行上次运行中失败的场景

**--strict**
> 除非每个测试都明确通过否则判定失败（将 undefined/pending 视为失败）

# CAVEATS

当前 Behat 3.x 要求 PHP 8.2 或更高版本（较早的 3.x 版本可在 PHP 5.3.1+ 上运行）。Feature 文件必须使用缩进规范的 Gherkin 语法。步骤定义必须唯一；重复的定义会导致歧义错误。默认上下文文件是 features/bootstrap/ 中的 **FeatureContext.php**。

# HISTORY

Behat 由 **Konstantin Kudryashov**（everzet）于 **2010** 年创建，是 Cucumber 的 PHP 移植版。它成为 PHP 事实上的 BDD 测试框架，在 Symfony 和 Drupal 社区被广泛用于验收测试。

# SEE ALSO

[phpunit](/man/phpunit)(1), [phpspec](/man/phpspec)(1), [cucumber](/man/cucumber)(1), [composer](/man/composer)(1), [php](/man/php)(1)

# RESOURCES

```[Source code](https://github.com/Behat/Behat)```

```[Documentation](https://docs.behat.org/)```

<!-- verified: 2026-06-19 -->
