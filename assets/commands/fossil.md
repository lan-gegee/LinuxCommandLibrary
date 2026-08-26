# TAGLINE

集项目管理于一体的分布式版本控制

# TLDR

**初始化新仓库**

```fossil init [repo.fossil]```

**克隆仓库**

```fossil clone [url] [repo.fossil]```

**在目录中打开仓库**

```fossil open [repo.fossil]```

**查看状态**

```fossil status```

**添加文件**

```fossil add [file]```

**提交变更**

```fossil commit -m "[message]"```

**查看时间线**

```fossil timeline```

**启动 Web UI**

```fossil ui```

# SYNOPSIS

**fossil** _command_ [_options_] [_args_]

# SUBCOMMANDS

**init**
> 创建新仓库。

**clone**
> 克隆仓库。

**open**
> 打开仓库检出。

**status**
> 显示工作副本状态。

**add**
> 添加文件。

**commit**
> 记录变更。

**update**
> 将检出更新到更新的版本或分支。

**diff**
> 显示工作副本中的变更。

**revert**
> 将文件恢复到已提交状态。

**branch**
> 创建或列出分支。

**pull**
> 从远程拉取。

**push**
> 推送到远程。

**sync**
> 与远程同步。

**ui**
> 启动内置 Web 界面（并打开浏览器）。

**timeline**
> 显示提交历史。

# CONFIGURATION

**_FOSSIL_**
> 包含仓库、wiki、工单和所有元数据的 SQLite 数据库文件。

**~/.fossil**
> 用户设置与全局忽略模式。

# DESCRIPTION

**fossil** 是一个面向软件项目的分布式版本控制系统，将源代码管理、bug 跟踪、wiki 文档和基于 Web 的项目管理集成在单一工具中。与 Git 不同，Fossil 将所有内容存储在一个单独的 SQLite 数据库文件里。

Fossil 由 D. Richard Hipp 为管理 SQLite 项目而创建，强调简洁和自包含。仓库文件包含完整的项目历史、工单、wiki 页面和技术笔记。这种设计让备份变得简单，并消除了不同系统之间的同步问题。

Fossil 内置了通过 **fossil ui** 访问的 Web 界面，无需外部工具即可浏览、管理工单和编辑 wiki。该系统使用内容寻址存储和加密校验和来确保数据完整性。

autosync 特性自动保持仓库同步，简化了分布式开发。Fossil 的分支模型鼓励使用特性分支，并提供以图形方式展示开发历史的 timeline 可视化。

# CAVEATS

与 Git 不同的工作流需要适应。包含大量二进制资源的项目中，单个仓库文件可能变得很大。相比 Git，其生态系统的集成与工具支持较少。

# HISTORY

**Fossil** 由 **D. Richard Hipp** 于 **2006** 年创建，用于管理 SQLite 项目。由于对现有版本控制系统感到失望，Hipp 将所有项目管理需求整合到一个工具中设计了 Fossil。自诞生以来，它一直是 SQLite 及其他项目的主要版本控制系统。

# INSTALL

```apt: sudo apt install fossil```

```dnf: sudo dnf install fossil```

```pacman: sudo pacman -S fossil```

```apk: sudo apk add fossil```

```zypper: sudo zypper install fossil```

```brew: brew install fossil```

```nix: nix profile install nixpkgs#fossil```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git](/man/git)(1), [hg](/man/hg)(1)
