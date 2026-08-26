# TAGLINE

交互式 TeX Live Manager 会话

# TLDR

**启动交互式 tlmgr shell**

```tlmgr shell```

**启动 shell 并执行一条命令**（例如列出更新）

```tlmgr shell <<< "update --list"```

**将多条命令通过管道传入 shell**

```printf "info [package]\nquit\n" | tlmgr shell```

# SYNOPSIS

**tlmgr shell**

# DESCRIPTION

**tlmgr shell** 启动一个交互式 TeX Live Manager 会话，你可以在其中连续执行多条 tlmgr 命令而无需每次重新启动程序。由于 TeX Live 软件包数据库只加载一次，这对批量操作来说更快。

一般来说，所有可以在命令行上给出的 tlmgr 操作都可以作为 shell 中的命令使用（例如 `update --list`、`install`、`info`、`search`）。输入 `quit` 或 `exit`（或发送 EOF）可退出 shell。`protocol` 命令会打印当前的协议版本。该 shell 还支持机器可读输出，便于外部工具编写脚本。

# SEE ALSO

[tlmgr](/man/tlmgr)(1), [tlmgr-install](/man/tlmgr-install)(1), [tlmgr-update](/man/tlmgr-update)(1)
