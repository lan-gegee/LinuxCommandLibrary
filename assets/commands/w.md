# TAGLINE

显示已登录用户及其活动

# TLDR

**显示谁已登录**以及他们正在做什么

```w```

**不显示表头**

```w -h```

**显示指定用户**

```w [username]```

**短格式**（不含登录时间、JCPU、PCPU）

```w -s```

**显示 IP 地址**而不是主机名

```w -i```

# SYNOPSIS

**w** [**-hisf**] [_user_]

# PARAMETERS

**-h**, **--no-header**
> 不打印表头行

**-s**, **--short**
> 短格式；不打印登录时间、JCPU 或 PCPU

**-f**, **--from**
> 切换是否打印 FROM（远程主机）字段

**-i**, **--ip-addr**
> 显示 IP 地址而不是主机名

**-o**, **--old-style**
> 旧式输出（以空格分隔）

**-u**, **--no-current**
> 计算当前进程时间时忽略用户名

# OUTPUT COLUMNS

**USER**：用户名
**TTY**：终端名称
**FROM**：远程主机（本地登录显示 -）
**LOGIN@**：登录时间
**IDLE**：空闲时间
**JCPU**：附加到该 tty 的所有进程占用的时间
**PCPU**：当前进程占用的时间
**WHAT**：当前进程的命令行

# DESCRIPTION

**w** 显示当前已登录用户及其进程的信息。第一行显示当前时间、系统运行时长、用户数量和平均负载（与 **uptime** 的输出相同）。

之后的每一行对应一个已登录用户，显示其终端、登录时间、空闲时间、CPU 使用情况和当前活动。这可以快速概览系统的使用情况和用户活动。

"WHAT" 列显示每个用户当前的前台进程，便于了解大家正在运行什么。

空闲时间显示距用户上一次终端活动过去了多久——有助于识别不活跃的会话。

# CAVEATS

对于本地登录或主机名解析失败的情况，FROM 字段可能为空或显示 "-"。

CPU 时间列（JCPU、PCPU）可能无法准确反映所有活动，尤其是后台进程或使用终端复用器时。

某些进程脱离终端后可能不会出现在 WHAT 中。

# INSTALL

```apt: sudo apt install procps```

```dnf: sudo dnf install procps-ng```

```pacman: sudo pacman -S procps-ng```

```apk: sudo apk add procps-ng```

```zypper: sudo zypper install procps```

```brew: brew install procps```

```nix: nix profile install nixpkgs#procps```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[who](/man/who)(1), [uptime](/man/uptime)(1), [users](/man/users)(1), [last](/man/last)(1), [finger](/man/finger)(1)
