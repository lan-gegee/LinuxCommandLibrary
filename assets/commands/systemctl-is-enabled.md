# TAGLINE

检查单元的开机启用状态

# TLDR

检查**启用**状态

```systemctl is-enabled [unit]```

检查**多个**单元

```systemctl is-enabled [unit1 unit2 ...]```

**安静**模式（仅返回退出码）

```systemctl is-enabled [unit] -q```

显示**目标**和符号链接

```systemctl is-enabled [unit] -l```

# SYNOPSIS

**systemctl is-enabled** [_OPTIONS_] _UNIT_...

# PARAMETERS

**-q, --quiet**
> 不输出内容，仅返回退出码

**-l, --full**
> 不截断输出；同时在输出中显示安装目标

**--system**
> 检查系统单元（默认）

**--user**
> 检查用户单元

# DESCRIPTION

**systemctl is-enabled** 检查单元文件是否被设置为开机启动。它返回启用状态：enabled、disabled、static、masked、generated、transient、indirect 或 alias。

退出码 0 表示该单元已被启用，或会通过其他方式在开机时启动。

# ENABLEMENT STATES

**enabled** - 开机时启动

**disabled** - 开机时不启动

**static** - 没有 install 区段，只能作为依赖被启动

**masked** - 完全禁止启动

**indirect** - 通过另一个单元间接启用

**generated** - 由生成器工具动态生成

**alias** - 名称是另一个单元的别名

# CAVEATS

"已启用"表示已配置为启动，而不是当前正在运行。请使用 `is-active` 检查运行时状态。static 单元没有 [Install] 区段，只能作为依赖被启动。

# SEE ALSO

[systemctl](/man/systemctl)(1), [systemctl-is-active](/man/systemctl-is-active)(1), [systemctl-enable](/man/systemctl-enable)(1), [systemctl-disable](/man/systemctl-disable)(1), [systemctl-status](/man/systemctl-status)(1)
