# TAGLINE

Keycloak（开源身份和访问管理解决方案）的命令行界面

# TLDR

**以开发模式启动 Keycloak**

```kc.sh start-dev```

**以生产模式启动**

```kc.sh start --hostname=[auth.example.com]```

**构建优化后的配置**

```kc.sh build```

**导出 realm 配置**

```kc.sh export --dir [/export] --realm [myrealm]```

**导入 realm 配置**

```kc.sh import --file [realm.json]```

**显示可用选项**

```kc.sh start --help```

**显示版本**

```kc.sh --version```

# SYNOPSIS

**kc.sh** _command_ [_options_]

# COMMANDS

**start**
> 以生产模式启动服务器（需要先 build）。

**start-dev**
> 以默认设置的开发模式启动。

**build**
> 生成优化后的服务器配置。

**export**
> 将 realm 数据导出到文件。

**import**
> 从文件导入 realm 数据。

**show-config**
> 显示当前配置。

**tools**
> 用于补全和 vault 操作的实用命令。

# PARAMETERS

**--hostname** _name_
> 服务器的公开主机名。

**--hostname-admin** _name_
> 管理控制台的主机名。

**--http-port** _port_
> HTTP 监听端口。默认：8080。

**--https-port** _port_
> HTTPS 监听端口。默认：8443。

**--db** _type_
> 数据库类型：dev-file、dev-mem、postgres、mysql、mariadb、mssql、oracle。

**--db-url** _url_
> 完整的数据库 JDBC URL。

**--db-username** _user_
> 数据库用户名。

**--db-password** _pass_
> 数据库密码。

**--features** _list_
> 启用特性开关。

**--health-enabled** _bool_
> 启用健康检查端点。

**--metrics-enabled** _bool_
> 启用指标端点。

**--proxy** _mode_
> 代理模式：edge、reencrypt、passthrough。

**--log-level** _level_
> 日志级别：fatal、error、warn、info、debug、trace。

**--help**, **-h**
> 显示帮助信息。

# DESCRIPTION

**kc.sh** 是 Keycloak 的命令行界面。Keycloak 是一个开源的身份和访问管理解决方案，kc.sh 负责管理服务器生命周期、配置以及数据导入/导出。

开发模式（**start-dev**）以宽松的安全设置运行，适合本地测试。生产部署在运行 **build** 优化配置后使用 **start** 启动。build 步骤会生成基于 Quarkus 的优化发行版。

Keycloak 支持 SAML 2.0、OpenID Connect、OAuth 2.0 以及 LDAP/AD 集成，提供社交登录、用户联合、细粒度授权和多因素认证等功能。

**export** 和 **import** 命令用于传输 realm 配置，包括客户端、角色、用户和认证流程。可用于备份、迁移或基础设施即代码工作流。

配置可以通过命令行选项、环境变量（KC_ 前缀）或配置文件提供。

# CAVEATS

生产模式要求显式配置主机名并设置 TLS。当配置发生更改时，必须先运行 build 命令再进行生产启动。部分选项需要重启才能生效。开发环境（H2）与生产部署之间的数据库配置差异很大。

# HISTORY

Keycloak 由 **Red Hat** 创建，于 **2014 年 9 月**首次发布。它源自 PicketLink 项目，后来成为 Red Hat 的战略性身份管理方案。该项目于 **2023 年**加入 CNCF 成为孵化项目。17 版（2022 年）引入了基于 Quarkus 的架构，取代了 WildFly。Keycloak 被广泛用于企业单点登录、API 安全和用户管理。

# INSTALL

```pacman: sudo pacman -S keycloak```

```nix: nix profile install nixpkgs#keycloak```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[authelia](/man/authelia)(1), [vault](/man/vault)(1)
