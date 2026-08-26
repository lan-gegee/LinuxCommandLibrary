# TAGLINE

单用户模式的 root 登录提示符

# TLDR

在默认控制台上**启动** sulogin

```sudo sulogin```

在指定 TTY 设备上**启动** sulogin

```sudo sulogin [/dev/ttyX]```

**设置**输入密码的最大超时时间

```sudo sulogin -t [timeout]```

以登录 Shell 方式**启动** root 的 Shell

```sudo sulogin -p```

**强制**进入 root Shell 而不询问密码

```sudo sulogin -e```

# SYNOPSIS

**sulogin** [_options_] [_tty_device_]

# PARAMETERS

**-t**, **--timeout** _seconds_
> 等待密码的最长时间，超时后继续启动

**-p**, **--login-shell**
> 以登录 Shell 方式启动 Shell

**-e**, **--force**
> 检查默认密码文件，若 root 没有密码则跳过提示

**-h**, **--help**
> 显示帮助信息

**-V**, **--version**
> 显示版本信息

# DESCRIPTION

**sulogin** 由 init 在系统进入单用户模式时调用。它会提示输入 root 密码并启动一个 root Shell，用于系统维护和恢复。

该命令通常在启动过程中进入单用户模式或救援模式时被自动调用。它在常规多用户服务尚未运行时提供对系统的安全访问。

# CAVEATS

需要物理控制台访问权限。**-e** 选项仅应在 root 未设置密码时使用（常见于 initramfs 环境）。属于 util-linux 软件包。

# INSTALL

```apt: sudo apt install util-linux```

```dnf: sudo dnf install util-linux```

```pacman: sudo pacman -S util-linux```

```apk: sudo apk add util-linux-login```

```zypper: sudo zypper install util-linux```

```brew: brew install util-linux```

```nix: nix profile install nixpkgs#util-linux```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[init](/man/init)(1), [login](/man/login)(1), [su](/man/su)(1), [agetty](/man/agetty)(1)
