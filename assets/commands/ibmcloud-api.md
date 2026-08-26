# TAGLINE

设置或显示 IBM Cloud API 端点

# TLDR

**显示当前 API 端点**

```ibmcloud api```

**设置 API 端点**

```ibmcloud api [https://cloud.ibm.com]```

**设置私有端点**

```ibmcloud api https://private.cloud.ibm.com```

通过 VPC **设置私有端点**

```ibmcloud api https://private.cloud.ibm.com --vpc```

**取消 API 端点**

```ibmcloud api --unset```

**跳过 SSL 校验**

```ibmcloud api [endpoint] --skip-ssl-validation```

# SYNOPSIS

**ibmcloud** **api** [_endpoint_] [_options_]

# PARAMETERS

**--unset**
> 清除 API 端点。

**--skip-ssl-validation**
> 跳过 SSL 校验（不推荐）。

**--vpc**
> 私有端点使用 VPC 连接。

# DESCRIPTION

**ibmcloud api** 设置或显示 IBM Cloud API 端点。如果既未指定端点也未指定 **--unset**，则显示当前 API 端点。默认公共端点是 https://cloud.ibm.com。私有网络访问请使用 https://private.cloud.ibm.com。使用 **ibmcloud login** 登录之前必须先设置 API 端点。

# SEE ALSO

[ibmcloud](/man/ibmcloud)(1), [ibmcloud-login](/man/ibmcloud-login)(1)
