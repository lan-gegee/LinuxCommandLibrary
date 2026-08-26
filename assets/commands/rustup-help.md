# TAGLINE

显示 rustup 命令的帮助

# TLDR

**显示顶层帮助**

```rustup help```

查看**特定子命令**的帮助

```rustup help [command]```

查看**嵌套子命令**的帮助

```rustup help [toolchain] [install]```

查看 override **子命令**的帮助

```rustup help override```

# SYNOPSIS

**rustup** **help** [_subcommand_...]

# PARAMETERS

_subcommand_
> 要深入查看的一个或多个子命令名称。不带参数时，rustup 打印其顶层帮助。

# DESCRIPTION

**rustup help** 打印 **rustup** 及其任意子命令的用法、选项和子命令列表。它等价于运行命令时加上 **--help**，但接受以位置参数（而非标志）形式传入的嵌套子命令名称。

# INSTALL

```apt: sudo apt install rustup```

```dnf: sudo dnf install rustup```

```pacman: sudo pacman -S rustup```

```zypper: sudo zypper install rustup```

```brew: brew install rustup```

```nix: nix profile install nixpkgs#rustup```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rustup](/man/rustup)(1)
