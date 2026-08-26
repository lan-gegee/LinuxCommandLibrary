# TAGLINE

扫描 PHP 依赖中的安全漏洞

# TLDR

**审计依赖项**的安全漏洞

```composer audit```

**以 JSON 格式输出审计结果**

```composer audit --format=json```

**只审计生产环境依赖**

```composer audit --no-dev```

**审计锁定的软件包并将已弃养的包报告为失败**

```composer audit --locked --abandoned=fail```

# SYNOPSIS

**composer** **audit** [_options_]

# PARAMETERS

**--format** _format_
> 输出格式：`table`（默认）、`plain`、`json` 或 `summary`。

**--locked**
> 审计 composer.lock 中记录的确切版本，而非已安装的软件包。

**--no-dev**
> 忽略开发依赖（require-dev）。

**--abandoned** _mode_
> 如何处理已弃养（abandoned）的软件包：`ignore`、`report` 或 `fail`（Composer 2.8+）。

**--ignore** _package_
> 忽略指定软件包的安全公告。可重复使用。

# DESCRIPTION

**composer audit** 通过查询 Packagist 官方安全公告数据库对 PHP 依赖执行安全漏洞扫描。该命令在 Composer 2.4 中引入，提供内置机制来识别存在已知安全问题软件包，无需再借助第三方安全扫描工具。

该命令会分析 composer.json 中的依赖声明以及 composer.lock 中锁定的版本，报告所有发布了 CVE（公共漏洞和暴露）条目或安全公告的软件包。结果包括漏洞严重程度、受影响的版本以及建议的修复步骤。

此功能类似于 JavaScript 的 npm audit 和 Ruby 的 bundle audit，为 PHP 开发者提供了维护安全依赖链的标准化方式。它在 CI/CD 流水线中尤其有价值——自动化安全检查有助于防止含漏洞的代码进入生产环境。

# CAVEATS

需要 Composer 2.4 或更新版本。只能检测已知且已公开的漏洞。

# INSTALL

```dnf: sudo dnf install composer```

```pacman: sudo pacman -S composer```

```apk: sudo apk add composer```

```brew: brew install composer```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[composer](/man/composer)(1), [composer-require-checker](/man/composer-require-checker)(1)
