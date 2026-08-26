# TAGLINE

Git 与 Perforce 的双向集成

# TLDR

**从 Perforce 仓库（depot）克隆**并保留完整历史

```git p4 clone //depot/path@all```

**克隆到特定目录**

```git p4 clone //depot/path@all [directory]```

**从 Perforce 同步最新更改**

```git p4 sync```

**将 git 提交提交回 Perforce**

```git p4 submit```

**将当前分支变基到 Perforce 更改之上**

```git p4 rebase```

**带分支检测地克隆**

```git p4 clone --detect-branches //depot/path@all```

# SYNOPSIS

**git p4** _command_ [_options_]

# PARAMETERS

**clone** _DEPOT_
> 从 Perforce depot 导入。

**sync**
> 从 Perforce 抓取更改。

**submit**
> 将 git 提交提交到 Perforce。

**rebase**
> 变基到 Perforce 的更改上。

**--branch** _BRANCH_
> 目标分支。

**--detect-branches**
> 自动检测 Perforce 分支映射。

**--bare**
> 执行裸克隆（不创建工作目录）。

**--use-client-spec**
> 使用 Perforce client spec 进行文件过滤。

**--origin** _ref_
> 提交时用于识别待提交内容的上游位置（默认：HEAD 可达的最近 p4 提交）。

**--shelve**
> 创建 shelved changelist 而不是直接提交。

**--conflict** _(ask|skip|quit)_
> 提交期间的冲突处理方式（默认：ask）。

**--verbose**
> 输出更详细的信息。

**--help**
> 显示帮助信息。

# DESCRIPTION

**git p4** 实现 Git 与 Perforce 之间的双向交互。它可以将 Perforce depot 历史导入 Git 仓库，也能把 Git 提交提交回 Perforce，同时支持迁移场景和长期的混合工作流。

该工具把 Perforce depot 路径映射到 Git 分支，让团队在本地使用 Git 工作的同时与 Perforce 服务器保持同步。它既支持从 Perforce 向 Git 的渐进式迁移，也支持长期的双系统并行方案。

**clone** 命令基于 Perforce 创建新的 Git 仓库。**sync** 抓取新更改但不修改工作文件。**rebase** 同步并将当前分支变基。**submit** 将 Git 提交作为单独的 changelist 发送到 Perforce。

# CAVEATS

需要 Python 和 p4 客户端。部分 Perforce 特性无法映射到 Git。复杂的分支布局处理起来比较困难。

# HISTORY

git p4 是为从 **Perforce** 迁移到 Git、或需要同时使用两种系统的团队而创建的。

# INSTALL

```dnf: sudo dnf install git-p4```

```zypper: sudo zypper install git-p4```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git](/man/git)(1), [p4](/man/p4)(1), [git-log](/man/git-log)(1)
