# TAGLINE

实时监视磁盘 I/O 延迟，就像 ping 显示网络延迟一样

# TLDR

**测量磁盘延迟**

```ioping [path]```

**执行指定次数的请求**

```ioping -c [10] [path]```

**以指定大小测量**

```ioping -s [1M] [path]```

**测量磁盘寻道速率**

```ioping -R [/dev/sda]```

**测量顺序读写速度**

```ioping -RL [/dev/sda]```

**使用直接 I/O**

```ioping -D [path]```

**安静模式并输出统计信息**

```ioping -q -c [100] [path]```

# SYNOPSIS

**ioping** [_options_] _path_|_device_

# PARAMETERS

**-c** _count_
> 执行 count 次请求后停止。

**-s** _size_
> 请求大小（默认 4k）。

**-R**
> 磁盘寻道速率测试。

**-L**
> 顺序操作（默认随机）。

**-D**
> 使用直接 I/O（O_DIRECT）。

**-W**
> 使用写入操作（对设备有危险）。

**-C**
> 使用缓存 I/O。

**-A**
> 使用异步 I/O。

**-q**
> 安静模式，仅显示摘要。

**-w** _seconds_
> 在指定时间后停止。

# DESCRIPTION

**ioping** 实时监视磁盘 I/O 延迟，就像 ping 显示网络延迟一样。它生成 I/O 模式并测量响应时间。SSD 的延迟应在毫秒以下；HDD 通常为几毫秒。延迟出现高峰可能预示存在问题。

# INSTALL

```apt: sudo apt install ioping```

```dnf: sudo dnf install ioping```

```pacman: sudo pacman -S ioping```

```apk: sudo apk add ioping```

```zypper: sudo zypper install ioping```

```brew: brew install ioping```

```nix: nix profile install nixpkgs#ioping```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fio](/man/fio)(1), [iostat](/man/iostat)(1), [ping](/man/ping)(1)
