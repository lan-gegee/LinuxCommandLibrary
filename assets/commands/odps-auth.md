# TAGLINE

管理 MaxCompute 身份验证

# TLDR

**登录 ODPS**

```odps auth login```

**配置凭证**

```odps auth config --access-id [id] --access-key [key]```

**显示当前用户**

```odps auth whoami```

**登出**

```odps auth logout```

# SYNOPSIS

**odps** **auth** [_command_] [_options_]

# PARAMETERS

**login**
> 向 ODPS 进行身份验证。

**logout**
> 移除凭证。

**config**
> 配置身份验证。

**whoami**
> 显示当前身份。

**--access-id** _ID_
> 访问密钥 ID。

**--access-key** _KEY_
> 访问密钥 Secret。

**--help**
> 显示帮助信息。

# DESCRIPTION

**odps auth** 管理 MaxCompute 的身份验证，配置访问凭证。

该工具负责登录与凭证的存储。属于 ODPS CLI 的一部分。

# CAVEATS

凭证保存在本地。属于阿里云 ODPS 工具的一部分。

# HISTORY

odps auth 为阿里云 MaxCompute 提供**身份验证管理**功能。

# SEE ALSO

[odps](/man/odps)(1), [odpscmd](/man/odpscmd)(1)
