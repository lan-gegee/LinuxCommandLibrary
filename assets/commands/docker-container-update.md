# TAGLINE

动态更新容器的资源限制

# TLDR

**更新 CPU 限制**

```docker container update --cpus [2] [container]```

**更新内存限制**

```docker container update --memory [512m] [container]```

**更新重启策略**

```docker container update --restart [always] [container]```

**更新多个容器**

```docker container update --memory [1g] [container1] [container2]```

# SYNOPSIS

**docker** **container** **update** [_options_] _container_ [_container..._]

# PARAMETERS

**--cpus** _decimal_
> CPU 数量。

**--memory** **-m** _bytes_
> 内存限制。

**--memory-swap** _bytes_
> 交换空间限制。

**--restart** _policy_
> 重启策略（no、on-failure、always、unless-stopped）。

**--cpu-shares** _int_
> CPU 份额（相对权重）。

**--cpu-period** _int_
> 限制 CPU CFS（完全公平调度器）周期。

**--cpu-quota** _int_
> 限制 CPU CFS 配额。

**--cpuset-cpus** _string_
> 允许执行的 CPU（如 0-3、0,1）。

**--cpuset-mems** _string_
> 允许执行的内存节点（0-3、0,1）。

**--memory-reservation** _bytes_
> 内存软限制。

**--kernel-memory** _bytes_
> 内核内存限制（已弃用）。

**--blkio-weight** _uint16_
> 块设备 IO 相对权重，取值 10 到 1000，0 表示禁用。

**--pids-limit** _int_
> 调整容器的进程数上限（设为 -1 表示不限制）。

# DESCRIPTION

**docker container update** 动态更新一个或多个运行中容器的资源约束和重启策略，无需重启容器。这使管理员能够根据工作负载变化调整资源限制，或修正初始配置的错误。

虽然大多数资源限制的修改会立即生效，但某些设置可能需要重启容器才能完全应用。重启策略的更新尤其有用，可用于更改容器是否应在失败或系统启动时自动重启。

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

[docker-update](/man/docker-update)(1), [docker-container](/man/docker-container)(1)
