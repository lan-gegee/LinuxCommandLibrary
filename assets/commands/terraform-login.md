# TAGLINE

向远程主机认证 Terraform CLI

# TLDR

**登录** HCP Terraform（默认）

```terraform login```

**登录**指定的 **Terraform Enterprise** 实例

```terraform login [hostname]```

# SYNOPSIS

**terraform login** [_hostname_]

# PARAMETERS

**hostname**
> 要认证的 Terraform 服务主机名。默认为 **app.terraform.io**（HCP Terraform）。对于 Terraform Enterprise，请指定你组织的主机名

# DESCRIPTION

**terraform login** 为 **HCP Terraform**（原 Terraform Cloud）、**Terraform Enterprise** 或任何实现了 Terraform 登录协议的主机获取并保存 API 令牌。该命令会启动网页浏览器，引导用户前往服务的登录页面。授权后，Terraform 通过带 **PKCE** 的 **OAuth 2.0** 接收 API 令牌并将其保存在本地。

默认情况下，令牌以明文形式存储在 **~/.terraform.d/credentials.tfrc.json** 中。也可以配置**凭据助手**（credentials helper），把令牌存储到外部的机密管理系统中。

# CONFIGURATION

令牌默认存储在 **~/.terraform.d/credentials.tfrc.json** 中。可以通过 **TF_CLI_CONFIG_FILE** 环境变量覆盖该位置。令牌也可按 **TF_TOKEN_\<hostname_with_underscores\>** 的命名模式通过环境变量提供（例如 **TF_TOKEN_app_terraform_io**）。CLI 配置中的 **credentials_helper** 块可与外部机密存储集成。

# CAVEATS

该命令是**交互式**的且会启动网页浏览器，因此不能在无头或 CI/CD 环境中使用。自动化场景请通过环境变量或凭据文件手动配置凭据。令牌默认以**明文**存储。Terraform 不会自动处理令牌刷新或过期；令牌过期后需重新运行 **terraform login**。只有**用户令牌**或**团队令牌**可用；组织令牌不能用于 CLI 操作。

# HISTORY

于 **2020** 年初随 **Terraform v0.12.21** 与 **terraform logout** 一同推出，用于简化 CLI 与 Terraform Cloud 和 Enterprise 的连接，取代了此前手动生成并配置 API 令牌的流程。

# INSTALL

```pacman: sudo pacman -S terraform```

```nix: nix profile install nixpkgs#terraform```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[terraform](/man/terraform)(1), [terraform-logout](/man/terraform-logout)(1), [terraform-console](/man/terraform-console)(1)
