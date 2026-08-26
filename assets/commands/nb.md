# TAGLINE

命令行笔记、书签与知识库应用

# TLDR

在编辑器中**创建笔记**

```nb add```

**创建带内容的笔记**

```nb add "[Note content here]"```

**列出**当前笔记本中的**笔记**

```nb ls```

按关键词**搜索笔记**

```nb search "[query]"```

按 ID **编辑笔记**

```nb edit [1]```

按 ID **删除笔记**

```nb delete [1]```

自动抓取标题**保存书签**

```nb bookmark "[https://example.com]"```

**查看笔记**

```nb show [1]```

与远程 git 仓库**同步笔记**

```nb sync```

**切换笔记本**

```nb use [notebook_name]```

# SYNOPSIS

**nb** [_subcommand_] [_options_] [_arguments_]

# PARAMETERS

**add** [_text_]
> 创建新笔记。不带参数时打开已配置的编辑器。

**ls**
> 列出笔记，可选按关键词过滤。

**search** _query_
> 跨笔记进行全文搜索。

**edit** _id_
> 在编辑器中打开已有笔记。

**delete** _id_
> 删除笔记。**--force** 跳过确认。

**show** _id_
> 显示笔记内容。

**bookmark** _url_
> 保存书签，自动抓取标题和内容。

**todo** _action_
> 管理待办事项。

**notebooks**
> 管理笔记本（由独立 git 仓库支撑的笔记分组）。

**sync**
> 向已配置的远程 git 仓库拉取并推送变更。

**use** _notebook_
> 切换活动笔记本。

**--help**
> 显示 nb 或某个子命令的帮助信息。

# DESCRIPTION

**nb** 是一款命令行笔记、书签、归档和知识库应用。笔记以纯 Markdown（或任意文本格式）形式存储在本地文件系统中，每个笔记本都是一个 git 仓库，从而提供版本历史、冲突解决和远程同步能力。

除普通笔记外，**nb** 还支持带标签的待办清单、加密笔记（通过 OpenSSL 或 GPG）、书签（含缓存页面快照）、置顶笔记、基于 **rg**/**ag**/**grep** 的搜索，以及导入导出多种格式。它以单个 Bash 脚本运行，并带有可选插件。

# CONFIGURATION

**~/.nb/**
> 默认目录，包含各笔记本（每个都是 git 仓库）和配置。

**~/.nbrc**
> 用户配置文件：编辑器、默认笔记本、配色主题、同步远程仓库等。

# CAVEATS

以 Bash 脚本实现——可在 macOS 和 Linux 上运行，Windows 需要 WSL 或 Git Bash。同步依赖于为每个笔记本配置的 git 远程仓库。加密笔记需要安装 OpenSSL 或 GPG。

# HISTORY

**nb** 由 **xwmx** 创建，是一个单文件 Bash 命令行笔记工具，强调纯文本和基于 git 的同步。

# INSTALL

```brew: brew install nb```

```nix: nix profile install nixpkgs#nb```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jrnl](/man/jrnl)(1), [notes](/man/notes)(1), [taskwarrior](/man/taskwarrior)(1), [git](/man/git)(1)
