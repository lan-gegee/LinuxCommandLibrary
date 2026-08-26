# TAGLINE

简单而现代的文件加密

# TLDR

使用口令**加密**文件

```age -p [file.txt] > [file.txt.age]```

使用口令**解密**文件

```age -d [file.txt.age] > [file.txt]```

使用**接收者公钥**加密

```age -r [age1publickey...] [file.txt] > [file.txt.age]```

使用**多个接收者**加密

```age -r [key1] -r [key2] [file.txt] > [file.txt.age]```

使用 **SSH 公钥**加密

```age -R [~/.ssh/id_ed25519.pub] [file.txt] > [file.txt.age]```

使用**身份文件**解密

```age -d -i [key.txt] [file.txt.age] > [file.txt]```

# SYNOPSIS

**age** [_-e_|_-d_] [_-a_] [_-i identity_] [_-r recipient_] [_-R file_] [_-o output_] [_input_]

# DESCRIPTION

**age** 是一款简单、现代的文件加密工具：密钥短小明确，没有任何配置选项，并且能与 Unix 管道自由组合。它被设计为 GPG 的替代品，界面更干净，也不容易踩坑。

age 支持面向一个或多个接收者加密、口令加密，还可以使用 SSH 密钥做基于接收者的加密。整个格式的设计目标是简单且易于审计。

# PARAMETERS

**-e**, **--encrypt**
> 加密输入（默认操作）

**-d**, **--decrypt**
> 解密输入

**-p**, **--passphrase**
> 使用口令加密

**-r**, **--recipient** _recipient_
> 加密给指定接收者的公钥（可重复）。

**-R**, **--recipients-file** _file_
> 从文件读取接收者列表，每行一个（可重复）。

**-i**, **--identity** _identity_
> 解密用的身份（私钥）文件（可重复）。与 **-e** 搭配时也可用于 SSH 身份或已加密的身份。

**-o** _file_
> 输出文件（默认：标准输出）

**-a**, **--armor**
> 使用 ASCII armor 封装格式

# CAVEATS

age 不提供文件签名；需要认证加密时，请将 age 与 signify 或 minisign 搭配使用。其密钥与 GPG 密钥不能互换。没有内置的密钥管理；密钥只是普通文件。

# HISTORY

**age** 由 Ben Cartwright-Cox 和 Filippo Valsorda 设计，并于 **2019** 年首次发布。它的诞生是为了解决 GPG 的复杂性与易用性问题，同时提供一个安全、简洁、契合现代使用场景的加密工具。

# INSTALL

```apt: sudo apt install age```

```dnf: sudo dnf install age```

```pacman: sudo pacman -S age```

```apk: sudo apk add age```

```zypper: sudo zypper install age```

```brew: brew install age```

```nix: nix profile install nixpkgs#age```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[age-keygen](/man/age-keygen)(1), [gpg](/man/gpg)(1), [ssh-keygen](/man/ssh-keygen)(1)

# RESOURCES

```[Source code](https://github.com/FiloSottile/age)```

```[Homepage](https://age-encryption.org/)```

<!-- verified: 2026-06-11 -->
