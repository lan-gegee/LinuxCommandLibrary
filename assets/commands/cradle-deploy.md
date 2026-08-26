# TAGLINE

将 Cradle PHP 应用部署到服务器

# TLDR

**部署到生产**服务器

```cradle deploy production```

**部署到预发布**环境

```cradle deploy staging```

**使用自定义配置部署**

```cradle deploy --config [deploy.yml]```

不实际部署而**预览变更**

```cradle deploy --dry-run production```

**部署指定分支**

```cradle deploy production --branch [release]```

部署时**跳过数据库迁移**

```cradle deploy --no-migrate production```

# SYNOPSIS

**cradle deploy** [_options_] _environment_

# PARAMETERS

_ENVIRONMENT_
> 目标部署环境（production、staging、development）。

**--config** _FILE_
> 使用自定义的部署配置文件。

**--dry-run**
> 预演部署而不实际做出更改。

**--branch** _BRANCH_
> 部署指定的 Git 分支。

**--no-migrate**
> 部署期间跳过数据库迁移。

**--force**
> 即使存在未提交的更改也强制部署。

**--verbose**
> 显示详细的部署输出。

**--help**
> 显示帮助信息。

# DESCRIPTION

**cradle deploy** 是 Cradle PHP 框架的部署命令。它将应用部署到远程服务器的过程自动化，处理代码同步、依赖安装、数据库迁移和缓存清理等任务。

该命令读取部署配置，其中指定了服务器详情、部署路径以及各环境专有的设置。它支持多环境，可为生产、预发布和开发服务器使用不同的配置。

部署通常包括推送代码更改、运行 composer install、执行数据库迁移以及清理缓存。dry-run 选项让你在正式执行部署之前预览将要进行的更改。

# CAVEATS

需要对目标服务器的 SSH 访问权限。部署配置必须指定正确的路径和凭据。请先使用 **--dry-run** 验证部署步骤。数据库迁移应在生产部署之前先行测试。

# HISTORY

cradle deploy 作为 Cradle 框架 CLI 工具的一部分而诞生，用于简化部署工作流程。它沿用了其他 PHP 框架部署工具所确立的模式，为把应用推送到服务器提供一致的接口。

# SEE ALSO

[cradle](/man/cradle)(1), [rsync](/man/rsync)(1), [ssh](/man/ssh)(1), [composer](/man/composer)(1)
