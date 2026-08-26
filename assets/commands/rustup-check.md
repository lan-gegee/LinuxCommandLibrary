# TAGLINE

检查 Rust 工具链更新

# TLDR

**检查**已安装工具链和 rustup 自身的可用更新

```rustup check```

# SYNOPSIS

**rustup** **check**

# DESCRIPTION

**rustup check** 查询官方 Rust 仓库，显示 rustup 管理的所有 Rust 工具链的已安装版本与可用版本对比。它会展示每个已安装工具链（stable、beta、nightly）以及 rustup 自身是否有可用更新，但不会下载或安装任何东西。这使它非常适合快速判断是否需要执行 **rustup update**。

该命令需要联网才能检查最新版本。

# INSTALL

```apt: sudo apt install rustup```

```dnf: sudo dnf install rustup```

```pacman: sudo pacman -S rustup```

```zypper: sudo zypper install rustup```

```brew: brew install rustup```

```nix: nix profile install nixpkgs#rustup```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rustup](/man/rustup)(1), [rustup-update](/man/rustup-update)(1), [rustup-show](/man/rustup-show)(1), [rustup-toolchain](/man/rustup-toolchain)(1), [rustc](/man/rustc)(1), [cargo](/man/cargo)(1)
