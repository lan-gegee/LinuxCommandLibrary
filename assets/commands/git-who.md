# TAGLINE

按作者和最后提交日期列出远程分支

# TLDR

按作者**显示**所有远程分支

```git-who```

**显示**特定作者的分支

```git-who [author-name]```

只**显示**过期分支（超过 30 天）

```git-who --stale```

按最后提交日期**排序**

```git-who --sort date```

# SYNOPSIS

**git-who** [_options_] [_author_]

# PARAMETERS

**--stale**
> 只显示过期分支（超过 30 天）

**--sort** _FIELD_
> 排序依据：date、author、name（默认：date）

**--remote** _REMOTE_
> 指定远程仓库（默认：origin）

**--format** _FORMAT_
> 输出格式：table、csv、json

**-v, --version**
> 显示版本并退出

**-h, --help**
> 显示帮助并退出

# DESCRIPTION

**git-who** 列出远程 Git 分支，并显示每个分支上最后一次提交的作者和日期。它有助于识别哪些分支由谁负责以及分支有多久未更新。

该工具适用于仓库清理、查找旧分支以及了解团队中的分支归属情况。

# OUTPUT

显示各分支的以下信息：
- 分支名称
- 最后一次提交的作者
- 最后一次提交的日期
- 距最后一次提交的天数

# CAVEATS

需要能够访问远程仓库。可能需要执行 fetch 才能获得准确数据。性能取决于分支数量。

# HISTORY

**git-who** 的创建目的是通过提供分支归属和活跃度的可视化信息，帮助团队管理其 Git 分支。

# INSTALL

```zypper: sudo zypper install git-who```

```brew: brew install git-who```

```nix: nix profile install nixpkgs#git-who```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git-branch](/man/git-branch)(1), [git-for-each-ref](/man/git-for-each-ref)(1), [git](/man/git)(1)
