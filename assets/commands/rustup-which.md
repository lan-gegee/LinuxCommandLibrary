# TAGLINE

显示 Rust 工具链二进制文件的路径

# TLDR

**查找 cargo 的路径**

```rustup which cargo```

**查找 rustc 的路径**

```rustup which rustc```

**在特定工具链中查找工具**

```rustup which --toolchain nightly rustfmt```

# SYNOPSIS

**rustup** **which** [_options_] _command_

# PARAMETERS

**--toolchain** _name_
> 在指定的工具链中查找。

# DESCRIPTION

**rustup which** 显示 Rust 工具的路径。它会展示对于给定命令实际会执行哪个二进制文件。对排查工具链问题很有用。

# INSTALL

```apt: sudo apt install rustup```

```dnf: sudo dnf install rustup```

```pacman: sudo pacman -S rustup```

```zypper: sudo zypper install rustup```

```brew: brew install rustup```

```nix: nix profile install nixpkgs#rustup```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rustup](/man/rustup)(1), [which](/man/which)(1)
