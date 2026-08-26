# TAGLINE

回溯搜索 /var/log/wtmp 文件并列出全部用户的登录记录

# TLDR

查看**所有登录**历史

```last```

查看**特定用户**的登录记录

```last username```

显示**最近 10 条**登录记录

```last -n 10```

显示带**完整时间戳**的登录记录

```last -F```

用 **IP 地址**代替主机名显示登录记录

```last -i```

显示自特定日期**以来**的登录记录

```last -s -7days```

查看**系统重启**记录

```last reboot```

查看**失败的登录**（需要 root）

```lastb```

# SYNOPSIS

**last** [_options_] [_username_...] [_tty_...]

# DESCRIPTION

**last** 向前回溯搜索 /var/log/wtmp 文件，并显示自该文件创建以来所有用户登录和注销的记录列表。相关的 **lastb** 命令则显示来自 /var/log/btmp 的失败登录尝试。

# PARAMETERS

**-a, --hostlast**
> 在最后一列显示主机名

**-d, --dns**
> 将远程登录的 IP 地址转换为主机名

**-f, --file FILE**
> 使用其他文件代替 /var/log/wtmp

**-F, --fulltimes**
> 打印完整的登录与注销日期和时间

**-i, --ip**
> 显示 IP 地址而不是主机名

**-n, --limit NUM**
> 仅显示指定数量的行

**-R, --nohostname**
> 不显示主机名字段

**-s, --since TIME**
> 显示自指定时间以来的登录记录

**-t, --until TIME**
> 显示截至指定时间的登录记录

**-w, --fullnames**
> 显示完整的用户名和域名

**-x, --system**
> 显示系统关机条目和运行级别变更

**-p, --present TIME**
> 显示在指定时间在线的用户

**--time-format FORMAT**
> 定义输出的时间格式（notime、short、full、iso）

# CAVEATS

伪用户 "reboot" 会在系统每次重启时记录条目，因此可用于追踪启动历史。wtmp 和 btmp 文件必须存在；管理员可能需要用 **touch** 创建它们。

# HISTORY

**last** 自早期 BSD 系统时代起就是标准的 Unix 实用工具，一直提供用户登录记账功能。

# INSTALL

```apt: sudo apt install wtmpdb```

```apk: sudo apk add util-linux-login```

```zypper: sudo zypper install wtmpdb```

```nix: nix profile install nixpkgs#last```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lastb](/man/lastb)(1), [who](/man/who)(1), [w](/man/w)(1)
