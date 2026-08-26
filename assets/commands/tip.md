# TAGLINE

通过串行线路连接远程系统

# TLDR

**连接**到 /etc/remote 中定义的系统

```tip [system_name]```

以特定波特率**连接**

```tip -[115200] [system_name]```

直接**连接**串口设备

```tip [/dev/ttyUSB0]```

以详细输出模式**连接**

```tip -v [system_name]```

禁用波浪号转义序列**连接**

```tip -n [system_name]```

# SYNOPSIS

**tip** [**-v**] [**-**_speed_] {_system_ | _phone-number_ | _device_}

# DESCRIPTION

**tip** 通过串行线路、调制解调器或直连的串口设备与远程主机建立全双工终端连接。它是与串口控制台、微控制器、路由器管理端口或拨号系统通信的经典 Unix 方式之一。

连接目标通常是 **/etc/remote** 数据库中的命名条目，该数据库记录了每个系统的设备、波特率等设置。目标也可以直接给设备路径，或者在有调制解调器时给出要拨打的电话号码。

连接期间 **tip** 基本是透明的：按键被发送到远端，远端输出显示在本地。发给本地 **tip** 进程的命令通过在行首输入波浪号（**~**）转义序列完成，例如 **~.** 断开连接、**~p** 发送文件、**~C** 派生本地 shell。

# PARAMETERS

**-v**

> 详细模式：运行脚本文件时回显其中的命令。

**-**_speed_

> 设置连接波特率（例如 **-115200** 或 **-9600**），覆盖来自 /etc/remote 的值。

**-n**

> 本次会话禁用波浪号转义序列的解释。

# ESCAPE SEQUENCES

**~.**

> 断开连接并退出。

**~c** _dir_

> 更改本地工作目录。

**~!**

> 在本地主机上派生交互式 shell。

**~p** _from_ [_to_]

> 向远程主机发送（put）文件。

**~t** _from_ [_to_]

> 从远程主机接收（take）文件。

**~#**

> 向远程系统发送 BREAK。

# CAVEATS

**tip** 是 BSD 实用工具，大多数 Linux 发行版默认未安装，更常见的是 **cu**、**minicom** 或 **picocom**。支持的转义序列和选项的确切集合因实现而异；请查阅本地手册页。

# HISTORY

**tip** 起源于 Berkeley Unix（BSD），与 **cu**（call Unix）工具及 UUCP 工具套件同期出现。它至今仍是 BSD 系统基础组件的一部分，是最古老的串口终端访问工具之一。

# SEE ALSO

[cu](/man/cu)(1), [minicom](/man/minicom)(1), [picocom](/man/picocom)(1), [screen](/man/screen)(1), [stty](/man/stty)(1)

# RESOURCES

```[Source code](https://github.com/freebsd/freebsd-src/tree/main/usr.bin/tip)```

<!-- verified: 2026-06-16 -->
