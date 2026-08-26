# TAGLINE

简单的命令行时间跟踪工具

# TLDR

**开始跟踪时间**

```zeit track --project [myproject] --task "[coding]"```

**列出某个项目的时间条目**

```zeit list --project [myproject]```

**以 JSON 格式导出条目**

```zeit export --format json```

# SYNOPSIS

**zeit** _command_ [_options_]

# DESCRIPTION

**zeit** 是一个跨平台的终端时间跟踪工具，支持按项目、任务和条目进行分层归类。它在本地存储数据，支持自然语言参数，并可将记录的时间块导出为 JSON 以供外部工具使用。

# HISTORY

**zeit** 由 **Marius**（mrusme）创建，使用 **Go** 编写。

# INSTALL

```aur: yay -S zeit```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[watson](/man/watson)(1)
