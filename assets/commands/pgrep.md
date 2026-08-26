# TAGLINE

按名称或属性搜索进程并返回其 PID

# TLDR

**按名称查找进程**

```pgrep [nginx]```

**匹配完整命令行查找**

```pgrep -f "[python script.py]"```

**列出进程名和 PID**

```pgrep -l [ssh]```

**按用户查找进程**

```pgrep -u [username] [process]```

**查找最新的匹配进程**

```pgrep -n [chrome]```

**查找最旧的匹配进程**

```pgrep -o [firefox]```

**统计匹配的进程数量**

```pgrep -c [apache]```

**精确名称匹配**

```pgrep -x [bash]```

# SYNOPSIS

**pgrep** [_-flnoxc_] [_-u user_] [_-g group_] [_-P ppid_] [_pattern_]

# PARAMETERS

**-l**, **--list-name**
> 列出 PID 和进程名。

**-a**, **--list-full**
> 列出 PID 和完整命令行。

**-f**, **--full**
> 匹配完整命令行。

**-x**, **--exact**
> 精确匹配（而非子串匹配）。

**-n**, **--newest**
> 选择最新（最近）的匹配。

**-o**, **--oldest**
> 选择最旧（最早）的匹配。

**-c**, **--count**
> 统计匹配数量而不是列出。

**-d** _DELIM_, **--delimiter** _DELIM_
> 输出分隔符（默认：换行符）。

**-u** _USER_, **--euid** _USER_
> 匹配有效用户 ID。

**-U** _USER_, **--uid** _USER_
> 匹配真实用户 ID。

**-g** _GROUP_, **--pgroup** _GROUP_
> 匹配进程组。

**-G** _GROUP_, **--group** _GROUP_
> 匹配真实组 ID。

**-P** _PPID_, **--parent** _PPID_
> 匹配父进程 ID。

**-t** _TERM_, **--terminal** _TERM_
> 匹配控制终端。

**-v**, **--inverse**
> 反选（取反）匹配。

**-i**, **--ignore-case**
> 不区分大小写匹配。

# DESCRIPTION

**pgrep** 按名称或属性搜索进程并返回其 PID。相比将 ps 通过管道传给 grep，它是更专注的替代方案。

模式默认针对进程名（可执行文件名）匹配。-f 标志将匹配范围扩展到包含参数的完整命令行。支持正则表达式。

选择过滤器可以按用户、组、终端或父进程收窄结果，并可组合使用以实现精确定位。-v 标志反转选择，找出不匹配的进程。

-newest（-n）和 -oldest（-o）选项只返回单个匹配，在存在多个实例时很有用。计数模式（-c）报告匹配的进程数量而不逐一列出。

输出格式选项控制分隔符和详细程度，便于与 shell 脚本及其他工具集成。

# CAVEATS

默认是子串匹配——"sh" 会匹配 bash、fish、zsh。需要精确匹配请使用 -x。进程名可能被截断。僵尸进程仍可能被匹配到。模式是正则表达式。pgrep 找不到它自己。

# HISTORY

**pgrep** 最初随 **Solaris 7**（1998 年）推出，后作为 **procps** 的一部分移植到 Linux。它比传统的 `ps aux | grep pattern` 方式提供更干净的接口，避免了常见的"grep 匹配到自己"的问题。该工具是大多数 Linux 系统上 procps-ng 软件包的一部分。

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

[pkill](/man/pkill)(1), [ps](/man/ps)(1), [pidof](/man/pidof)(1), [kill](/man/kill)(1)
