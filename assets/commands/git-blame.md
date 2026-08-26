# TAGLINE

显示每一行最后一次修改的修订版本和作者

# TLDR

**追溯**一个文件

```git blame [file.txt]```

**追溯指定行**

```git blame -L [10,20] [file.txt]```

**显示电子邮件地址**

```git blame -e [file.txt]```

**忽略空白**

```git blame -w [file.txt]```

**检测被移动的行**

```git blame -M [file.txt]```

# SYNOPSIS

**git blame** [_options_] [_rev_] [_--_] _file_

# PARAMETERS

_FILE_
> 要标注的文件。

**-L** _START_,_END_
> 标注指定的行范围。

**-e**, **--show-email**
> 显示作者邮箱。

**-w**
> 忽略空白更改。

**-M**
> 检测文件内被移动的行。

**-C**
> 检测从其他文件复制而来的行。

**-C**, **-C -C**
> 检测从其他文件复制而来的行。重复使用可将搜索范围扩大到该提交未触及的文件。

**--since** _DATE_
> 只显示指定日期之后的提交。

**--ignore-rev** _REV_
> 在分配归属时忽略某个修订版本，例如一次批量重排格式的提交。

**--ignore-revs-file** _FILE_
> 忽略文件中列出的每个修订版本。常通过 **blame.ignoreRevsFile** 在整个仓库范围内设置。

**--reverse** _START_.._END_
> 从后向前改为从前向后遍历历史，显示每行仍然存在的最后一个修订版本。

**--porcelain**, **--line-porcelain**
> 供脚本使用的稳定机器可读输出。

**-l**
> 显示完整未缩写的提交哈希。

**-s**
> 不显示作者姓名和时间戳。

**-f**, **--show-name**
> 显示原始提交中的文件名。

**-n**, **--show-number**
> 显示原始提交中的行号。

**--help**
> 显示帮助信息。

# DESCRIPTION

**git blame** 显示文件的每一行最后一次被哪个修订版本的哪位作者修改。它为每行标注提交信息，帮助弄清更改是何时以及为何做出的。

这个命令对代码考古、理解代码历史、找到特定代码该去问谁都必不可少。**-M** 和 **-C** 等选项可以检测跨文件移动和复制的代码，从而显示原始作者而不是搬动代码的人。

可以用 **-L** 指定行范围以聚焦特定区段，**-w** 则忽略空白更改以找出有意义的修改。其输出对于调试、代码评审和理解特定代码段的演变过程都极有价值。

# CAVEATS

blame 报告的是最后*触及*某行的提交，未必就是引入你正在调查的那个行为的提交。除非传入 **-w**、**-M** 或 **-C**，否则空白修复、重命名和代码移动都会认领它们并未真正编写的行。

全仓库范围的重排版会把真实历史埋在一次机械提交之后。把这类提交记录在文件中并让 **blame.ignoreRevsFile** 指向它，这样 **git blame** 默认就会跳过它们。

对大文件在很深的历史上做标注很慢，因为 git 需要重建并比较许多修订版本。如果只关心少数几行，可用 **-L** 缩小工作量。

默认输出格式面向人类，且在不同版本间不稳定；要解析请改用 **--porcelain** 或 **--line-porcelain**。

blame 默认会跟随文件的重命名。用 **rebase** 或 **filter-branch** 重写历史会改变 blame 所指向的提交，因此指向 blame 输出的链接可能失效。

# HISTORY

**git blame** 于 **2006 年**加入，沿用了 CVS 和 Subversion 对同一概念的命名。**git annotate** 与它并存，是一种兼容性拼法，输出格式不同。**--ignore-rev** 和 **--ignore-revs-file** 选项随 git **2.23**（**2019 年**）到来，用以应对全仓库重排版提交带来的问题。

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

[git-annotate](/man/git-annotate)(1), [git-log](/man/git-log)(1), [git-bisect](/man/git-bisect)(1), [git-show](/man/git-show)(1), [git-diff](/man/git-diff)(1)

# RESOURCES

```[Source code](https://github.com/git/git)```

```[Homepage](https://git-scm.com/)```

```[Documentation](https://git-scm.com/docs/git-blame)```

<!-- verified: 2026-07-16 -->

