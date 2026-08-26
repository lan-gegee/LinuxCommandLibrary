# TAGLINE

生成 Tarsnap 加密密钥

# TLDR

**生成新密钥**

```tarsnap-keygen --keyfile [/root/tarsnap.key] --user [email@example.com] --machine [hostname]```

带口令**生成**

```tarsnap-keygen --keyfile [/root/tarsnap.key] --user [email@example.com] --machine [hostname] --passphrased```

# SYNOPSIS

**tarsnap-keygen** [_options_]

# PARAMETERS

**--keyfile** _path_
> 输出密钥文件的路径。

**--user** _email_
> Tarsnap 账户邮箱。

**--machine** _name_
> 机器名称标识。

**--passphrased**
> 用口令加密密钥。

# DESCRIPTION

**tarsnap-keygen** 为 Tarsnap 备份服务生成加密密钥。它创建特定于机器的密钥，用于加密、去重的备份。tarsnap 的各种操作都需要密钥。

# CAVEATS

请妥善保管并备份密钥文件。丢失密钥意味着无法再访问备份。

# INSTALL

```pacman: sudo pacman -S tarsnap```

```brew: brew install tarsnap```

```nix: nix profile install nixpkgs#tarsnap```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tarsnap](/man/tarsnap)(1)
