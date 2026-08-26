# TAGLINE

Keycloak 管理 CLI

# TLDR

**登录 Keycloak**

```kcadm.sh config credentials --server [url] --realm [master] --user [admin]```

**创建 realm**

```kcadm.sh create realms -s realm=[name] -s enabled=true```

**创建用户**

```kcadm.sh create users -r [realm] -s username=[user] -s enabled=true```

**获取用户**

```kcadm.sh get users -r [realm]```

**更新用户**

```kcadm.sh update users/[id] -r [realm] -s email=[email]```

**设置密码**

```kcadm.sh set-password -r [realm] --username [user] --new-password [pass]```

# SYNOPSIS

**kcadm.sh** _command_ [_options_]

# PARAMETERS

**config credentials**
> 配置身份验证。

**create** _RESOURCE_
> 创建资源。

**get** _RESOURCE_
> 获取资源。

**update** _RESOURCE_
> 更新资源。

**delete** _RESOURCE_
> 删除资源。

**-r** _REALM_
> 目标 realm。

**-s** _ATTR=VALUE_
> 设置属性。

**--help**
> 显示帮助信息。

# DESCRIPTION

**kcadm.sh** 是 Keycloak 的管理 CLI。它管理 Keycloak 身份与访问管理配置。

该工具提供对 Keycloak 的完整管理能力，可以创建用户、realm、客户端和角色。

# CAVEATS

需要 Java。Keycloak 必须处于运行状态。需要管理员凭据。

# HISTORY

kcadm.sh 是开源身份与访问管理方案 **Keycloak** 的官方管理 CLI。

# SEE ALSO

[keycloak](/man/keycloak)(1), [curl](/man/curl)(1)
