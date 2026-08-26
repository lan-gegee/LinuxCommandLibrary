# TAGLINE

从镜像仓库中删除容器镜像

# TLDR

**按标签删除镜像**

```crane delete [registry.example.com/repo:tag]```

**按摘要删除镜像**

```crane delete [registry.example.com/repo]@[sha256:abc123...]```

**删除并显示详细输出**

```crane delete -v [registry.example.com/repo:tag]```

# SYNOPSIS

**crane** **delete** [_options_] _image_ref_

# PARAMETERS

**-v**, **--verbose**
> 启用详细日志输出。

**--platform** _PLATFORM_
> 以 os/arch 形式指定平台（例如 linux/amd64）。

**--insecure**
> 允许在不使用 TLS 的情况下获取镜像引用。

# DESCRIPTION

**crane delete** 通过标签或摘要引用从容器镜像仓库中删除镜像清单（manifest）。镜像引用必须包含完整的镜像仓库路径。

按标签删除时，镜像仓库会移除标签到清单的映射关系。按摘要删除时，则会移除清单本身。请谨慎使用，因为根据镜像仓库的配置与策略，删除可能是永久性的。

该命令向镜像仓库的清单端点发送 HTTP DELETE 请求。它需要对目标仓库具备相应的身份验证和授权。

# CAVEATS

部分镜像仓库不支持删除，或需要特殊权限。在垃圾回收运行之前，删除标签并不一定会释放存储空间。按摘要删除清单可能影响指向同一清单的其他标签。Docker Hub 和一些托管型镜像仓库可能对删除设有速率限制或其他限制。

# INSTALL

```pacman: sudo pacman -S crane```

```apk: sudo apk add crane```

```zypper: sudo zypper install crane```

```brew: brew install crane```

```nix: nix profile install nixpkgs#crane```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[crane](/man/crane)(1), [crane-tag](/man/crane-tag)(1), [crane-digest](/man/crane-digest)(1), [crane-ls](/man/crane-ls)(1), [crane-manifest](/man/crane-manifest)(1)
