# TAGLINE

动态更新容器资源限制

# TLDR

**更新 CPU 限制**

```docker update --cpus [2] [container]```

**更新内存限制**

```docker update --memory [512m] [container]```

**更新重启策略**

```docker update --restart [always] [container]```

**更新多个容器**

```docker update --memory [1g] [container1] [container2]```

**移除内存限制**

```docker update --memory [0] [container]```

# SYNOPSIS

**docker** **update** [_options_] _container_ [_container..._]

# PARAMETERS

**--cpus** _decimal_
> CPU 数量。

**--memory**, **-m** _bytes_
> 内存限制。

**--memory-swap** _bytes_
> 交换区限制（-1 表示无限制）。

**--restart** _string_
> 重启策略（no、on-failure、always、unless-stopped）。

**--cpu-shares** _int_
> CPU 权重（相对值）。

**--memory-reservation** _bytes_
> 内存软限制。

**--cpuset-cpus** _string_
> 允许执行的 CPU（如 0-3、0,1）。

**--pids-limit** _int_
> 调整容器 PID 数上限（-1 表示无限制）。

**--blkio-weight** _uint16_
> 块 IO 相对权重（10-1000），0 表示禁用。

**--cpu-period** _int_
> 限制 CPU CFS 周期（微秒）。

**--cpu-quota** _int_
> 限制 CPU CFS 配额（微秒）。

# DESCRIPTION

**docker update** 动态更新容器的资源约束。无需重建容器即可更改 CPU、内存和重启设置。可用于运行中或已停止的容器。不支持 Windows 容器。

# CAVEATS

**--kernel-memory** 选项自 Docker 20.10 起已弃用。在某些系统上，对运行中容器的内存更改可能需要重启容器才能完全生效。

# INSTALL

```apt: sudo apt install docker-cli```

```dnf: sudo dnf install docker-cli```

```pacman: sudo pacman -S docker```

```apk: sudo apk add docker-cli```

```zypper: sudo zypper install docker```

```brew: brew install docker```

```nix: nix profile install nixpkgs#docker```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[docker](/man/docker)(1), [docker-container-update](/man/docker-container-update)(1), [docker-run](/man/docker-run)(1), [docker-inspect](/man/docker-inspect)(1)
