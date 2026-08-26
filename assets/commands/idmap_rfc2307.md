# TAGLINE

使用 RFC 2307 LDAP 模式的 Samba ID 映射后端

# TLDR

**在 smb.conf 中配置**

```idmap config DOMAIN : backend = rfc2307```

**设置范围**

```idmap config DOMAIN : range = 10000-99999```

# SYNOPSIS

**idmap_rfc2307** is a Samba configuration module

# PARAMETERS

**backend**
> 设置为 rfc2307。

**range**
> UID/GID 范围。

**ldap_server**
> LDAP 服务器模式。

**bind_path_user**
> 用户搜索基准（base）。

**bind_path_group**
> 组搜索基准（base）。

# DESCRIPTION

**idmap_rfc2307** 是一个使用 RFC 2307 LDAP 模式的 Samba ID 映射后端。它将 Windows SID 映射到存储在 LDAP 中的 Unix UID/GID。

该后端从 Active Directory 或 LDAP 中读取 uidNumber 和 gidNumber 属性。它提供跨系统一致的 ID 映射。

# CAVEATS

Samba 配置模块。需要支持 RFC 2307 模式的 LDAP。需要 AD 集成。

# HISTORY

idmap_rfc2307 是 **Samba** 的组成部分，用于企业级 Unix/Windows ID 映射。

# SEE ALSO

