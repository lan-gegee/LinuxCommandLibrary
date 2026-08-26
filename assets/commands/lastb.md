# TAGLINE

与 last 相同，但显示 /var/log/btmp 中记录的失败登录尝试

# TLDR

列出**失败的登录尝试**

```sudo lastb```

列出自某日期**以来**的失败登录

```sudo lastb -s [YYYY-MM-DD]```

列出**截至**某日期的失败登录

```sudo lastb -t [YYYY-MM-DD]```

显示在特定时间**在线**的用户

```sudo lastb -p [YYYY-MM-DD HH:MM]```

将 IP 解析为**主机名**

```sudo lastb -d```

将输出限制为指定的**条目数量**

```sudo lastb -n [10]```

显示包含年份和秒数的**完整时间戳**

```sudo lastb -F```

从**指定的 btmp 文件**读取

```sudo lastb -f [/var/log/btmp.1]```

# SYNOPSIS

**lastb** [_options_] [_username_...] [_tty_...]

# PARAMETERS

**-s**, **--since** _TIME_
> 显示自指定时间以来的记录

**-t**, **--until** _TIME_
> 显示截至指定时间的记录

**-p**, **--present** _TIME_
> 显示在指定时间在线的用户

**-d**, **--dns**
> 将 IP 地址转换为主机名

**-n**, **--limit** _NUM_
> 将输出限制为 NUM 条记录

**-f**, **--file** _FILE_
> 从指定文件读取而不是 /var/log/btmp

**-F**, **--fulltimes**
> 打印完整的登录与注销日期和时间

**-i**, **--ip**
> 显示 IP 地址而不是主机名

**-R**, **--nohostname**
> 不显示主机名字段

**-w**, **--fullnames**
> 显示完整的用户名和域名

**-x**, **--system**
> 显示系统关机条目和运行级别变更

**--time-format** _FORMAT_
> 输出时间戳格式：notime、short、full 或 iso

# DESCRIPTION

**lastb** 的用法与 last 相同，但显示的是 /var/log/btmp 中记录的失败登录尝试。它适合用于安全审计，以识别暴力破解攻击或未授权访问企图。

输出内容为每次失败登录尝试的用户名、终端、来源地址和时间戳。

# CAVEATS

读取 /var/log/btmp 需要 root 权限。遭受攻击时 btmp 文件可能变得很大，建议配置日志轮转。若从未写入过，该文件可能不存在。

# HISTORY

lastb 用于对失败登录进行安全审计，是 last 命令的补充。btmp 文件格式与 wtmp 一致，但记录的是失败而非成功的登录。

# INSTALL

```apk: sudo apk add util-linux-login```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[last](/man/last)(1), [lastlog](/man/lastlog)(8), [faillog](/man/faillog)(8), [utmpdump](/man/utmpdump)(1), [login](/man/login)(1)
