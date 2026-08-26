# TAGLINE

将外部单元文件链接到 systemd

# TLDR

**链接**单元文件

```systemctl link [path/to/unit.service]```

链接**多个**单元文件

```systemctl link [path/to/unit1.service path/to/unit2.service ...]```

# SYNOPSIS

**systemctl link** _PATH_...

# DESCRIPTION

**systemctl link** 在单元文件搜索路径中创建一个符号链接，指向位于其他位置的单元文件。这样无需复制文件即可让 systemd 命令使用该单元。

链接创建在 `/etc/systemd/system/` 中（使用 `--user` 时为对应的用户目录）。原始文件必须使用绝对路径。

# CAVEATS

被链接的文件必须保持在原位；删除它会破坏链接。请使用 `systemctl disable` 移除链接。被链接的单元不会被自动启用；如需开机启动，请在链接后使用 `systemctl enable`。

# HISTORY

**link** 子命令允许测试或使用存放在标准位置之外的单元文件，在开发过程中或单元文件由外部配置管理系统管理时非常有用。

# SEE ALSO

[systemctl-enable](/man/systemctl-enable)(1), [systemctl-disable](/man/systemctl-disable)(1), [systemctl](/man/systemctl)(1)
