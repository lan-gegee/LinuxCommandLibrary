# TAGLINE

将单元启用状态重置为默认值

# TLDR

重置为**预设**默认值

```systemctl preset [unit1 unit2 ...]```

仅**启用**模式

```systemctl preset [unit] --preset-mode enable-only```

仅**禁用**模式

```systemctl preset [unit] --preset-mode disable-only```

**安静**模式

```systemctl preset [unit] -q```

# SYNOPSIS

**systemctl preset** [_OPTIONS_] _UNIT_...

# PARAMETERS

**--preset-mode=** _MODE_
> full（默认）、enable-only 或 disable-only

**-q, --quiet**
> 不输出内容，仅返回退出码

**--user**
> 操作用户单元

# DESCRIPTION

**systemctl preset** 将指定单元文件的启用状态重置为预设策略文件中定义的默认值。`/usr/lib/systemd/system-preset/` 和 `/etc/systemd/system-preset/` 中的预设文件定义了哪些单元默认应被启用或禁用。

通常在安装软件包后使用，以根据发行版策略设置初始启用状态。

# CAVEATS

预设策略因发行版而异。对单元执行 preset 可能改变它是否开机启动。可使用 `--preset-mode` 将更改限制为只启用或只禁用。

# HISTORY

**preset** 子命令实现了基于策略的启用机制，允许发行版定义默认服务状态，同时让管理员可以覆盖这些设置。

# SEE ALSO

[systemctl-preset-all](/man/systemctl-preset-all)(1), [systemctl-enable](/man/systemctl-enable)(1)
