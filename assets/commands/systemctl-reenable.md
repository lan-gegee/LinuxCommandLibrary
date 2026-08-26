# TAGLINE

先禁用再重新启用单元

# TLDR

**重新启用**单元

```systemctl reenable [unit]```

重新启用**多个**单元

```systemctl reenable [unit1 unit2 ...]```

重新启用并立即**启动**

```systemctl reenable [unit] --now```

# SYNOPSIS

**systemctl reenable** [_OPTIONS_] _UNIT_...

# PARAMETERS

**--now**
> 重新启用后同时启动该单元

**--user**
> 操作用户单元

# DESCRIPTION

**systemctl reenable** 相当于先执行 `disable` 再执行 `enable`。它会移除该单元现有的所有符号链接，并根据单元文件中当前的 [Install] 区段重新创建它们。

当单元的 [Install] 区段发生变化时（例如它应被启用的 target 改变了），此命令非常有用，因为单独执行 `enable` 不会更新已存在的符号链接。

# CAVEATS

与 `enable` 不同，即使单元已经处于启用状态，此命令也总会重新创建符号链接。适用于更改服务所属 target 的场景。

# HISTORY

**reenable** 子命令在单元安装目标发生变化时提供一条命令即可更新启用配置的方式，省去了手动 disable/enable 的组合操作。

# SEE ALSO

[systemctl-enable](/man/systemctl-enable)(1), [systemctl-disable](/man/systemctl-disable)(1), [systemctl](/man/systemctl)(1)
