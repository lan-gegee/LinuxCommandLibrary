# TAGLINE

显示已登录的用户

# TLDR

**显示谁已登录**

```who```

**仅显示当前用户**

```who am i```

**显示列标题**

```who -H```

**显示登录时间和空闲时间**

```who -u```

**显示所有可用信息**

```who -a```

**统计已登录用户数**

```who -q```

**显示系统启动时间**

```who -b```

# SYNOPSIS

**who** [_options_] [_file_] [**am i**]

# PARAMETERS

**-a**, **--all**
> 打印所有可用信息

**-b**, **--boot**
> 上次系统启动的时间

**-d**, **--dead**
> 打印已死亡的进程

**-H**, **--heading**
> 打印列标题

**-l**, **--login**
> 打印系统登录进程

**-q**, **--count**
> 仅显示用户名和已登录用户数

**-r**, **--runlevel**
> 打印当前运行级别

**-p**, **--process**
> 打印由 init 派生的活动进程

**-s**, **--short**
> 仅打印名称、终端行和时间（默认）

**-t**, **--time**
> 打印上次系统时钟变更

**-T**, **-w**, **--mesg**
> 添加用户的消息状态（+、-、?）

**-u**, **--users**
> 列出已登录用户

**--lookup**
> 尝试通过 DNS 规范化主机名

**am i**
> 仅打印当前终端的用户信息

# DESCRIPTION

**who** 显示当前登录到系统的用户信息。它从跟踪登录会话的 **/var/run/utmp**（或其他指定文件）中读取数据。

基本输出包括用户名、终端行和登录时间。其他选项可显示空闲时间、进程 ID 和消息状态（即用户是否接受 write/talk 消息）。

**who am i** 显示最初登录会话的信息。与 **whoami**（显示有效用户）不同，即使已经用 **su** 切换到其他账户，**who am i** 显示的仍是最初登录的用户。

该命令可以从 **/var/log/wtmp** 读取历史登录数据，以显示过去的登录记录。

# CAVEATS

who 显示的是登录会话，而非所有用户进程。用户可能在没有活动登录会话的情况下运行进程。

远程连接可能显示为伪终端（pts/N）而非物理终端（tty）。

utmp 文件格式在不同 Unix 系统之间存在差异。某些信息可能在部分平台上不可用。

# INSTALL

```apt: sudo apt install coreutils```

```dnf: sudo dnf install coreutils```

```pacman: sudo pacman -S coreutils```

```apk: sudo apk add coreutils```

```zypper: sudo zypper install coreutils```

```brew: brew install coreutils```

```nix: nix profile install nixpkgs#coreutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[w](/man/w)(1), [whoami](/man/whoami)(1), [users](/man/users)(1), [last](/man/last)(1), [finger](/man/finger)(1)
