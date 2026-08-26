# TAGLINE

实时容器指标监控工具

# TLDR

只显示**活跃**容器

```ctop -a```

**反转**容器排序顺序

```ctop -r```

**反转**默认配色

```ctop -i```

显示**帮助**

```ctop -h```

# SYNOPSIS

**ctop** [_options_]

# DESCRIPTION

**ctop** 提供类似 top 的界面，用于实时监控容器指标。它显示系统上所有容器的 CPU 使用率、内存占用、网络 I/O 和块设备 I/O 统计信息。

该工具通过连接相应的套接字，支持 Docker、containerd 及其他容器运行时。界面完全可交互，用户可以按不同指标对容器排序、在活跃容器与全部容器之间切换过滤，还能深入查看单个容器的日志和统计信息。

ctop 对 DevOps 工作流、性能问题排查以及容器化应用监控特别有用，无需记住复杂的 docker stats 命令。它提供了跨所有容器的统一视图，正如 htop 之于系统进程。

# PARAMETERS

**-a**
> 只显示活跃（运行中）的容器

**-r**
> 反转排序顺序

**-i**
> 反转默认配色

**-h**
> 显示帮助

**-s** _field_
> 选择初始排序字段

# KEYBINDINGS

**q**
> 退出

**s**
> 选择排序字段

**r**
> 反转排序顺序

**Enter**
> 查看容器详情

# CAVEATS

需要访问容器运行时的套接字（通常为 /var/run/docker.sock）。可能需要用 sudo 运行，或以 docker 组的用户身份运行。性能指标取决于容器运行时自身的能力。

# HISTORY

**ctop** 由 **bcicen** 创建，于 **2016 年**作为开源项目发布。它作为 docker stats 的易用替代品迅速在容器社区流行开来，为容器监控提供了更直观的界面。

# INSTALL

```pacman: sudo pacman -S ctop```

```apk: sudo apk add ctop```

```brew: brew install ctop```

```nix: nix profile install nixpkgs#ctop```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[docker](/man/docker)(1), [top](/man/top)(1), [htop](/man/htop)(1)

# RESOURCES

```[Source code](https://github.com/bcicen/ctop)```

<!-- verified: 2026-06-26 -->
