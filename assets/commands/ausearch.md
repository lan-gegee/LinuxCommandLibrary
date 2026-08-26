# TAGLINE

搜索和查询审计日志事件

# TLDR

搜索 **SELinux AVC** 拒绝事件

```sudo ausearch -m avc```

按**可执行文件**搜索

```sudo ausearch -c httpd```

按**用户**搜索

```sudo ausearch -ui 1000```

搜索**最近**的事件

```sudo ausearch -ts recent```

搜索**失败的登录**

```sudo ausearch -m user_login -sv no```

按**文件**搜索

```sudo ausearch -f path/to/file```

输出**原始**格式

```sudo ausearch -m avc --raw```

# SYNOPSIS

**ausearch** [_OPTIONS_]

# DESCRIPTION

**ausearch** 在 Linux 审计日志中查询事件。它可以按消息类型、用户、进程、文件、时间范围等条件进行搜索，是安全分析和事件调查的必备工具。

# PARAMETERS

**-m, --message** _type_
> 搜索特定消息类型（avc、user_login 等）

**-c, --comm** _name_
> 按命令/可执行文件名搜索

**-ui, --uid** _uid_
> 按用户 ID 搜索

**-f, --file** _path_
> 搜索与特定文件相关的事件

**-ts, --start** _time_
> 搜索的开始时间（recent、today 或时间戳）

**-te, --end** _time_
> 搜索的结束时间

**-sv, --success** _yes|no_
> 按成功或失败过滤

**--raw**
> 以原始格式输出以便进一步处理

**-i, --interpret**
> 解读数值（UID、系统调用等）

**-k, --key** _key_
> 搜索匹配指定审计键的事件

**-p, --pid** _pid_
> 按进程 ID 搜索

**-sc, --syscall** _syscall_
> 按系统调用名称或编号搜索

**-x, --executable** _path_
> 搜索匹配可执行文件路径的事件

**--input-logs**
> 从指定的审计日志文件读取

# CONFIGURATION

**/etc/audit/auditd.conf**
> 审计守护进程的主配置文件，控制日志文件位置和保留策略。

**/etc/audit/audit.rules**
> 定义审计系统记录哪些事件，决定哪些事件可以被搜索到。

# CAVEATS

访问审计日志需要 root 权限。审计守护进程必须正在运行并记录事件。过大的审计日志会拖慢搜索速度；使用时间过滤器缩小结果范围。

# HISTORY

**ausearch** 属于 **audit** 软件包，为 Linux 审计框架提供搜索功能。

# INSTALL

```apt: sudo apt install auditd```

```dnf: sudo dnf install audit```

```pacman: sudo pacman -S audit```

```apk: sudo apk add audit```

```zypper: sudo zypper install audit```

```nix: nix profile install nixpkgs#audit```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aureport](/man/aureport)(8), [auditctl](/man/auditctl)(8), [audit2why](/man/audit2why)(1)
