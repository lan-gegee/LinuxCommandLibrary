# TAGLINE

创建并验证签名

# TLDR

**生成密钥对**

```minisign -G```

**签署文件**

```minisign -Sm [file]```

**验证签名**

```minisign -Vm [file] -p [pubkey.pub]```

**带注释签署**

```minisign -Sm [file] -c "[Signed by me]"```

**使用受信任密钥验证**

```minisign -Vm [file] -P [public_key_string]```

# SYNOPSIS

**minisign** [_options_]

# PARAMETERS

**-G**
> 生成新的密钥对。

**-S**
> 签署文件。

**-V**
> 验证签名。

**-R**
> 从现有私钥重建公钥文件。

**-m** _FILE_
> 要签署或验证的文件。

**-o**
> 配合 **-S** 使用，生成预哈希签名（大于 1 GiB 的文件必须使用）。

**-H**
> 配合 **-V** 使用，要求签名为预哈希签名。

**-q**
> 安静模式；验证成功时不再显示 "Comment" 横幅。

**-Q**
> 格式化输出公钥和签名注释。

**-s** _FILE_
> 私钥文件（默认 `~/.minisign/minisign.key`）。

**-p** _FILE_
> 公钥文件。

**-P** _KEY_
> 在命令行上提供的公钥（base64）。

**-x** _FILE_
> 签名文件路径（默认 `<input>.minisig`）。

**-c** _COMMENT_
> 存储在签名中的不受信任注释。

**-t** _COMMENT_
> 受信任注释（被签名，篡改会使签名失效）。

**-f**
> 强制：不提示直接覆盖现有文件。

**-W**
> 不加密新生成的私钥。

**-v**
> 显示 minisign 版本后退出。

**--help**
> 显示帮助信息。

# DESCRIPTION

**minisign** 创建并验证签名。它比 GPG 更简单，且具有良好的安全性。

该工具使用 Ed25519 签名。专为签署软件发行版设计。

# CAVEATS

与 GPG 不兼容。仅用于签名（不支持加密）。设计上追求简单。

# HISTORY

Minisign 由 **Frank Denis** 创建，是一款极其简单的文件签名工具。

# INSTALL

```apt: sudo apt install minisign```

```dnf: sudo dnf install minisign```

```pacman: sudo pacman -S minisign```

```apk: sudo apk add minisign```

```zypper: sudo zypper install minisign```

```brew: brew install minisign```

```nix: nix profile install nixpkgs#minisign```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gpg](/man/gpg)(1), [age](/man/age)(1), [ssh-keygen](/man/ssh-keygen)(1)
