# TAGLINE

检查当前内核是否已启用 LXC 所需的特性

# TLDR

检查**当前内核**的支持情况

```lxc-checkconfig```

检查**特定内核**配置

```CONFIG=/path/to/config lxc-checkconfig```

# SYNOPSIS

**lxc-checkconfig**

# DESCRIPTION

**lxc-checkconfig** 检查当前内核是否已启用支持 LXC 容器所需的特性。它会检查命名空间、cgroups 以及其他内核能力。

# CHECKS PERFORMED

**Namespaces**: User, PID, UTS, IPC, Network
**Cgroups**: v1/v2, controllers
**Misc**: Seccomp, checkpoint/restore

# CAVEATS

设置 CONFIG 环境变量可检查其他内核配置文件。有助于诊断容器在系统上无法运行的原因。

# INSTALL

```apt: sudo apt install lxc```

```dnf: sudo dnf install lxc```

```pacman: sudo pacman -S lxc```

```apk: sudo apk add lxc```

```zypper: sudo zypper install lxc```

```brew: brew install lxc```

```nix: nix profile install nixpkgs#lxc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lxc-create](/man/lxc-create)(1), [lxc-start](/man/lxc-start)(1)
