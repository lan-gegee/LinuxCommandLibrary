# TAGLINE

远程桌面客户端应用程序

# TLDR

**启动 Remmina**

```remmina```

**连接到已保存的连接**

```remmina -c [connection_name]```

**连接到 RDP 服务器**

```remmina -c rdp://[user]@[host]```

**连接到 VNC 服务器**

```remmina -c vnc://[host]```

**连接到 SSH**

```remmina -c ssh://[user]@[host]```

# SYNOPSIS

**remmina** [_-a_|_-i_|_-n_|_-q_|_-v_] [_-c file_] [_-e file_] [_-p tabindex_] [_-s server_] [_-t protocol_] [_options_]

# PARAMETERS

**-c**, **--connect** _file_
> 连接到文件或受支持的 URI（RDP、VNC、SSH、SPICE）所描述的桌面。

**-e**, **--edit** _file_
> 打开并编辑连接配置文件。

**-n**, **--new**
> 创建新的连接配置。

**-t**, **--protocol** _protocol_
> 为新连接使用默认协议（RDP、VNC、SSH、SPICE）。

**-s**, **--server** _server_
> 为新连接使用默认服务器名（与 --new 一起使用）。

**-p**, **--pref** _tabindex_
> 显示首选项对话框的指定页。

**-i**, **--icon**
> 以托盘图标方式启动。

**-k**, **--kiosk**
> 以 kiosk 模式（瘦客户端）启动。

**-q**, **--quit**
> 退出应用程序。

**-v**, **--version**
> 显示版本。

**--update-profile**
> 以非交互方式修改连接配置（需要 --set-option）。

**--set-option** _OPTION[=VALUE]_
> 设置配置选项，与 --update-profile 一起使用。

# DESCRIPTION

**Remmina** 是一个支持多种协议（包括 RDP、VNC、SSH、SPICE 等）的 GTK 远程桌面客户端。它提供统一的界面来管理远程连接。

# EXAMPLES

```bash
# Launch GUI
remmina

# Connect to RDP
remmina -c rdp://administrator@192.168.1.100

# Connect to VNC
remmina -c vnc://192.168.1.100:5900

# SSH connection
remmina -c ssh://user@server.example.com

# Connect using saved profile
remmina -c ~/.local/share/remmina/myserver.remmina

# Update a profile's username non-interactively
remmina --update-profile ~/.local/share/remmina/myserver.remmina --set-option username=admin
```

# PROTOCOLS

```
RDP    - Windows Remote Desktop
VNC    - Virtual Network Computing
SSH    - Secure Shell
SPICE  - Virtual machine display
NX     - NoMachine protocol
SFTP   - Secure file transfer
```

# CONFIGURATION

**~/.local/share/remmina/**
> 存放已保存连接配置的目录，每个配置为 .remmina 文件，记录服务器地址、协议、凭据和显示设置。

**~/.config/remmina/remmina.pref**
> 全局首选项文件，控制默认行为、键盘快捷键、外观和插件设置。

# CAVEATS

需要相应的协议插件。RDP 支持依赖 FreeRDP。部分功能需要额外的软件包。

# HISTORY

Remmina 由 **Vic Lee** 于 2009 年从 **grdc** 分叉而来，旨在打造一个功能更丰富的远程桌面客户端。

# INSTALL

```apt: sudo apt install remmina```

```dnf: sudo dnf install remmina```

```pacman: sudo pacman -S remmina```

```apk: sudo apk add remmina```

```zypper: sudo zypper install remmina```

```nix: nix profile install nixpkgs#remmina```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xfreerdp](/man/xfreerdp)(1), [vncviewer](/man/vncviewer)(1), [ssh](/man/ssh)(1)
