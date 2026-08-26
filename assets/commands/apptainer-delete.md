# TAGLINE

从远程库删除容器镜像。

# TLDR

从 Container Library **删除镜像**

```apptainer delete library://[user/collection/container]:[tag]```

删除**特定架构**的镜像

```apptainer delete -A [amd64|arm64|ppc64le] library://[user/collection/container]:[tag]```

**不经确认强制删除**镜像

```apptainer delete -F library://[user/collection/container]:[tag]```

从**特定的库服务器**删除镜像

```apptainer delete --library [https://library.example.com] library://[user/collection/container]:[tag]```

使用 **HTTP** 而不是 HTTPS 删除镜像

```apptainer delete --no-https library://[hostname/user/collection/container]:[tag]```

# SYNOPSIS

**apptainer delete** [_options_] _library://path_

# DESCRIPTION

**apptainer delete** 从远程 Container Library 中移除容器镜像。这是一项破坏性操作，会永久地从远程注册表中移除指定的镜像或镜像标签。

该命令需要先对目标库进行身份验证，并拥有删除镜像的相应权限。

# PARAMETERS

**-A, --arch** _architecture_
> 删除特定 CPU 架构的镜像（默认：amd64）。

**-F, --force**
> 不经确认提示强制删除。

**--library** _url_
> 指定要从中删除的 Container Library URL。

**--no-https**
> 库连接使用 HTTP 而不是 HTTPS。

# CAVEATS

此操作不可逆。已删除的镜像无法恢复。删除前请确保已备份重要的容器镜像。只有镜像所有者或库管理员才能删除镜像。

# INSTALL

```dnf: sudo dnf install apptainer```

```pacman: sudo pacman -S apptainer```

```apk: sudo apk add apptainer```

```zypper: sudo zypper install apptainer```

```brew: brew install apptainer```

```nix: nix profile install nixpkgs#apptainer```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[apptainer](/man/apptainer)(1), [apptainer-push](/man/apptainer-push)(1), [apptainer-pull](/man/apptainer-pull)(1), [apptainer-search](/man/apptainer-search)(1)

# RESOURCES

```[Source code](https://github.com/apptainer/apptainer)```

```[Homepage](https://apptainer.org)```

```[Documentation](https://apptainer.org/docs/)```

<!-- verified: 2026-06-11 -->
