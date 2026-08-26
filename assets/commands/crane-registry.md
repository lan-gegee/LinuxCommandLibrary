# TAGLINE

本地内存中的容器镜像仓库

# TLDR

**启动本地镜像仓库**

```crane registry serve```

**在指定的地址和端口上提供服务**

```crane registry serve --address [localhost:5000]```

**使用磁盘上的 blob 存储**

```crane registry serve --disk [path/to/storage]```

# SYNOPSIS

**crane** **registry** **serve** [_options_]

# PARAMETERS

**--address** _addr_
> 要监听的地址（默认：从 $PORT 自动选择端口或 :0）。

**--disk** _dir_
> 将 blob 存储到指定目录的磁盘上，而不是内存中。

**-h**, **--help**
> 显示该命令的帮助信息。

# DESCRIPTION

**crane registry** 启动一个用于测试和开发的本地容器镜像仓库，无需部署完整的镜像仓库服务。默认情况下，数据存储在内存中。使用 **--disk** 可将 blob 持久化到目录。

# CAVEATS

服务器停止后内存中的存储会丢失。**--disk** 选项提供持久化能力，但仍然不适合生产使用。不提供身份验证或 TLS。

# INSTALL

```pacman: sudo pacman -S crane```

```apk: sudo apk add crane```

```zypper: sudo zypper install crane```

```brew: brew install crane```

```nix: nix profile install nixpkgs#crane```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[crane](/man/crane)(1), [crane-push](/man/crane-push)(1), [crane-pull](/man/crane-pull)(1)
