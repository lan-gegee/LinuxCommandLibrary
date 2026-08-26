# TAGLINE

用 Rust 编写的快速端口扫描器

# TLDR

**扫描目标**

```rustscan -a [target]```

**指定端口范围扫描**

```rustscan -a [target] -r [1-1000]```

**扫描多个目标**

```rustscan -a [target1],[target2]```

**通过管道传给 nmap**

```rustscan -a [target] -- -sV -sC```

**设置批次大小**

```rustscan -a [target] -b [1000]```

**扫描特定端口**

```rustscan -a [target] -p [22,80,443]```

**增大超时时间**

```rustscan -a [target] --timeout [3000]```

# SYNOPSIS

**rustscan** [_-a targets_] [_-p ports_] [_-r range_] [_options_] [-- _nmap args_]

# PARAMETERS

**-a**, **--addresses** _TARGETS_
> 目标地址。

**-p**, **--ports** _PORTS_
> 特定端口。

**-r**, **--range** _RANGE_
> 端口范围。

**-b**, **--batch-size** _N_
> 并发连接数。

**--timeout** _MS_
> 连接超时时间。

**-u**, **--ulimit** _N_
> 文件描述符限制。

**-- ** _ARGS_
> 传递给 nmap 的参数。

**-g**, **--greppable**
> 便于 grep 的输出。

# DESCRIPTION

**rustscan** 是一个用 Rust 编写的快速端口扫描器。它能快速找出开放端口，然后可选地交给 nmap 处理。

异步扫描实现了极高的速度。全部 65535 个端口可在数秒内扫完。

nmap 集成提供了深入分析能力。RustScan 找端口，nmap 分析服务。

批次大小控制扫描的激进程度。数值越高越快，但可能漏掉端口。

自适应学习会根据网络状况进行调整，避免压垮目标主机。

# CAVEATS

高扫描速率可能触发 IDS。为保证可靠性请调整批次大小。仅限用于已授权的扫描。

# HISTORY

**RustScan** 由 **bee-san** 创建，目标是更快的端口扫描。它将 Rust 的性能与 nmap 的能力结合在一起。

# INSTALL

```pacman: sudo pacman -S rustscan```

```zypper: sudo zypper install rustscan```

```brew: brew install rustscan```

```nix: nix profile install nixpkgs#rustscan```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nmap](/man/nmap)(1), [masscan](/man/masscan)(1), [zmap](/man/zmap)(1)
