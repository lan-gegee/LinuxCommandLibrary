# TAGLINE

管理身份与访问管理（IAM）

# TLDR

**列出 API 密钥**

```ibmcloud iam api-keys```

**创建 API 密钥**

```ibmcloud iam api-key-create [name]```

**列出服务 ID**

```ibmcloud iam service-ids```

**显示访问组**

```ibmcloud iam access-groups```

**获取用户策略**

```ibmcloud iam user-policies [user]```

# SYNOPSIS

**ibmcloud iam** _command_ [_options_]

# PARAMETERS

_COMMAND_
> IAM 命令。

**api-keys**
> 列出 API 密钥。

**api-key-create**
> 创建 API 密钥。

**service-ids**
> 列出服务 ID。

**access-groups**
> 列出访问组。

**user-policies**
> 显示用户策略。

**--help**
> 显示帮助信息。

# DESCRIPTION

**ibmcloud iam** 管理身份与访问管理（Identity and Access Management）。它处理 API 密钥、服务 ID、访问组和策略。

该工具控制 IBM Cloud 资源的身份验证和授权。它支持安全的服务间通信。

# CAVEATS

需要账户所有者或管理员权限。策略更改立即生效。提供审计跟踪。

# HISTORY

ibmcloud iam 是 **IBM Cloud** CLI 的 IAM 管理组件。

# SEE ALSO

[ibmcloud](/man/ibmcloud)(1), [ibmcloud-login](/man/ibmcloud-login)(1)
