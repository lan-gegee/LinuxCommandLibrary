# TAGLINE

审计 PHP 依赖中的已知漏洞

# TLDR

**检查项目**

```security-checker security:check```

**检查指定文件**

```security-checker security:check [composer.lock]```

以 **JSON 输出**

```security-checker security:check --format=json```

**使用自定义端点检查**

```security-checker security:check --end-point=[url]```

# SYNOPSIS

**security-checker** security:check [_--format fmt_] [_options_] [_lockfile_]

# PARAMETERS

**security:check**
> 检查漏洞。

**--format** _FMT_
> 输出格式（text、json、yaml）。

**--end-point** _URL_
> 自定义漏洞数据库。

**--timeout** _SEC_
> 请求超时时间。

**-v**
> 详细输出。

# DESCRIPTION

**security-checker** 通过将 **composer.lock** 文件与 FriendsOfPHP 安全公告数据库进行比对，审计 PHP 项目依赖中的已知安全漏洞。它会识别出已发布 CVE 或安全问题通告的已安装软件包。

发现漏洞时该工具会返回非零退出码，因此适合作为门禁检查集成到 CI/CD 流水线中。输出支持文本、JSON 和 YAML 格式，既便于人工审查，也便于其他工具进行程序化处理。

# CAVEATS

仅适用于 PHP/Composer。数据库可能滞后。需要联网。

# HISTORY

**security-checker** 由 **SensioLabs**（Symfony）创建，用于检查 PHP 项目依赖中的已知安全漏洞。

# SEE ALSO

[composer](/man/composer)(1), [npm-audit](/man/npm-audit)(1), [snyk](/man/snyk)(1)
