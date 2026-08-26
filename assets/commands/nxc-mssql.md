# TAGLINE

通过 NetExec 测试 Microsoft SQL Server 凭据并执行查询

# TLDR

**针对目标测试 MSSQL 凭据**

```nxc mssql [192.168.1.100] -u [user] -p [password]```

**使用本地身份验证而非 Windows 身份验证**

```nxc mssql [target] -u [sa] -p [password] --local-auth```

**执行 SQL 查询**

```nxc mssql [target] -u [sa] -p [password] -q "[SELECT @@version]"```

**通过 xp_cmdshell 执行 OS 命令**

```nxc mssql [target] -u [sa] -p [password] -x "[whoami]"```

**检查权限提升路径**

```nxc mssql [target] -u [user] -p [password] -M mssql_priv```

**尝试提升为 sysadmin 权限**

```nxc mssql [target] -u [user] -p [password] -M mssql_priv -o ACTION=privesc```

# SYNOPSIS

**nxc mssql** _target_ [**-u** _user_] [**-p** _pass_] [_options_]

# PARAMETERS

**-u** _user_
> 用于身份验证的用户名。

**-p** _pass_
> 用于身份验证的密码。

**-q** _query_
> 在目标上执行 SQL 查询。

**-x** _cmd_
> 通过 xp_cmdshell 执行 OS 命令。

**--local-auth**
> 使用本地身份验证而非 Windows 域身份验证。

**--port** _port_
> MSSQL 端口（默认：1433）。

**-M** _module_
> 运行特定模块（例如 mssql_priv）。

**-o** _KEY=VALUE_
> 模块选项（例如 ACTION=privesc）。

**--put-file** _src_ _dst_
> 向目标系统上传文件。

**--get-file** _src_ _dst_
> 从目标系统下载文件。

# DESCRIPTION

**nxc mssql** 是 **NetExec**（前身为 CrackMapExec）的 Microsoft SQL Server 协议模块。它可测试凭据、执行 SQL 查询、运行 OS 命令，并支持对 MSSQL 目标进行权限提升。

该工具支持 Windows（NTLM/Kerberos）和本地 SQL Server 身份验证。它可以在多个目标上喷洒凭据、执行查询，并使用 **mssql_priv** 之类的模块检查和利用权限提升路径。

# CAVEATS

仅限授权的安全评估用途。使用前需获得适当授权。OS 命令执行要求目标上启用 xp_cmdshell。

# SEE ALSO

[nxc](/man/nxc)(1), [sqlcmd](/man/sqlcmd)(1)
