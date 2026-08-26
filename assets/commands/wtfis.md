# TAGLINE

被动式主机名、域名与 IP 查询工具

# TLDR

**查询域名**

```wtfis [example.com]```

**结合 Shodan 信息查询 IP**

```wtfis -s [8.8.8.8]```

**启用全部信息增强**

```wtfis -A [example.com]```

# SYNOPSIS

**wtfis** [_options_] _hostname_|_domain_|_IP_

# DESCRIPTION

**wtfis** 利用 VirusTotal、IP2Whois 和 Shodan 等 OSINT 服务收集并以彩色、人类可读的格式呈现域名、主机名和 IP 地址的信息。它会尽量减少 API 调用次数，以免触及免费额度的速率限制。

# HISTORY

**wtfis** 由 **pirxthepilot**（Joon）创建，使用 **Python** 编写。

# INSTALL

```brew: brew install wtfis```

```nix: nix profile install nixpkgs#wtfis```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[whois](/man/whois)(1), [nslookup](/man/nslookup)(1), [dig](/man/dig)(1)
