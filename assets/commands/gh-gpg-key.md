# TAGLINE

管理 GitHub 上用于提交签名的 GPG 密钥

# TLDR

**列出你 GitHub 账户上的 GPG 密钥**

```gh gpg-key list```

**从文件添加 GPG 密钥**

```gh gpg-key add [key.pub]```

**从标准输入添加 GPG 密钥**

```gpg --armor --export [key_id] | gh gpg-key add -```

**添加带标题的 GPG 密钥**

```gh gpg-key add [key.pub] --title "[Work laptop]"```

**按 ID 删除 GPG 密钥**

```gh gpg-key delete [key_id]```

# SYNOPSIS

**gh** **gpg-key** _subcommand_ [_options_]

# SUBCOMMANDS

**list**
> 列出与已认证用户关联的 GPG 密钥。

**add** [_key-file_]
> 向你的 GitHub 账户添加 GPG 公钥。若传入 **-** 而非文件，则从标准输入读取。

**delete** _key-id_
> 按数字 ID 从你的 GitHub 账户移除 GPG 密钥。

# PARAMETERS

**-t**, **--title** _string_
> 新密钥的标题（由 **add** 使用）。

**--yes**
> 跳过交互式确认提示（由 **delete** 使用）。

# DESCRIPTION

**gh gpg-key** 管理与你 GitHub 账户关联的 GPG 密钥。GitHub 用这些密钥验证经过签名的提交和标签，当签名与已注册密钥匹配时，会在网页 UI 中显示 "Verified" 徽章。

密钥必须以 ASCII 封装（ASCII-armored）格式导出（例如通过 **gpg --armor --export**）。要启用验证，密钥中的邮箱还必须与账户上某个已验证邮箱一致，且提交必须在本地完成签名（例如通过 **git config commit.gpgsign true**）。

# CAVEATS

需要通过 **gh auth login** 进行身份验证。执行操作的用户其令牌必须具有 **admin:gpg_key** 权限范围。上传到 GitHub 的密钥不能用于解密任何内容——GitHub 只存储公钥用于签名验证。

# INSTALL

```apt: sudo apt install gh```

```dnf: sudo dnf install gh```

```pacman: sudo pacman -S github-cli```

```apk: sudo apk add github-cli```

```zypper: sudo zypper install gh```

```brew: brew install gh```

```nix: nix profile install nixpkgs#gh```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gh](/man/gh)(1), [gh-ssh-key](/man/gh-ssh-key)(1), [gpg](/man/gpg)(1), [git-commit](/man/git-commit)(1)
