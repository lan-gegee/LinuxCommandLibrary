# TAGLINE

重新加载配置或重启单元

# TLDR

**重新加载或重启**单元

```systemctl reload-or-restart [unit]```

用**模式匹配**重新加载或重启

```systemctl reload-or-restart [pattern]```

**异步**执行（不等待）

```systemctl reload-or-restart [unit] --no-block```

针对**用户**单元

```systemctl reload-or-restart [unit] --user```

# SYNOPSIS

**systemctl reload-or-restart** [_OPTIONS_] _PATTERN_...

# PARAMETERS

**--no-block**
> 立即返回而不等待

**--user**
> 操作用户单元

# DESCRIPTION

**systemctl reload-or-restart** 在一个或多个单元支持重载时重新加载它们；如果不支持，则改为停止后再次启动。如果这些单元尚未运行，则会被启动。

当你不确定某个服务是否支持热重载时，这个命令可以用来应用配置更改。如果单元定义了 `ExecReload=`，则在不中断服务的情况下重新加载配置；否则该单元会被停止并再次启动。

# CAVEATS

只有单元定义了 ExecReload 时重载才会生效。重启会造成短暂的服务中断。对于不支持重载的单元，此命令总是会重启它们。

# HISTORY

**reload-or-restart** 子命令提供了一种应用配置更改的安全方式，无需事先了解服务是否支持热重载。

# SEE ALSO

[systemctl-reload](/man/systemctl-reload)(1), [systemctl-restart](/man/systemctl-restart)(1), [systemctl-try-reload-or-restart](/man/systemctl-try-reload-or-restart)(1)
