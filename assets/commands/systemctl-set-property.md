# TAGLINE

在运行时修改单元属性

# TLDR

**设置**单元属性

```systemctl set-property [unit] [property]=[value]```

设置**多个**属性

```systemctl set-property [unit] [prop1=val1 prop2=val2 ...]```

仅对**本次运行**生效

```systemctl set-property [unit] [property]=[value] --runtime```

**重置**为默认值

```systemctl set-property [unit] [property]=```

# SYNOPSIS

**systemctl set-property** _UNIT_ _PROPERTY=VALUE_...

# PARAMETERS

**--runtime**
> 更改仅为临时性（重启后清除）

# DESCRIPTION

**systemctl set-property** 在运行时修改单元属性。默认情况下，更改会持久保存，存储在 `/etc/systemd/system/<unit>.d/` 下的 drop-in 文件中。

常见属性包括 CPUQuota、MemoryMax、IOWeight 等资源控制设置。

# COMMON PROPERTIES

**CPUQuota=** - CPU 时间限制（如 50%）

**MemoryMax=** - 内存限制

**IOWeight=** - I/O 优先级

**TasksMax=** - 最大任务数

# CAVEATS

某些属性无法在运行时更改。持久化更改会以 drop-in 文件形式存储。使用 `systemctl revert` 可以移除自定义属性。

# HISTORY

**set-property** 子命令支持在运行时调整资源控制，无需重启服务即可进行动态系统调优。

# SEE ALSO

[systemctl-show](/man/systemctl-show)(1), [systemctl-revert](/man/systemctl-revert)(1)
