# TAGLINE

PuTTY 安全文件复制客户端

# TLDR

**复制文件到远程**

```pscp [file] [user]@[host]:[path]```

**从远程复制**

```pscp [user]@[host]:[file] [local_path]```

**递归复制目录**

```pscp -r [directory] [user]@[host]:[path]```

**使用特定密钥**

```pscp -i [key.ppk] [file] [user]@[host]:[path]```

**指定端口**

```pscp -P [2222] [file] [user]@[host]:[path]```

# SYNOPSIS

**pscp** [_options_] [_source_] [_destination_]

# PARAMETERS

**-r**
> 递归复制目录。

**-i** _key_
> 私钥文件（PPK 格式）。

**-P** _port_
> SSH 端口。

**-l** _user_
> 登录用户名。

**-pw** _password_
> 密码（不安全）。

**-q**
> 静默模式。

**-v**
> 详细模式。

# DESCRIPTION

**pscp** 是 PuTTY 面向 Windows 的 SCP（Secure Copy）客户端。它通过 SSH 传输文件，类似于 Unix 的 scp 命令，但使用 PuTTY 的连接代码。

# CAVEATS

仅限 Windows（PuTTY 套件的一部分）。使用 PPK 密钥格式。在 Unix 上请改用 scp。

# HISTORY

pscp 是 **PuTTY** 的一部分，后者是 **Simon Tatham** 于 1999 年创建的 Windows SSH 客户端套件。

# INSTALL

```apt: sudo apt install putty-tools```

```dnf: sudo dnf install pssh```

```apk: sudo apk add pssh```

```zypper: sudo zypper install pssh```

```brew: brew install pssh```

```nix: nix profile install nixpkgs#pssh```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[scp](/man/scp)(1), [putty](/man/putty)(1), [plink](/man/plink)(1)
