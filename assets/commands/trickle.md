# TAGLINE

面向应用程序的用户态带宽整形器

# TLDR

限制命令的下载速度

```trickle -d [100] [command]```

限制命令的上传速度

```trickle -u [50] [command]```

同时限制下载和上传

```trickle -d [100] -u [50] [command]```

以独立模式运行

```trickle -s -d [100] -u [50] [command]```

限制 wget 的下载速度

```trickle -d [200] wget [https://example.com/file.iso]```

限制 scp 的传输速度

```trickle -d [50] -u [50] scp [file] [user@host:/path]```

# SYNOPSIS

**trickle** [_options_] _command_ [_args_]

# PARAMETERS

**-d** _rate_
> 将下载带宽限制为 rate KB/s。

**-u** _rate_
> 将上传带宽限制为 rate KB/s。

**-s**
> 以独立模式运行，不依赖 trickled。

**-w** _length_
> 峰值检测窗口大小，单位 KB。数值越小越激进，但可能过度整形（默认：512）。

**-t** _seconds_
> 平滑时间间隔，单位秒（默认：5）。

**-l** _length_
> 平滑长度，单位 KB（默认：10）。

**-L** _latency_
> 设置用于整形计算的延迟，单位毫秒。

**-n** _path_
> trickled 套接字路径（默认：/tmp/.trickled.sock）。

**-v**
> 提高详细程度。可多次指定。

**-V**
> 显示版本信息。

**-h**
> 显示帮助。

# DESCRIPTION

**trickle** 是一个轻量级的用户态带宽整形器，用于限制单个应用程序的网络带宽消耗。它通过拦截套接字调用来工作，无需 root 权限，也无需修改内核。

该工具使用预加载（LD_PRELOAD）技术向动态链接的应用注入带宽限制。在独立模式 (-s) 下，每个应用拥有各自的带宽限制。当 trickled 守护进程运行时，多个应用之间可以共享带宽。

典型用例包括：防止单个下载占满整个连接、测试应用在低带宽下的行为，以及在多个进程之间公平分配带宽。

# CAVEATS

仅对使用 TCP (SOCK_STREAM) 套接字的动态链接可执行文件有效。对静态链接或 setuid 程序无效。UDP 流量不受影响。独立模式使用固定限额；守护进程模式可通过 trickled 共享限额。

# HISTORY

**trickle** 由 Marius Aamodt Eriksen 开发，是一种简单的应用层带宽限制方案。它提供了 tc 等复杂流量控制方案的替代选择，完全在用户态工作，无需系统级配置。

# INSTALL

```apt: sudo apt install trickle```

```nix: nix profile install nixpkgs#trickle```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tc](/man/tc)(1), [wondershaper](/man/wondershaper)(1), [nethogs](/man/nethogs)(1)
