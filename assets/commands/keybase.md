# TAGLINE

Keybase 的命令行客户端，提供端到端加密聊天、文件共享

# TLDR

**登录 Keybase**

```keybase login```

**查看状态**

```keybase status```

**搜索用户**

```keybase search [username]```

**为用户加密文件**

```keybase encrypt -i [file] -o [file.enc] [username]```

**解密文件**

```keybase decrypt -i [file.enc] -o [file]```

**签名消息**

```keybase sign -m "[message]"```

**验证签名**

```keybase verify -i [file.sig]```

**发起聊天**

```keybase chat send [username] "[message]"```

# SYNOPSIS

**keybase** [_command_] [_options_]

# PARAMETERS

**login**
> 登录 Keybase。

**signup**
> 创建新账户。

**status**
> 显示账户状态。

**encrypt**
> 为用户加密数据。

**decrypt**
> 解密数据。

**sign**
> 签名消息或文件。

**verify**
> 验证签名。

**chat**
> Keybase 聊天操作。

**fs**
> Keybase 文件系统操作。

**git**
> Keybase git 操作。

**pgp**
> 管理 PGP 密钥。

**log send**
> 发送日志以供调试。

# DESCRIPTION

**keybase** 是 Keybase 的命令行客户端，提供端到端加密聊天、文件共享和身份验证功能。它使用公钥加密技术在各社交网络间验证身份，并包含加密文件系统（KBFS）和加密 git 仓库。

# INSTALL

```nix: nix profile install nixpkgs#keybase```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gpg](/man/gpg)(1), [ssh](/man/ssh)(1)
