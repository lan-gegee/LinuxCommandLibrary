# TAGLINE

用 yadm 加密敏感的 dotfiles

# TLDR

**加密敏感文件**

```yadm encrypt```

# SYNOPSIS

**yadm** **encrypt** [_options_]

# DESCRIPTION

**yadm encrypt** 加密 ~/.config/yadm/encrypt 中列出的文件，为敏感配置（SSH 密钥、令牌）创建加密归档。使用 GPG 对称加密。加密归档可以安全地提交到仓库。

# SEE ALSO

[yadm](/man/yadm)(1), [yadm-decrypt](/man/yadm-decrypt)(1)
