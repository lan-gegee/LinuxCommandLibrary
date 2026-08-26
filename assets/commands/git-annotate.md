# TAGLINE

用提交信息标注文件的每一行

# TLDR

**显示**逐行的作者归属

```git annotate [path/to/file]```

**标注**指定修订版本的文件

```git annotate [revision] -- [path/to/file]```

只**标注**一段行范围

```git annotate -L [10],[20] [path/to/file]```

**忽略**仅涉及空白的更改

```git annotate -w [path/to/file]```

跨移动和复制**追溯**该行的原始提交

```git annotate -C -C [path/to/file]```

**显示**电子邮件地址而不是作者姓名

```git annotate -e [path/to/file]```

# SYNOPSIS

**git annotate** [_options_] [_rev-opts_] [_rev_] [**--**] _file_

# PARAMETERS

**-L** _start_,_end_
> 只标注给定的行范围。也接受 **:**_funcname_ 来选择某个函数，以及 **-L 10,+5** 之类的形式。

**-w**
> 比较版本时忽略空白，因此重新缩进不会改变归属。

**-M**[_num_]
> 检测在同一文件内被移动或复制的行，并归因于原始提交。

**-C**[_num_]
> 检测在同一提交中从其他文件移动或复制而来的行。重复使用（**-C -C**）可将搜索范围扩大到该提交未触及的文件。

**-e**, **--show-email**
> 显示作者的电子邮件地址而不是姓名。

**-l**
> 显示完整未缩写的提交哈希。

**-t**
> 显示原始时间戳而不是人类可读的日期。

**-f**, **--show-name**
> 显示原始提交中的文件名。

**-n**, **--show-number**
> 显示原始提交中的行号。

**-s**
> 不显示作者姓名和时间戳。

**--porcelain**
> 供脚本使用的机器可读输出。

**--line-porcelain**
> 类似 **--porcelain**，但对每一行都重复完整的提交信息。

**--reverse** _start_.._end_
> 从后向前改为从前向后遍历历史，显示每行仍然存在的最后一个修订版本。

**--ignore-rev** _rev_
> 在分配归属时忽略某个修订版本，例如一次批量重排格式的提交。

**--ignore-revs-file** _file_
> 忽略文件中列出的所有修订版本。

# DESCRIPTION

**git annotate** 用最后一次引入每行的提交信息来标注文件的每一行。给定一个修订版本时，它标注的是该时间点的文件状态，而不是工作树中的版本。

它与 **git blame** 使用相同的机制，唯一真正的区别是输出格式。保留 **git annotate** 是为了向后兼容现有脚本，也是为了给来自 CVS 和 Subversion 的用户提供一个熟悉的命令名——在那里 **annotate** 是约定俗成的拼法。

无论哪种拼法，它的价值都在于"考古"：找到引入 bug 的更改、理解某行为什么长成这样、或者弄清楚该去问谁。为此 **-C** 和 **-M** 很重要，因为不使用它们时，被重命名的文件或被移动的代码块会显示重构提交，而不是真正写出这段代码的提交。

**--ignore-rev** 和 **--ignore-revs-file** 则解决一个常见烦恼：全仓库范围的重排版用一次机械提交掩盖了真实历史。

# CAVEATS

blame 把每一行归因于最后*触及*它的提交，这并不等于导致你正在追查的那个行为的提交。除非传入 **-w**、**-M** 或 **-C**，否则一次空白修复、重命名或代码移动都会认领它并未真正编写的行。

由于 **git annotate** 仅为兼容性而存在，新工作应使用 **git blame**，后者拥有支持更好的输出格式，也是 git 文档视作规范的形式。

对大文件在很深的历史上做标注很慢，因为 git 需要重建并比较许多修订版本。如果只关心几行，可用 **-L** 限制工作量。

默认输出格式不够稳定，不适合解析；在脚本中请使用 **--porcelain** 或 **--line-porcelain**。

# HISTORY

**git annotate** 在 git 诞生初期的 **2005 年**加入，当时是一个 Perl 脚本，为 **git blame** 已有的功能提供 CVS 风格的名称和输出格式。后来用 C 重新实现，如今是 **git blame** 同一份代码之上的薄前端。

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

[git-blame](/man/git-blame)(1), [git-log](/man/git-log)(1), [git-diff](/man/git-diff)(1), [git-bisect](/man/git-bisect)(1)

# RESOURCES

```[Source code](https://github.com/git/git)```

```[Homepage](https://git-scm.com/)```

```[Documentation](https://git-scm.com/docs/git-annotate)```

<!-- verified: 2026-07-16 -->
