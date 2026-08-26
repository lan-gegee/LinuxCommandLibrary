# TAGLINE

系统运行/停机历史与统计报告工具

# TLDR

**显示运行/停机摘要**

```tuptime```

**列出所有启动/关机事件**

```tuptime -l```

**以 CSV 格式输出**

```tuptime --csv```

# SYNOPSIS

**tuptime** [_options_]

# DESCRIPTION

**tuptime** 报告系统的历史与统计实时数据，并在重启之间保留这些数据。它将所有启动和关机事件记录在 SQLite 数据库中，计算运行和停机时间百分比，记录使用过的内核，并找出最长、最短以及平均的运行/停机时段。

# HISTORY

**tuptime** 由 **Ricardo Fraile**（rfmoz）创建，用 **Python** 编写。

# INSTALL

```dnf: sudo dnf install tuptime```

```nix: nix profile install nixpkgs#tuptime```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[uptime](/man/uptime)(1), [last](/man/last)(1), [systemd-analyze](/man/systemd-analyze)(1)
