# TAGLINE

管理 TeX Live 的 GPG 验证密钥

# TLDR

**列出 GPG 密钥**

```tlmgr key list```

**添加密钥**

```tlmgr key add [keyfile]```

**移除密钥**

```tlmgr key remove [keyid]```

# SYNOPSIS

**tlmgr key** _action_ [_args_]

# PARAMETERS

**list**
> 列出已安装的密钥。

**add** _file_
> 从文件添加 GPG 密钥。

**remove** _keyid_
> 按 ID 移除密钥。

# DESCRIPTION

**tlmgr key** 管理用于 TeX Live 软件包验证的 GPG 密钥。确保软件包来自可信来源。TeX Live Manager 安全功能的组成部分。

# SEE ALSO

[tlmgr-repository](/man/tlmgr-repository)(1), [tlmgr](/man/tlmgr)(1)
