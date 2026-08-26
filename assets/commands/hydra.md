# TAGLINE

支持多种协议的高速网络登录破解工具

# TLDR

**暴力破解 SSH**

```hydra -l [user] -P [passwords.txt] ssh://[target]```

**HTTP 表单暴力破解**

```hydra -l [admin] -P [pass.txt] [target] http-post-form "/login:user=^USER^&pass=^PASS^:Invalid"```

**FTP 暴力破解**

```hydra -L [users.txt] -P [pass.txt] ftp://[target]```

**指定线程数**

```hydra -t [4] -l [user] -P [pass.txt] [target] [service]```

**详细输出**

```hydra -v -l [user] -P [pass.txt] [target] ssh```

# SYNOPSIS

**hydra** [_options_] _target_ _service_

# PARAMETERS

_TARGET_
> 目标主机。

_SERVICE_
> 要攻击的服务（ssh、ftp、http-post-form）。

**-l** _LOGIN_
> 单个用户名。

**-L** _FILE_
> 从文件加载多个用户名。

**-p** _PASS_
> 单个密码。

**-P** _FILE_
> 从文件加载多个密码。

**-C** _FILE_
> 冒号分隔的 `login:pass` 列表，用于替代 **-L**/**-P**。

**-e** _nsr_
> 额外尝试空密码（**n**）、以登录名作为密码（**s**）和/或反转的登录名（**r**）。

**-x** _MIN:MAX:CHARSET_
> 通过暴力生成密码而非使用字典（例如 `1:8:a` 表示长度 1-8 的小写字母）。

**-M** _FILE_
> 攻击从文件读取的目标列表，每行一个（`host[:port]`）。

**-o** _FILE_
> 将找到的用户名/密码对写入文件而非 stdout。

**-b** _FORMAT_
> **-o** 的输出格式：`text`（默认）、`json` 或 `jsonv1`。

**-f** / **-F**
> 一旦找到有效凭据立即退出：按主机生效（**-f**），或在所有目标上全局生效（**-F**，需要 **-M**）。

**-t** _TASKS_
> 每个目标运行的并行连接数（默认：16）。

**-T** _TASKS_
> 使用 **-M** 时的总并行连接数（默认：64）。

**-s** _PORT_
> 为服务指定非默认端口。

**-S**
> 通过 SSL/TLS 建立连接。

**-4** / **-6**
> 使用 IPv4（默认）或 IPv6 地址。

**-R**
> 从 `hydra.restore` 恢复先前中止或崩溃的会话。

**-v** / **-V**
> 详细模式 / 显示每次尝试的用户名+密码组合。

**-h**
> 显示帮助信息。

# DESCRIPTION

**Hydra** 是一款并行化的网络登录破解工具，用于经授权的渗透测试和安全审计。它针对远程认证服务系统地尝试用户名和密码组合，凭据来自用户提供的字典、单一值或暴力字符集生成器（**-x**）。多个连接线程并行运行（可通过 **-t** 配置），使其能够高效地测试大量组合。

Hydra 开箱即支持超过 50 种协议和服务，包括 SSH、FTP、Telnet、HTTP/HTTPS（basic auth、表单和 digest）、SMB、RDP、MySQL、PostgreSQL、SMTP、IMAP、LDAP、VNC 等。对于 Web 应用，其 `http-post-form` 和 `http-get-form` 模块接受自定义请求模板，并使用 `^USER^`/`^PASS^` 占位符标记注入凭据。结果可保存到文件（**-o**）以便日后分析，被中断的会话可用 **-R** 恢复。

# CAVEATS

仅可用于你有权测试的系统——未经授权的使用在大多数司法管辖区属于违法行为。激烈的攻击可能触发账户锁定、IPS/WAF 封禁或降低目标服务的性能。打印简短选项摘要的是 `-h`（而非 `--help`）；`hydra -U <service>` 可打印模块专属选项。

# HISTORY

Hydra 由 **THC**（The Hacker's Choice）的 **van Hauser** 于 **2000 年**创建，号称首个并行化的网络登录破解工具。开发工作在 GitHub 上持续进行，David Maciejak 等人也做出了贡献。

# INSTALL

```apt: sudo apt install hydra```

```dnf: sudo dnf install hydra```

```pacman: sudo pacman -S hydra```

```apk: sudo apk add hydra```

```zypper: sudo zypper install hydra```

```brew: brew install hydra```

```nix: nix profile install nixpkgs#hydra```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ncrack](/man/ncrack)(1), [medusa](/man/medusa)(1), [john](/man/john)(1)

# RESOURCES

```[Source code](https://github.com/vanhauser-thc/thc-hydra)```

<!-- verified: 2026-07-19 -->
