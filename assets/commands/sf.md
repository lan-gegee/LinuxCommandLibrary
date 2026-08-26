# TAGLINE

Salesforce 开发命令行界面

# TLDR

通过网页浏览器**登录 Salesforce org**

```sf org login web```

从定义文件**创建 scratch org**

```sf org create scratch --definition-file [config/project-scratch-def.json] --alias [my-scratch]```

向 org **部署源码**

```sf project deploy start --target-org [my-org]```

从 org **检索元数据**

```sf project retrieve start --target-org [my-org]```

**运行 Apex 测试**

```sf apex run test --target-org [my-org] --code-coverage```

**执行 SOQL 查询**

```sf data query --query "[SELECT Id, Name FROM Account LIMIT 10]" --target-org [my-org]```

按版本 ID **安装软件包**

```sf package install --package [04t...] --target-org [my-org]```

**列出所有可用命令**

```sf commands```

# SYNOPSIS

**sf** _command_ [_subcommand_] [_flags_]

# COMMANDS

**org login web**
> 通过网页浏览器以 OAuth 方式对 org 进行身份验证

**org login jwt**
> 使用基于 JWT 的流程进行身份验证

**org create scratch**
> 创建用于开发的 scratch org

**org create sandbox**
> 创建沙箱 org

**org list**
> 列出所有已认证的 org

**org display**
> 显示 org 的详细信息

**project deploy start**
> 将源码部署到 org

**project retrieve start**
> 从 org 检索元数据

**project convert mdapi**
> 将 Metadata API 格式转换为源码格式

**apex run**
> 执行匿名 Apex 代码

**apex run test**
> 运行 Apex 测试

**data query**
> 执行 SOQL 查询

**data create record**
> 在 org 中创建记录

**package create**
> 创建软件包

**package install**
> 在 org 中安装软件包

**config set**
> 设置 CLI 配置值

**alias set**
> 为 org 创建别名

# PARAMETERS

**--target-org**, **-o** _alias_
> 通过用户名或别名指定目标 org

**--json**
> 以 JSON 格式输出结果

**--help**
> 显示命令的帮助信息

**--version**
> 显示 CLI 版本

# DESCRIPTION

**sf**（Salesforce CLI）是 Salesforce 开发的官方命令行界面。它管理 Salesforce DX 项目、创建和管理 scratch org 与沙箱、部署和检索源码、运行测试，并处理软件包开发。

CLI 采用分层命令结构，命令按主题分组（org、project、data、apex、package）。大多数命令接受 **--target-org** 标志来指定要操作的 org，以及 **--json** 用于机器可读输出。

配置存储在 **~/.sf/** 中，项目特定设置位于 **sfdx-project.json**。可以使用 **sf alias set** 为 org 创建别名以便使用。

# CONFIGURATION

**~/.sf/**
> 用户级配置目录，存储身份验证令牌、org 连接和 CLI 设置。

**sfdx-project.json**
> 项目级配置文件，定义源路径、命名空间、API 版本和软件包依赖。

**SF_ACCESS_TOKEN**
> 用于直接提供 org 访问令牌的环境变量。

# CAVEATS

较旧的 **sfdx** 命令已弃用；请迁移到 **sf** 命令。某些操作需要特定的 org 权限或 Salesforce 版本。Scratch org 有时间限制（默认 7 天），打包时还需考虑命名空间问题。

# HISTORY

Salesforce CLI 于 **2017** 年作为 **sfdx**（Salesforce DX CLI）随 Salesforce DX 开发模型一同推出。**sf** 命令于 **2022** 年推出，是一个经过重新设计、结构更优的统一 CLI。sfdx 风格的命令于 **2024** 年弃用，全面过渡到 sf。

# INSTALL

```brew: brew install sf```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [git](/man/git)(1), [jq](/man/jq)(1)
