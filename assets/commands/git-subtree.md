# TAGLINE

以子目录的方式合并和拆分仓库

# TLDR

**添加子树**

```git subtree add --prefix=[dir] [repo] [branch]```

**拉取子树的改动**

```git subtree pull --prefix=[dir] [repo] [branch]```

**推送子树的改动**

```git subtree push --prefix=[dir] [repo] [branch]```

**拆分子树**

```git subtree split --prefix=[dir] -b [new_branch]```

**合并子树**

```git subtree merge --prefix=[dir] [commit]```

# SYNOPSIS

**git** **subtree** _command_ [_options_]

# SUBCOMMANDS

**add**
> 将仓库添加为子树。

**pull**
> 拉取子树的改动。

**push**
> 推送子树的改动。

**merge**
> 合并子树的改动。

**split**
> 提取子树的历史。

# PARAMETERS

**--prefix** _dir_
> 子树所在的子目录。

**--squash**
> 压缩历史。

**-b** _branch_
> split 使用的分支名。

# DESCRIPTION

**git subtree** 把仓库合并为子目录，或从子目录中拆分出仓库，是子模块的替代方案。与子模块不同，子树把所有内容都保存在同一个仓库中并拥有统一的历史，因此克隆时无需任何额外的 init/update 步骤即可获得引入的代码。

`split` 命令将某个子目录的历史提取到一个独立分支中；`add`、`pull` 和 `push` 则负责与上游仓库保持持续同步。

# CAVEATS

它以 `contrib` 脚本的形式分发，不是核心 `git` 二进制的一部分，因此并非所有环境都默认安装（例如某些 Linux 发行版将其单独打包，如 Debian/Ubuntu 的 `git-subtree` 软件包）。合入庞大的上游历史时，其全部提交都会被加入你的仓库。

# INSTALL

```dnf: sudo dnf install git-subtree```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git-submodule](/man/git-submodule)(1), [git-merge](/man/git-merge)(1)

# RESOURCES

```[Source code](https://github.com/git/git/tree/master/contrib/subtree)```

```[Documentation](https://manpages.debian.org/testing/git-man/git-subtree.1.en.html)```

<!-- verified: 2026-07-17 -->
