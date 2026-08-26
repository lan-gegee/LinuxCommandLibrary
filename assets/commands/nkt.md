# TAGLINE

在终端中记笔记，支持日志、任务和卡片盒笔记法（Zettelkasten）

# TLDR

**添加一条日志**

```nkt log [journal_name]```

**阅读笔记**

```nkt read [note_name]```

**编辑一条笔记**

```nkt edit [note_name]```

**列出所有笔记**

```nkt list```

# SYNOPSIS

**nkt** _command_ [_options_] [_arguments_]

# DESCRIPTION

**nkt** 是一个终端笔记工具，结合了日志、笔记、任务清单和习惯打卡链。它的灵感来自 Dendron、jrnl、vim-wiki，以及 Zettelkasten 和"Don't break the chain"等方法。

功能包括带时间戳的日志条目、跨所有笔记的模糊查找（类似 fzf）、使用 **@tag** 语法的基于标签的组织方式、任务管理，以及便于导航的笔记间链接。

# CAVEATS

笔记存储在本地。该项目已从 GitHub 迁移到 sourcehut。

# HISTORY

**nkt** 由 **fjebaker** 创建，使用 **Zig** 编写。

# INSTALL

```brew: brew install nkt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nb](/man/nb)(1), [jrnl](/man/jrnl)(1)
