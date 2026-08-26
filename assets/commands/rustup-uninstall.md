# TAGLINE

移除已安装的 Rust 工具链

# TLDR

**卸载工具链**

```rustup uninstall nightly```

**卸载特定版本**

```rustup uninstall [1.70.0]```

# SYNOPSIS

**rustup** **uninstall** _toolchain_...

# DESCRIPTION

**rustup uninstall** 移除已安装的 Rust 工具链。它是 rustup toolchain uninstall 的别名。可释放未使用工具链占用的磁盘空间。

# INSTALL

```apt: sudo apt install rustup```

```dnf: sudo dnf install rustup```

```pacman: sudo pacman -S rustup```

```zypper: sudo zypper install rustup```

```brew: brew install rustup```

```nix: nix profile install nixpkgs#rustup```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rustup](/man/rustup)(1), [rustup-toolchain](/man/rustup-toolchain)(1), [rustup-install](/man/rustup-install)(1)
