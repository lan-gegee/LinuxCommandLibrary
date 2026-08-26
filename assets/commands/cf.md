# TAGLINE

用于应用部署的 Cloud Foundry CLI

# TLDR

**登录 Cloud Foundry**

```cf login -a [api.example.com]```

**推送应用**

```cf push [app-name]```

**列出应用**

```cf apps```

**查看应用日志**

```cf logs [app-name]```

**伸缩应用**

```cf scale [app-name] -i [3]```

**创建服务实例**

```cf create-service [service] [plan] [name]```

**将服务绑定到应用**

```cf bind-service [app-name] [service-name]```

# SYNOPSIS

**cf** [_global_options_] _command_ [_arguments_] [_command_options_]

# DESCRIPTION

**cf** 是 Cloud Foundry CLI，用于管理 Cloud Foundry 平台上的应用和服务。它处理应用的完整生命周期，包括部署、伸缩、日志以及跨多个云提供商的服务绑定。

Cloud Foundry 采用推送式部署模型：开发者运行 `cf push` 上传应用代码，平台随后自动构建、容器化并部署。应用按组织和空间组织，提供多租户隔离。CLI 负责开发者与 Cloud Foundry API 之间的交互。

数据库、消息队列和缓存等服务从服务市场开通并绑定到应用，连接凭证通过环境变量注入。

# COMMANDS

**login**
> 向 Cloud Foundry 认证

**push**
> 部署应用

**apps**
> 列出空间中的应用

**logs**
> 查看应用日志

**scale**
> 伸缩应用实例

**start**, **stop**, **restart**
> 管理应用状态

**delete**
> 删除应用

**services**
> 列出服务实例

**create-service**
> 创建服务实例

**bind-service**
> 将服务绑定到应用

**env**
> 显示环境变量

**ssh**
> SSH 进入应用容器

**orgs**, **spaces**
> 列出组织/空间

# PARAMETERS

**-a** _URL_
> API 端点 URL

**-u** _user_
> 用户名

**-p** _pass_
> 密码

**-o** _org_
> 组织

**-s** _space_
> 空间

**-i** _num_
> 实例数量

**-m** _memory_
> 内存限制（如 256M）

**-f** _manifest_
> manifest 文件路径

**--skip-ssl-validation**
> 跳过 SSL 证书验证

# CONFIGURATION

**~/.cf/config.json**
> CLI 配置文件，包括 API 端点、访问令牌以及当前的 org/space 目标。

**manifest.yml**
> 应用部署清单，定义内存、实例数、路由和服务绑定。

# CAVEATS

请使用 cf v8（当前受支持的版本）。运行 `cf help -a` 可查看所有命令。交互式密码提示在 Cygwin/Git Bash 中存在问题。

# INSTALL

```brew: brew install cf```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [heroku](/man/heroku)(1), [docker](/man/docker)(1)

# RESOURCES

```[Source code](https://github.com/cloudfoundry/cli)```

```[Documentation](https://docs.cloudfoundry.org/cf-cli/)```

<!-- verified: 2026-06-22 -->
