# TAGLINE

结束当前的 IBM Cloud CLI 会话

# TLDR

**从 IBM Cloud 注销**

```ibmcloud logout```

**注销并清除缓存**

```ibmcloud logout -a```

# SYNOPSIS

**ibmcloud logout** [_options_]

# PARAMETERS

**-a**, **--all**
> 清除所有缓存数据。

**--help**
> 显示帮助信息。

# DESCRIPTION

**ibmcloud logout** 结束当前的 IBM Cloud CLI 会话。它会移除存储的凭据和令牌。

该命令在本地清除认证状态。切换账户前或出于安全考虑时使用。

# CAVEATS

仅影响本地凭据。API 密钥仍然有效。之后需要重新登录。

# HISTORY

ibmcloud logout 是 **IBM Cloud** CLI 身份验证系统的组成部分。

# SEE ALSO

[ibmcloud](/man/ibmcloud)(1), [ibmcloud-login](/man/ibmcloud-login)(1)
