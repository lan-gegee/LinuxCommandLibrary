# TAGLINE

列出容器镜像仓库中的标签

# TLDR

**列出仓库中的所有标签**

```crane ls [registry/repository]```

**以完整镜像引用的形式列出标签**

```crane ls --full-ref [registry/repository]```

**列出标签但排除基于摘要的标签**

```crane ls -O [registry/repository]```

**从不安全（HTTP）的镜像仓库列出标签**

```crane ls --insecure [registry/repository]```

# SYNOPSIS

**crane** **ls** [_options_] _REPOSITORY_

# PARAMETERS

**--full-ref**
> 打印完整的镜像引用，而不仅仅是标签名。

**-O**, **--omit-digest-tags**
> 在输出中省略基于摘要的标签（例如 sha256-...）。

**--platform** _PLATFORM_
> 以 os/arch[/variant] 格式指定平台（例如 linux/amd64）。默认：全部。

**--insecure**
> 允许在不使用 TLS（纯 HTTP）的情况下获取镜像引用。

**-v**, **--verbose**
> 启用调试日志。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**crane ls** 通过查询镜像仓库的标签列表 API 来列出容器镜像仓库中的所有标签。它是 **crane** 的一部分——crane 是 Google go-containerregistry 项目中用于与远程容器镜像仓库交互的工具。

该命令适用于查看可用的镜像版本，而无需在本地拉取任何镜像。

# CAVEATS

私有镜像仓库需要身份验证（通过 **crane auth** 或 Docker 配置文件设置）。**--insecure** 标志会强制使用 HTTP 而非 HTTPS，只应针对本地或受信任的镜像仓库使用。

# INSTALL

```pacman: sudo pacman -S crane```

```apk: sudo apk add crane```

```zypper: sudo zypper install crane```

```brew: brew install crane```

```nix: nix profile install nixpkgs#crane```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[crane](/man/crane)(1), [crane-pull](/man/crane-pull)(1), [crane-digest](/man/crane-digest)(1), [crane-catalog](/man/crane-catalog)(1), [crane-tag](/man/crane-tag)(1)
