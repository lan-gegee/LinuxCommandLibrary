# TAGLINE

为 yadm 文件提供透明加密

# TLDR

**初始化 git-crypt**

```yadm git-crypt init```

**解锁仓库**

```yadm git-crypt unlock```

**添加 GPG 密钥**

```yadm git-crypt add-gpg-user [key-id]```

# SYNOPSIS

**yadm** **git-crypt** _command_ [_args_...]

# DESCRIPTION

**yadm git-crypt** 封装 git-crypt 以提供透明加密。匹配 .gitattributes 模式的文件在推送时被加密、拉取时被解密。这是 yadm encrypt 之外的按文件加密方案。

# SEE ALSO

[yadm](/man/yadm)(1), [git-crypt](/man/git-crypt)(1)
