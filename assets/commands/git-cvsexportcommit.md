# TAGLINE

将单个 Git 提交导出到 CVS 检出目录

# TLDR

**导出提交并自动提交到 CVS**

```git cvsexportcommit -v -c [commit]```

**将提交导出到指定的 CVS 工作目录**

```git cvsexportcommit -v -w [path/to/cvs_workdir] [commit]```

**导出提交并保留作者信息**

```git cvsexportcommit -v -c -a [commit]```

**即使 CVS 文件不是最新也强制导出**

```git cvsexportcommit -f -c [commit]```

**在导出和提交前先更新 CVS 文件**

```git cvsexportcommit -u -v -c [commit]```

# SYNOPSIS

**git** **cvsexportcommit** [-h] [-u] [-v] [-c] [-P] [-p] [-a] [-d _cvsroot_] [-w _cvs-workdir_] [-W] [-f] [-m _msgprefix_] [-k] [_parent-commit_] _commit-id_

# PARAMETERS

**-c**
> 如果补丁应用干净则自动提交。若有任何代码块应用失败或出现其他问题，则不会提交。

**-p**
> 应用补丁时吹毛求疵（偏执模式）。会以 --fuzz=0 调用 patch。

**-a**
> 添加作者信息。会在提交信息中加入 Author 行，以及 Committer（若与 Author 不同）。

**-d** _cvsroot_
> 设置要使用的备用 CVSROOT。对应 CVS 的 -d 参数。

**-f**
> 即使文件不是最新也强制合并。

**-P**
> 强制指定父提交，即使它并非直接父提交。

**-m** _msgprefix_
> 在提交信息前加上给定前缀。适用于补丁系列。

**-u**
> 在尝试导出之前，先从 CVS 仓库更新受影响的文件。

**-k**
> 在应用补丁前，反转工作 CVS 检出中的 CVS 关键字展开（例如 $Revision: 1.2.3.4$ 变回 $Revision$）。

**-w** _cvs-workdir_
> 指定用于导出的 CVS 检出位置。默认取 cvsexportcommit.cvsdir 的值。

**-W**
> 表明当前工作目录既是 Git 检出也是 CVS 检出。Git 会先把工作目录重置到父提交再继续。

**-v**
> 详细输出。

# DESCRIPTION

**git cvsexportcommit** 将单个 Git 提交导出到 CVS 检出目录，实现从 Git 向旧式 CVS 仓库迁移更改。它把特定 Git 提交的改动应用到 CVS 工作目录，并可选择自动提交。

该命令处理文件的增、改、删，将 Git 的提交语义转换为等价的 CVS 操作。在团队从 CVS 过渡到 Git、但又必须与依赖 CVS 的系统保持同步的混合环境中，它特别有用。

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

[git](/man/git)(1), [cvs](/man/cvs)(1), [git-format-patch](/man/git-format-patch)(1)
