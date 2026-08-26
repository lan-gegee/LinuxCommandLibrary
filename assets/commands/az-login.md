# TAGLINE

进行 Azure 身份验证

# TLDR

以交互方式**登录**

```az login```

使用客户端密码以**服务主体**身份登录

```az login --service-principal -u [app-id] -p [client-secret] --tenant [tenant-id]```

使用证书以**服务主体**身份登录

```az login --service-principal -u [app-id] --certificate [/path/to/cert.pem] --tenant [tenant-id]```

使用**托管标识**登录

```az login --identity```

使用**设备代码**登录

```az login --use-device-code```

登录到**特定租户**

```az login --tenant [tenant-id]```

# SYNOPSIS

**az login** [_options_]

# DESCRIPTION

**az login** 让 Azure CLI 通过你的 Azure 账户完成身份验证。它支持多种身份验证方式，包括交互式浏览器登录、服务主体、托管标识和设备代码流。

默认情况下它使用用户账户登录：在 Windows 上使用 Web Account Manager（WAM），在 Linux 和 macOS 上使用基于浏览器的登录，当没有可用浏览器时回退到设备代码流。该命令会将身份验证令牌存储在本地，供后续 Azure CLI 命令使用。

# PARAMETERS

**--service-principal**
> 以服务主体身份登录

**-u**, **--username** _name_
> 用户名或服务主体的客户端 ID

**-p**, **--password** _password_
> 用户密码或服务主体的机密。未提供时会提示输入。不再接受证书；请改用 --certificate

**--certificate** _path_
> 包含服务主体密钥和公钥证书的 PEM 文件

**-t**, **--tenant** _id_
> Microsoft Entra 租户 ID 或域。服务主体登录必填

**--identity**, **-i**
> 使用托管标识登录

**--client-id** _id_
> 用户分配的托管标识的客户端 ID（与 --identity 一起使用）

**--federated-token** _token_
> 用于 OIDC 令牌交换的联合令牌（例如 GitHub Actions、Workload Identity）

**--use-device-code**
> 使用设备代码流（适用于没有浏览器的系统）

**--allow-no-subscriptions**
> 允许登录没有订阅的租户，对 az ad 等租户级命令很有用

**--skip-subscription-discovery**
> 登录期间跳过订阅发现。需要 --tenant

**--scope** _scope_
> 授权请求中使用的 OAuth 作用域

# AUTHENTICATION METHODS

**Interactive**（默认）
> 打开浏览器进行身份验证

**Service Principal**
> 面向应用程序的自动化身份验证

**Managed Identity**
> 面向 Azure 资源（虚拟机、App Service 等）

**Device Code**
> 面向没有浏览器访问能力的系统

# WORKFLOW

```bash
# Interactive login
az login

# Select subscription
az account set --subscription "My Subscription"

# Verify login
az account show
```

# CAVEATS

令牌存储在 ~/.azure 目录中。交互式登录需要浏览器。服务主体凭证应妥善保管。托管标识仅在 Azure 资源上有效。多次登录会创建多个上下文。

# HISTORY

**az login** 自 **2017** 年的 Azure CLI 2.0 起就是其组成部分，并随着 Azure 身份平台的演进支持了各种身份验证方式。

# INSTALL

```dnf: sudo dnf install azure-cli```

```pacman: sudo pacman -S azure-cli```

```zypper: sudo zypper install azure-cli```

```brew: brew install azure-cli```

```nix: nix profile install nixpkgs#azure-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[az](/man/az)(1), [az-logout](/man/az-logout)(1), [az-account](/man/az-account)(1)

# RESOURCES

```[Source code](https://github.com/Azure/azure-cli)```

```[Documentation](https://learn.microsoft.com/en-us/cli/azure/reference-index)```

<!-- verified: 2026-06-18 -->
