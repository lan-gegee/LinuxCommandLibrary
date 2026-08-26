# TAGLINE

在本地文件系统与 Pod 中的容器之间复制文件和目录

# TLDR

**复制文件到 Pod**

```kubectl cp [localfile] [pod-name]:[/path/in/container]```

**从 Pod 复制文件**

```kubectl cp [pod-name]:[/path/in/container] [localfile]```

**复制到指定容器**

```kubectl cp [localfile] [pod-name]:[path] -c [container]```

**复制整个目录**

```kubectl cp [localdir] [pod-name]:[/remote/dir]```

**从指定命名空间的 Pod 复制**

```kubectl cp [namespace]/[pod-name]:[/path/in/container] [localfile]```

**复制时不保留权限**

```kubectl cp [localfile] [pod-name]:[path] --no-preserve```

# SYNOPSIS

**kubectl** **cp** _src_ _dest_ [_options_]

# PARAMETERS

**-c**, **--container** _name_
> 多容器 Pod 中的容器名称。

**-n**, **--namespace** _name_
> Kubernetes 命名空间。

**--no-preserve**
> 不保留文件所有者和权限。

**--retries** _int_
> 遇到网络错误时的重试次数（默认：0）。

# DESCRIPTION

**kubectl cp** 在本地文件系统与 Pod 中的容器之间复制文件和目录。内部使用 tar 实现，因此容器中必须存在 tar。支持双向复制。

# CAVEATS

需要容器中安装了 tar。如果缺少 tar，复制将会失败。由于数据要经过 API 服务器流式传输，大文件传输可能较慢。不会跟随被复制目录中的符号链接。命名空间/Pod 格式使用 `/` 作为分隔符（例如 `mynamespace/mypod:/path`）。

# INSTALL

```apt: sudo apt install kubectl```

```pacman: sudo pacman -S kubectl```

```apk: sudo apk add kubectl```

```brew: brew install kubectl```

```nix: nix profile install nixpkgs#kubectl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [kubectl-exec](/man/kubectl-exec)(1)
