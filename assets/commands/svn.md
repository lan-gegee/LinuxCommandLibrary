# TAGLINE

Apache Subversion 版本控制客户端

# TLDR

**检出仓库**到本地目录

```svn checkout [url] [path/to/directory]```

将工作副本**更新到最新修订版**

```svn update```

**将文件纳入版本控制**

```svn add [path/to/file]```

带提交说明**提交变更**

```svn commit -m "[message]"```

**显示工作副本的状态**

```svn status```

**显示工作副本与仓库的差异**

```svn diff [path/to/file]```

**查看文件或目录的提交日志**

```svn log [path]```

**还原文件的本地修改**

```svn revert [path/to/file]```

# SYNOPSIS

**svn** _subcommand_ [_options_] [_args_]

# PARAMETERS

**checkout** (**co**)
> 从仓库检出一个工作副本。

**update** (**up**)
> 将仓库中的变更拉入工作副本。

**add**
> 将文件和目录纳入版本控制。

**delete** (**del**, **rm**)
> 将文件和目录从版本控制中移除。

**commit** (**ci**)
> 将工作副本的变更发送到仓库。

**status** (**st**)
> 打印工作副本中文件和目录的状态。

**diff** (**di**)
> 显示本地修改或修订版之间的差异。

**log**
> 显示提交日志消息。

**revert**
> 撤销对文件或目录的本地修改。

**merge**
> 将两个来源之间的差异应用到工作副本路径。

**copy** (**cp**)
> 在工作副本或仓库中复制文件或目录。

**move** (**mv**)
> 移动或重命名文件或目录。

**info**
> 显示本地或远程条目的信息。

**blame** (**annotate**)
> 对每一行内联显示作者和修订信息。

**-m**, **--message** _msg_
> 为提交指定日志消息。

**-r**, **--revision** _rev_
> 指定修订号或范围（如 **-r 100**、**-r 100:200**）。

**-c**, **--change** _rev_
> 应用某个修订带来的变更（**-r rev-1:rev** 的语法糖）。

**-q**, **--quiet**
> 不打印内容，或只打印摘要信息。

**-v**, **--verbose**
> 打印额外信息。

**--depth** _arg_
> 限制操作范围：**empty**、**files**、**immediates** 或 **infinity**。

**--username** _user_
> 指定认证用户名。

**--password** _pass_
> 指定认证密码。

**--non-interactive**
> 不进行交互式提示（便于脚本使用）。

# DESCRIPTION

**svn** 是 Apache Subversion 的官方命令行客户端。Subversion 是一种集中式版本控制系统，长期管理文件和目录，跟踪修改并允许取回历史版本。

该客户端与 Subversion 仓库通信，执行检出工作副本、提交变更、更新到最新修订版以及合并分支等操作。Subversion 支持原子提交、目录版本控制以及高效的二进制文件处理。

工作副本在 **.svn** 目录中维护元数据，记录基准修订版和本地修改。**svn** 客户端利用这些元数据判断哪些内容发生了变化、哪些需要与仓库同步。

# CAVEATS

与 Git 不同，Subversion 的大多数操作需要网络访问，因为历史记录存储在服务器上。每个子目录中都存在 **.svn** 目录，复制工作副本时可能引发问题。如果需要不带版本控制元数据的干净目录，请使用 **svn export** 而不是直接复制。

# HISTORY

Subversion 由 **CollabNet** 于 **2000 年**创建，作为 CVS 的替代品，解决了 CVS 在原子提交和目录版本控制等方面的局限。该项目由 Karl Fogel、Ben Collins-Sussman 和 Jim Blandy 主导。1.0 版本于 **2004 年 2 月**发布。Subversion 于 **2010 年**成为 **Apache 软件基金会**的项目。虽然 Git 在开源开发领域已在很大程度上取代了它，但 Subversion 在企业环境中仍然很流行。

# INSTALL

```apt: sudo apt install subversion```

```dnf: sudo dnf install subversion```

```pacman: sudo pacman -S subversion```

```apk: sudo apk add subversion```

```zypper: sudo zypper install subversion```

```brew: brew install subversion```

```nix: nix profile install nixpkgs#subversion```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git](/man/git)(1), [cvs](/man/cvs)(1), [svnadmin](/man/svnadmin)(8), [svnserve](/man/svnserve)(8)
