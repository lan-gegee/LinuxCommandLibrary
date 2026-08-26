# TAGLINE

高速网络身份验证破解工具

# TLDR

**破解 SSH 登录**

```ncrack -p [22] --user [root] -P [wordlist.txt] [192.168.1.1]```

**破解多个服务**

```ncrack [ssh://192.168.1.1,ftp://192.168.1.2]```

**使用用户名列表**

```ncrack -U [users.txt] -P [passwords.txt] [ssh://target]```

**设置计时模板**

```ncrack -T[4] [ssh://target]```

**从文件读取目标**

```ncrack -iL [hosts.txt] -p [22] --user [admin]```

**将结果保存到文件**

```ncrack -oN [results.txt] [ssh://target] -U [users.txt] -P [passwords.txt]```

# SYNOPSIS

**ncrack** [_options_] [_target_...]

# PARAMETERS

**-p** _ports_
> 目标端口。

**--user** _user_
> 单个用户名。

**-U** _file_
> 用户名列表。

**-P** _file_
> 密码列表。

**-T** _0-5_
> 计时模板。

**-iL** _file_
> 输入目标列表。

**-oN** _file_
> 普通格式输出。

**-oX** _file_
> XML 格式输出。

**-v**
> 详细输出。

# DESCRIPTION

**Ncrack** 是一款高速网络身份验证破解工具。它支持多种协议，包括 SSH、RDP、FTP、Telnet、HTTP 等。

由 Nmap 开发者设计，ncrack 采用模块化架构，允许添加新的协议模块。

# SUPPORTED PROTOCOLS

```
ssh, rdp, ftp, telnet
http, https, pop3, imap
smb, vnc, sip, redis
mongodb, cassandra, mssql
```

# CAVEATS

仅在获得授权时使用。可能触发安全告警。可能导致账户被锁定。建议进行速率限制。

# HISTORY

Ncrack 由 **Nmap Project** 团队开发，于 **2009 年**首次发布，作为与 Nmap 互补的网络身份验证破解工具。

# INSTALL

```apt: sudo apt install ncrack```

```dnf: sudo dnf install ncrack```

```pacman: sudo pacman -S ncrack```

```brew: brew install ncrack```

```nix: nix profile install nixpkgs#ncrack```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[hydra](/man/hydra)(1), [medusa](/man/medusa)(1), [nmap](/man/nmap)(1), [john](/man/john)(1)
