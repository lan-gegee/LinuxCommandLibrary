# TAGLINE

切换前台虚拟终端

# TLDR

将控制台切换到 **TTY 编号 N**（需要 root）

```sudo chvt [N]```

# SYNOPSIS

**chvt** _N_

# DESCRIPTION

**chvt** 将前台虚拟终端切换为终端 N。虚拟终端（VT）是大多数 Linux 系统上通过 Ctrl+Alt+F1 至 F7 访问的文本控制台。

这等同于按下 Ctrl+Alt+FN，但可以通过程序调用完成，或在键盘快捷键不可用时使用。

# PARAMETERS

_N_
> 要切换到的虚拟终端编号（通常为 1-7）

# CAVEATS

需要 root 权限。目标 VT 必须存在。在带图形桌面的系统上，VT7 或 VT1 通常是 X/Wayland 会话。可用的 VT 取决于系统配置。

# INSTALL

```apt: sudo apt install kbd```

```dnf: sudo dnf install kbd```

```pacman: sudo pacman -S kbd```

```apk: sudo apk add kbd```

```zypper: sudo zypper install kbd```

```nix: nix profile install nixpkgs#kbd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fgconsole](/man/fgconsole)(1), [deallocvt](/man/deallocvt)(1)
