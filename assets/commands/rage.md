# TAGLINE

简单现代的文件加密工具

# TLDR

**使用口令加密文件**

```rage -p -o [encrypted.age] [file.txt]```

**使用接收者公钥加密**

```rage -r [age1...] -o [encrypted.age] [file.txt]```

**解密文件**

```rage -d -i [key.txt] [encrypted.age]```

**生成新密钥**

```rage-keygen -o [key.txt]```

**使用 SSH 密钥加密**

```rage -R [~/.ssh/id_ed25519.pub] [file.txt]```

**输出 ASCII 装甲格式**

```rage -a -r [age1...] [file.txt]```

**加密给多个接收者**

```rage -r [age1...] -r [age1...] -o [encrypted.age] [file.txt]```

**使用口令解密**

```rage -d -p [encrypted.age]```

**加密标准输入**

```echo "secret" | rage -r [age1...] -o [secret.age]```

# SYNOPSIS

**rage** [_-e_|_-d_] [_-r recipient_] [_-i identity_] [_-o output_] [_options_] [_file_]

# PARAMETERS

**-e**, **--encrypt**
> 加密模式。

**-d**, **--decrypt**
> 解密模式。

**-r**, **--recipient** _KEY_
> 接收者公钥。

**-R**, **--recipients-file** _FILE_
> 包含接收者的文件。

**-i**, **--identity** _FILE_
> 身份/私钥。

**-p**, **--passphrase**
> 使用口令。

**-a**, **--armor**
> 输出 ASCII 装甲格式。

**-o**, **--output** _FILE_
> 输出文件。省略时写入标准输出。

**-j** _PLUGINS_
> 使用指定的 age 插件。

# DESCRIPTION

**rage** 是 age 加密工具的 Rust 实现，提供简单、现代的文件加密。

公钥加密支持 age 密钥或 SSH 密钥。接收者通过其公钥指定。

口令模式使用 scrypt 进行密钥派生。简单场景无需管理密钥。

ASCII 装甲输出为纯文本，适合通过电子邮件或其他文本通道传输。

多个接收者支持群组加密。任何一位接收者都可以解密。

# CAVEATS

使用 age 格式；与 GPG 不兼容。密钥管理完全靠手动，没有密钥服务器或信任网络。加密需要接收者的公钥或口令。

# HISTORY

**rage** 是 **age**（Actually Good Encryption）的 Rust 实现，由 Filippo Valsorda 设计。Age 的目标是成为比 GPG 更简单的替代品。

# INSTALL

```pacman: sudo pacman -S rage```

```apk: sudo apk add rage```

```zypper: sudo zypper install rage```

```brew: brew install rage```

```nix: nix profile install nixpkgs#rage```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[age](/man/age)(1), [age-keygen](/man/age-keygen)(1), [gpg](/man/gpg)(1), [ssh-keygen](/man/ssh-keygen)(1), [openssl](/man/openssl)(1)
