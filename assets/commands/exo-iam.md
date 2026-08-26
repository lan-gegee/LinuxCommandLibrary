# TAGLINE

Exoscale 身份与访问管理

# TLDR

**列出 API 密钥**

```exo iam api-key list```

**创建带角色的 API 密钥**

```exo iam api-key create [name] [role-name]```

**删除 API 密钥**

```exo iam api-key delete [key_id]```

**列出 IAM 角色**

```exo iam role list```

**创建 IAM 角色**

```exo iam role create [role-name] --policy [policy.json]```

**显示角色详情**

```exo iam role show [role-name]```

**显示组织策略**

```exo iam org-policy show```

# SYNOPSIS

**exo iam** _resource_ _action_ [_options_]

# PARAMETERS

**api-key** _ACTION_
> 管理 API 密钥（list、create、delete）。

**api-key create** _NAME_ _ROLE-NAME|ROLE-ID_
> 使用指定的角色名或角色 ID 创建新的 API 密钥。

**api-key list**
> 列出所有 API 密钥。

**api-key delete** _ID_
> 删除一个 API 密钥。

**role** _ACTION_
> 管理 IAM 角色（list、create、delete、show、update）。

**role create** _NAME_ **--policy** _FILE_
> 使用策略文件创建新的 IAM 角色。

**role show** _NAME|ID_
> 显示 IAM 角色的详情。

**role update** _NAME|ID_ **--policy** _FILE_
> 更新现有 IAM 角色的策略。

**org-policy** _ACTION_
> 管理组织级 IAM 策略（show、reset）。

**--help**
> 显示帮助信息。

# DESCRIPTION

**exo iam** 管理 Exoscale 云的身份与访问控制。它处理用于身份验证的 API 密钥以及用于访问控制的角色。

API 密钥提供对 Exoscale 资源的编程访问。每个密钥都绑定到一个角色，该角色通过策略定义其权限。角色包含的策略会指定在 compute、dns、dbaas、sos 和 block-storage 等服务中允许和拒绝的操作。org-policy 子命令管理组织级默认策略。

# CAVEATS

密钥的机密内容仅在创建时显示一次。已删除的密钥无法恢复。角色会影响所有资源。根密钥拥有完全访问权限。

# HISTORY

exo iam 是 **Exoscale CLI** 的一部分，为 Exoscale 云账户提供安全与访问管理。

# INSTALL

```dnf: sudo dnf install exo```

```pacman: sudo pacman -S exo```

```apk: sudo apk add exoscale```

```nix: nix profile install nixpkgs#exo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[exo](/man/exo)(1), [exo-compute](/man/exo-compute)(1)
