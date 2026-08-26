# TAGLINE

用于 UFW 防火墙管理的终端界面

# TLDR

**启动防火墙管理 TUI**

```sudo tufw```

# SYNOPSIS

**sudo tufw**

# DESCRIPTION

**tufw** 为简单防火墙（UFW）提供了基于终端的界面，带有下拉菜单和表单化的规则编辑。每个操作在幕后都会转换为常规的 UFW 命令。通过 SSH 连接使用也毫无问题。

# CAVEATS

必须以 root 身份运行。

# HISTORY

**tufw** 由 **Thomas Pellegatta**（peltho）创建，用 **Go** 编写。

# INSTALL

```aur: yay -S tufw```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ufw](/man/ufw)(8), [iptables](/man/iptables)(8), [firewalld](/man/firewalld)(1)
