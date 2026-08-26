# TAGLINE

管理 DigitalOcean App Platform 应用

# TLDR

**列出所有应用**

```doctl apps list```

**从 spec 文件创建应用**

```doctl apps create --spec [app.yaml]```

**获取应用详情**

```doctl apps get [app_id]```

**删除一个应用**

```doctl apps delete [app_id]```

**列出应用的部署**

```doctl apps list-deployments [app_id]```

**查看部署日志**

```doctl apps logs [app_id]```

**更新应用 spec**

```doctl apps update [app_id] --spec [app.yaml]```

# SYNOPSIS

**doctl apps** _command_ [_options_]

# PARAMETERS

_COMMAND_
> 操作：list、create、get、delete、update、logs 等。

**list**
> 列出所有应用。

**create** **--spec** _FILE_
> 从规范文件创建应用。

**get** _APP_ID_
> 获取应用详情。

**delete** _APP_ID_
> 删除应用。

**list-deployments** _APP_ID_
> 列出应用的部署。

**logs** _APP_ID_
> 查看应用日志。

**--spec** _FILE_
> 应用规范文件（YAML）。

**--help**
> 显示帮助信息。

# DESCRIPTION

**doctl apps** 管理 DigitalOcean App Platform 应用。App Platform 是一项平台即服务（PaaS）产品，可自动构建、部署和伸缩应用。

该命令覆盖应用的完整生命周期：从规范创建应用、管理部署、查看日志以及配置伸缩。App 规范以 YAML 格式定义服务、worker、静态站点和作业。

App Platform 支持 Docker、Node.js、Python、Go 和静态站点等多种运行时，并可从 Git 仓库自动构建。

# CAVEATS

App Platform 会产生使用费用。构建时间因应用复杂度而异。某些功能需要特定的 spec 配置。部署回滚可能需要手动干预。

# HISTORY

doctl apps 于 **2020 年** App Platform 发布时加入 DigitalOcean CLI，为 DigitalOcean 托管的应用托管平台提供了命令行访问方式。

# INSTALL

```dnf: sudo dnf install doctl```

```pacman: sudo pacman -S doctl```

```apk: sudo apk add doctl```

```brew: brew install doctl```

```nix: nix profile install nixpkgs#doctl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[doctl](/man/doctl)(1), [heroku](/man/heroku)(1)

# RESOURCES

```[Source code](https://github.com/digitalocean/doctl)```

```[Documentation](https://docs.digitalocean.com/reference/doctl/reference/apps/)```

<!-- verified: 2026-07-11 -->
