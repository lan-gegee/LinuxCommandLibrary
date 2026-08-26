# TAGLINE

Heroku 平台即服务的 CLI

# TLDR

**登录**

```heroku login```

**创建应用**

```heroku create [app-name]```

**通过 Git 部署**

```git push heroku main```

**查看日志**

```heroku logs --tail```

**打开应用**

```heroku open```

**在 dyno 上运行命令**

```heroku run [bash]```

**调整 dyno 数量**

```heroku ps:scale web=[2]```

**设置环境变量**

```heroku config:set [KEY]=[VALUE] -a [app-name]```

**列出应用**

```heroku apps```

**显示 release 历史**

```heroku releases -a [app-name]```

**回滚到先前的 release**

```heroku rollback [v42] -a [app-name]```

**连接 Postgres**

```heroku pg:psql -a [app-name]```

**切换维护模式**

```heroku maintenance:on -a [app-name]```

# SYNOPSIS

**heroku** _command_ [_options_]

# PARAMETERS

_COMMAND_
> 要执行的子命令。

**login**
> 向 Heroku 进行身份验证。

**create**
> 创建新应用。

**logs**
> 查看应用日志。

**run**
> 运行一次性命令。

**ps**
> 进程管理。

**config**
> 管理环境变量。

**addons**
> 管理插件（add-on）。

**apps**
> 管理应用。

**releases**
> 显示应用 release 历史；使用 **rollback** 回滚。

**maintenance**
> 切换维护模式（**:on** / **:off**）。

**pg**
> 管理 Heroku Postgres 数据库。

**redis**
> 管理 Heroku Redis 实例。

**domains**
> 列出、添加或移除自定义域名。

**certs**
> 管理 SSL/TLS 证书。

**buildpacks**
> 管理应用的 buildpack。

**-a**, **--app** _APP_
> 目标应用名称。

**-r**, **--remote** _REMOTE_
> 要使用的应用 Git remote。

**-j**, **--json**
> 以 JSON 格式输出。

**--help**
> 显示帮助信息。

# DESCRIPTION

**heroku** 是 Heroku 平台即服务的 CLI。它管理 Heroku 云上的应用、插件和基础设施。

该工具处理部署、扩缩容、日志和配置。它与 Git 集成进行部署，并支持多种语言。

# CAVEATS

需要 Heroku 账户。部分功能需要付费。存在速率限制。

# HISTORY

Heroku 最初于 **2007 年**面向 Ruby 应用推出，并于 **2010 年**被 **Salesforce** 收购。这款 CLI 工具提供对该平台的命令行管理。

# INSTALL

```brew: brew install heroku```

```nix: nix profile install nixpkgs#heroku```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git](/man/git)(1), [docker](/man/docker)(1), [flyctl](/man/flyctl)(1)
