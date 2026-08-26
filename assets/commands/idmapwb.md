# TAGLINE

指 Samba 中 Winbind 的 ID 映射功能

# TLDR

**在 smb.conf 中配置**

```idmap config * : backend = tdb```

**设置范围**

```idmap config * : range = 10000-999999```

# SYNOPSIS

**idmapwb** is a Winbind ID mapping component

# PARAMETERS

**backend**
> ID 映射后端类型。

**range**
> UID/GID 范围分配。

**read only**
> 只读模式。

# DESCRIPTION

**idmapwb** 指 Samba 中 Winbind 的 ID 映射功能。它将 Windows SID 转换为 Unix UID 和 GID。

该组件使用可配置的后端，如 tdb、ad 或 rfc2307。它让 Unix 系统能够与 Windows 域用户协同工作。

# CAVEATS

属于 Samba/Winbind。通过 smb.conf 配置。需要加入域。

# HISTORY

idmapwb 是 **Samba Winbind** 的组成部分，用于 Windows-Unix 身份集成。

# SEE ALSO

[wbinfo](/man/wbinfo)(1)
