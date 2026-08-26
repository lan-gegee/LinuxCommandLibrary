# TAGLINE

锁定所有虚拟控制台，防止对系统的未授权访问

# TLDR

**锁定**所有控制台

```physlock```

锁定并**静音**内核消息

```physlock -m```

锁定并**禁用 SysRq**

```physlock -s```

使用**自定义消息**锁定

```physlock -p "[Locked!]"```

锁定并**脱离**（用于挂起脚本）

```physlock -d```

# SYNOPSIS

**physlock** [**-d**] [**-m**] [**-s**] [**-p** _message_] [**-l**]

# PARAMETERS

**-d**
> 分支并脱离（守护进程化）

**-m**
> 锁定期间静音内核消息

**-s**
> 锁定期间禁用 SysRq 键

**-p _message_**
> 在密码提示前显示消息

**-l**
> 只锁定当前 tty

# DESCRIPTION

**physlock** 锁定所有虚拟控制台，防止对系统的未授权访问。与只保护图形会话的屏幕锁不同，physlock 保护所有 TTY，阻止通过 Ctrl+Alt+F1-F6 切换进行的访问。

解锁需要通过当前用户或 root 的身份验证。这使它适合保护存在物理接触风险（kiosk）的系统，尤其是服务器或自助终端。

# CAVEATS

不锁定图形显示；在 X11/Wayland 会话中需配合屏幕锁使用（如 i3lock、slock）。身份验证需要 PAM。脱离模式（**-d**）适用于挂起/休眠脚本（如 systemd 睡眠钩子）。禁用 SysRq 仅在内核启用 CONFIG_MAGIC_SYSRQ 时有效。必须以 root 或具有相应权限的身份运行。

# HISTORY

**physlock** 由 **Bert Muennich** 创建，作为 vlock 的轻量级替代品。它专注于以最少的依赖保护物理控制台访问，适合嵌入式和精简系统。

# INSTALL

```apt: sudo apt install physlock```

```apk: sudo apk add physlock```

```zypper: sudo zypper install physlock```

```nix: nix profile install nixpkgs#physlock```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[vlock](/man/vlock)(1), [xlock](/man/xlock)(1), [loginctl](/man/loginctl)(1)
