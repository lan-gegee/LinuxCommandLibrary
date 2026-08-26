# TAGLINE

以文件锁的方式运行命令

# TLDR

**持锁运行**

```lckdo [/var/lock/mylock] [command]```

**等待锁**

```lckdo -W [lockfile] [command]```

**被锁定时失败**

```lckdo -n [lockfile] [command]```

**带超时**

```lckdo -w [10] [lockfile] [command]```

# SYNOPSIS

**lckdo** [_options_] _lockfile_ _command_

# PARAMETERS

_LOCKFILE_
> 锁文件路径。

_COMMAND_
> 要执行的命令。

**-n**
> 非阻塞（被锁定时立即失败）。

**-W**
> 无限期等待锁。

**-w** _SECONDS_
> 等待超时时间。

**--help**
> 显示帮助信息。

# DESCRIPTION

**lckdo** 在持有排他文件锁的情况下执行命令，确保同一时刻只有一个该命令实例在运行。这对 cron 作业和计划任务特别有价值，因为重叠执行可能导致数据损坏或资源竞争。

该工具会在运行命令前获取指定锁文件上的排他锁，并在命令完成后释放它。默认情况下它会一直等到锁可用；你也可以用 -n 在锁被占用时立即失败，或用 -w 设置超时。注意 lckdo 已被弃用，建议改用 `flock`，后者提供相同的功能，并且是标准 util-linux 软件包的一部分。

# CAVEATS

已弃用，建议改用 flock。moreutils 的一部分。锁文件必须可写。

# HISTORY

lckdo 曾是 **moreutils** 的一部分，用于在文件锁下运行命令，现已被 flock 取代。

# INSTALL

```apt: sudo apt install moreutils```

```dnf: sudo dnf install moreutils```

```pacman: sudo pacman -S moreutils```

```apk: sudo apk add moreutils```

```zypper: sudo zypper install moreutils```

```brew: brew install moreutils```

```nix: nix profile install nixpkgs#moreutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[flock](/man/flock)(1), [chronic](/man/chronic)(1)
