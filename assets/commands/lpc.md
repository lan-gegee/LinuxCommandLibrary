# TAGLINE

行式打印机控制程序

# TLDR

**显示所有打印机的状态**

```lpc status all```

**显示指定打印机的状态**

```lpc status [printer]```

**进入交互模式**

```lpc```

# SYNOPSIS

**lpc** [_command_] [_printer_]

# PARAMETERS

_COMMAND_
> 要执行的控制命令。

_PRINTER_
> 打印机名称，或用 "all" 表示所有打印机。

**status**
> 显示打印机和队列状态。

**exit**, **quit**
> 退出 lpc 命令解释器。

**help**
> 显示简短帮助信息。

# DESCRIPTION

**lpc** 对 CUPS 提供的打印机和类队列提供有限的控制能力，也可用于查询队列状态。若未在命令行中指定命令，lpc 会显示提示符并从标准输入读取命令。

CUPS 版本的 lpc 仅实现了原始 Berkeley lpc 程序命令的一个子集。它不能用于配置打印队列——配置任务请使用 **lpadmin**。

# CAVEATS

该命令已**弃用**，将在未来的 CUPS 版本中移除。对非 root 用户，CUPS 实现仅支持 **status** 命令。查询队列状态请改用 **lpstat**，管理操作请使用 **lpadmin**。

# HISTORY

lpc 起源于 **BSD Unix** 的 Berkeley 行式打印机系统，用于控制打印队列。CUPS 提供了一个功能有限的兼容实现。

# INSTALL

```apt: sudo apt install lpr```

```dnf: sudo dnf install cups-client```

```apk: sudo apk add cups-client```

```zypper: sudo zypper install cups-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lp](/man/lp)(1), [lpq](/man/lpq)(1), [lpr](/man/lpr)(1), [lpstat](/man/lpstat)(1), [lpadmin](/man/lpadmin)(8)
