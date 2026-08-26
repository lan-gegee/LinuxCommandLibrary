# TAGLINE

验证提交的 GPG 签名

# TLDR

**验证已签名的提交**

```git verify-commit [commit]```

**验证多个提交**

```git verify-commit [commit1] [commit2]```

**显示原始签名**

```git verify-commit --raw [commit]```

**详细输出**

```git verify-commit -v [commit]```

# SYNOPSIS

**git** **verify-commit** [_options_] _commit_...

# PARAMETERS

**-v**, **--verbose**
> 输出提交内容。

**--raw**
> 打印原始签名。

# DESCRIPTION

**git verify-commit** 检查提交的 GPG 签名。它验证提交是否使用有效的 GPG 密钥签名，以确认提交作者的真实性与完整性。

该命令适用于出于安全或合规目的要求提交必须签名的场景。

# CAVEATS

签名者的公钥必须已经存在于本地 GPG 密钥环（或已配置的 SSH/X.509 验证器）中，验证才能成功；密钥未知时即使签名本身有效也会导致失败。若任一给定提交缺少有效签名，则以非零状态退出。

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

[git-commit](/man/git-commit)(1), [git-verify-tag](/man/git-verify-tag)(1), [git-log](/man/git-log)(1)

# RESOURCES

```[Documentation](https://git-scm.com/docs/git-verify-commit)```

```[Source code](https://github.com/git/git)```

<!-- verified: 2026-07-17 -->
