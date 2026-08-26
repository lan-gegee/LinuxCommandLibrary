# TAGLINE

查询 NTP 守护进程的状态和配置信息

# TLDR

以**交互模式启动 ntpq**

```ntpq```

打印 **NTP 对等服务器列表**

```ntpq -p```

打印 NTP 对等服务器列表但**不解析主机名**

```ntpq -n -p```

在**调试模式**下使用 ntpq

```ntpq -d```

打印 **NTP 系统变量**的值

```ntpq -c rv```

# SYNOPSIS

**ntpq** [_options_] [_host_...]

# PARAMETERS

**-n, --numeric**
> 以数字形式显示地址，不做 DNS 解析

**-c _command_, --command _command_**
> 执行命令而不进入交互模式

**-d, --debug-level**
> 启用调试输出

**-i, --interactive**
> 强制进入交互模式。

**-4**, **-6**
> 仅使用 IPv4 或 IPv6 解析主机名。

**-w, --wide**
> 使用更宽的对等表，长主机名不会被截断。

**-k** _FILE_, **--keyfile** _FILE_
> 从 _FILE_ 读取对称密钥，用于经过认证的控制请求。

**-a** _KEYID_, **--authentication** _KEYID_
> 发送经过认证的查询时使用给定的密钥 ID。

**-p, --peers**
> 打印所有已配置对等服务器的摘要（与交互模式的 `peers` 相同）。

**-V, --version**
> 打印版本信息并退出。

# DESCRIPTION

**ntpq** 查询 NTP 守护进程的状态和配置信息。它可以在交互模式和命令行模式下显示对等关联、系统变量和同步统计信息。

对等服务器列表（**-p**）显示所有已配置的时间源，各列含义如下：
- **remote**：服务器地址（* = 当前同步源）
- **refid**：参考时钟或上游服务器
- **st**：stratum 层级
- **reach**：可达性寄存器（377 = 最近所有查询均成功）
- **delay/offset/jitter**：以毫秒为单位的时间指标

交互模式提供额外的命令，可用于详细检查 NTP 守护进程的状态。

# CAVEATS

默认查询本地 ntpd；指定主机名可查询远程守护进程。要求 ntpd 正在运行。部分信息可能需要认证才能访问。输出格式晦涩；解释请参阅 NTP 文档。

# INSTALL

```apt: sudo apt install ntpsec```

```dnf: sudo dnf install ntpsec```

```apk: sudo apk add ntpsec```

```zypper: sudo zypper install ntpsec```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ntpd](/man/ntpd)(8), [ntpdate](/man/ntpdate)(8), [chronyc](/man/chronyc)(1), [timedatectl](/man/timedatectl)(1)
