# TAGLINE

通过远程 shell 在远程主机上执行命令

# TLDR

在远程主机上执行**命令**

```rsh remote_host ls -l```

以**指定用户名**执行

```rsh remote_host -l username ls -l```

将 **stdin 重定向**到 /dev/null 后执行

```rsh remote_host --no-err ls -l```

# SYNOPSIS

**rsh** [_options_] _host_ [_command_]

# PARAMETERS

**-l**, **--user** _username_
> 指定远程用户名

**--no-err**
> 将 stdin 重定向自 /dev/null

# DESCRIPTION

**rsh**（remote shell）使用 RSH 协议在远程主机上执行命令。它提供基本的远程命令执行能力。

注意：rsh 以未加密的方式传输数据，是不安全的。需要安全的远程命令执行请使用 SSH。

# CAVEATS

以明文传输凭据和数据。不建议在不可信的网络中使用。SSH 是安全的替代方案。

# HISTORY

属于 **GNU inetutils**，提供经典的 Unix 网络工具。出于安全原因已被 SSH 取代。

# INSTALL

```dnf: sudo dnf install rsh```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ssh](/man/ssh)(1), [rlogin](/man/rlogin)(1), [rcp](/man/rcp)(1)
