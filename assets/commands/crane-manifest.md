# TAGLINE

获取容器镜像的清单

# TLDR

**获取镜像清单**

```crane manifest [image:tag]```

**获取特定平台的清单**

```crane manifest --platform [linux/amd64] [image:tag]```

**格式化打印清单**

```crane manifest [image] | jq .```

# SYNOPSIS

**crane** **manifest** [_options_] _image_

# PARAMETERS

**--platform** _platform_
> 以 os/arch[/variant][:osversion] 形式指定平台（例如 linux/amd64）。默认：全部。

**--insecure**
> 允许在不使用 TLS 的情况下获取镜像引用。

**-v**, **--verbose**
> 启用调试日志。

# DESCRIPTION

**crane manifest** 获取容器镜像的清单（manifest）。清单描述了镜像的层、配置以及平台信息。

输出为 JSON 格式（OCI 或 Docker 清单 schema）。

# INSTALL

```pacman: sudo pacman -S crane```

```apk: sudo apk add crane```

```zypper: sudo zypper install crane```

```brew: brew install crane```

```nix: nix profile install nixpkgs#crane```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[crane](/man/crane)(1), [crane-config](/man/crane-config)(1), [crane-digest](/man/crane-digest)(1)
