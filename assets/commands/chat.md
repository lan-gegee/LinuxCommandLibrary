# TAGLINE

自动化调制解调器和串口设备对话脚本

# TLDR

直接执行**聊天脚本**

```chat '[expect_send_pairs]'```

从**文件**执行聊天脚本

```chat -f '[path/to/chat_script]'```

设置自定义**超时**

```chat -t [timeout_in_seconds] '[expect_send_pairs]'```

启用向 syslog 输出的**详细日志**

```chat -v '[expect_send_pairs]'```

使用**报告文件**记录日志

```chat -r [path/to/report_file] '[expect_send_pairs]'```

使用变量**拨号**

```chat -T '[phone_number]' '"ATDT\\T CONNECT"'```

包含**中止条件**

```chat 'ABORT "[error_string]" [expect_send_pairs]'```

# SYNOPSIS

**chat** [_options_] _script_

# DESCRIPTION

**chat** 通过交换期望-发送（expect-send）字符串对来自动化与调制解调器和串行设备的对话。它等待设备返回期望的字符串，然后发送响应，并按照脚本的序列反复执行这一过程。

主要用途是通过串行线路和调制解调器建立 PPP（Point-to-Point Protocol，点对点协议）连接。典型的聊天脚本会用 AT 命令初始化调制解调器、拨打电话号码、等待 CONNECT 响应并处理登录序列。还可以定义中止字符串，在出现 BUSY 或 NO CARRIER 等错误情况时终止脚本。

chat 属于 ppp 软件包，通常由 pppd 调用而不是直接运行。脚本可以在命令行内联指定，也可以从文件加载。

# PARAMETERS

**-f** _file_
> 从文件读取脚本

**-t** _seconds_
> 等待响应的超时时间

**-v**
> 向 syslog 记录详细日志

**-r** _file_
> 将特定字符串记录到报告文件

**-T** _string_
> 用该字符串替换脚本中的 \T

**-V**
> 将全部对话记录到 stderr

# SCRIPT SYNTAX

**ABORT** _string_
> 收到该字符串时中止

**TIMEOUT** _seconds_
> 为下一个期望设置超时

**REPORT** _string_
> 将该字符串记录到报告文件

# CAVEATS

主要用于旧式调制解调器/PPP 连接。时序非常关键；慢速设备需调整超时。转义序列可能需要正确加引号。

# INSTALL

```apt: sudo apt install ppp```

```dnf: sudo dnf install ppp```

```pacman: sudo pacman -S ppp```

```apk: sudo apk add ppp-chat```

```zypper: sudo zypper install ppp```

```nix: nix profile install nixpkgs#ppp```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pppd](/man/pppd)(8), [expect](/man/expect)(1)

# RESOURCES

```[Source code](https://github.com/ppp-project/ppp)```

```[Documentation](https://man7.org/linux/man-pages/man8/chat.8.html)```

<!-- verified: 2026-06-22 -->
