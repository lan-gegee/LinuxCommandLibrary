# TAGLINE

Debian 安全漏洞扫描器

# TLDR

列出存在漏洞的**已安装**软件包

```debsecan```

列出**特定套件**的漏洞

```debsecan --suite [release_code_name]```

只列出**已有修复**的漏洞

```debsecan --suite [release_code_name] --only-fixed```

列出已修复的漏洞并**邮件发送报告**

```debsecan --suite [sid] --only-fixed --format report --mailto [root] --update-history```

**升级**有漏洞的软件包

```sudo apt upgrade $(debsecan --only-fixed --format packages)```

# SYNOPSIS

**debsecan** [_options_]

# DESCRIPTION

**debsecan**（Debian Security Analyzer）列出已安装软件包中的已知漏洞。它对照 Debian 安全跟踪数据库进行检查，并报告影响系统的 CVE。

适用于安全审计以及找出需要更新的软件包。

# PARAMETERS

**--suite** _suite_
> Debian 发行版（stretch、buster、bullseye、sid）

**--only-fixed**
> 只显示有可用修复的漏洞

**--format** _format_
> 输出格式（summary、detail、report、packages）

**--mailto** _address_
> 将报告发送到指定邮箱地址

**--update-history**
> 跟踪漏洞历史

# CAVEATS

获取漏洞数据需要网络连接。套件必须与已安装的系统匹配。并非所有列出的漏洞在你的具体配置中都可被利用。

# SEE ALSO

[apt](/man/apt)(8), [unattended-upgrades](/man/unattended-upgrades)(8)

# RESOURCES

```[Homepage](https://www.enyo.de/fw/software/debsecan/)```

<!-- verified: 2026-07-11 -->
