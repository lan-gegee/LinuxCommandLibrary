# TAGLINE

Google Cloud 的身份与访问管理

# TLDR

**列出当前项目中的服务账号**

```gcloud iam service-accounts list```

**创建服务账号**

```gcloud iam service-accounts create [name] --display-name="[description]"```

**为服务账号创建密钥**

```gcloud iam service-accounts keys create [key.json] --iam-account=[email]```

**列出服务账号的密钥**

```gcloud iam service-accounts keys list --iam-account=[email]```

**列出所有预定义角色**

```gcloud iam roles list```

**描述特定角色及其权限**

```gcloud iam roles describe [roles/editor]```

**列出资源可授予的角色**

```gcloud iam list-grantable-roles [//cloudresourcemanager.googleapis.com/projects/my-project]```

# SYNOPSIS

**gcloud iam** _group_ _command_ [_options_]

# PARAMETERS

**service-accounts** _CMD_
> 管理服务账号（create、delete、describe、list、update、add/get/set-iam-policy-binding、keys）。

**roles** _CMD_
> 管理 IAM 角色（create、delete、describe、list、update、copy、undelete）。

**policies** _CMD_
> 管理 IAM 拒绝策略（deny policies）。

**workload-identity-pools** _CMD_
> 管理用于外部身份联合的工作负载身份池。

**list-grantable-roles** _RESOURCE_
> 列出给定资源可授予的角色。

**--iam-account** _EMAIL_
> 服务账号邮箱（与 service-accounts keys 子命令配合使用）。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gcloud iam** 提供对 Google Cloud 身份与访问管理系统的命令行访问，该系统控制谁（身份）以何种访问级别（角色）操作哪些资源。

服务账号代表应用和服务的非人类身份。可以为服务账号创建密钥，以便从外部环境进行身份验证。角色将相关权限打包成可分配的单元。IAM 策略则把角色绑定到特定资源上的主体（用户、组或服务账号）。

注意：向项目添加角色绑定要通过 **gcloud projects add-iam-policy-binding** 完成，而不是直接使用 **gcloud iam** 命令组。

# CAVEATS

IAM 变更可能需要一段时间才能传播生效。服务账号密钥是安全敏感凭据，应定期轮换。角色绑定是叠加式的；移除访问权限需要显式修改策略。

# HISTORY

gcloud iam 属于 **Google Cloud SDK**，用于管理 IAM——Google Cloud 的身份与访问控制系统。

# SEE ALSO

[gcloud](/man/gcloud)(1), [gcloud-auth](/man/gcloud-auth)(1), [gcloud-config](/man/gcloud-config)(1), [gcloud-projects](/man/gcloud-projects)(1)
