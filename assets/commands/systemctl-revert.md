# TAGLINE

将单元恢复为厂商默认值

# TLDR

将单元**还原**为厂商默认值

```systemctl revert [unit1 unit2 ...]```

还原一个**用户**单元

```systemctl revert [unit] --user```

# SYNOPSIS

**systemctl revert** _UNIT_...

# PARAMETERS

**--user**
> 操作用户单元

# DESCRIPTION

**systemctl revert** 通过移除所有本地自定义来将单元文件恢复为其原始的厂商版本。这会撤销 `edit`、`enable`、`disable`、`set-property` 和 `mask` 命令产生的效果。

它会移除 `/etc/systemd/system/<unit>.d/` 中的 drop-in 文件；如果单元文件是本地副本则将其移除；同时删除由 enable/disable/mask 创建的符号链接。

# CAVEATS

会不可逆地移除所有本地自定义。没有备份就无法找回被删除的自定义内容。在生产系统上请谨慎使用。

# HISTORY

**revert** 子命令提供了一种干净的方式将单元配置重置为发行版默认值，在排查问题或不再需要自定义时很有用。

# SEE ALSO

[systemctl-edit](/man/systemctl-edit)(1), [systemctl-mask](/man/systemctl-mask)(1), [systemctl](/man/systemctl)(1)
