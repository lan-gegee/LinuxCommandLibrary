# TAGLINE

添加 systemd unit 的软依赖

# TLDR

向 target 添加 **Wants** 依赖

```systemctl add-wants [target] [unit]```

添加**多个**依赖

```systemctl add-wants [target] [unit1 unit2 ...]```

添加**用户级**依赖

```systemctl add-wants [target] [unit] --user```

# SYNOPSIS

**systemctl add-wants** _TARGET_ _UNIT_...

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

**systemctl add-wants** 为一个或多个 unit 向指定的 systemd target 追加 `Wants=` 依赖。`Wants=` 关系建立的是软依赖：target 会尝试启动所列的 unit，但如果它们无法激活也不会失败。

该命令提供了一种程序化方式来建立 unit 依赖，无需手动编辑 unit 文件或在 `.wants/` 目录中创建符号链接。它常用于在特定引导 target 下启用服务。

# CAVEATS

不带 --runtime 所做的更改是持久的，重启后依然生效。Wants 依赖弱于 Requires；unit 启动失败不会影响 target。对于失败需要传播的关键依赖，请改用 add-requires。

# HISTORY

**add-wants** 子命令于 systemd 版本 **217** 加入 **systemctl**。Systemd 由 **Lennart Poettering** 和 **Kay Sievers** 在 Red Hat 创建，自 **2015 年**起成为多数主流 Linux 发行版的默认 init 系统。

# SEE ALSO

[systemctl](/man/systemctl)(1), [systemctl-add-requires](/man/systemctl-add-requires)(1)
