# TAGLINE

显示系统上已知用户和组的信息

# TLDR

**显示所有用户**（默认视图）

```lslogins```

**只显示用户账户**（非系统账户）

```lslogins --user-accs```

**只显示系统账户**

```lslogins --system-accs```

**显示特定用户的详情**

```lslogins [username]```

**列出特定组的成员**

```lslogins --groups [group1,group2]```

**显示最近登录信息**

```lslogins --last```

**显示失败的登录尝试**

```lslogins --failed```

**显示附加组的组成员身份**

```lslogins --supp-groups```

**选择特定列**

```lslogins -o [USER,UID,GID,HOMEDIR,SHELL]```

# SYNOPSIS

**lslogins** [_options_] [_username_...]

# DESCRIPTION

**lslogins** 显示 Linux 系统上已知用户和组的信息，整合了 `/etc/passwd`、`/etc/shadow`、`/etc/group`、`lastlog`、`faillog` 和 wtmp 中的数据。相比手动拼合 `who`、`last`、`id`、`getent` 的输出，它是一个更全面的替代方案。

默认以表格形式打印，每个用户一行。可用 `-o`、`--raw`、`--json`、`--colon-separate` 和 `--export` 调整输出的列和格式，便于脚本处理。

# PARAMETERS

**-a**, **--acc-expiration**
> 显示上次密码修改时间以及账户/密码过期日期。

**-c**, **--colon-separate**
> 用冒号而非换行分隔用户记录。

**-e**, **--export**
> 以 `NAME="value"` 的可被 Shell source 的形式输出。

**-f**, **--failed**
> 包含每个用户上次失败登录的数据。

**-G**, **--supp-groups**
> 显示附加组。

**-g**, **--groups** _GROUPS_
> 只显示属于所列组之一的用户（逗号分隔）。

**-L**, **--last**
> 显示来自 `lastlog` 的最近登录信息。

**-l**, **--logins** _LOGINS_
> 只显示登录名或 UID 位于逗号分隔列表中的用户。

**-n**, **--newline**
> 每个字段单独占一行打印。

**--noheadings**
> 不显示列标题。

**--notruncate**
> 不截断较长的输出列。

**-o**, **--output** _LIST_
> 要显示的列的逗号分隔列表。用 `--help` 可查看完整列清单。

**--output-all**
> 打印所有可用列。

**-p**, **--pwd**
> 显示密码状态信息。

**-r**, **--raw**
> 原始无格式输出。

**-s**, **--system-accs**
> 只显示系统账户（低于配置阈值的 UID）。

**-u**, **--user-accs**
> 只显示非系统的用户账户。

**-J**, **--json**
> 以 JSON 输出。

**-Z**, **--context**
> 显示 SELinux 用户上下文。

**--time-format** _TYPE_
> 日期列采用 `short`、`full` 或 `iso` 格式。

**-V**, **--version**
> 打印版本信息。

**-h**, **--help**
> 显示帮助和支持的列清单。

# CAVEATS

某些列（上次登录、失败登录、密码过期）要求调用用户对 `/var/log/lastlog`、`/var/log/faillog` 或 `/etc/shadow` 有读取权限——通常是 root。不附带 `lastlog`/`faillog` 的发行版会在这些列中显示空值。

# HISTORY

**lslogins** 被加入 **util-linux**（上游作者为 **Ondrej Oprala**），用于整合此前分散在 `who`、`last`、`lastlog`、`faillog` 和 `getent passwd` 中的信息。

# INSTALL

```apt: sudo apt install util-linux```

```dnf: sudo dnf install util-linux```

```pacman: sudo pacman -S util-linux```

```apk: sudo apk add util-linux-login```

```zypper: sudo zypper install util-linux```

```brew: brew install util-linux```

```nix: nix profile install nixpkgs#util-linux```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[who](/man/who)(1), [last](/man/last)(1), [id](/man/id)(1), [getent](/man/getent)(1), [passwd](/man/passwd)(1)
