# TAGLINE

Web 应用安全测试平台

# TLDR

**启动** Burp Suite

```burpsuite```

使用**默认配置**启动

```burpsuite --use-defaults```

打开特定的**项目文件**

```burpsuite --project-file=[path/to/file]```

加载特定的**配置文件**

```burpsuite --config-file=[path/to/file]```

**不加载扩展**启动

```burpsuite --disable-extensions```

# SYNOPSIS

**burpsuite** [_options_]

# DESCRIPTION

**Burp Suite** 是由 PortSwigger 开发的图形化 Web 应用安全测试平台。它提供了拦截 HTTP 流量、扫描漏洞和手动测试 Web 应用的工具。

该工具包括用于流量拦截的代理、自动化漏洞检测的扫描器、手动操作请求的 Repeater 以及自动化攻击的 Intruder。

# PARAMETERS

**--use-defaults**
> 以默认配置设置启动

**--project-file** _file_
> 打开特定的项目文件

**--config-file** _file_
> 从文件加载配置

**--disable-extensions**
> 启动时不加载扩展

**--user-config-file** _file_
> 从文件加载用户选项

# CAVEATS

免费的 Community Edition 功能有限；Professional Edition 需要付费。需要 Java 运行时环境。只能在你获得授权的应用上进行测试。拦截流量可能会破坏 TLS/SSL 校验。

# HISTORY

**Burp Suite** 由 Dafydd Stuttard（PortSwigger）创建，于 **2003 年**首次发布。它已成为使用最广泛的 Web 应用安全测试工具之一。

# INSTALL

```nix: nix profile install nixpkgs#burpsuite```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mitmproxy](/man/mitmproxy)(1), [nikto](/man/nikto)(1), [sqlmap](/man/sqlmap)(1)
