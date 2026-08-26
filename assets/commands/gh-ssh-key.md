# TAGLINE

管理用于 GitHub 身份验证的 SSH 密钥

# TLDR

**列出 SSH 密钥**

```gh ssh-key list```

**添加 SSH 密钥**

```gh ssh-key add [key.pub]```

**添加带标题的 SSH 密钥**

```gh ssh-key add [key.pub] -t "[title]"```

**删除 SSH 密钥**

```gh ssh-key delete [key_id]```

# SYNOPSIS

**gh** **ssh-key** _command_ [_options_]

# SUBCOMMANDS

**list**
> 列出 SSH 密钥。

**add**
> 添加 SSH 密钥。

**delete**
> 删除 SSH 密钥。

# PARAMETERS

**-t**, **--title** _title_
> 密钥标题。

# DESCRIPTION

**gh ssh-key** 管理与你 GitHub 账户关联的 SSH 公钥，用于安全的 Git 身份验证。SSH 密钥是 HTTPS 身份验证之外的另一种选择，可实现免密码的 git 操作。

该命令支持从公钥文件添加新的 SSH 密钥，公钥通常使用 **ssh-keygen** 生成。跨多台机器管理多个密钥时，可以为密钥添加标题以便识别。删除操作会将密钥从你的 GitHub 账户移除，并立即吊销相应访问权限。

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

[gh](/man/gh)(1), [gh-gpg-key](/man/gh-gpg-key)(1)

# RESOURCES

```[Documentation](https://cli.github.com/manual/gh_ssh-key)```

```[Source code](https://github.com/cli/cli)```

<!-- verified: 2026-07-15 -->
