# TAGLINE

用于版本控制的并发版本系统（CVS）

# TLDR

从仓库**检出模块**

```cvs checkout [module_name]```

用最新变更**更新工作副本**

```cvs update```

带提交信息**提交变更**

```cvs commit -m "[commit message]"```

将新文件**纳入版本控制**

```cvs add [filename]```

显示与仓库版本的差异

```cvs diff [filename]```

查看文件的提交历史

```cvs log [filename]```

创建分支

```cvs tag -b [branch_name]```

# SYNOPSIS

**cvs** [_global-options_] _command_ [_command-options_] [_arguments_]

# PARAMETERS

**checkout** (co)
> 从仓库获取一份工作副本。

**update** (up)
> 用仓库的变更更新工作副本。

**commit** (ci)
> 将变更提交到仓库。

**add**
> 将文件加入版本控制。

**remove** (rm)
> 将文件移出版本控制。

**diff**
> 显示版本之间的差异。

**log**
> 显示修订历史。

**status**
> 显示工作副本状态。

**tag**
> 为修订添加符号标签。

**-d** _CVSROOT_
> 指定仓库根路径。

**-m** _MESSAGE_
> 提交信息。

# DESCRIPTION

**CVS**（Concurrent Versions System）是一种版本控制系统，用于跟踪文件随时间的变化。它让多名开发者可以在同一代码库上协作，管理合并并保存所有变更的历史。

CVS 采用客户端-服务器架构，中央仓库存储所有版本。开发者检出工作副本、在本地修改，然后再提交回去。系统通过乐观锁和合并解决机制来处理并发修改。

常见操作包括检出代码、更新以获取他人的变更、提交修改、为并行开发创建分支以及为发布打标签。CVS 在文件级别跟踪变更，并以增量方式高效存储。

# CAVEATS

CVS 已被视为遗留系统；新项目更推荐使用 Git 等分布式 VCS。它无法很好地跟踪目录操作。多文件提交不保证原子性。分支与合并操作也比现代系统繁琐得多。

# HISTORY

CVS 由 Dick Grune 于 **1986 年**开发，后由 Brian Berliner 改进。它在整个 20 世纪 90 年代都是主流版本控制系统，被众多大型开源项目采用。2000 年代基本被 Subversion 取代，随后又被 Git 取代。

# INSTALL

```apt: sudo apt install cvs```

```dnf: sudo dnf install cvs```

```pacman: sudo pacman -S cvs```

```apk: sudo apk add cvs```

```zypper: sudo zypper install cvs```

```brew: brew install cvs```

```nix: nix profile install nixpkgs#cvs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[svn](/man/svn)(1), [git](/man/git)(1), [rcs](/man/rcs)(1)

# RESOURCES

```[Source code](https://savannah.nongnu.org/projects/cvs/)```

```[Homepage](https://www.nongnu.org/cvs/)```

<!-- verified: 2026-06-26 -->
