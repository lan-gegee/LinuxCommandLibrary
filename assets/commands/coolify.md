# TAGLINE

可自托管的 PaaS 平台

# TLDR

**在服务器上安装 Coolify**

```curl -fsSL https://get.coolify.io | bash```

**启动 Coolify** 服务

```coolify start```

**停止 Coolify** 服务

```coolify stop```

**重启 Coolify** 服务

```coolify restart```

**检查 Coolify 状态**

```coolify status```

**将 Coolify 更新**到最新版本

```coolify upgrade```

**查看 Coolify 日志**

```coolify logs```

# SYNOPSIS

**coolify** _command_ [_options_]

# PARAMETERS

**start**
> 启动所有 Coolify 服务和容器。

**stop**
> 停止所有 Coolify 服务。

**restart**
> 重启所有 Coolify 服务。

**status**
> 显示 Coolify 服务的当前状态。

**upgrade**
> 将 Coolify 升级到最新版本。

**logs**
> 显示 Coolify 服务的日志。

**backup**
> 备份 Coolify 的配置和数据。

**restore**
> 从备份恢复 Coolify。

**--help**
> 显示帮助信息。

# DESCRIPTION

**Coolify** 是 Heroku、Netlify 和 Vercel 的开源、可自托管替代品。它提供一个平台，让你能以最少的配置在自己的基础设施上部署应用、数据库和服务。

该平台支持多种部署方式，包括基于 Git 的部署、Docker 镜像和 docker-compose 文件。它通过 Let's Encrypt 自动处理 SSL 证书，提供内置监控，并支持 PostgreSQL、MySQL、MongoDB 和 Redis 等流行数据库。

Coolify 为这样的开发者和团队而设计：既想要 PaaS 平台的便利性，又要保持对自身基础设施和数据的掌控。它运行在 Docker 上，可以安装在满足最低要求的任何 Linux 服务器上。

# CAVEATS

需要主机系统已安装 Docker 和 Docker Compose。初次安装需要 root 权限。资源需求取决于部署的应用数量。某些高级功能可能需要额外配置。

# HISTORY

Coolify 由 Andras Bacsai 创建，是一个开源 PaaS 解决方案。开发始于约 **2021** 年，其灵感来自对商业平台自托管替代方案的需求。它已发展为支持多种应用类型，并在自托管社区中广受欢迎。

# SEE ALSO

[docker](/man/docker)(1), [docker-compose](/man/docker-compose)(1), [dokku](/man/dokku)(1)

# RESOURCES

```[Source code](https://github.com/coollabsio/coolify)```

```[Homepage](https://coolify.io)```

```[Documentation](https://coolify.io/docs)```

<!-- verified: 2026-06-23 -->
