# TAGLINE

以树状显示正在运行的进程

# TLDR

显示**所有进程的树状结构**

```pstree```

显示带有 **PID** 的树

```pstree -p```

显示**特定用户**拥有的进程

```pstree username```

显示**命令行参数**

```pstree -a```

显示特定进程的**子进程**

```pstree 1234```

显示特定进程的**父进程**

```pstree -s 1234```

**高亮**当前进程及其祖先

```pstree -h```

# SYNOPSIS

**pstree** [_-a_] [_-c_] [_-h_] [_-p_] [_-s_] [_-u_] [_pid_|_user_]

# DESCRIPTION

**pstree** 以树状结构显示正在运行的进程。若省略 pid，树根为 init 或指定的 pid。它用方括号和计数直观地合并相同的分支，并用花括号在父进程下方显示子线程。

# PARAMETERS

**-a, --arguments**
> 显示命令行参数

**-c, --compact-not**
> 禁用相同子树的合并

**-C, --color**
> 按属性（如 age）为进程名着色

**-g, --show-pgids**
> 显示进程组 ID

**-h, --highlight-all**
> 高亮当前进程及其祖先

**-H pid, --highlight-pid**
> 高亮指定进程及其祖先

**-l, --long**
> 显示完整长度的行，不截断

**-n, --numeric-sort**
> 按 PID 而非名称排序进程

**-N, --ns-sort**
> 按命名空间类型分别显示各自的树

**-p, --show-pids**
> 显示进程 ID

**-s, --show-parents**
> 显示指定进程的父进程

**-t, --thread-names**
> 显示完整的线程名称

**-T, --hide-threads**
> 隐藏线程；只显示进程

**-u, --uid-changes**
> 显示 uid 变化

**-Z, --security-context**
> 显示 SELinux 安全上下文

**-A**
> 使用 ASCII 制表符绘制线条

**-G**
> 使用 VT100 制表符绘制线条

**-U**
> 使用 UTF-8 制表符绘制线条

# CAVEATS

某些显示的值（如命令参数）读取自 /proc，可能已被进程修改。子线程显示在花括号 {} 中，重复的相同分支显示在方括号 [] 中并附带重复次数。

# HISTORY

**pstree** 是 **psmisc** 软件包的一部分。它提供进程的层级视图，补充了 ps 的平面列表形式。

# INSTALL

```apt: sudo apt install psmisc```

```dnf: sudo dnf install psmisc```

```pacman: sudo pacman -S psmisc```

```apk: sudo apk add psmisc```

```zypper: sudo zypper install psmisc```

```brew: brew install pstree```

```nix: nix profile install nixpkgs#psmisc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ps](/man/ps)(1), [top](/man/top)(1), [htop](/man/htop)(1), [proc](/man/proc)(5)
