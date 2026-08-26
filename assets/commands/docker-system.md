# TAGLINE

管理 Docker 系统资源与磁盘占用

# TLDR

**查看磁盘占用**

```docker system df```

**查看详细磁盘占用**

```docker system df -v```

**清理未使用的数据**

```docker system prune```

**清理所有未使用的数据（包括卷）**

```docker system prune -a --volumes```

**显示系统信息**

```docker system info```

**显示系统事件**

```docker system events```

# SYNOPSIS

**docker** **system** _command_ [_options_]

# SUBCOMMANDS

**df**
> 查看 Docker 磁盘占用。

**prune**
> 清理未使用的数据。

**info**
> 显示系统级信息。

**events**
> 从服务器获取实时事件。

# DESCRIPTION

**docker system** 管理 Docker 的系统资源，可用于监控磁盘占用以及清理未使用的容器、镜像、网络和卷。

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
