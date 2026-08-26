# TAGLINE

将系统时钟与远程服务器同步的网络时间协议守护进程

# TLDR

**启动**守护进程

```sudo ntpd```

**一次性**同步系统时间（同步后退出）

```sudo ntpd --quit```

同步一次并允许**大幅调整**

```sudo ntpd --panicgate --quit```

# SYNOPSIS

**ntpd** [_options_]

# PARAMETERS

**-q, --quit**
> 设置一次时间后退出

**-g, --panicgate**
> 允许大范围的时间校正（正常情况下偏差超过 1000 秒会被拒绝）

**-n, --nofork**
> 在前台运行，不守护进程化

**-c _file_, --configfile _file_**
> 使用备用配置文件

**-p _file_, --pidfile _file_**
> 指定 PID 文件位置

**-d, --debug-level**
> 提高调试详细程度（可重复使用）

# DESCRIPTION

**ntpd** 是网络时间协议守护进程，用于将系统时钟与远程 NTP 服务器或本地参考时钟同步。它通过持续调整时钟频率来补偿漂移，从而维持准确的时间。

守护进程从 **/etc/ntp.conf** 读取配置，该文件指定时间服务器、访问限制和行为选项。运行后它会逐渐微调时钟，避免可能干扰应用程序的剧烈时间跳变。

若要进行一次性同步而不运行持续运行的守护进程，请使用 **--quit** 选项。**--panicgate** 选项允许在时钟偏差很大时进行初始同步。

# CAVEATS

默认拒绝大幅时间跳变（>1000 秒）；对严重漂移的时钟做初始同步时请使用 **--panicgate**。会与其他时间同步守护进程冲突（systemd-timesyncd、chrony）。端口 123（UDP）必须可访问。现代系统通常更倾向于使用 **chrony** 或 **systemd-timesyncd**。

# HISTORY

NTP 由特拉华大学的 David L. Mills 开发，最早出现于 1985 年。参考实现 ntpd 数十年来一直是标准的 NTP 守护进程。

# INSTALL

```apt: sudo apt install ntpsec```

```dnf: sudo dnf install ntpsec```

```pacman: sudo pacman -S openntpd```

```apk: sudo apk add openntpd```

```zypper: sudo zypper install ntpsec```

```nix: nix profile install nixpkgs#openntpd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ntpq](/man/ntpq)(8), [ntpdate](/man/ntpdate)(8), [chrony](/man/chrony)(8), [timedatectl](/man/timedatectl)(1)
