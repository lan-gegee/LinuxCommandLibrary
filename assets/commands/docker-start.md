# TAGLINE

启动已停止的容器

# TLDR

**启动一个已停止的容器**

```docker start [container]```

**启动多个容器**

```docker start [container1] [container2]```

**启动并附加输出**

```docker start -a [container]```

**交互式启动**

```docker start -ai [container]```

# SYNOPSIS

**docker** **start** [_options_] _container_ [_container..._]

# PARAMETERS

**-a**, **--attach**
> 附加 STDOUT/STDERR 并转发信号。

**-i**, **--interactive**
> 附加容器的 STDIN。

**--detach-keys** _string_
> 覆盖脱离容器所用的按键序列。

**--checkpoint** _string_
> 从该检查点恢复。

**--checkpoint-dir** _string_
> 使用自定义的检查点存储目录。

# DESCRIPTION

**docker start** 启动一个或多个已停止的容器。容器会保留其创建时或上次运行时的配置。

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

[docker-container-start](/man/docker-container-start)(1), [docker-run](/man/docker-run)(1)
