# TAGLINE

用于流量捕获的 HTTP/HTTPS 代理

# TLDR

**启动代理服务器**

```proxify```

**指定端口**

```proxify -p [8888]```

**输出到目录**

```proxify -o [logs/]```

**上游代理**

```proxify -upstream [http://127.0.0.1:8080]```

**转储请求**

```proxify -dump-req```

**转储响应**

```proxify -dump-resp```

**按内容类型过滤**

```proxify -match-resp-body "[text/html]"```

# SYNOPSIS

**proxify** [_-p port_] [_-o dir_] [_-upstream proxy_] [_options_]

# PARAMETERS

**-p**, **--port** _PORT_
> 监听端口。

**-o**, **--output** _DIR_
> 输出目录。

**-upstream** _PROXY_
> 上游代理。

**-dump-req**
> 转储请求。

**-dump-resp**
> 转储响应。

**-match-resp-body** _PATTERN_
> 过滤响应体。

**-match-req-body** _PATTERN_
> 过滤请求体。

**-silent**
> 静默模式。

**-v**, **--verbose**
> 详细输出。

# DESCRIPTION

**proxify** 是一个轻量级 HTTP/HTTPS 代理，专为在安全测试期间捕获和记录 Web 流量而设计。它拦截请求和响应，将头部和请求体转储到控制台或按结构组织的输出目录，供后续分析。

模式匹配选项可按请求体或响应体内容过滤捕获的流量，让测试人员专注于特定的内容类型或感兴趣的关键词。上游代理支持使其能够通过 Burp Suite 或 mitmproxy 等工具串联，实现更深入的检查。

该工具由 ProjectDiscovery 开发，与其安全测试工具集集成。流量按域名分类保存，便于查看来自特定目标的捕获数据。

# CAVEATS

HTTPS 需要安装证书。大流量会消耗磁盘空间。某些应用会检测代理。

# HISTORY

**Proxify** 由 **ProjectDiscovery** 为安全测试而创建，为 Web 应用分析提供简单的流量拦截功能。

# INSTALL

```brew: brew install proxify```

```nix: nix profile install nixpkgs#proxify```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mitmproxy](/man/mitmproxy)(1), [burpsuite](/man/burpsuite)(1), [charles](/man/charles)(1)
