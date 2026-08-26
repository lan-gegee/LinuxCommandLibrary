# TAGLINE

通过 SMTP 以邮件形式发送补丁

# TLDR

**以邮件发送补丁**

```git send-email [*.patch]```

**发送到指定地址**

```git send-email --to=[maintainer@project.org] [patch]```

**附带封面信发送**

```git send-email --cover-letter [*.patch]```

**试运行**

```git send-email --dry-run [patch]```

# SYNOPSIS

**git send-email** [_options_] _patches_

# PARAMETERS

_PATCHES_
> 要发送的补丁文件。

**--to** _ADDRESS_
> 收件人邮箱。

**--cc** _ADDRESS_
> 抄送收件人。

**--cover-letter**
> 包含封面信。

**--dry-run**
> 显示将要发送的内容。

**--annotate**
> 发送前编辑补丁。

**--smtp-server** _HOST_
> SMTP 服务器。

**--smtp-encryption** _tls|ssl_
> SMTP 连接的加密方式。

**--suppress-cc** _category_
> 抑制某一类别的自动抄送（如 self、author、cccmd）。

**--compose**
> 发送前编写一段引导信息/封面信。

**--in-reply-to** _MESSAGE-ID_
> 将补丁作为对给定消息的回复进行串联。

**--help**
> 显示帮助信息。

# DESCRIPTION

**git send-email** 将补丁作为格式规范的邮件发送。对于采用邮件工作流的项目（如 Linux 内核），这是提交补丁的标准方式。

该命令负责处理 SMTP 配置、邮件串联和补丁格式化。它与 `git format-patch` 的输出无缝衔接，并支持为补丁系列添加封面信。

# CONFIGURATION

**sendemail.smtpServer**
> SMTP 服务器主机名或 sendmail 可执行文件路径，通过 `git config` 配置。

**sendemail.smtpUser**
> 用于身份验证的 SMTP 用户名。

**sendemail.to**
> 默认收件人地址。

# CAVEATS

需要配置 SMTP。某些防火墙会拦截 SMTP。封面信需要手动编辑。

# HISTORY

git send-email 支持 Linux 内核及其他项目所使用的**基于邮件的补丁工作流**，负责发送格式规范的补丁邮件。

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

[git-format-patch](/man/git-format-patch)(1), [git-am](/man/git-am)(1), [git-imap-send](/man/git-imap-send)(1)

# RESOURCES

```[Source code](https://github.com/git/git)```

```[Homepage](https://git-scm.com/)```

```[Documentation](https://git-scm.com/docs/git-send-email)```

<!-- verified: 2026-07-17 -->
