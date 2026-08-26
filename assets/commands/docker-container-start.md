# TAGLINE

启动一个或多个已停止的容器

# TLDR

**启动已停止的容器**

```docker container start [container]```

**启动多个容器**

```docker container start [container1] [container2]```

**启动并附着输出**

```docker container start -a [container]```

**以交互方式启动**

```docker container start -ai [container]```

# SYNOPSIS

**docker** **container** **start** [_options_] _container_ [_container..._]

# PARAMETERS

**-a**, **--attach**
> 附着 STDOUT/STDERR。

**-i**, **--interactive**
> 附着 STDIN。

# DESCRIPTION

**docker container start** 启动一个或多个已停止的容器，使其从先前的状态恢复运行。与创建新容器的 **docker container run** 不同，此命令作用于已存在的、已停止的容器。

容器会以其原有配置恢复运行，包括环境变量、卷、网络设置以及最初指定的命令。这使它适合重启服务或在开发容器中继续工作。

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

[docker-start](/man/docker-start)(1)
