# TAGLINE

将工作目录中的更改暂存以备下次提交

# TLDR

**暂存指定文件**

```git add [path/to/file]```

**暂存当前目录的所有更改**

```git add .```

**暂存整个仓库的所有更改**

```git add -A```

**只暂存已修改和已删除**的文件（不包括新文件）

```git add -u```

**交互式选择要暂存的 hunk**

```git add -p [path/to/file]```

**暂存匹配某个模式的文件**

```git add "*.js"```

**强制添加被忽略的文件**

```git add -f [path/to/ignored/file]```

用于暂存的**交互模式**

```git add -i```

# SYNOPSIS

**git add** [_OPTIONS_] [**--**] _PATHSPEC_...

# PARAMETERS

**-A**, **--all**
> 暂存整个工作树中的所有更改（新增、修改、删除）。

**-u**, **--update**
> 只暂存已跟踪文件的修改和删除，不包含新文件。

**-p**, **--patch**
> 交互式地从每个文件中选择要暂存的 hunk。

**-i**, **--interactive**
> 进入交互模式选择要暂存的文件。

**-f**, **--force**
> 允许添加被忽略的文件。

**-n**, **--dry-run**
> 显示将被暂存的内容，但不实际暂存。

**-v**, **--verbose**
> 在文件被添加时显示出来。

**-N**, **--intent-to-add**
> 仅记录该路径稍后将被添加，并暂存空内容。让新文件对 **git diff** 可见。

**-e**, **--edit**
> 在编辑器中打开 diff 并暂存编辑后的结果。

**--refresh**
> 刷新索引而不添加文件。

**--ignore-removal**, **--no-all**
> 暂存新增和修改的文件，但不包括删除。

**--ignore-errors**
> 遇到无法添加的文件时继续处理，而不是中止。

**--renormalize**
> 对所有已跟踪文件重新应用行尾和 clean 过滤器。修改 **.gitattributes** 后很有用。

**--chmod**=(**+**|**-**)**x**
> 覆盖索引中记录的可执行位。

**--sparse**
> 允许更新稀疏检出（sparse-checkout）锥形范围之外的条目。

**--pathspec-from-file**=_file_
> 从文件读取 pathspec（每行一个），或用 **-** 表示标准输入。

# DESCRIPTION

**git add** 将工作目录中的更改暂存以备下次提交。它把内容加入暂存区（索引），生成一个快照，这些文件将在运行 **git commit** 时被纳入提交。

更改可以在文件级别暂存，也可以通过 **-p**（补丁模式）在 hunk 级别有选择地暂存。在补丁模式下，你可以逐个检查每处更改并决定是否暂存，从而对提交进行细粒度控制。

借助暂存区，你可以增量式地准备提交，精确选择要包含哪些更改。可以使用 **git restore --staged** 或 **git reset** 取消暂存。

# CAVEATS

暂存文件捕获的是那一刻的状态。如果暂存后又修改了该文件，必须再次运行 git add 才能暂存新的更改。除非使用 **-f**，否则该命令不会暂存被忽略的文件。**git add .** 只暂存当前目录及其子目录中的更改，而 **git add -A** 会暂存整个仓库的更改。

# HISTORY

自 Linus Torvalds 于 **2005 年**发布 Git 之初，git add 就是其中一员。暂存区（也称索引）的概念是 Git 的标志性特性，与直接提交工作目录更改的版本控制系统相比，它允许更灵活地准备提交。

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

[git-commit](/man/git-commit)(1), [git-status](/man/git-status)(1), [git-restore](/man/git-restore)(1), [git-reset](/man/git-reset)(1), [git-diff](/man/git-diff)(1), [git-rm](/man/git-rm)(1)

# RESOURCES

```[Source code](https://github.com/git/git)```

```[Homepage](https://git-scm.com/)```

```[Documentation](https://git-scm.com/docs/git-add)```

<!-- verified: 2026-07-16 -->

