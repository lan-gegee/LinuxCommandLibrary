# TAGLINE

列出容器镜像仓库中的仓库

# TLDR

**列出**镜像仓库中的仓库

```crane catalog [registry]```

以完整镜像引用的形式**列出仓库**

```crane catalog --full-ref [registry]```

使用平台专属设置**列出仓库**

```crane catalog --platform [linux/amd64] [registry]```

# SYNOPSIS

**crane** **catalog** [_options_] _registry_

# PARAMETERS

**--full-ref**
> 为每个仓库打印完整的镜像引用。

**--platform** _platform_
> 以 os/arch 形式指定平台（例如 linux/amd64）。

**--insecure**
> 允许在不使用 TLS 的情况下获取镜像引用。

# DESCRIPTION

**crane catalog** 列出容器镜像仓库中的所有仓库。这要求镜像仓库支持 catalog API（OCI Distribution 规范定义的 `_catalog` 端点）。

注意，出于安全考虑，许多镜像仓库会限制或禁用 catalog 端点。

# CAVEATS

并非所有镜像仓库都支持 catalog API。对于大型镜像仓库，结果可能分页返回。主流云镜像仓库（Docker Hub、GCR、ECR）通常会对 catalog 端点加以限制或完全禁用。

# INSTALL

```pacman: sudo pacman -S crane```

```apk: sudo apk add crane```

```zypper: sudo zypper install crane```

```brew: brew install crane```

```nix: nix profile install nixpkgs#crane```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[crane](/man/crane)(1), [crane-ls](/man/crane-ls)(1), [crane-copy](/man/crane-copy)(1)
