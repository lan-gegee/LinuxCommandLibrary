# TAGLINE

模块化设计的多用途暴力破解工具

# TLDR

**暴力破解 FTP 登录**

```patator ftp_login host=[target] user=FILE0 password=FILE1 0=[users.txt] 1=[passwords.txt]```

**暴力破解 SSH 登录**

```patator ssh_login host=[target] user=[admin] password=FILE0 0=[passwords.txt]```

**HTTP 表单暴力破解**

```patator http_fuzz url=[http://target/login] method=POST body='user=admin&pass=FILE0' 0=[passwords.txt]```

**暴力破解 MySQL**

```patator mysql_login host=[target] user=[root] password=FILE0 0=[passwords.txt]```

**显示可用模块**

```patator```

**设置并发级别**

```patator [module] ... -t [10]```

# SYNOPSIS

**patator** _module_ [_options_] _host=target_ _param=value_...

# PARAMETERS

**-t** _N_
> 线程数量。

**-x** _ACTION:CONDITION_
> 满足条件时执行的动作。

**-l** _DIR_
> 日志目录。

**--timeout** _SECS_
> 连接超时时间。

**--retries** _N_
> 重试次数。

**FILE0**, **FILE1**, 等
> 文件占位符。

**0=**, **1=**, 等
> 文件赋值。

**RANGE0**
> 数字范围。

**COMBO00**
> 组合文件。

# MODULES

**ssh_login** - SSH 身份验证
**ftp_login** - FTP 身份验证
**http_fuzz** - HTTP 请求
**mysql_login** - MySQL 身份验证
**smtp_login** - SMTP 身份验证
**pop_login** - POP3 身份验证
**dns_forward** - DNS 查询

# DESCRIPTION

**patator** 是一款模块化设计的多用途暴力破解工具。它支持大量协议和服务。

各模块分别处理特定协议，如 SSH、FTP、HTTP 和数据库。每个模块都有协议专属的选项。

文件占位符支持字典组合。多个文件可以组合生成用户名/密码对。

条件动作可以过滤响应。例如忽略成功登录、记录特定错误或在匹配到结果时停止。

速率限制和线程控制资源占用。代理支持实现匿名化测试。

# CAVEATS

仅用于获得授权的渗透测试。激进的测试可能触发账户锁定。网络监控可能检测到攻击行为。

# HISTORY

**patator** 由 **Sebastien Macke**（lanjelot）创建，作为 Hydra 和 Medusa 的替代品。它强调安全测试的灵活性和可脚本化。

# INSTALL

```aur: yay -S patator```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[hydra](/man/hydra)(1), [medusa](/man/medusa)(1), [ncrack](/man/ncrack)(1)
