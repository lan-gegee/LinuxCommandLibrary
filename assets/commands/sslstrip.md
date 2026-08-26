# TLDR

在默认端口启动 **SSL 剥离**

```sslstrip```

监听**指定端口**

```sslstrip --listen=8080```

记录**所有 SSL** 流量

```sslstrip --ssl --listen=8080```

记录**所有 HTTP 和 SSL** 流量

```sslstrip --listen=8080 --all```

将日志写入**文件**

```sslstrip --listen=8080 --write=output.log```

显示**帮助**

```sslstrip --help```

# SYNOPSIS

**sslstrip** [_options_]

# DESCRIPTION

**sslstrip** 是一款安全测试工具，通过在受害者与服务器之间充当代理来实施 SSL 剥离攻击。它将 HTTPS 链接转换为 HTTP，从而拦截本应加密的流量。该工具用于获得授权的渗透测试和安全研究。

# PARAMETERS

**-l, --listen PORT**
> 要监听的端口（默认：10000）

**-a, --all**
> 记录所有 SSL 和 HTTP 流量

**-s, --ssl**
> 记录与服务器之间的所有 SSL 流量

**-w, --write FILE**
> 指定日志文件路径

**-p, --post**
> 仅记录 HTTP POST 请求（默认）

**-f, --favicon**
> 在安全请求上替换为锁形图标

**-k, --killsessions**
> 终止进行中的会话

**-h, --help**
> 显示帮助信息

# CAVEATS

此工具仅用于获得授权的安全测试。未经授权对不属于你或未获测试许可的系统使用属于违法行为。需要配合 ARP 欺骗或类似的中间人设置才能拦截流量。启用 HSTS 预加载的现代浏览器可以阻止此类攻击。

# HISTORY

**sslstrip** 由 Moxie Marlinspike 创建，并在 Black Hat DC 2009 上演示，用以说明 Web 应用中 SSL/TLS 实现的漏洞。

# INSTALL

```nix: nix profile install nixpkgs#sslstrip```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[arpspoof](/man/arpspoof)(8), [ettercap](/man/ettercap)(8), [mitmproxy](/man/mitmproxy)(1), [dsniff](/man/dsniff)(8), [bettercap](/man/bettercap)(1)

# RESOURCES

```[Source code](https://github.com/moxie0/sslstrip)```

<!-- verified: 2026-06-10 -->
