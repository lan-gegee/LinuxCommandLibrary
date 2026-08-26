# TAGLINE

管理 Asterisk PBX 服务器的交互式控制台

# TLDR

**连接**到正在运行的 Asterisk 控制台

```asterisk -r```

**连接并输出详细日志**

```asterisk -rvvv```

从 Shell **执行 CLI 命令**

```asterisk -rx "sip show peers"```

**重新加载拨号计划**

```asterisk -rx "dialplan reload"```

**显示当前通话**

```asterisk -rx "core show channels"```

**显示 SIP 注册状态**

```asterisk -rx "sip show registry"```

**优雅关闭** Asterisk

```asterisk -rx "core stop gracefully"```

# SYNOPSIS

**asterisk** **-r** [**-v**...]

**asterisk** **-rx** "_command_"

# PARAMETERS

**-r**
> 通过远程控制台连接到正在运行的 Asterisk 实例

**-R**
> 与 -r 相同，但断开连接后会尝试重新连接

**-v**
> 提高详细程度（可重复使用：-vvv 表示更详细）

**-x** _command_
> 执行一条 CLI 命令后退出

**-c**
> 以控制台模式（前台）启动 Asterisk

**-g**
> 崩溃时转储核心（用于调试）

**-n**
> 禁用 ANSI 彩色输出

# CLI COMMANDS

**core show help** [_command_]
> 显示 CLI 命令的帮助信息

**core show channels**
> 列出活动的通道和通话

**core show applications**
> 列出可用的拨号计划应用程序

**dialplan reload**
> 重新加载拨号计划配置

**sip show peers**
> 显示已配置的 SIP 对端

**sip show registry**
> 显示 SIP 注册状态

**pjsip show endpoints**
> 显示 PJSIP 端点（现代 SIP 协议栈）

**module reload** _module_
> 重新加载指定模块

**logger reload**
> 重新加载日志配置

**core stop gracefully**
> 待通话结束后停止 Asterisk

**core stop now**
> 立即停止 Asterisk

**database show** [_family_]
> 显示 AstDB 数据库内容

# DESCRIPTION

**Asterisk CLI** 是用于管理 Asterisk PBX（专用交换机）服务器的命令行界面。它提供对电话系统的实时监控、配置重载和管理控制。

使用 **asterisk -r** 连接到正在运行的 Asterisk 实例。对于脚本和自动化场景，使用 **asterisk -rx "command"** 以非交互方式执行命令。交互式控制台内支持命令的 Tab 补全。

CLI 可访问所有 Asterisk 子系统，包括 SIP/PJSIP 对端、活动通道、拨号计划、语音信箱、队列以及内部数据库。详细级别（-v 标志）控制实时事件输出的数量。

配置更改通常需要重新加载模块而非完全重启。修改 extensions.conf 后使用 **dialplan reload**，或针对特定模块使用 **module reload**。

# CONFIGURATION

**/etc/asterisk/asterisk.conf**
> 主配置文件，控制全局设置、模块路径和日志。

**/etc/asterisk/extensions.conf**
> 拨号计划配置，定义呼叫路由规则和 IVR 逻辑。

**/etc/asterisk/sip.conf**
> 传统 SIP 对端和中继配置。

**/etc/asterisk/pjsip.conf**
> 现代 PJSIP 端点与传输配置。

# CAVEATS

必须先启动 Asterisk 守护进程才能用 **-r** 连接。某些命令需要加载特定模块。传统 **chan_sip** 模块使用 **sip** 命令，而现代部署使用 **pjsip** 命令。过高的详细级别会影响繁忙系统的性能。

# HISTORY

**Asterisk** 由 Digium（现 Sangoma）的 **Mark Spencer** 创建，于 **1999** 年首次发布。它开创了基于软件的 PBX 系统和 VoIP 电话。CLI 随 Asterisk 一同演进，Asterisk 12（2013 年）引入 PJSIP，在传统 chan_sip 模块之外提供了现代 SIP 协议栈。

# INSTALL

```dnf: sudo dnf install asterisk```

```aur: yay -S asterisk```

```apk: sudo apk add asterisk```

```nix: nix profile install nixpkgs#asterisk```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[asterisk](/man/asterisk)(8)
