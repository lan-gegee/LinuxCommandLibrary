# TAGLINE

用于浏览整数数列在线百科（OEIS）的 TUI 和 CLI 工具

# TLDR

**启动 OEIS 浏览器**

```oeis-tui```

**按关键词搜索数列**

```oeis-tui search "[keyword]"```

**获取特定数列**

```oeis-tui get [A000045]```

# SYNOPSIS

**oeis-tui** [_command_] [_options_]

# DESCRIPTION

**oeis-tui** 是一个可在终端中浏览整数数列在线百科（OEIS）的 TUI 和 CLI 工具。它支持按 ID、关键词、作者或部分数列项进行搜索，提供分页浏览以及概览、公式等详情标签页。

其 CLI 提供对 UNIX 友好的多种格式输出，适合通过管道与其他工具集成。

# CAVEATS

查询 OEIS 数据库需要互联网连接。

# HISTORY

**oeis-tui** 由 **hako** 创建，使用 **Go** 编写。

# INSTALL

```zypper: sudo zypper install oeis-tui```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bc](/man/bc)(1), [numbat](/man/numbat)(1)
