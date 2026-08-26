# TAGLINE

添加 systemd unit 的硬依赖

# TLDR

向 target 添加 **Requires** 依赖

```systemctl add-requires [target] [unit]```

添加**多个**依赖

```systemctl add-requires [target] [unit1 unit2 ...]```

添加**用户级**依赖

```systemctl add-requires [target] [unit] --user```

# SYNOPSIS

**systemctl add-requires** _TARGET_ _UNIT_...

# PARAMETERS

**--system**
> 操作系统级配置（默认）

**--user**
> 操作用户级配置

**--runtime**
> 做出临时更改，重启前有效

**--global**
> 对所有用户登录全局生效

# DESCRIPTION

**systemctl add-requires** 为一个或多个 unit 向指定的 systemd target 追加 `Requires=` 依赖。`Requires=` 关系建立的是硬依赖：如果所列的任何 unit 启动失败，该 target 自身也将无法激活。

该命令提供了一种程序化方式来建立 unit 依赖，无需手动编辑 unit 文件或在 `.requires/` 目录中创建符号链接。

# CAVEATS

不带 --runtime 所做的更改是持久的，重启后依然生效。硬依赖（Requires）可能在某个 unit 无法启动时引发连锁失败。如果失败不应传播，请考虑使用较软的 add-wants 依赖。

# HISTORY

**add-requires** 子命令于 systemd 版本 **217** 加入 **systemctl**。Systemd 由 **Lennart Poettering** 和 **Kay Sievers** 在 Red Hat 创建，自 **2015 年**起成为多数主流 Linux 发行版的默认 init 系统。

# SEE ALSO

[systemctl](/man/systemctl)(1), [systemctl-add-wants](/man/systemctl-add-wants)(1)
