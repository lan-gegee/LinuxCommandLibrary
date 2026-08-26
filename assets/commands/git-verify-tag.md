# TAGLINE

验证标签的 GPG 签名

# TLDR

**验证已签名的标签**

```git verify-tag [tag]```

**验证多个标签**

```git verify-tag [tag1] [tag2]```

**显示原始签名**

```git verify-tag --raw [tag]```

**详细输出**

```git verify-tag -v [tag]```

# SYNOPSIS

**git** **verify-tag** [_options_] _tag_...

# PARAMETERS

**-v**, **--verbose**
> 输出标签内容。

**--raw**
> 打印原始签名。

**--format** _format_
> 格式化输出。

# DESCRIPTION

**git verify-tag** 检查标签的 GPG 签名。它验证标签是否使用有效的 GPG 密钥签名，以确认所标记发布的真实性。

它常用于在安全敏感的工作流程中验证发布标签的完整性。

# CAVEATS

签名者的公钥必须已经存在于本地 GPG 密钥环（或已配置的 SSH/X.509 验证器）中；密钥未知时即使是格式良好的签名也会导致验证失败。若任一给定标签缺少有效签名，则以非零状态退出。

# INSTALL

```apt: sudo apt install git```

```dnf: sudo dnf install git```

```pacman: sudo pacman -S git```

```apk: sudo apk add git```

```zypper: sudo zypper install git```

```brew: brew install git```

```nix: nix profile install nixpkgs#git```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git-tag](/man/git-tag)(1), [git-verify-commit](/man/git-verify-commit)(1)

# RESOURCES

```[Documentation](https://git-scm.com/docs/git-verify-tag)```

```[Source code](https://github.com/git/git)```

<!-- verified: 2026-07-17 -->
