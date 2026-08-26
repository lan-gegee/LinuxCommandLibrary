# TAGLINE

管理 Azure 订阅和访问令牌

# TLDR

**列出已登录账户的所有订阅**（默认仅显示启用的）

```az account list```

**显示当前订阅**

```az account show```

**设置活动订阅**

```az account set --subscription [subscription-id-or-name]```

为当前账户**获取访问令牌**

```az account get-access-token```

为 Microsoft Graph **获取访问令牌**

```az account get-access-token --resource-type ms-graph```

跨所有云**列出所有订阅**，包括禁用的

```az account list --all```

**列出当前订阅支持的区域**

```az account list-locations```

**清除所有缓存的订阅**

```az account clear```

# SYNOPSIS

**az account** _subcommand_ [_options_]

# DESCRIPTION

**az account** 管理 Azure 订阅信息和访问令牌。它可以列出、选择和管理与你的 Azure 账户关联的订阅，并获取用于以编程方式访问 Azure 资源的访问令牌。

在使用多个 Azure 订阅并在 CLI 会话中切换时，这个命令组必不可少。

# SUBCOMMANDS

**Subscription Management**
> list, show, set, clear, list-locations

**Access Tokens**
> get-access-token

**Management Groups**
> management-group create, management-group delete, management-group list, management-group show, management-group update

**Locks**
> lock create, lock delete, lock list, lock show, lock update

**Aliases (Extension)**
> alias create, alias delete, alias list, alias show

**Subscriptions (Extension)**
> subscription list, subscription show

# PARAMETERS

**--subscription**, **-s** _value_
> 要使用的订阅名称或 ID（`set`、`show`、`get-access-token` 接受）

**--all**
> （`list`）包含所有云、所有状态的订阅，而不仅是启用的。

**--refresh**
> （`list`）从服务器获取最新订阅，而非本地缓存。

**--resource-type** _value_
> 访问令牌的资源类型。可接受的值：**aad-graph**、**arm**、**batch**、**data-lake**、**media**、**ms-graph**、**oss-rdbms**。

**--resource** _uri_
> 访问令牌的 Azure 资源终结点 URI（Microsoft Entra v1.0）。

**--scope** _value_
> 访问令牌的作用域，空格分隔（Microsoft Entra v2.0）。默认为 Azure Resource Manager。

**--tenant**, **-t** _value_
> 跨租户令牌请求使用的租户 ID。仅适用于用户账户和服务主体账户。

# CAVEATS

访问令牌的有效期最短 5 分钟，最长 60 分钟。令牌输出中的 **expires_on** 字段是 POSIX 时间戳（UTC），而 **expiresOn** 是本地日期时间。自 2025 年 9 月起，Microsoft 要求用户身份启用 MFA；脚本应迁移到服务主体或托管标识。

# INSTALL

```dnf: sudo dnf install azure-cli```

```pacman: sudo pacman -S azure-cli```

```zypper: sudo zypper install azure-cli```

```brew: brew install azure-cli```

```nix: nix profile install nixpkgs#azure-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[az](/man/az)(1), [az-login](/man/az-login)(1), [az-logout](/man/az-logout)(1)
