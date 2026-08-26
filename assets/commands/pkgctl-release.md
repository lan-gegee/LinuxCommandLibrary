# TAGLINE

发布 Arch Linux 软件包构建产物

# TLDR

**带提交信息发布软件包**

```pkgctl release -m "[commit message]"```

**发布并自动更新 pacman 数据库**

```pkgctl release --db-update -m "[commit message]"```

**发布到 staging 仓库**

```pkgctl release --staging -m "[commit message]"```

**发布到 testing 仓库**

```pkgctl release --testing -m "[commit message]"```

# SYNOPSIS

**pkgctl release** [_options_]

# PARAMETERS

**-m**, **--message** _message_
> 发布时的提交信息。

**-u**, **--db-update**
> 在最后一步自动更新 pacman 数据库。

**-s**, **--staging**
> 发布到 staging 仓库。

**-t**, **--testing**
> 发布到 testing 仓库。

**-h**, **--help**
> 显示帮助文本。

# DESCRIPTION

**pkgctl release** 执行发布步骤，提交、打标签并将构建产物上传到 Arch Linux 仓库。它将软件包发布的收尾工作流程自动化。

该命令将版本打标签、源码提交和产物上传作为一次协调的操作来完成。默认情况下，产物会上传到你在 repos.archlinux.org 上的暂存目录，并在软件包 git 仓库中创建签名的标签。若还要更新二进制软件包仓库，请传入 `--db-update`，或单独使用 `pkgctl db update`。

# CAVEATS

需要通过 `pkgctl auth` 进行身份验证。发布前请确保构建产物已经过充分测试。

# SEE ALSO

[pkgctl](/man/pkgctl)(1), [pkgctl-auth](/man/pkgctl-auth)(1), [pkgctl-build](/man/pkgctl-build)(1), [pkgctl-db-update](/man/pkgctl-db-update)(1)
