# TAGLINE

控制和管理 Linux 审计系统的规则。

# TLDR

显示**状态**

```sudo auditctl -s```

**列出**所有规则

```sudo auditctl -l```

**删除**所有规则

```sudo auditctl -D```

**启用/禁用**审计

```sudo auditctl -e 1```

**监视**文件的更改

```sudo auditctl -a always,exit -F arch=b64 -F path=/path/to/file -F perm=wa```

递归监视**目录**

```sudo auditctl -a always,exit -F arch=b64 -F dir=/path/to/dir/ -F perm=wa```

用过滤**键**监视文件以便于搜索

```sudo auditctl -w /etc/passwd -p wa -k passwd_changes```

**删除**特定规则

```sudo auditctl -W /etc/passwd```

# SYNOPSIS

**auditctl** [_OPTIONS_]

# DESCRIPTION

**auditctl** 控制 Linux 审计系统的行为并管理其规则。它可以启用或禁用审计、添加或删除审计规则，以及显示当前的审计状态和配置。

规则可以监视对特定文件和目录的访问、按进程属性跟踪系统调用，以及按用户、组或架构过滤事件。该工具直接与内核审计子系统通信以立即应用规则，但这些运行时规则在重启后会丢失，除非将其持久化到审计规则文件中。

# PARAMETERS

**-s**
> 显示审计系统状态

**-l**
> 列出当前已加载的所有审计规则

**-D**
> 删除所有审计规则

**-b** _backlog_
> 设置待处理审计缓冲区的最大数量（内核默认：64）

**-e** _0|1|2_
> 禁用（0）、启用（1）或锁定（2）审计配置。锁定后的配置必须重启才能更改。

**-f** _0|1|2_
> 设置失败模式：0=静默，1=printk，2=panic

**-r** _rate_
> 设置消息速率限制（条/秒）（0=不限制）

**-a** _list,action_
> 将一条规则追加到列表末尾（如 always,exit）

**-d** _list,action_
> 从指定列表删除匹配的规则

**-w** _path_
> 对文件或目录设置监视以观察更改

**-W** _path_
> 移除对文件或目录的监视

**-F** _field=value_
> 添加字段比较条件（path、perm、arch、uid、pid 等）

**-S** _syscall_
> 指定要审计的系统调用名称或编号（与 -a 一起使用）

**-k** _key_
> 为审计规则设置过滤键，便于搜索日志

**-p** _permissions_
> 权限过滤器（r=读，w=写，x=执行，a=属性变更）

**-R** _file_
> 从文件中读取并执行 auditctl 命令

# CONFIGURATION

**/etc/audit/audit.rules**
> 由 auditd 在启动时加载的持久化审计规则。用 auditctl 添加的规则若未保存到这里，重启后即丢失。

# CAVEATS

需要 root 权限。用 auditctl 添加的规则在重启后不会保留；如需持久化请写入 /etc/audit/audit.rules。过度的审计会影响系统性能。

# HISTORY

**auditctl** 是 **audit** 软件包的一部分，为安全监控和合规性提供 Linux 审计框架。

# INSTALL

```apt: sudo apt install auditd```

```dnf: sudo dnf install audit```

```pacman: sudo pacman -S audit```

```apk: sudo apk add audit```

```zypper: sudo zypper install audit```

```nix: nix profile install nixpkgs#audit```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[ausearch](/man/ausearch)(8), [aureport](/man/aureport)(8), [auditd](/man/auditd)(8)
