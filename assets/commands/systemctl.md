# TAGLINE

控制 systemd 服务与系统

# TLDR

显示所有**正在运行的服务**

```systemctl status```

列出**失败的**单元

```systemctl --failed```

**启动/停止/重启**一个服务

```systemctl start|stop|restart unit```

设置服务开机**启用/禁用**

```systemctl enable|disable unit```

重载 **systemd 配置**

```systemctl daemon-reload```

检查单元是否**处于活动/已启用/失败状态**

```systemctl is-active|is-enabled|is-failed unit```

按状态列出所有**服务单元**

```systemctl list-units -t service --state running```

显示单元文件的**内容**

```systemctl cat unit```

# SYNOPSIS

**systemctl** [_OPTIONS_...] _COMMAND_ [_UNIT_...]

# DESCRIPTION

**systemctl** 控制 systemd 系统与服务管理器。它可用于查看和控制 systemd 系统的状态、管理服务、检查单元依赖，以及执行重启或关机等系统操作。

# PARAMETERS

**-t, --type=TYPE**
> 按单元类型过滤（service、socket、target、mount、timer 等）

**--state=STATE**
> 按单元状态过滤（active、inactive、failed、running 等）

**-a, --all**
> 显示所有单元，包括未激活的单元

**--user**
> 管理用户服务而不是系统服务

**--no-block**
> 立即返回而不等待操作完成

**--now**
> 将 enable/disable 与 start/stop 结合执行

**--force**
> 覆盖安全检查或符号链接冲突

**-q, --quiet**
> 抑制输出

**-n, --lines=NUM**
> status 显示的日志行数

**--no-pager**
> 不将输出送入分页器

**-o, --output=FORMAT**
> 控制日志输出格式（short、verbose、json 等）

# COMMON COMMANDS

**list-units**：列出活动单元或指定单元
**list-unit-files**：显示已安装的单元文件及其启用状态
**status**：显示运行时状态和最近的日志
**start/stop**：启动或停止单元
**restart**：先停止再启动单元
**reload**：在不停止服务的情况下重载单元配置
**enable/disable**：启用或禁用单元开机激活
**mask/unmask**：完全禁用或重新启用一个单元
**edit**：使用 drop-in 片段编辑单元文件
**cat**：显示单元文件内容
**show**：以机器可读格式显示单元属性
**daemon-reload**：重载 systemd 配置和单元文件
**is-active/is-enabled/is-failed**：检查单元状态
**kill**：向单元的进程发送信号
**poweroff/reboot/halt**：系统电源命令
**suspend/hibernate**：进入睡眠状态

# CAVEATS

某些命令需要 root 权限。**--user** 标志管理 ~/.config/systemd/user/ 下的用户级服务。修改单元文件后请执行 **daemon-reload**。被屏蔽的单元即使手动也无法启动。

# HISTORY

**systemctl** 是 **systemd** 的一部分，由 Lennart Poettering 于 2010 年推出。它取代了传统的 SysV init 脚本以及 **service** 和 **chkconfig** 等服务管理工具。

# INSTALL

```apt: sudo apt install systemd```

```dnf: sudo dnf install systemd```

```pacman: sudo pacman -S systemd```

```zypper: sudo zypper install systemd```

```brew: brew install systemd```

```nix: nix profile install nixpkgs#systemd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[journalctl](/man/journalctl)(1), [service](/man/service)(8)
