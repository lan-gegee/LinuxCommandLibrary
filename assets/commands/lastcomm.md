# TAGLINE

从进程记账数据中显示之前执行的命令信息

# TLDR

**显示最近的命令**

```lastcomm```

**按用户显示命令**

```lastcomm [username]```

**显示特定命令**

```lastcomm --command [vim]```

**从指定文件显示**

```lastcomm -f [/var/account/pacct]```

**按终端显示命令**

```lastcomm --tty [pts/0]```

# SYNOPSIS

**lastcomm** [_options_] [_user_] [_command_] [_terminal_]

# PARAMETERS

**--command** _name_
> 按命令名称过滤。

**--user** _name_
> 按用户过滤。

**--tty** _name_
> 按终端过滤。

**-f** _file_
> 使用指定的记账文件。

**--forwards**
> 最早的记录优先显示。

**--strict-match**
> 仅限精确匹配。

**--debug**
> 调试输出。

# DESCRIPTION

**lastcomm** 从进程记账数据中显示先前执行的命令信息，包括命令名、标志、用户、终端和执行时间。

必须先启用进程记账，lastcomm 才会有数据。记账文件通常为 /var/account/pacct。

# OUTPUT FLAGS

```
S - Superuser (root) executed
F - Forked but didn't exec
D - Dumped core
X - Killed by signal
```

# ENABLING ACCOUNTING

```bash
# Enable accounting
sudo accton /var/account/pacct

# Disable accounting
sudo accton off
```

# CAVEATS

需要启用进程记账。记账会带来额外的系统开销。文件会持续增长（用 sa 进行轮转）。并非所有系统都提供此功能。

# HISTORY

lastcomm 属于 Unix 进程记账系统的一部分，其历史可追溯到早期 Unix。它提供已执行命令的历史追踪功能，对审计和故障排查很有用。

# INSTALL

```apt: sudo apt install acct```

```apk: sudo apk add acct```

```zypper: sudo zypper install acct```

```nix: nix profile install nixpkgs#acct```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sa](/man/sa)(8), [accton](/man/accton)(8), [last](/man/last)(1), [ac](/man/ac)(1)
