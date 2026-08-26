# TAGLINE

分析并解释 SELinux 拒绝消息

# TLDR

**分析**所有最近的 SELinux 拒绝事件

```sudo sealert -a /var/log/audit/audit.log```

**查询**特定的警报 ID

```sudo sealert -l alert_id```

显示最近警报的**摘要**

```sudo sealert -b```

以 HTML 格式显示**所有警报**

```sudo sealert -a /var/log/audit/audit.log -H```

# SYNOPSIS

**sealert** [_options_]

# PARAMETERS

**-a**, **--analyze** _file_
> 扫描审计日志文件中的 AVC，进行分析并将警报写入 stdout。

**-l**, **--lookupid** _id_
> 按 ID 查询特定警报并写入 stdout。使用 `*` 可返回所有警报。

**-b**, **--browser**
> 启动警报浏览器图形界面。

**-f**, **--fix** _uuid_
> 对具有给定 UUID 的 AVC 执行修复命令。需要配合 **--plugin**。

**-P**, **--plugin** _plugin_
> 指定与 **--fix** 配合使用的插件名称。

**-H**
> 以 HTML 格式而非纯文本输出警报（配合 **-l** 或 **-a** 使用）。

**-s**, **--service**
> 启动 sealert D-Bus 服务（通常由 D-Bus 调用）。

**-S**, **--noservice**
> 以独立应用程序方式启动 sealert，不使用 D-Bus 服务。

**-u**, **--user** _user_
> 以指定用户身份登录。

**-p**, **--password** _password_
> 设置用户密码。

# DESCRIPTION

**sealert** 分析并解释 SELinux 的 AVC（Access Vector Cache）拒绝消息。它以人类可读的方式解释访问为何被拒绝，并给出解决方案建议。

作为 setroubleshoot 的一部分，它帮助管理员理解并解决 SELinux 策略违规问题。

# CAVEATS

需要启用 SELinux 审计日志。解决方案仅为建议，应用前应先审查。

# HISTORY

属于 **setroubleshoot-server** 软件包，提供友好的 SELinux 故障排查功能。

# SEE ALSO

[audit2why](/man/audit2why)(1), [audit2allow](/man/audit2allow)(1), [ausearch](/man/ausearch)(8)
