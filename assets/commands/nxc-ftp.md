# TAGLINE

netExec FTP 模块

# TLDR

**检查 FTP 凭据**

```nxc ftp [target] -u [user] -p [password]```

**匿名登录检查**

```nxc ftp [target] -u anonymous -p anonymous```

**列出目录**

```nxc ftp [target] -u [user] -p [password] --ls [/path]```

**下载文件**

```nxc ftp [target] -u [user] -p [password] --get [file]```

# SYNOPSIS

**nxc** **ftp** [_target_] [_options_]

# PARAMETERS

_TARGET_
> FTP 服务器地址。

**-u** _USER_
> 用户名。

**-p** _PASSWORD_
> 密码。

**--ls** _PATH_
> 列出目录。

**--get** _FILE_
> 下载文件。

**--put** _FILE_
> 上传文件。

**--help**
> 显示帮助信息。

# DESCRIPTION

**nxc ftp** 是 NetExec 的 FTP 模块，用于测试 FTP 服务器的安全性。

该工具可检查凭据和访问权限，是 NetExec 套件的一部分。

# CAVEATS

安全工具。仅限授权使用。NetExec 的组成部分。

# HISTORY

nxc ftp 在 NetExec 中提供 **FTP 渗透测试**功能。

# SEE ALSO

[nxc](/man/nxc)(1), [ftp](/man/ftp)(1), [lftp](/man/lftp)(1)
