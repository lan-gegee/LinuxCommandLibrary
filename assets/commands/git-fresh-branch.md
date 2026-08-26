# TAGLINE

创建没有提交历史的孤儿分支

# TLDR

**创建孤儿分支**

```git fresh-branch [branch_name]```

# SYNOPSIS

**git** **fresh-branch** _name_

# PARAMETERS

_NAME_
> 要创建的新分支的名称。

# DESCRIPTION

**git fresh-branch** 创建一个新的孤儿分支，它没有任何父提交，与仓库现有历史也没有关联。它会将 HEAD 指向新的（尚不存在的）分支引用，清空索引，并对工作树运行 **git clean -fdx**，从而在同一仓库内留下完全干净的一片天地。

它的主要用例是用于 GitHub Pages 托管的 gh-pages 分支，文档或网站内容与代码共存于同一仓库，但不共享历史。其他用途包括文档分支、实验分支，或存放第三方代码的 vendor 分支。

如果工作树中存在未跟踪的改动，该命令会先提示确认再继续，因为 **git clean -fdx** 会不可恢复地删除它们。

# CAVEATS

属于 git-extras 软件包。会在没有真正备份的情况下销毁未跟踪文件和索引；运行前请提交或储藏任何想要保留的内容。效果等同于 **git checkout --orphan** _name_ 之后再清空索引和工作树。

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

[git-checkout](/man/git-checkout)(1), [git-clean](/man/git-clean)(1), [git-extras](/man/git-extras)(1)

# RESOURCES

```[Source code](https://github.com/tj/git-extras)```

```[Documentation](https://github.com/tj/git-extras/blob/master/man/git-fresh-branch.md)```

<!-- verified: 2026-07-17 -->
