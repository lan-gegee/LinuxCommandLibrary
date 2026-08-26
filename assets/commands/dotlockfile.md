# TAGLINE

邮箱风格的文件锁定工具

# TLDR

**创建锁文件**

```dotlockfile [file.lock]```

**带重试地创建**

```dotlockfile -r [5] [file.lock]```

**移除锁文件**

```dotlockfile -u [file.lock]```

**加锁并检查 PID**

```dotlockfile -p [file.lock]```

**尝试加锁一次**（不等待）

```dotlockfile -r [0] [file.lock]```

**以秒为单位设置超时**加锁

```dotlockfile -r [10] -l [file.lock]```

# SYNOPSIS

**dotlockfile** [_options_] _lockfile_

# PARAMETERS

_LOCKFILE_
> 要创建/移除的锁文件路径。

**-r** _RETRIES_
> 重试次数（0 = 只试一次，-1 = 无限重试）。

**-u**, **--unlock**
> 移除锁文件。

**-p**, **--use-pid**
> 将 PID 写入锁文件。

**-l**
> 加锁（默认动作）。

**-c**, **--check**
> 检查锁是否已失效。

**--help**
> 显示帮助信息。

# DESCRIPTION

**dotlockfile** 按照邮箱锁定惯例（name.lock）创建锁文件。它为需要串行化资源访问的脚本和应用程序提供原子化的文件锁定。

该工具处理重试逻辑、失效锁检测和 PID 跟踪。配合 -p 使用时，它会将进程 ID 写入锁文件，从而能够检测持锁进程是否已经死亡。

dotlockfile 常用于 shell 脚本中，防止对文件的并发访问，或确保同一脚本一次只运行一个实例。

# CAVEATS

网络文件系统上的锁文件可能不可靠。必须在脚本退出时手动移除锁。失效锁检测需要 -p 选项。不适合高竞争场景。

# HISTORY

dotlockfile 实现了传统的 Unix 锁文件惯例，这种惯例曾被广泛用于邮箱锁定。它是 **liblockfile** 软件包的一部分，该包提供了标准化的文件锁定工具。

# INSTALL

```apt: sudo apt install liblockfile-bin```

```dnf: sudo dnf install liblockfile```

```pacman: sudo pacman -S liblockfile```

```apk: sudo apk add liblockfile```

```brew: brew install liblockfile```

```nix: nix profile install nixpkgs#liblockfile```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[flock](/man/flock)(1)
