# TAGLINE

通过应用过滤器重写分支历史

# TLDR

**从历史中移除文件**

```git filter-branch --tree-filter 'rm -f [file]' HEAD```

**重写作者**

```git filter-branch --env-filter 'GIT_AUTHOR_EMAIL="[new@email]"' HEAD```

**子目录过滤器**

```git filter-branch --subdirectory-filter [dir] HEAD```

**移除空提交**

```git filter-branch --prune-empty HEAD```

**强制重写**

```git filter-branch -f --tree-filter '[command]' HEAD```

# SYNOPSIS

**git** **filter-branch** [_options_] [_--_] [_rev-list_]

# PARAMETERS

**--env-filter** _cmd_
> 重写作者/提交者的环境变量（姓名、邮箱、日期）。

**--tree-filter** _cmd_
> 重写树及其内容；需要检出每个提交，因此在大型仓库上很慢。

**--index-filter** _cmd_
> 无需检出树即可重写索引；比 **--tree-filter** 快得多。常与 **git rm --cached** 一起使用。

**--parent-filter** _cmd_
> 重写提交的父提交列表。

**--msg-filter** _cmd_
> 重写提交信息。

**--commit-filter** _cmd_
> 完全替换创建提交的步骤。

**--tag-name-filter** _cmd_
> 重写指向被改写提交的标签名称。

**--subdirectory-filter** _dir_
> 只重写涉及 _dir_ 的历史，并将其作为新的项目根目录。

**--prune-empty**
> 移除过滤后变为空提交的提交。

**--original** _namespace_
> 备份引用的命名空间（默认 **refs/original**）。

**-d** _dir_
> 要使用的临时目录（例如 tmpfs，以提升 I/O 速度）。

**-f**, **--force**
> 强制执行操作，覆盖已存在的备份命名空间。

# DESCRIPTION

**git filter-branch** 是一个功能强大但已被弃用的工具，它通过对分支中的每个提交应用过滤命令来重写 Git 历史。它会遍历整个提交历史，允许修改树、提交信息、作者信息或其他元数据。

subdirectory-filter 特别适用于将一个子目录提取为保留了完整历史的新仓库。它在大型仓库上性能明显较差，因为必须检出每个提交的树。这一局限促成了 git-filter-repo 作为官方替代品的诞生。

# CAVEATS

**官方已弃用**，建议改用 git-filter-repo。在大型仓库上很慢。会改变历史，使提交哈希失效并需要强制推送。协作者必须重新克隆。会创建需要手动清理的备份引用。

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

[git-filter-repo](/man/git-filter-repo)(1), [git-rebase](/man/git-rebase)(1), [git-rm](/man/git-rm)(1)

# RESOURCES

```[Source code](https://github.com/git/git)```

```[Homepage](https://git-scm.com/)```

```[Documentation](https://git-scm.com/docs/git-filter-branch)```

<!-- verified: 2026-07-17 -->
