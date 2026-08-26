# TAGLINE

实时监视并显示 NetworkManager 事件

# TLDR

开始**监视** NetworkManager 的变化

```nmcli monitor```

# SYNOPSIS

**nmcli monitor**

# DESCRIPTION

**nmcli monitor** 实时监视并显示 NetworkManager 事件。它会在事件发生时展示网络连接、设备状态和连通性状态的变化。

显示的事件包括连接的激活与停用、设备状态变化（连接中、已连接、已断开）、IP 地址分配以及整体连通性状态的变化。

该命令会持续运行，直到用 **Ctrl+C** 中断，因此适合用于调试网络问题或编写对网络事件作出响应的脚本。

# CAVEATS

在前台运行并占用终端。只显示监视启动之后发生的事件；不显示历史事件。如果要在脚本中解析输出，可以考虑使用 nmcli 的 **-t**（terse）选项获取机器可读的输出。

# INSTALL

```apt: sudo apt install network-manager```

```apk: sudo apk add networkmanager-cli```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nmcli](/man/nmcli)(1), [nmcli-general](/man/nmcli-general)(1), [nmcli-connection](/man/nmcli-connection)(1), [nmcli-device](/man/nmcli-device)(1)
