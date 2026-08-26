# TAGLINE

列出本地系统持有的所有文件锁信息

# TLDR

列出**所有锁**

```lslocks```

以**指定列**列出

```lslocks -o PID,COMMAND,PATH```

不带表头的**原始**输出

```lslocks --raw --noheadings```

列出**特定 PID** 的锁

```lslocks --pid [pid]```

以 **JSON** 输出

```lslocks --json```

# SYNOPSIS

**lslocks** [_options_]

# DESCRIPTION

**lslocks** 列出本地系统持有的所有文件锁信息，显示建议锁和强制锁、持有进程以及锁的细节。

# PARAMETERS

**-o, --output COLUMNS**
> 指定输出的列

**-p, --pid PID**
> 显示特定进程的锁

**-J, --json**
> JSON 输出格式

**-r, --raw**
> 原始输出，无格式化

**-n, --noheadings**
> 不显示列标题

**-u, --notruncate**
> 不截断输出

# OUTPUT COLUMNS

**COMMAND**: 进程名
**PID**: 进程 ID
**TYPE**: 锁类型（FLOCK、POSIX、LEASE）
**SIZE**: 被锁定区域的大小
**PATH**: 被锁定的文件路径

# INSTALL

```apt: sudo apt install util-linux```

```dnf: sudo dnf install util-linux```

```pacman: sudo pacman -S util-linux```

```apk: sudo apk add util-linux-misc```

```zypper: sudo zypper install util-linux```

```brew: brew install util-linux```

```nix: nix profile install nixpkgs#util-linux```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[flock](/man/flock)(1), [lsof](/man/lsof)(8)
