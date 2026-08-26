# TAGLINE

SSH 密钥生成器与格式转换器

# TLDR

**生成 SSH 密钥**对

```fzputtygen -t [rsa] -o [key.ppk]```

**将 OpenSSH 转换为** PuTTY 格式

```fzputtygen [key] -o [key.ppk]```

**导出公钥**

```fzputtygen [key.ppk] -L```

**将 PuTTY 转换为** OpenSSH

```fzputtygen [key.ppk] -O private-openssh -o [key]```

**更改密码短语**

```fzputtygen [key.ppk] -P```

# SYNOPSIS

**fzputtygen** [_options_] [_keyfile_]

# PARAMETERS

_KEYFILE_
> 要处理的密钥文件。

**-t** _TYPE_
> 密钥类型：rsa、dsa、ecdsa、ed25519。

**-o** _FILE_
> 输出文件。

**-O** _FORMAT_
> 输出格式。

**-L**
> 输出公钥。

**-P**
> 更改密码短语。

**--help**
> 显示帮助信息。

# DESCRIPTION

**fzputtygen** 是 FileZilla 基于 PuTTYgen 的密钥生成器和转换器。它可以创建 SSH 密钥，并在 PuTTY（.ppk）和 OpenSSH 格式之间转换。

该工具可生成用于 SSH 身份验证的 RSA、DSA、ECDSA 和 Ed25519 密钥。它在 PuTTY 和 OpenSSH 客户端之间切换时所需的格式转换也由它完成。

fzputtygen 为 FileZilla 的 SFTP 连接提供密钥管理能力。

# CAVEATS

PPK 格式并非通用。建议使用密码短语保护。密钥类型支持因版本而异。

# HISTORY

fzputtygen 改编自 **PuTTYgen**，供 FileZilla 使用。它提供密钥生成和格式转换功能，支撑 FileZilla 的 SFTP 能力。

# INSTALL

```apt: sudo apt install filezilla```

```dnf: sudo dnf install filezilla```

```pacman: sudo pacman -S filezilla```

```apk: sudo apk add filezilla```

```zypper: sudo zypper install filezilla```

```nix: nix profile install nixpkgs#filezilla```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ssh-keygen](/man/ssh-keygen)(1), [filezilla](/man/filezilla)(1)
