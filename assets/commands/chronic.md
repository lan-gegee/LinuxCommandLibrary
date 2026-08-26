# TAGLINE

除非命令失败，否则静默其输出

# TLDR

**除非失败，否则静默运行命令**

```chronic [command]```

**详细模式，区分 stderr/stdout**

```chronic -v [command]```

**以 stderr 输出作为触发条件**

```chronic -e [command]```

**详细模式并以 stderr 触发**

```chronic -ve [command]```

**在 cron 任务中代替重定向到 /dev/null**

```0 1 * * * chronic backup```

**运行备份脚本，仅在失败或产生 stderr 时显示输出**

```chronic -ve /usr/local/bin/backup.sh```

# SYNOPSIS

**chronic** [-ev] _command_ ...

# DESCRIPTION

**chronic** 静默运行一个命令，仅当该命令失败（非零退出码或崩溃）时才显示输出。它是 moreutils 的一部分。非常适合需要详细输出但希望成功时保持安静的 cron 任务。

# PARAMETERS

**-v**
> 详细模式：区分 stdout/stderr，并报告返回值

**-e**
> stderr 触发：只要 stderr 非空就显示输出

# EXIT STATUS

**0**
> 命令成功且无 stderr 输出（在 -e 模式下）

**1**
> 命令失败

**2**
> 命令成功但产生了 stderr 输出（在 -e 模式下）

# BEHAVIOR

- 成功（退出码 0）：丢弃输出
- 失败（退出码 != 0）：显示输出
- 使用 -e 时：即使成功，stderr 输出也会触发显示

# CAVEATS

moreutils 软件包的一部分。比重定向到 /dev/null 更好，因为你仍然能看到错误。

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

[moreutils](/man/moreutils)(1), [cron](/man/cron)(8), [crontab](/man/crontab)(1), [sponge](/man/sponge)(1), [ts](/man/ts)(1)
