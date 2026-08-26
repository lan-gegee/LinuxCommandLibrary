# TAGLINE

在 AX.25 端口上周期性发送消息

# TLDR

在端口上每 30 分钟（默认）**发送一次信标**

```beacon [port] "[message text]"```

以分钟为单位**自定义发送间隔**

```beacon -t [interval] [port] "[message text]"```

**只发送一次**消息后退出

```beacon -s [port] "[message text]"```

**指定源呼号**而非接口默认值

```beacon -c [src_call] [port] "[message text]"```

**设置目的呼号**（及可选的数字中继）

```beacon -d "[dest_call] [digi1] [digi2]" [port] "[message text]"```

**在前台运行**，不转为守护进程

```beacon -f [port] "[message text]"```

**发送一次性的邮件信标**（目的地址设为 MAIL）

```beacon -m [port] "[message text]"```

# SYNOPSIS

**beacon** [_-c src_call_] [_-d dest_call[digi ..]_] [_-f_] [_-l_] [_-m_] [_-s_] [_-t interval_] [_-v_] _port_ "_message_"

# PARAMETERS

**-c** _src_call_
> 配置信标的源呼号。默认为接口的 AX.25 呼号。

**-d** _dest_call_
> 配置目的呼号。默认为 **IDENT**。参数加引号时可后跟数字中继，以空格分隔。

**-f**
> 不转入后台；进程保持附着于终端。

**-l**
> 启用向系统日志记录错误。默认禁用。

**-m**
> 只发送一次消息，目的地址设为 **MAIL** 而非 **IDENT**。

**-s**
> 只发送一次消息文本后退出。

**-t** _interval_
> 发送间隔，以分钟为单位。默认为 **30**。

**-v**
> 显示版本信息。

_port_
> 在 **/etc/ax25/axports** 中定义的 AX.25 端口名。

_message_
> 要发送的文本。请给字符串加引号，使空格和特殊字符原样传递。

# DESCRIPTION

**beacon** 是 Linux 业余分组无线电工具集 **ax25-tools** 的一部分。它在配置好的 AX.25 端口上周期性地发送一个包含用户指定文本消息的 UI（Unnumbered Information）帧。信标用于宣告电台的存在、宣传服务，或在分组网络上发布 APRS 风格的位置和状态数据。

默认目的地址为 **IDENT**，消息每 30 分钟发送一次；两者均可覆盖。程序通常会自我守护化，以便在操作员继续其他工作时保持在后台运行。**-s** 和 **-m** 选项会将其变为一次性发送器。

指定的 _port_ 必须是 **/etc/ax25/axports** 中列出的已配置 AX.25 接口（通常是 KISS TNC、声卡调制解调器或内核 AX.25 设备）。

# EXAMPLES

每 15 分钟宣告一次 BBS：

```beacon -t 15 radio "Welcome to AB1CDE BBS, telnet bbs.example.org"```

发送单个 MAIL 信标后退出：

```beacon -m radio "QSL via email ab1cde@example.org"```

经由两个数字中继发送信标：

```beacon -d "APRS WIDE1-1 WIDE2-1" radio "!4807.38N/01131.00E>Test station"```

# CONFIGURATION

AX.25 端口在 **/etc/ax25/axports** 中定义，每个端口一行：

```
# portname callsign  baudrate  paclen  window description
radio      AB1CDE-1  1200      256     2      VHF packet on 144.39 MHz
```

传给 **beacon** 的端口名必须与第一列匹配。调用 **beacon** 前，AX.25 网络协议栈和 TNC（内核 KISS、**kissattach**、**soundmodem** 等）必须已经就绪。

# CAVEATS

需要 AX.25 内核协议栈和已连接的 AX.25 接口；没有有效端口时 **beacon** 无法启动。频繁发送信标会浪费共享无线电信道容量，在业余分组网络中被普遍劝阻。除 APRS 场景外，许多操作员建议间隔设为 30 分钟或更长。运行 **beacon** 通常需要能打开 AX.25 套接字的权限（通常是 root 或属于相应组）。

# HISTORY

**beacon** 随 Linux AX.25 协议栈的用户态工具集 **ax25-tools** 一同发布。Linux 的 AX.25 实现于 **20 世纪 90 年代初**由 **Alan Cox** 等人启动，目的是把业余分组无线电带入 Linux，此后 **ax25-tools**一直由 Linux AX.25 项目维护。由于 AX.25 链路层协议自其 1984 年原始规范以来保持稳定，这个工具几十年来几乎没有变化。

# INSTALL

```apt: sudo apt install ax25-tools```

```dnf: sudo dnf install ax25-tools```

```aur: yay -S ax25-tools```

```apk: sudo apk add ax25-tools```

```zypper: sudo zypper install ax25-tools```

```nix: nix profile install nixpkgs#ax25-tools```

<!-- packages: 2026-07-22 -->
# SEE ALSO

