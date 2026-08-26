# TAGLINE

终端中的像素级精确 VNC 客户端（Kitty 图形协议）

# TLDR

**按主机名和显示编号连接**到 VNC 显示

```desktui [desk:1]```

**用主机名和原始端口连接**

```desktui [10.0.0.5::5900]```

**连接**并将桌面缩放到适合终端

```desktui [10.0.0.5::5900] --scale fit```

**只读模式会话**（不向远程发送输入）

```desktui [desk:1] --view-only```

**使用密码文件**

```desktui [desk:1] --password-file [~/.vnc/passwd.txt]```

**打印终端的图形能力**

```desktui --print-caps```

**不连接 VNC 服务器，绘制测试图案**

```desktui --test-pattern```

**经 SSH 隧道连接**并用环境变量提供密码

```VNC_PASSWORD=[secret] desktui [localhost::5901]```

# SYNOPSIS

**desktui** [_options_] [_target_]

# PARAMETERS

_target_

> 常见客户端格式的 VNC 地址：**host**、**host:display**、**host::port**、IPv6，或 **desk:1** 这类显示风格的名称。

**--scale** _MODE_

> 桌面适配模式：**native**（请求服务器把桌面调整为终端大小；支持时为默认）、**fit**、**integer** 或 **1:1**。可在运行中通过本地前缀键加 **m** 切换。

**--view-only**

> 不向远程发送键盘或指针输入（用前缀键加 **v** 切换）。

**--no-clipboard**

> 禁用双向剪贴板同步（默认开启）。

**--password-file** _FILE_

> 从 _FILE_ 读取 VNC 密码而不是交互式询问。

**--quality** _N_

> 请求 Tight 质量等级（启用 JPEG）。未设置时在服务器允许的情况下保持无损。

**--compression** _N_

> 提供给服务器的压缩提示。

**--fps** _N_

> 限制帧率（默认目标是在链路允许时达到无损约 60 fps）。

**--prefix** _KEY_

> 本地命令前缀键（默认 **Ctrl+A**）。与 tmux 或其他多路复用器冲突时使用。

**--print-caps**

> 探测并打印终端的图形与输入能力，然后退出。

**--test-pattern**

> 不连接服务器，直接测试像素管线。

**--log-file** _FILE_

> 将诊断信息写入 _FILE_（图形会话期间 stdout 不能用于日志）。

# DESCRIPTION

**desktui** 是一个终端 VNC (RFB) 客户端，通过 **Kitty 图形协议**将远程桌面渲染成真正的像素——每个终端像素对应一个远程像素，而非半块字符拼成的 ASCII 图画。它面向实现了 Kitty 图形协议的终端（尤其是 **Ghostty**、**kitty** 和 **WezTerm**）。启动时会探测终端能力，如果图像图形不可用则拒绝启动并给出明确的错误提示。

连接时 desktui 优先采用 **native** 缩放：它发送 **SetDesktopSize**，让远程桌面与终端的可用像素区域完全一致，不做任何重采样。拒绝该请求的服务器（**x11vnc** 上很常见）则回退到 **fit**、**integer** 或带平移的 **1:1** 模式。输入会透传到远程；本地命令隐藏在前缀键之后（默认 **Ctrl+A**）：退出、刷新、重新缩放、平移、只读模式以及统计信息。

认证支持无认证和经典 VNC 密码（TigerVNC、x11vnc、TightVNC、QEMU、Kasm）。密码来自 **--password-file**、**$VNC_PASSWORD**，或在服务器询问时交互输入。不支持 Apple Remote Desktop 认证、RealVNC 私有认证以及仅限 VeNCrypt/TLS 的服务器。对于不可信网络请使用 SSH 隧道：VNC 密码认证及其后的会话并不是现代意义上的 TLS。

# CAVEATS

需要支持 Kitty 图形协议的终端；没有图像支持的普通终端无法运行 desktui。共享内存帧传输（**t=s**）在本机终端上快得多；通过 SSH 时需要付出 zlib+base64 的开销，全屏运动帧率受限于压缩路径（项目实测约 48 fps）。macOS 屏幕共享和 RealVNC 私有方案会以明确的消息报错失败。任何非本地的 VNC 端点都建议走 SSH 隧道。

# SEE ALSO

[vncviewer](/man/vncviewer)(1), [tigervnc](/man/tigervnc)(1), [x11vnc](/man/x11vnc)(1), [vncserver](/man/vncserver)(1), [kitty](/man/kitty)(1), [ghostty](/man/ghostty)(1), [wezterm](/man/wezterm)(1)

# RESOURCES

```[Source code](https://github.com/mishushakov/desktui)```

<!-- verified: 2026-07-26 -->
