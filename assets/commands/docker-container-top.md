# TAGLINE

显示容器内正在运行的进程

# TLDR

**查看容器中正在运行的进程**

```docker container top [container]```

**使用自定义 ps 选项查看**

```docker container top [container] aux```

# SYNOPSIS

**docker** **container** **top** _container_ [_ps options_]

# DESCRIPTION

**docker container top** 显示容器内正在运行的进程，类似于 Unix 的 **ps** 命令，但范围限定在特定容器的进程命名空间内。它可以让你随时了解容器内部实际在执行什么。

该命令接受标准的 **ps** 选项，以自定义输出格式并控制显示哪些进程属性。它对调试容器、验证预期进程是否在运行以及在进程级别排查资源占用特别有用。

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

[docker-top](/man/docker-top)(1), [docker-container-stats](/man/docker-container-stats)(1)

# RESOURCES

```[Source code](https://github.com/docker/cli)```

```[Documentation](https://docs.docker.com/reference/cli/docker/)```

<!-- verified: 2026-07-11 -->
