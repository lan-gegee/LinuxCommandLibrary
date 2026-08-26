# TAGLINE

列出与另一分支存在差异的文件

# TLDR

**列出与 master 不同的文件**（默认为新增、复制或修改）

```git delta```

**列出与指定分支不同的文件**

```git delta [branch]```

**只显示与 master 相比修改和重命名的文件**

```git delta master MR```

**只显示与某分支相比删除的文件**

```git delta [branch] D```

# SYNOPSIS

**git delta** [_branch_] [_filter_]

# PARAMETERS

_branch_
> 用于比较的基准分支。未指定时默认为 **master**。

_filter_
> 差异过滤字符，用于选择文件状态类型。使用与 **git diff --diff-filter** 相同的过滤字母：**A**（added，新增）、**C**（copied，复制）、**D**（deleted，删除）、**M**（modified，修改）、**R**（renamed，重命名）。多个字母可以组合（如 **MR**）。默认为 **ACM**（新增、复制、修改）。

# DESCRIPTION

**git delta** 列出与指定分支存在差异的文件，仅显示文件名而不显示内容差异。默认与 **master** 分支比较，并显示已新增、复制或修改的文件。

filter 参数允许使用 git 的 diff-filter 记法将结果限定为特定的变更类型。这有助于准备代码评审、制定部署计划，或快速评估特性分支上改动的范围。

它是 **git-extras** 套件的组成部分。不要与独立的 **delta** 项目（dandavison/delta）混淆，后者是一个用于 git diff 输出的语法高亮分页器。

# CAVEATS

需要安装 **git-extras** 软件包。只显示文件名，不显示内容差异。默认比较分支是 **master** 而非 **main**——对于以 **main** 作为默认分支的仓库可能需要调整。

# INSTALL

```dnf: sudo dnf install git-delta```

```pacman: sudo pacman -S git-delta```

```zypper: sudo zypper install git-delta```

```brew: brew install git-delta```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git-diff](/man/git-diff)(1), [git-log](/man/git-log)(1), [git-branch](/man/git-branch)(1), [git-extras](/man/git-extras)(1), [delta](/man/delta)(1)
