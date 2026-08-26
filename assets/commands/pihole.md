# TAGLINE

管理 Pi-hole（网络级广告拦截器）的命令行界面

# TLDR

检查 Pi-hole **状态**

```pihole status```

**更新** Pi-hole

```sudo pihole -up```

**启用**或**禁用**拦截

```pihole enable```

```pihole disable```

**更新** gravity（屏蔽列表）

```pihole -g```

**允许**或**拒绝**某个域名

```pihole allow example.com```

```pihole deny example.com```

在各列表中**查询**某个域名

```pihole -q example.com```

查看**实时日志**

```pihole -t```

不重启而**重新加载** DNS

```pihole reloaddns```

# SYNOPSIS

**pihole** [_command_] [_options_]

# DESCRIPTION

**pihole** 是管理 Pi-hole 的命令行界面。Pi-hole 是一个网络级广告和跟踪器拦截应用，充当 DNS 黑洞（sinkhole）。

# PARAMETERS

**status**
> 显示当前 Pi-hole 状态

**enable**
> 启用 Pi-hole 拦截

**disable [TIME]**
> 禁用 Pi-hole 拦截（可选指定时长）

**-up, updatePihole**
> 将 Pi-hole 更新到最新版本

**-g, updateGravity**
> 更新 gravity 数据库（屏蔽列表）

**allow DOMAIN**
> 将域名加入允许列表

**deny DOMAIN**
> 将域名加入拒绝列表

**-q, query DOMAIN**
> 在各列表中搜索域名

**-t, tail**
> 查看 DNS 查询的实时日志

**reloaddns**
> 不重启而重新加载 DNS 列表并清空缓存

**restartdns**
> 重启 DNS 服务器

**-c, chronometer**
> 在控制台显示实时统计

**-a, admin**
> 管理控制台选项（密码重置等）

**checkout**
> 切换 Pi-hole 分支（用于开发）

# CAVEATS

大多数命令需要 root 权限或使用 sudo。Pi-hole 充当 DNS 服务器，因此禁用它会影响所有以其作为 DNS 的设备。Web 管理界面提供更多管理选项。

# HISTORY

**Pi-hole** 是一个全网广告拦截器，运行在 Raspberry Pi（或其他 Linux 系统）上，在 DNS 层面拦截广告和跟踪。

# INSTALL

```nix: nix profile install nixpkgs#pihole```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dnsmasq](/man/dnsmasq)(8), [unbound](/man/unbound)(8)
