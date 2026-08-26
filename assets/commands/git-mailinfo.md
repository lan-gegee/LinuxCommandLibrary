# TAGLINE

从邮件中提取补丁

# TLDR

**提取补丁信息**

```git mailinfo [msg.txt] [patch.txt] < [email.txt]```

**保留主题前缀**

```git mailinfo -k [msg.txt] [patch.txt] < [email.txt]```

# SYNOPSIS

**git mailinfo** [_options_] _msg_ _patch_

# PARAMETERS

_MSG_
> 用于保存提交信息的输出文件。

_PATCH_
> 用于保存补丁的输出文件。

**-k**
> 保持主题行原样不变。

**-b**
> 从主题中剥离方括号包裹的字符串。

**-u**
> 以 UTF-8 编码。

**--scissors**
> 移除剪刀线之前的内容。

**--help**
> 显示帮助信息。

# DESCRIPTION

**git mailinfo** 从邮件中提取补丁和提交信息。它解析邮件头和正文，将提交信息与补丁内容分离，并处理编码和作者信息的提取。

该命令是 `git am` 内部使用的底层（plumbing）工具。它处理基于补丁的开发工作流所用的邮件格式，例如 Linux 内核项目采用的工作流。

# CAVEATS

底层（plumbing）命令。通常由 git am 调用。输入必须符合标准邮件格式。

# HISTORY

git mailinfo 是 **Git** 邮件补丁工作流的一部分，支撑 Linux 内核所采用的邮件补丁开发模式。

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

[git-am](/man/git-am)(1), [git-mailsplit](/man/git-mailsplit)(1)

# RESOURCES

```[Source code](https://github.com/git/git)```

```[Homepage](https://git-scm.com/)```

```[Documentation](https://git-scm.com/docs/git-mailinfo)```

<!-- verified: 2026-07-17 -->
