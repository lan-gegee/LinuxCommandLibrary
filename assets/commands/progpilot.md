# TAGLINE

PHP 代码静态安全分析器

# TLDR

**扫描 PHP 文件**

```progpilot [src/]```

**扫描特定文件**

```progpilot [file.php]```

**使用配置**

```progpilot --configuration [config.yml] [src/]```

**使用自定义包含与排除路径扫描**

```progpilot --include [app/] --exclude [vendor/] [src/]```

**输出到文件**

```progpilot --output [report.json] [src/]```

**详细模式**

```progpilot -v [src/]```

# SYNOPSIS

**progpilot** [_--configuration file_] [_--json_] [_--output file_] [_options_] _files_

# PARAMETERS

**--configuration** _FILE_
> YAML 配置文件。

**--json**
> JSON 输出格式。

**--output** _FILE_
> 输出文件。

**-v**, **--verbose**
> 详细输出。

**--include** _PATH_
> 包含路径。

**--exclude** _PATH_
> 排除路径。

**--help**
> 显示帮助。

# VULNERABILITIES DETECTED

**SQL Injection** - Database query manipulation
**XSS** - Cross-site scripting
**Code Injection** - Arbitrary code execution
**Path Traversal** - File access outside root
**Command Injection** - Shell command execution

# DESCRIPTION

**progpilot** 通过追踪用户可控数据在应用中的流动，对 PHP 代码执行静态安全分析。它使用污点分析来识别未净化输入到达危险函数（如数据库查询、shell 命令或 HTML 输出）的位置，标记潜在的 SQL 注入、XSS、命令注入和路径穿越漏洞。

其分析方式是对 source（用户输入进入的位置）、sink（危险操作发生的位置）和 sanitizer（中和污点数据的函数）建模。这三者都可以通过 YAML 配置文件进行配置，团队由此可以定义自定义安全规则、添加应用特定的敏感函数并抑制误报。

输出包括漏洞类型、文件位置以及受影响的代码路径。JSON 输出模式便于集成到 CI/CD 管道中，在开发过程中自动执行安全检查。

# CONFIGURATION

**progpilot.yml**（或通过 **--configuration** 指定自定义路径）
> YAML 配置文件，定义分析所用的 source、sink、sanitizer、包含/排除路径以及自定义漏洞规则。

# CAVEATS

静态分析存在误报。复杂的代码路径可能被遗漏。PHP 版本覆盖情况不一。

# HISTORY

**progpilot** 由 **designsecurity** 创建，是一款开源的 PHP 静态安全分析器。它使用污点分析技术在应用代码中追踪用户可控数据。

# SEE ALSO

[phpstan](/man/phpstan)(1), [psalm](/man/psalm)(1), [php](/man/php)(1)
