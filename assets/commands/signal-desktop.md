# TAGLINE

加密通讯桌面应用程序

# TLDR

**启动 Signal Desktop**

```signal-desktop```

最小化到系统托盘**启动**

```signal-desktop --start-in-tray```

**使用自定义配置文件**，用户数据相互独立

```signal-desktop --user-data-dir=[~/.config/SignalProfile]```

启用系统托盘图标

```signal-desktop --use-tray-icon```

打开 DevTools **启动**以便调试

```signal-desktop --enable-dev-tools```

# SYNOPSIS

**signal-desktop** [_options_]

# PARAMETERS

**--start-in-tray**
> 以窗口最小化到系统托盘的方式启动 Signal。

**--use-tray-icon**
> 在系统托盘中显示图标。允许最小化到托盘而不是退出应用。

**--user-data-dir=**_PATH_
> 使用自定义的用户数据目录。适合运行多个 Signal 配置或管理多个手机号码。

**--enable-dev-tools**
> 启动时打开 Chromium DevTools 面板以便调试。

**--enable-gpu**
> 启用 GPU 加速。

**--no-sandbox**
> 禁用 Chromium 沙箱（出于安全考虑不建议）。

**--proxy-server=**_URL_
> 为网络连接使用代理服务器。

# DESCRIPTION

**signal-desktop** 是 Signal Private Messenger 的官方 Linux 桌面应用。它提供与 Signal 手机应用同步的端到端加密消息、语音通话和视频通话。桌面客户端要求先在手机上安装并设置好 Signal，由手机作为主设备。

该应用基于 Electron 构建，提供功能完整的消息界面，包括群聊、阅后即焚消息、表情回应和文件分享。消息通过 Signal 的安全协议在已关联设备之间同步。

Signal Desktop 可通过基于 Debian 的发行版上的官方 APT 软件仓库安装，也可以作为 Snap 包或 Flatpak 安装。

# CAVEATS

Signal Desktop 需要与移动设备上的既有 Signal 账号关联，不能作为独立客户端使用。使用 **--user-data-dir** 运行多个配置时，每个配置必须关联不同的手机号码。某些功能可能需要手机应用定期在线才能同步。

# HISTORY

**Signal Desktop** 于 **2015 年**最初作为 Chrome 应用发布，随后于 **2017 年**过渡为独立的 Electron 应用。Signal 本身源自 TextSecure，由 Open Whisper Systems（Moxie Marlinspike 于 **2013 年**创立）开发。用于端到端加密的 Signal 协议已被众多其他通讯平台采用。**2018 年**，Signal 基金会成立为非营利组织以支持 Signal 的开发。桌面客户端持续活跃开发并定期推送安全更新。

# INSTALL

```pacman: sudo pacman -S signal-desktop```

```nix: nix profile install nixpkgs#signal-desktop```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[telegram-desktop](/man/telegram-desktop)(1), [gpg](/man/gpg)(1)
