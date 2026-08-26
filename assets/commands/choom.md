# TAGLINE

显示和调整 OOM killer 分数

# TLDR

显示进程的 **OOM killer 分数**

```choom -p [pid]```

**更改**进程的 OOM killer 调整分数

```choom -p [pid] -n [-1000..+1000]```

以指定的 OOM killer 分数**运行**命令

```choom -n [-1000..+1000] [command] [arguments]```

# SYNOPSIS

**choom** [_options_]

# DESCRIPTION

**choom** 显示并更改进程的内存不足（OOM）killer 分数调整值。当系统内存严重不足时，OOM killer 会终止进程。

分数调整范围为 -1000（绝不杀死）到 +1000（最先杀死）。设为 -1000 实际上等于对该进程禁用 OOM 杀死。

# PARAMETERS

**-p, --pid** _pid_
> 指定进程 ID

**-n, --adjust** _value_
> 设置 OOM 分数调整值（-1000 到 +1000）

# CAVEATS

修改其他用户进程的 OOM 分数需要相应权限。对过多进程设置 -1000 可能导致系统在内存耗尽时没有可杀死的候选进程，从而造成系统挂起。

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

[proc](/man/proc)(5), [kill](/man/kill)(1), [ps](/man/ps)(1)

# RESOURCES

```[Source code](https://github.com/util-linux/util-linux)```

```[Documentation](https://man7.org/linux/man-pages/man1/choom.1.html)```

<!-- verified: 2026-06-22 -->
