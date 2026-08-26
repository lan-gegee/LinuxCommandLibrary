# TAGLINE

检查单元是否失败

# TLDR

检查是否有**任何失败的**单元

```systemctl is-failed```

检查**特定单元**是否失败

```systemctl is-failed unit_name```

检查**多个单元**

```systemctl is-failed unit1 unit2```

**安静**模式（仅返回退出码）

```systemctl is-failed -q unit_name```

检查**用户**单元

```systemctl is-failed --user unit_name```

# SYNOPSIS

**systemctl is-failed** [_OPTIONS_] [_PATTERN_...]

# DESCRIPTION

**systemctl is-failed** 检查一个或多个 systemd 单元是否失败。只要任一指定单元处于失败状态就返回退出码 0，适用于脚本编写和监控。

# PARAMETERS

**PATTERN**
> 要检查的单元名称或模式（省略时检查所有单元）

**-q, --quiet**
> 不输出内容，仅返回退出码

**--user**
> 检查用户单元而不是系统单元

# CAVEATS

退出码 0 表示至少有一个单元失败；非零表示没有失败或未找到单元。不带参数时会检查所有单元，只要其中有失败的就返回 0。

# HISTORY

**systemctl is-failed** 是 **systemd** 的一部分，为脚本编写和自动化提供状态检查命令。

# SEE ALSO

[systemctl](/man/systemctl)(1), [systemctl-is-active](/man/systemctl-is-active)(1), [systemctl-status](/man/systemctl-status)(1)
