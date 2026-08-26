# TAGLINE

控制 NumLock 的状态

# TLDR

报告 Num Lock 是**开启还是关闭**

```numlockx status```

**开启** Num Lock

```numlockx on```

**关闭** Num Lock

```numlockx off```

**切换**当前 Num Lock 状态

```numlockx toggle```

# SYNOPSIS

**numlockx** [_on_|_off_|_toggle_|_status_]

# PARAMETERS

**on**
> 开启 Num Lock

**off**
> 关闭 Num Lock

**toggle**
> 切换当前 Num Lock 状态

**status**
> 显示当前 Num Lock 状态

# DESCRIPTION

**numlockx** 是一个在 X11 会话脚本中控制 NumLock 键状态的程序。它常用于登录脚本或桌面启动文件中，确保会话开始时 Num Lock 处于期望的状态。

该命令直接通过 X11 操作键盘 LED 和状态，因此在 BIOS 的 Num Lock 设置无法保持的系统上，或对登录时希望特定 Num Lock 状态的用户来说很有用。

不带参数时，numlockx 会开启 Num Lock（相当于 **numlockx on**）。

# CAVEATS

仅在 X11 会话中有效；在 Wayland 或虚拟控制台中不起作用。某些桌面环境可能在登录期间重置其状态。控制台下的 Num Lock 控制请改用 **setleds**。

# INSTALL

```apt: sudo apt install numlockx```

```dnf: sudo dnf install numlockx```

```pacman: sudo pacman -S numlockx```

```zypper: sudo zypper install numlockx```

```nix: nix profile install nixpkgs#numlockx```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[setleds](/man/setleds)(1), [xset](/man/xset)(1), [xmodmap](/man/xmodmap)(1)
