# TAGLINE

Git 与 Subversion 之间的双向桥接

# TLDR

**克隆 SVN 仓库**

```git svn clone [svn://server/repo]```

**按标准布局克隆**（trunk/branches/tags）

```git svn clone -s [svn://server/repo]```

**带作者映射克隆**

```git svn clone -s --authors-file=[authors.txt] [svn://server/repo]```

**获取 SVN 的改动**

```git svn fetch```

**基于 SVN 变基**

```git svn rebase```

**提交到 SVN**

```git svn dcommit```

# SYNOPSIS

**git svn** _command_ [_options_]

# PARAMETERS

**clone** _URL_
> 克隆 SVN 仓库。

**fetch**
> 从 SVN 拉取更新。

**rebase**
> 基于 SVN 提交变基。

**dcommit**
> 将提交推送到 SVN。

**log**
> 显示 SVN 风格的日志输出。

**info**
> 显示文件或目录的信息，类似 svn info。

**branch** _name_
> 在 SVN 中创建新分支。

**create-ignore**
> 根据 svn:ignore 属性生成 .gitignore 文件。

**show-ignore**
> 将 svn:ignore 属性打印到 stdout。

**reset** **-r** _revision_
> 撤销 fetch 的效果，回退到指定版本。

**-s**, **--stdlayout**
> 标准的 trunk/branches/tags 布局。

**-T** _PATH_
> trunk 路径。

**-b** _PATH_
> branches 路径。

**-t** _PATH_
> tags 路径。

**--authors-file** _FILE_
> 将 SVN 用户名映射为 Git 作者。

**--prefix** _PREFIX_
> SVN 远程引用名的前缀。

**-r** _ARG_, **--revision** _ARG_
> 指定要操作的 SVN 版本（或版本范围）。

**--ignore-paths** _REGEX_
> 拉取时要跳过的路径的 Perl 正则表达式。

# DESCRIPTION

**git svn** 提供 Git 与 Subversion 仓库之间的双向操作。它让开发者在使用 SVN 服务器的过程中仍能在本地使用 Git，使仍在使用 Subversion 的团队也能享受完整的 Git 工作流。

该命令可将 SVN 仓库克隆为 Git 仓库、双向同步改动，并把 SVN 的 trunk/branches/tags 结构映射为 Git 分支。

# CAVEATS

某些 git 特性无法对应到 SVN。在 dcommit 之前重写历史（rebase/amend）会破坏 SVN 跟踪。合并应使用 git svn rebase 而非 git merge。由于需要与 SVN 往返通信，操作比原生 git 慢。

# HISTORY

git svn 让从 **Subversion** 到 Git 的渐进式迁移成为可能：团队可以在本地使用 git，同时保持与 SVN 的兼容。

# INSTALL

```dnf: sudo dnf install git-svn```

```zypper: sudo zypper install git-svn```

```brew: brew install git-svn```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git](/man/git)(1), [svn](/man/svn)(1)
