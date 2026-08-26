# TAGLINE

带交互式终端 UI 的 AWS SSO 会话与凭证管理器

# TLDR

**启动交互式 TUI**，选择 SSO profile、账户和角色

```sesh```

直接向指定的 SSO、账户和角色**认证**

```sesh [MyOrg] [MyAccount] [AdminRole]```

为特定会话**在浏览器中打开 AWS 控制台**

```sesh [MyOrg] [MyAccount] [AdminRole] -b```

以指定区域**设置凭证**

```sesh [MyOrg] [MyAccount] [AdminRole] -r [eu-west-1]```

**使用自定义的 AWS profile 名称**

```sesh [MyOrg] [MyAccount] [AdminRole] --profile [production]```

**显示当前会话的身份**

```sesh -w```

**输出环境变量**，供 Shell eval 集成使用

```sesh --eval [MyOrg] [MyAccount]```

# SYNOPSIS

**sesh** [**-v**|**--version**] [**-b**|**--browser**] [**-w**|**--whoami**] [**-r**|**--region** _region_] [**-e**|**--eval**] [**-p**|**--profile** _name_] [_ssoname_ _accountname_ [_rolename_]]

# PARAMETERS

**-v**, **--version**
> 显示版本信息并退出

**-b**, **--browser**
> 在默认浏览器中打开 AWS 控制台，而不是设置凭证

**-w**, **--whoami**
> 打印活动会话对应的 AWS 账户名称和 ID

**-r** _region_, **--region** _region_
> 指定会话使用的 AWS 区域

**-e**, **--eval**
> 向 stdout 输出用于设置 AWS 环境变量的 shell export 命令；供 shell 集成使用

**-p** _name_, **--profile** _name_
> 为凭证条目使用自定义的 AWS profile 名称；工具会记住每个账户与角色组合对应的 profile 名称

# DESCRIPTION

**awsesh**（调用名为 **sesh**）是一款轻量级命令行工具，用于管理 AWS SSO 会话和凭证。它提供了基于 Charm 库（Bubble Tea、Bubbles、Lip Gloss）构建的交互式终端用户界面，用户可以浏览 SSO profile、通过模糊搜索按名称筛选账户、选择角色并建立已认证的会话。

该工具有两种主要运行模式。在交互式 TUI 模式下，不带位置参数运行 **sesh** 会启动全屏终端界面，用户可以在其中添加、编辑和删除 SSO profile，浏览账户并进行筛选，设置每个账户的区域，指定自定义 profile 名称，以及直接在 AWS 控制台中打开账户。在 CLI 模式下，在命令行中提供 SSO 名称、账户名称以及可选的角色名称即可直接完成会话认证，无需 TUI。

会话建立后，awsesh 会将临时凭证写入 AWS 共享凭证文件（通常为 **~/.aws/credentials**），并可通过 shell 集成设置以下环境变量：**AWS_PROFILE**、**AWS_REGION**、**AWS_ACCESS_KEY_ID**、**AWS_SECRET_ACCESS_KEY**、**AWS_SESSION_TOKEN** 和 **AWS_SESSION_EXPIRATION**。对于拥有超过 100 个 SSO 账户的组织，角色采用懒加载方式，以避免触发 AWS API 速率限制。

# CONFIGURATION

awsesh 自身的配置遵循 XDG Base Directory 规范，同时尊重标准的 AWS 配置环境变量：

**AWS_CONFIG_FILE**
> AWS 配置文件路径（默认：~/.aws/config）

**AWS_SHARED_CREDENTIALS_FILE**
> AWS 共享凭证文件路径（默认：~/.aws/credentials）

Shell 集成通过在你的 shell 配置文件（~/.bashrc、~/.zshrc 或 fish 配置）中添加一个包装函数来配置：

```sesh() { eval "$(command sesh --eval "$@")"; }```

这样环境变量就能在当前 shell 会话中生效，这是兼容 **Starship** 提示符等工具所必需的。

# CAVEATS

该应用会直接修改 AWS 凭证文件（~/.aws/credentials。拥有复杂或手工维护的凭证配置的用户应在首次使用前备份该文件。此工具目前处于 beta 阶段，尚未发布稳定的 1.0 版本。beta 分支上有一个基于 API 架构的 TypeScript 重写版本，支持插件和脚本扩展。

# HISTORY

**awsesh** 由 **Elva Labs** 的 **Alvin Johansson** 和 **Sebastian Bille** 创建，仓库于 **2025 年 3 月**发布在 GitHub 上。首个打标签的版本（v0.0.1）于 **2025 年 3 月 25 日**发布。该项目使用 Go 编写，基于 MIT 许可证授权，并在 2026 年间持续以 beta 版本积极开发。

# SEE ALSO

[aws-sso](/man/aws-sso)(1), [aws-vault](/man/aws-vault)(1), [aws-configure](/man/aws-configure)(1), [aws](/man/aws)(1)
