# TAGLINE

基于 Ncurses 的 QEMU 虚拟机管理 TUI

# TLDR

**启动虚拟机管理器**

```nemu```

# SYNOPSIS

**nemu** [_options_]

# DESCRIPTION

**nemu** 是一款基于 ncurses 的 TUI 工具，可在终端中管理 QEMU 虚拟机。它提供虚拟机创建、配置、状态监视、CPU 用量跟踪以及通过 VNC 或 SPICE 连接等功能，完全无需图形桌面环境。

特性包括支持 qcow2 和 raw 磁盘镜像格式、可配置的刷新超时，以及在支持的终端中使用 Kitty 图形协议预览虚拟机画面。

# CAVEATS

需要安装 QEMU。虚拟机画面预览等部分功能需要支持 Kitty 图形协议的终端。

# HISTORY

**nemu** 由 **nemuTUI** 项目开发，使用 **C** 语言编写。

# INSTALL

```apk: sudo apk add nemu```

```brew: brew install nemu```

```nix: nix profile install nixpkgs#nemu```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[qemu](/man/qemu)(1), [virsh](/man/virsh)(1), [virt-manager](/man/virt-manager)(1)
