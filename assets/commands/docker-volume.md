# TAGLINE

管理 Docker 持久化数据卷

# TLDR

**列出所有数据卷**

```docker volume ls```

**创建命名数据卷**

```docker volume create [name]```

**查看数据卷详情**

```docker volume inspect [volume]```

**删除指定数据卷**

```docker volume rm [volume]```

**删除所有未使用的数据卷**

```docker volume prune```

**免确认删除所有未使用的数据卷**

```docker volume prune --force```

**使用 NFS 驱动选项创建数据卷**

```docker volume create --driver local --opt type=nfs --opt o=addr=[host],rw --opt device=:[path] [name]```

**按过滤条件列出数据卷**

```docker volume ls --filter dangling=true```

# SYNOPSIS

**docker** **volume** _command_ [_options_]

# SUBCOMMANDS

**ls**
> 列出数据卷。支持 --filter 和 --format 选项。

**create**
> 创建数据卷。可选指定 --driver 和 --opt。

**inspect**
> 显示一个或多个数据卷的详细信息。

**rm**
> 删除一个或多个数据卷。若数据卷正在使用则失败。

**prune**
> 删除所有未使用的本地数据卷。

# DESCRIPTION

**docker volume** 管理 Docker 数据卷。数据卷独立于容器持久化数据，是保存容器生成数据的推荐机制。与绑定挂载不同，数据卷由 Docker 管理，可在所有平台上使用。

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

[docker-run](/man/docker-run)(1), [docker-inspect](/man/docker-inspect)(1), [docker-container](/man/docker-container)(1), [docker-compose](/man/docker-compose)(1)
