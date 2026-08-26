# TAGLINE

开源 PBX 与电话服务器

# TLDR

**连接**到正在运行的服务器

```asterisk -r -vvv```

运行**单条命令**

```asterisk -r -x "command"```

显示 **SIP 对端**

```asterisk -r -x "sip show peers"```

显示**当前通话**

```asterisk -r -x "core show channels"```

显示**语音信箱**用户

```asterisk -r -x "voicemail show users"```

**挂断**一个通道

```asterisk -r -x "hangup request channel_ID"```

**重新加载** SIP 配置

```asterisk -r -x "sip reload"```

# SYNOPSIS

**asterisk** [_OPTIONS_]

# DESCRIPTION

**asterisk** 用于运行和管理 Asterisk PBX（专用交换机）电话服务器。它处理 VoIP 呼叫和传统电话线路，提供语音信箱、会议、交互式语音应答（IVR）等功能。

# PARAMETERS

**-r**
> 重新连接到正在运行的 Asterisk 实例

**-R**
> 与 -r 相同，但断开连接后会尝试重新连接

**-x** _command_
> 执行一条 CLI 命令后退出

**-v**
> 提高详细程度（可多次使用）

**-c**
> 以控制台模式（前台）启动 Asterisk

**-g**
> 崩溃时转储核心

**-n**
> 在控制台中禁用 ANSI 颜色

# CONFIGURATION

**/etc/asterisk/asterisk.conf**
> 主配置文件，控制全局设置、目录路径和模块加载。

**/etc/asterisk/extensions.conf**
> 拨号计划配置，定义呼叫路由、IVR 菜单和应用逻辑。

**/etc/asterisk/sip.conf**
> 传统 SIP 通道驱动配置，用于对端、中继和注册。

**/etc/asterisk/pjsip.conf**
> 现代 PJSIP 协议栈配置，涵盖端点、传输与认证。

**/etc/asterisk/voicemail.conf**
> 语音信箱系统配置，包括邮箱定义和通知设置。

**/etc/asterisk/modules.conf**
> 控制 Asterisk 启动时加载哪些模块。

# CAVEATS

需要正确配置 SIP/PJSIP、拨号计划和分机。电话系统要求理解 VoIP 协议、编解码器和网络知识。配置内容繁多，通常存放于 /etc/asterisk/ 目录。

# HISTORY

**Asterisk** 是由 Digium（现 Sangoma）创建的开源 PBX 和电话工具包，支撑着从小型办公室到大型呼叫中心的各种通信解决方案。

# INSTALL

```dnf: sudo dnf install asterisk```

```aur: yay -S asterisk```

```apk: sudo apk add asterisk```

```nix: nix profile install nixpkgs#asterisk```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[asterisk-cli](/man/asterisk-cli)(8)
