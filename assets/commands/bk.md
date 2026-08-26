# TAGLINE

分布式版本控制系统

# TLDR

**克隆一个仓库**

```bk clone [bk://server/repository]```

**将新文件**纳入版本控制

```bk new [file1] [file2]```

**提交更改**

```bk commit -y"[commit message]"```

**将更改推送**到远端

```bk push```

**从远端拉取更改**

```bk pull```

**显示变更历史**

```bk changes```

**获取所有用户文件**

```bk -U get```

**显示仓库状态**

```bk status```

# SYNOPSIS

**bk** _command_ [_options_] [_arguments_]

# DESCRIPTION

**bk**（BitKeeper）是一个分布式版本控制系统，率先引入了许多后来被 Git 采用的概念。它支持嵌套仓库（子模块）、原子提交，并能高效处理大型代码库。

BitKeeper 提供简单的命令行界面，用于管理源代码历史、分支、合并以及跨分布式团队的协作。

# SUBCOMMANDS

**clone**
> 创建仓库的副本

**new**
> 将新文件纳入版本控制

**commit**
> 将更改记录到仓库

**push**
> 将更改发送到远程仓库

**pull**
> 从远端获取并合并更改

**changes**
> 显示提交历史

**status**
> 显示工作树状态

**diff**
> 显示修订版本之间的差异

**get**
> 从仓库检出文件

**import**
> 从非 BitKeeper 来源导入文件

# PARAMETERS

**-y** _message_
> 提交消息（配合 commit 命令）

**-U**
> 仅对用户文件进行操作

**-A**
> 对包括元数据在内的所有文件进行操作

**-r** _rev_
> 指定修订版本

# CAVEATS

BitKeeper 在 **2016 年**之前为专有软件，之后以 Apache 2.0 许可证开源。此后开发已停止；最终版本是 **2018 年**的 **7.3.3**。大多数项目已迁移到 Git。尽管功能相似，部分命令与 Git 中的对应命令有所不同。

# HISTORY

BitKeeper 由 **Larry McVoy** 于 **1998 年**创建，因在 **2002 至 2005 年**间被用于 Linux 内核开发而闻名。当许可纠纷导致自由使用受限后，Linus Torvalds 创建了 **Git** 作为替代品。BitKeeper 于 **2016 年**开源。

# INSTALL

```apk: sudo apk add bitkeeper```

```zypper: sudo zypper install bk```

```brew: brew install bk```

```nix: nix profile install nixpkgs#bk```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git](/man/git)(1), [hg](/man/hg)(1), [svn](/man/svn)(1)

# RESOURCES

```[Source code](https://github.com/bitkeeper-scm/bitkeeper)```

<!-- verified: 2026-06-19 -->
