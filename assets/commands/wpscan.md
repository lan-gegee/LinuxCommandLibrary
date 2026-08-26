# TAGLINE

WordPress 安全漏洞扫描器

# TLDR

**扫描 WordPress 站点**

```wpscan --url [https://example.com]```

**枚举用户**

```wpscan --url [https://example.com] -e u```

**枚举插件**

```wpscan --url [https://example.com] -e vp```

**枚举主题**

```wpscan --url [https://example.com] -e vt```

**完整枚举**

```wpscan --url [https://example.com] -e ap,at,u```

**密码暴力破解**

```wpscan --url [https://example.com] -U [admin] -P [passwords.txt]```

**使用 API token**

```wpscan --url [https://example.com] --api-token [TOKEN]```

**输出到文件**

```wpscan --url [https://example.com] -o [output.txt]```

# SYNOPSIS

**wpscan** [_--url url_] [_-e enumerate_] [_-U user_] [_-P passwords_] [_options_]

# PARAMETERS

**--url** _URL_
> 目标 URL。

**-e** _LIST_
> 枚举选项。

**-U** _USER_
> 用于暴力破解的用户名。

**-P** _FILE_
> 密码字典文件。

**--api-token** _TOKEN_
> WPScan API token。

**-o** _FILE_
> 输出文件。

**-f** _FORMAT_
> 输出格式（cli、json 等）。

**--random-user-agent**
> 随机 user agent。

**--wp-content-dir** _DIR_
> wp-content 目录。

**--detection-mode** _MODE_
> 检测模式（mixed、passive、aggressive）。

**--force**
> 不检查目标是否为 WordPress。

**-v**
> 详细模式。

# ENUMERATION OPTIONS

**u**
> 用户。

**vp**
> 存在漏洞的插件。

**ap**
> 所有插件。

**vt**
> 存在漏洞的主题。

**at**
> 所有主题。

**cb**
> 配置备份。

**dbe**
> 数据库导出。

# DESCRIPTION

**wpscan** 是一款 WordPress 安全扫描器。它可以识别漏洞、错误配置和弱凭据。

用户枚举通过多种技术找出有效用户名，这些用户名可用于针对性攻击。

插件和主题枚举可识别已安装的组件。存在漏洞的插件是 WordPress 的主要攻击面之一。

漏洞数据库需要 API token。免费 token 的请求数有限；付费 token 提供更多额度。

密码暴力破解用于测试凭据强度。目标可能启用了速率限制，请负责任地使用。

检测模式在隐蔽性与全面性之间权衡。aggressive 模式可能触发安全插件。

# CAVEATS

只能在获得授权的情况下使用。可能触发安全告警。获取漏洞数据需要 API token。完整扫描会消耗大量资源。

# HISTORY

**WPScan** 由 **WPScan Team** 大约于 **2011 年**创建。它已成为标准的 WordPress 安全评估工具，被安全专业人士和漏洞赏金猎人广泛使用。

# INSTALL

```pacman: sudo pacman -S wpscan```

```nix: nix profile install nixpkgs#wpscan```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nmap](/man/nmap)(1), [nikto](/man/nikto)(1), [sqlmap](/man/sqlmap)(1), [burp](/man/burp)(1)
