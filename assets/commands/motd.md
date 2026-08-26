# TAGLINE

用户登录时显示的信息

# TLDR

**编辑静态 MOTD**

```sudo nano /etc/motd```

**查看 MOTD**

```cat /etc/motd```

**添加动态 MOTD 脚本**

```sudo nano /etc/update-motd.d/[99-custom]```

**让动态脚本可执行**

```sudo chmod +x /etc/update-motd.d/[99-custom]```

**重新生成动态 MOTD**

```run-parts /etc/update-motd.d/```

# SYNOPSIS

**/etc/motd**

# DESCRIPTION

**motd**（Message of the Day，每日消息）会在用户登录时显示。它可以是静态文本文件，也可以由脚本动态生成。

/etc/motd 的内容由 login(1) 在登录成功后、执行登录 Shell 之前显示。在使用 PAM 的系统上，pam_motd 模块负责显示，并可以展示来自多个位置的内容。动态 MOTD 系统会运行 /etc/update-motd.d/ 中的脚本。

# STATIC MOTD

```
# /etc/motd
Welcome to myserver
Authorized users only
```

# DYNAMIC MOTD

```bash
#!/bin/bash
# /etc/update-motd.d/10-sysinfo
echo "System: $(uname -n)"
echo "Uptime:$(uptime -p)"
echo "Users: $(who | wc -l)"
```

# FILE LOCATIONS

```
/etc/motd              - Static message
/etc/motd.d/           - Static message directory
/run/motd              - Runtime generated message
/run/motd.d/           - Runtime message directory
/usr/lib/motd          - Distribution-provided message
/usr/lib/motd.d/       - Distribution-provided message directory
/etc/update-motd.d/    - Dynamic scripts (Ubuntu/Debian)
/run/motd.dynamic      - Generated output (Ubuntu/Debian)
```

# CAVEATS

在 Ubuntu/Debian 上，动态 MOTD 需要 update-motd 软件包。脚本必须可执行。SSH 可能通过 sshd_config 中的 Banner 指令配置了单独的横幅。PAM 配置会影响显示。每个消息文件的大小限制为 64KB。

# INSTALL

```aur: yay -S motd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[login](/man/login)(1), [sshd](/man/sshd)(8), [pam_motd](/man/pam_motd)(8), [wall](/man/wall)(1)
