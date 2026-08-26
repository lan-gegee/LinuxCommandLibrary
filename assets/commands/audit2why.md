# TAGLINE

将 SELinux 拒绝消息转换为人类可读的解释。

# TLDR

解释**最近**的 SELinux 拒绝事件

```sudo audit2why```

解释**指定审计日志**文件中的 SELinux 拒绝

```sudo audit2why -i [path/to/audit.log]```

解释审计日志中的**所有 SELinux 拒绝**

```sudo ausearch -m avc | audit2why```

解释**特定服务**的拒绝

```sudo ausearch -m avc -c [service_name] | audit2why```

# SYNOPSIS

**audit2why** [_options_] < _input_

# DESCRIPTION

**audit2why** 将来自审计日志的 SELinux 拒绝消息转换为人类可读的解释。它会找出每次拒绝的原因，并常常给出解决方案，例如切换布尔值、创建策略模块或修正文件上下文。

该工具从标准输入或指定文件读取审计事件。它通常与 **ausearch** 配合使用，以过滤和分析特定类型的拒绝。

# PARAMETERS

**-a**, **--all**
> 同时从审计日志和系统消息日志读取输入。

**-b**, **--boot**
> 读取自上次启动以来的审计消息作为输入。

**-d**, **--dmesg**
> 从 _dmesg_(1) 的输出读取输入。

**-i** _file_, **--input** _file_
> 从指定文件而非 stdin 读取审计事件。

**-l**, **--lastreload**
> 只读取上次策略重载之后生成的审计事件。

**-p** _file_, **--policy** _file_
> 使用给定的策略文件而非当前生效的策略进行分析。

**-w**, **--why**
> 显示每次拒绝的原因（audit2why 的默认行为）。

**-v**, **--verbose**
> 启用详细输出。

# CAVEATS

读取审计日志需要 root 权限。该工具只负责解释拒绝，不会自动修复。启用建议的布尔值之前应仔细审查，因为它们可能带来安全影响。属于 **policycoreutils-python-utils** 软件包的一部分。

# SEE ALSO

[audit2allow](/man/audit2allow)(1), [ausearch](/man/ausearch)(8), [sealert](/man/sealert)(8), [semanage](/man/semanage)(8)
