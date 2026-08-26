# TAGLINE

用 git 管理大文件，而不把文件内容检入 git

# TLDR

**初始化**仓库以使用 annex

```git annex init "[laptop]"```

将大文件**添加**到 annex

```git annex add [largefile.zip]```

从拥有该内容的远程仓库**下载**

```git annex get [file]```

**丢弃**本地副本，同时保持文件被跟踪

```git annex drop [file]```

**显示**哪些仓库保存着某个文件的内容

```git annex whereis [file]```

将内容**复制**到远程

```git annex copy [file] --to [origin]```

与所有远程仓库**同步**元数据

```git annex sync```

**同步**元数据和文件内容

```git annex sync --content```

**检查**存储的内容是否完好

```git annex fsck```

**解锁**文件以便就地编辑

```git annex unlock [file]```

# SYNOPSIS

**git annex** _command_ [_options_] [_files_...]

# PARAMETERS

**init** [_description_]
> 初始化一个仓库以配合 annex 使用，并给它一个人类可读的描述。

**add** _files_
> 将文件加入 annex，用指向其内容的指针替换原文件。

**get** _files_
> 从拥有该内容的远程仓库下载。

**drop** _files_
> 在验证其他地方存在足够副本之后，移除本地内容。

**copy** _files_ **--to**/**--from** _remote_
> 向远程复制或从远程复制内容，保留源副本。

**move** _files_ **--to**/**--from** _remote_
> 类似 **copy**，但完成后会丢弃源副本。

**sync** [**--content**]
> 与远程同步 git 元数据。**--content** 还会传输文件内容。

**whereis** _files_
> 列出已知保存着每个文件内容的仓库。

**unlock** _files_, **lock** _files_
> 解锁文件以便就地修改，然后再锁定它以存储新版本。

**fsck**
> 验证存储的内容与其校验和一致，并且存在足够多的副本。

**numcopies** _n_
> 设置每个文件必须存在多少份副本，**drop** 才会允许移除其中一份。

**info** [_remote_]
> 显示仓库或远程的统计信息，包括磁盘占用。

**initremote** _name_ **type**=_type_
> 建立特殊远程（special remote），例如 S3、rsync 或目录。

**--help**
> 显示帮助信息。

# DESCRIPTION

**git-annex** 让 git 可以管理那些内容太大而无法放进 git 历史的文件。git 跟踪的不是文件本身，而是一个很小的指针，实际字节则保存在 **.git/annex/objects** 下独立的对象库中。历史、分支和合并都照常工作，因为在 git 眼里这个仓库只包含小的指针文件。

它在"把大文件放到别处"之上增加的理念是：仓库不必持有每个文件的内容。每个克隆可以只携带放得下的那部分子集，而 git-annex 会在 **git-annex** 分支中维护一份分布式记录，说明哪些仓库持有哪些内容。**git annex whereis** 回答"实际的字节在哪里"，**git annex get** 则按需取回它们。正因如此，它才能管理远超任何单块磁盘容量的档案库。

内容按校验和寻址，因此相同的文件只存储一次，损坏也能被检测出来。**git annex fsck** 会验证校验和并检查 **numcopies** 保证——正是这一机制阻止 **drop** 删除某样东西的最后一份副本。

默认情况下，annex 化的文件表现为指向对象库的符号链接，这使它们保持只读并防止意外修改。**git annex unlock** 用可写副本替换符号链接，**lock** 则把结果存为新版本。较新的 **v6**/**v7** 仓库模式和 **adjusted unlocked branch** 让解锁状态成为常态，这对无法跟随符号链接的工具更友好。

**特殊远程（special remotes）**是这套设计的另一半：annex 远程完全不必是 git 仓库。S3、Backblaze B2、rsync 目标、WebDAV、可移动驱动器等都可以存放内容，让 git-annex 把它们当作存储使用，而 git 本身从不与它们直接对话。

# CONFIGURATION

**.git/annex/objects/**
> 本地内容库，按校验和为键保存文件。

**.git/config**
> 仓库与远程配置，包括 annex 相关设置。

**git-annex** 分支
> 一个孤儿分支，跟踪所有内容的位置和元数据。在仓库之间同步；不要手工编辑。

**.gitattributes**
> 通过 **annex.largefiles** 属性控制哪些文件被 annex 化而不是直接提交给 git。

# CAVEATS

学习曲线确实存在。其中的概念（键、后端、特殊远程、numcopies、信任级别、**git-annex** 分支、锁定与解锁文件）无法映射到 git 的任何其他机制上，而且仓库版本历史（**v5** 到 **v10**）意味着你在网上找到的许多文档描述的都是早已改变的行为。

锁定的文件是**符号链接**。保存时整个替换文件的编辑器、复制目录树的构建系统以及不支持符号链接的文件系统都会与它们发生冲突。Windows 支持尤其长期滞后，因为它缺乏真正的符号链接。

当无法验证别处仍留有 **numcopies** 份副本时，**git annex drop** 会拒绝移除内容，而它的判断依据是自己的位置日志。如果该日志过期了——比如另一个仓库被删除却未被告知——记录就可能声称存在实际上并不存在的副本。**git annex fsck** 正是用来校正这一点，值得定期运行而不是出了问题才想起来。

对 annex 仓库执行普通的 **git clone** 只会得到指针而非内容：文件看似存在，但在 **git annex get** 取回之前都是断开的符号链接。

除非传入 **--content**，否则 **git annex sync** 不传输文件内容，这让期望它表现得像 **git pull** 加 **git push** 的人感到意外。

git-annex 和 **git-lfs** 以不同的方式解决重叠的问题。LFS 更简单，得到 GitHub、GitLab 等平台的直接支持，并且在检出时总是拉取内容。git-annex 对内容存放位置和各克隆携带什么则灵活得多。两者之间的迁移很麻烦，所以这个选择值得慎重对待。

# HISTORY

**git-annex** 由 **Joey Hess** 编写，首次发布于 **2010 年**。其助手（assistant）和 Web 应用的开发由 **2012 年**一次成功的 **Kickstarter** 众筹资助。它使用 **Haskell** 编写，至今广泛用于研究数据管理，尤其是作为 **DataLad** 项目的基础，同时也用于个人媒体档案。

# INSTALL

```apt: sudo apt install git-annex```

```dnf: sudo dnf install git-annex```

```pacman: sudo pacman -S git-annex```

```apk: sudo apk add git-annex```

```zypper: sudo zypper install git-annex```

```brew: brew install git-annex```

```nix: nix profile install nixpkgs#git-annex```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git](/man/git)(1), [git-lfs](/man/git-lfs)(1), [git-clone](/man/git-clone)(1), [rsync](/man/rsync)(1)

# RESOURCES

```[Source code](https://git.joeyh.name/index.cgi/git-annex.git/)```

```[Homepage](https://git-annex.branchable.com/)```

```[Documentation](https://git-annex.branchable.com/git-annex/)```

<!-- verified: 2026-07-16 -->
