# TAGLINE

管理 Rspamd 垃圾邮件过滤守护进程

# TLDR

**检查配置**

```rspamadm configtest```

**导出配置**

```rspamadm configdump```

**训练垃圾邮件过滤器**

```rspamadm learn_spam [spam_folder/]```

**训练正常邮件（ham）过滤器**

```rspamadm learn_ham [ham_folder/]```

**控制守护进程**

```rspamadm control stat```

# SYNOPSIS

**rspamadm** _command_ [_options_]

# COMMANDS

**configtest**
> 测试配置。

**configdump**
> 导出配置。

**control** _action_
> 控制守护进程。

**learn_spam** _path_
> 学习垃圾邮件样本。

**learn_ham** _path_
> 学习正常邮件（ham）样本。

**statconvert**
> 转换统计格式。

**pw**
> 密码哈希。

# DESCRIPTION

**rspamadm** 是 Rspamd 的管理工具，Rspamd 是一个快速的垃圾邮件过滤系统。它负责配置管理、过滤器的训练以及守护进程的控制。

# EXAMPLES

```bash
# Test configuration
rspamadm configtest

# Dump current config
rspamadm configdump

# Learn spam directory
rspamadm learn_spam /var/mail/spam/

# Learn ham
rspamadm learn_ham /var/mail/ham/

# Check daemon status
rspamadm control stat

# Reload daemon
rspamadm control reload

# Generate password hash
rspamadm pw --encrypt
```

# CAVEATS

需要已安装 Rspamd。某些命令需要 root 权限。持续训练可以提升识别准确率。

# HISTORY

rspamadm 是由 **Vsevolod Stakhov** 开发的 **Rspamd** 的组成部分，后者是一个高级垃圾邮件过滤系统。

# INSTALL

```apt: sudo apt install rspamd```

```pacman: sudo pacman -S rspamd```

```apk: sudo apk add rspamd```

```zypper: sudo zypper install rspamd```

```nix: nix profile install nixpkgs#rspamd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rspamd](/man/rspamd)(8), [rspamc](/man/rspamc)(1)
