# TAGLINE

结合 Active Directory 的特权命令执行

# TLDR

**以 root 身份运行命令**

```dzdo [command]```

**以指定用户身份运行**

```dzdo -u [username] [command]```

**以登录 shell 运行**

```dzdo -i```

**运行一个 root shell**

```dzdo -s```

**列出用户的权限**

```dzdo -l```

# SYNOPSIS

**dzdo** [_options_] [_command_]

# PARAMETERS

_COMMAND_
> 要以提升权限执行的命令。

**-u** _USER_
> 以指定用户身份运行。

**-i**
> 运行登录 shell。

**-l**
> 列出允许的命令。

**-s**
> 运行 shell 而非特定命令。

**-n**
> 非交互式（不提示输入密码）。

**-H**
> 将 HOME 环境变量设为目标用户的主目录。

**-k**
> 使用户缓存的凭据失效。

**-v**
> 校验/延长凭据而不运行命令。

**-V**
> 显示版本信息。

# DESCRIPTION

**dzdo** 是 Centrify 对 sudo 的替代品，通过与 Active Directory 集成提供特权命令执行。它允许用户根据集中管理的策略以 root 或其他用户身份运行命令。

dzdo 与 Centrify 的 DirectControl 集成，在 Unix/Linux 和 Windows 系统之间实现统一身份管理。策略在 Active Directory 中管理，而非本地 sudoers 文件。

该工具提供与 sudo 类似的功能，但具备企业级的认证和授权特性。

# CONFIGURATION

**/etc/centrifydc/centrifydc.conf**
> Centrify DirectControl 配置文件，控制 AD 集成和认证设置。

# CAVEATS

需要 Centrify DirectControl。策略在 AD 中集中管理。在边界情况下行为可能与 sudo 不同。需要企业授权许可。

# HISTORY

dzdo 是 **Centrify DirectControl**（现为 **Delinea**）的一部分，为 企业环境提供兼容 sudo 的权限提升并集成 Active Directory。

# SEE ALSO

[doas](/man/doas)(1), [su](/man/su)(1), [sudo](/man/sudo)(8)
