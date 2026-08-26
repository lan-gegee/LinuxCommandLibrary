# TAGLINE

将补丁上传到 IMAP 草稿文件夹

# TLDR

**通过 IMAP 发送补丁**

```git format-patch origin | git imap-send```

**从文件发送**

```git imap-send < [patches.mbox]```

# SYNOPSIS

**git imap-send** [_options_]

# PARAMETERS

**--curl**
> 对 IMAP 使用 libcurl。

**-v**, **--verbose**
> 详细输出。

**-q**, **--quiet**
> 安静模式。

**--help**
> 显示帮助信息。

# DESCRIPTION

**git imap-send** 将补丁上传到 IMAP 草稿文件夹，让你可以在发送之前在邮件客户端中审阅和撰写补丁邮件。它从 stdin 读取 mbox 格式的补丁，并将其上传到配置好的 IMAP 服务器。

它支持 Linux 内核等项目采用的邮件驱动补丁提交工作流——这些项目通过邮件列表评审补丁，而不是基于网页的拉取请求。

# CONFIGURATION

**~/.gitconfig**
> IMAP 服务器配置，包括 [imap] 区段中的主机、用户、端口和 SSL 设置。

# CAVEATS

需要配置 IMAP 服务器。SSL 配置可能比较复杂。是 git send-email 的替代方案。

# HISTORY

git imap-send 为采用**基于电子邮件的补丁提交**的项目而创建，可与标准邮件客户端集成。

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

[git-send-email](/man/git-send-email)(1), [git-format-patch](/man/git-format-patch)(1)

# RESOURCES

```[Source code](https://github.com/git/git)```

```[Homepage](https://git-scm.com/)```

```[Documentation](https://git-scm.com/docs/git-imap-send)```

<!-- verified: 2026-07-17 -->
