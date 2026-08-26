# TAGLINE

在远程主机上执行命令

# TLDR

在远程主机上执行**命令**

```rexec -h remote_host ls -l```

指定**远程用户名**

```rexec -u username -h remote_host ps aux```

抑制**错误流**的创建

```rexec -n -h remote_host ls -l```

指定**远程端口**

```rexec -P 1234 -h remote_host ls -l```

# SYNOPSIS

**rexec** [_options_] _command_

# PARAMETERS

**-h**, **--host** _host_
> 指定远程主机

**-u**, **--username** _user_
> 指定远程用户名

**-P**, **--port** _port_
> 指定远程端口

**-n**, **--noerr**
> 不创建单独的错误流

**-d**, **--password** _password_
> 指定密码（使用 '-' 表示从 stdin 读取）

# DESCRIPTION

**rexec** 使用 rexec 协议（TCP 端口 512）在远程主机上执行命令。它以用户名和密码进行身份验证，然后在远程系统上运行指定的命令。

注意：rexec 以明文传输凭据和数据，是不安全的。请使用 SSH 进行加密的远程命令执行。

# CAVEATS

以未加密方式传输凭据和数据。不建议在不受信任的网络上使用。建议改用 SSH 作为安全替代方案。

# HISTORY

属于 **GNU inetutils** 的一部分，提供经典的 Unix 网络工具。出于安全原因，已在很大程度上被 SSH 取代。

# SEE ALSO

[ssh](/man/ssh)(1), [rsh](/man/rsh)(1), [rlogin](/man/rlogin)(1)
