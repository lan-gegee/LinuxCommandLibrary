# TAGLINE

显示 gcrane 命令的帮助信息

# TLDR

**显示 gcrane 的常规帮助**

```gcrane help```

**显示特定子命令的帮助**

```gcrane help [copy]```

**显示 gc 子命令的帮助**

```gcrane help [gc]```

**使用 --help 标志显示帮助**

```gcrane --help```

# SYNOPSIS

**gcrane** **help** [_command_]

# DESCRIPTION

**gcrane help** 显示 gcrane 及其子命令的帮助信息。不带参数时，它会列出所有可用命令的概览及简要说明。给定具体命令名时，它会显示详细的用法信息，包括所有标志和参数。

帮助系统记录了 gcrane 在标准 crane 功能之外针对 GCR 的扩展功能，包括递归复制操作和垃圾回收命令。

# INSTALL

```zypper: sudo zypper install gcrane```

```nix: nix profile install nixpkgs#gcrane```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gcrane](/man/gcrane)(1), [gcrane-copy](/man/gcrane-copy)(1), [gcrane-gc](/man/gcrane-gc)(1), [crane](/man/crane)(1)
