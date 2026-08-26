# TAGLINE

向 Kodi 媒体中心发送命令

# TLDR

**发送一个动作**

```kodi-send --action="[PlayPause]"```

**发送到指定主机**

```kodi-send --host=[192.168.1.100] --action="[Stop]"```

**发送一条通知**

```kodi-send --notification="[Backup complete]"```

**以带延迟的宏形式发送多个动作**

```kodi-send --action="[Up]" --delay=[500] --action="[Select]"```

**发送按键事件**

```kodi-send --button="[KB_Return]"```

**打开一个媒体 URL**

```kodi-send --action="PlayMedia([url])"```

# SYNOPSIS

**kodi-send** [_options_]

# PARAMETERS

**-a**, **--action** _ACTION_
> 要发送的动作。可多次指定以构成宏。

**--button** _BUTTON_
> 发送按键事件。可多次指定。

**--host** _HOST_
> Kodi 主机地址（默认 localhost）。

**--port** _PORT_
> Kodi EventClient 端口（默认 9777）。

**--notification** _MESSAGE_
> 向 Kodi 发送通知。

**--log** _MESSAGE_
> 向 Kodi 发送日志消息。

**--loglevel** _LEVEL_
> 使用 --log 时的日志级别（默认 LOGDEBUG）。

**--mouse** _X,Y_
> 向 Kodi 发送鼠标位置。

**-d**, **--delay** _T_
> 等待 T 毫秒。可在动作之间使用以构成宏。

**--keymap** _KEYMAP_
> 指定自定义键位映射。

**--help**
> 显示帮助信息。

# DESCRIPTION

**kodi-send** 是一款通过远程控制网络中 Kodi 媒体中心实例的命令行工具。它默认使用端口 9777 上的 Kodi EventClient UDP 协议通信，发送模拟遥控器按键、导航事件和媒体播放操作的动作命令。

该工具支持大量 Kodi 内置动作，包括播放控制（播放、暂停、停止、跳转）、音量调节、菜单导航（方向移动和选择），以及通过 URL 或文件路径加载媒体。由于完全基于命令行运行，kodi-send 非常适合编写自动化媒体工作流脚本、将 Kodi 接入家庭自动化系统，或构建自定义遥控界面。

# CAVEATS

需要启用 Kodi EventClient。需要网络访问。属于 kodi-eventclients 的一部分。

# HISTORY

kodi-send 是 **Kodi**（前身为 XBMC）事件客户端工具的一部分，用于远程控制媒体中心。

# INSTALL

```apt: sudo apt install kodi-eventclients-kodi-send```

```pacman: sudo pacman -S kodi```

```apk: sudo apk add kodi```

```nix: nix profile install nixpkgs#kodi```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[curl](/man/curl)(1)
