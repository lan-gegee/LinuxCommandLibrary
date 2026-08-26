# TAGLINE

应用来自 mbox 格式电子邮件消息的补丁

# TLDR

**从邮箱文件应用补丁**

```git am [patches.mbox]```

**应用补丁文件**

```git am [*.patch]```

**使用三方合并应用**

```git am --3way [patch]```

**应用并添加 Signed-off-by 签名行**

```git am --signoff [patch]```

**解决冲突后继续**

```git am --continue```

**跳过当前补丁**

```git am --skip```

**显示 am 停止处的补丁**

```git am --show-current-patch```

**中止补丁应用**

```git am --abort```

# SYNOPSIS

**git am** [_options_] [_mbox_|_maildir_]

# PARAMETERS

_MBOX_
> 包含补丁的邮箱（mailbox）文件。

**--3way**, **-3**
> 当补丁无法干净应用时回退到三方合并。

**--signoff**, **-s**
> 在提交消息中添加 Signed-off-by 签名行。

**--keep**, **-k**
> 向 git mailinfo 传递 -k；保留主题前缀。

**--quiet**, **-q**
> 只打印错误消息。

**--whitespace** _action_
> 处理空白错误：nowarn、warn、fix、error、error-all。

**--reject**
> 将被拒绝的 hunk 保留在 .rej 文件中，而不是直接失败。

**--patch-format** _format_
> 指定补丁格式：mbox、mboxrd、stgit、stgit-series、hg。

**--skip**
> 跳过当前补丁。

**--continue**, **--resolved**, **-r**
> 在手动解决冲突后继续。

**--abort**
> 中止并恢复原来的分支状态。

**--quit**
> 中止但保持 HEAD 和索引不变。

**--show-current-patch** [**=diff**|**=raw**]
> 显示 am 停止处的补丁；默认为 raw。

**--gpg-sign** [_keyid_], **-S** [_keyid_]
> 对生成的提交进行 GPG 签名。

**-i**, **--interactive**
> 以交互方式运行。

**--help**
> 显示帮助信息。

# DESCRIPTION

**git am**（apply mailbox）应用来自电子邮件消息的补丁。它读取 mbox 格式的补丁，这种格式常用于开源项目中基于电子邮件的补丁提交流程。

该命令从电子邮件格式中提取补丁内容和提交消息，创建保留原始作者信息的提交。它可以处理补丁系列，并通过 --skip、--abort 和 --continue 操作管理冲突。

这一工作流至今仍是 Linux 内核开发流程以及其他依赖基于邮件的代码评审和补丁提交的项目的基础。

# CAVEATS

补丁必须是正确的 mbox/maildir 格式。发生冲突时需要手动解决，然后执行 `--continue`。原始作者信息和日期从邮件头部保留。

# HISTORY

git am 是为 **Linux 内核**开发流程设计的，在该流程中补丁通过邮件列表以电子邮件方式提交和评审。

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

[git-apply](/man/git-apply)(1), [git-format-patch](/man/git-format-patch)(1), [git-send-email](/man/git-send-email)(1)
