# TAGLINE

配置数据库集群的维护时间窗口

# TLDR

**获取维护窗口**

```doctl databases maintenance-window get [cluster_id]```

**更新维护窗口**

```doctl databases maintenance-window update [cluster_id] --day [monday] --hour [02:00]```

# SYNOPSIS

**doctl** **databases** **maintenance-window** _command_ [_options_]

# SUBCOMMANDS

**get**
> 获取维护窗口。

**update**
> 更新维护窗口。

# PARAMETERS

**--day** _string_
> 星期几（monday 到 sunday）。

**--hour** _string_
> UTC 时间的小时（00:00 到 23:00）。

# DESCRIPTION

**doctl databases maintenance-window** 管理 DigitalOcean 托管数据库集群的维护窗口。维护工作包括在此窗口内应用的更新和补丁。

DigitalOcean 会对托管数据库执行自动化维护，包括安全补丁、版本更新和系统优化。维护窗口定义了这些操作可以进行的时间，你可以把它们安排在低流量时段，以尽量减少对应用的影响。

可以同时配置维护开始时的星期几和小时（UTC 时区）。结合应用的使用模式规划该窗口，有助于确保维护不会影响峰值流量时段。

# SEE ALSO

[doctl-databases](/man/doctl-databases)(1)

# RESOURCES

```[Source code](https://github.com/digitalocean/doctl)```

```[Documentation](https://docs.digitalocean.com/reference/doctl/reference/databases/)```

<!-- verified: 2026-07-11 -->
