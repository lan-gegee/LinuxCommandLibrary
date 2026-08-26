# TAGLINE

构建和部署全栈 Web 与移动应用

# TLDR

**创建**新的 Amplify 应用

```aws amplify create-app --name [app_name] --repository [repo_url]```

**列出**账户中的所有 Amplify 应用

```aws amplify list-apps```

为应用**创建**新分支

```aws amplify create-branch --app-id [app_id] --branch-name [branch_name]```

**启动**部署作业

```aws amplify start-job --app-id [app_id] --branch-name [branch_name] --job-type RELEASE```

**获取**特定应用的详细信息

```aws amplify get-app --app-id [app_id]```

为应用**关联**自定义域名

```aws amplify create-domain-association --app-id [app_id] --domain-name [example.com]```

**删除**Amplify 应用

```aws amplify delete-app --app-id [app_id]```

# SYNOPSIS

**aws amplify** _command_ [_options_]

# DESCRIPTION

**AWS Amplify** 让开发者能够借助集成的 CI/CD 工作流开发和部署由云驱动的移动与 Web 应用。该服务由两个主要部分组成：用于持续交付和托管的 **Amplify Hosting**，以及为客户端应用开发提供 SDK、库和工具的 **Amplify Framework**。

**Amplify Hosting** 提供完全托管、可直接对接 Git 仓库的持续部署托管服务。每次代码提交都会自动构建并部署 Web 应用，支持 React、Angular、Vue、Next.js 等现代框架以及静态站点生成器。

该服务提供以下功能：

> **持续部署** - 每次提交都自动从 Git 分支构建并部署

> **分支部署** - 将不同分支部署到独立的环境，用于功能测试和预发布

> **自定义域名** - 关联自定义域名，SSL/TLS 证书自动管理

> **后端环境** - 将前端分支连接到不同的后端环境

> **访问控制** - 通过密码认证保护分支的预览环境

**Amplify Framework** 提供客户端库和 CLI 工具，可将认证、API、存储和分析等 AWS 服务集成到移动与 Web 应用中，无需管理后端基础设施。

# AVAILABLE COMMANDS

**create-app**
> 从仓库或手动部署创建新的 Amplify 应用

**delete-app**
> 永久删除 Amplify 应用及其所有关联资源

**get-app**
> 检索特定应用的详细信息

**list-apps**
> 列出当前区域的所有 Amplify 应用

**update-app**
> 更新应用配置，包括构建设置和环境变量

**create-branch**
> 创建用于持续部署的新分支

**delete-branch**
> 删除分支并停止其部署

**list-branches**
> 列出应用的所有分支

**start-job**
> 手动触发构建和部署作业

**stop-job**
> 取消正在运行的构建或部署作业

**list-jobs**
> 列出某个分支的构建和部署作业

**create-deployment**
> 为手动部署的应用创建部署

**start-deployment**
> 启动手动部署

**create-domain-association**
> 为 Amplify 应用关联自定义域名

**update-domain-association**
> 更新域名配置和 SSL 设置

**delete-domain-association**
> 移除自定义域名的关联

**create-webhook**
> 创建 webhook 以便从外部来源触发构建

**create-backend-environment**
> 为应用创建后端环境

**get-job**
> 获取特定构建和部署作业的详情

**tag-resource**
> 为 Amplify 资源添加元数据标签

# CAVEATS

Git 仓库集成需要有效的凭证以及相应的仓库权限。自定义域名验证需要更改 DNS 配置。如果构建设置与项目的框架要求不匹配，构建可能失败。删除应用会永久移除所有分支、部署及关联数据。

# HISTORY

**AWS Amplify** 在 **AWS re:Invent 2017** 上发布，是面向移动与 Web 应用开发的框架和工具链。**Amplify Console**（现名 Amplify Hosting）于 **2018 年 11 月**上线，为现代 Web 应用提供持续部署和托管能力。

# INSTALL

```brew: brew install aws-amplify```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws-cloudfront](/man/aws-cloudfront)(1), [aws-codecommit](/man/aws-codecommit)(1), [aws-cognito-idp](/man/aws-cognito-idp)(1), [aws](/man/aws)(1)
