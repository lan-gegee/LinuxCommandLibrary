# TAGLINE

对 Git 仓库中的文件进行透明加密

# TLDR

**在仓库中初始化 git-crypt**

```git-crypt init```

**添加 GPG 用户**

```git-crypt add-gpg-user [user@example.com]```

**解锁仓库**

```git-crypt unlock```

**锁定仓库**

```git-crypt lock```

**导出对称密钥**

```git-crypt export-key [/path/to/key]```

**用密钥文件解锁**

```git-crypt unlock [/path/to/key]```

# SYNOPSIS

**git-crypt** _command_ [_options_]

# PARAMETERS

**init** [**-k** _keyname_]
> 生成密钥并让仓库准备好使用 git-crypt。

**add-gpg-user** [**-n**] [**--trusted**] _gpg-user-id_...
> 添加可以解锁仓库的 GPG 用户。**-n**, **--no-commit** 跳过自动提交该变更；**--trusted** 跳过 GPG 信任网检查。

**unlock** [_keyfile_]
> 解密仓库。默认使用 GPG 加密的密钥，也可以指定对称密钥文件。

**lock** [**-a**] [**-k** _keyname_] [**-f**]
> 重新加密文件并移除缓存的密钥。**-a**, **--all** 锁定所有密钥而不只是默认密钥；**-f**, **--force** 即使工作目录不干净也执行锁定。

**export-key** [**-k** _keyname_] _file_
> 将对称密钥导出到 _file_。

**status** [**-e**] [**-u**] [**-f**]
> 显示文件的加密状态。**-e** 只显示已加密文件，**-u** 只显示未加密文件，**-f**, **--fix** 会加密本应加密却未加密的文件。

# DESCRIPTION

**git-crypt** 支持对 Git 仓库中的文件进行透明加密。被配置的文件在提交时加密、检出时解密，使敏感数据可以与普通代码一同安全保存。

加密通过 .gitattributes 模式配置。持有对称密钥或获得授权 GPG 密钥的用户可以解锁仓库，查看和编辑受保护的文件。

# CONFIGURATION

**.gitattributes**
> 通过 filter 和 diff 属性定义哪些文件需要加密。

```
secrets/** filter=git-crypt diff=git-crypt
*.key filter=git-crypt diff=git-crypt
.env filter=git-crypt diff=git-crypt
```

# CAVEATS

加密后的文件显示为二进制。文件名不会被加密。多用户访问需要 GPG。历史中保存的是加密版本。不适合大文件（请使用 git-lfs）。

# HISTORY

git-crypt 由 **Andrew Ayer** 创建，用于解决在 git 仓库中存放机密信息的问题。相比 git-secret 等替代方案，它的设置更简单。

# INSTALL

```apt: sudo apt install git-crypt```

```dnf: sudo dnf install git-crypt```

```pacman: sudo pacman -S git-crypt```

```apk: sudo apk add git-crypt```

```zypper: sudo zypper install git-crypt```

```brew: brew install git-crypt```

```nix: nix profile install nixpkgs#git-crypt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git](/man/git)(1), [gpg](/man/gpg)(1), [git-secret](/man/git-secret)(1)

# RESOURCES

```[Source code](https://github.com/AGWA/git-crypt)```

<!-- verified: 2026-07-17 -->
