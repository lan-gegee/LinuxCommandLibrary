# TAGLINE

将 mbox 拆分为单封邮件

# TLDR

**将 mbox 拆分为多封邮件**

```git mailsplit -o [output-dir] [mbox]```

**从标准输入读取并拆分**

```git mailsplit -o [output-dir]```

# SYNOPSIS

**git mailsplit** [_options_] [_mbox_]

# PARAMETERS

_MBOX_
> 要拆分的邮箱文件。

**-o** _DIR_
> 输出目录。

**-b**
> 保留 mbox 的 "From " 行。

**-d** _DIGITS_
> 编号的填充位数。

**-f** _NUM_
> 从 N 开始编号。

**--keep-cr**
> 保留回车符。

**--help**
> 显示帮助信息。

# DESCRIPTION

**git mailsplit** 将 mbox 文件拆分为单封邮件。每封邮件会成为输出目录中的一个编号文件，为 `git am` 处理补丁做好准备。

该命令是 `git am` 内部使用的底层（plumbing）工具，用于处理包含多个补丁的邮箱文件。它会检测 mbox 格式的边界，并将每封邮件分离到各自的文件中。

# CAVEATS

底层（plumbing）命令。通常由 git am 调用。输出为单独的邮件文件。

# HISTORY

git mailsplit 是 **Git** 邮件补丁工作流的一部分，负责把邮箱拆分为单封邮件以便处理。

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

[git-am](/man/git-am)(1), [git-mailinfo](/man/git-mailinfo)(1)

# RESOURCES

```[Source code](https://github.com/git/git)```

```[Homepage](https://git-scm.com/)```

```[Documentation](https://git-scm.com/docs/git-mailsplit)```

<!-- verified: 2026-07-17 -->
