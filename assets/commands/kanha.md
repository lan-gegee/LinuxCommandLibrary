# TAGLINE

Web 应用渗透测试套件

# TLDR

对隐藏路径进行 **URL 模糊测试**

```kanha fuzz -u [https://example.com/FUZZ] -w [path/to/wordlist.txt]```

**检查 HTTP 响应码**

```kanha httpx -l [path/to/urls.txt]```

**执行反向 DNS 查询**

```kanha rdns -l [path/to/ips.txt]```

**检测子域名接管**

```kanha takeover -l [path/to/subdomains.txt]```

# SYNOPSIS

**kanha** _command_ [_options_]

# DESCRIPTION

**kanha** 是一个用于 web 应用渗透测试的 CLI 套件，它把多项安全测试功能整合到一个工具中，包括 **URL 模糊测试**、**反向 DNS 查询**、**HTTP 响应码检查**和**子域名接管检测**。

每个子命令针对 web 应用安全测试的一个特定方面，使其成为安全研究员和渗透测试人员称手的的一体化工具包。

# CAVEATS

只可用于你获得明确授权测试的系统。模糊测试可能产生大量网络流量。结果应人工核实是否存在误报。

# HISTORY

**kanha** 用 **Rust** 编写，设计目标是为基于终端的工作流提供一个快速的多功能 web 应用安全测试工具包。

# INSTALL

```nix: nix profile install nixpkgs#kanha```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nmap](/man/nmap)(1), [curl](/man/curl)(1), [nikto](/man/nikto)(1)
