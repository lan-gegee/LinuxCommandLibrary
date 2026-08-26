# TAGLINE

测试 SSH 凭据并执行命令

# TLDR

**测试 SSH 凭据**

```nxc ssh [192.168.1.0/24] -u [user] -p [password]```

**使用密钥文件测试**

```nxc ssh [target] -u [user] --key-file [id_rsa]```

**执行命令**

```nxc ssh [target] -u [user] -p [password] -x [id]```

**测试密码列表**

```nxc ssh [target] -u [user] -p [passwords.txt]```

# SYNOPSIS

**nxc ssh** _target_ [_options_]

# PARAMETERS

**-u** _user_
> 用户名或文件。

**-p** _pass_
> 密码或文件。

**--key-file** _file_
> SSH 私钥。

**-x** _cmd_
> 执行命令。

**--port** _port_
> SSH 端口。

# DESCRIPTION

**nxc ssh** 测试 SSH 凭据并执行命令。是 NetExec 安全测试框架的一部分，支持密码喷洒和凭据验证。

# CAVEATS

仅限授权的安全评估用途。使用前需获得适当授权。

# SEE ALSO

[nxc](/man/nxc)(1), [ssh](/man/ssh)(1)
