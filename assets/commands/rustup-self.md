# TAGLINE

管理 rustup 自身的安装

# TLDR

**升级** rustup 二进制文件本身

```rustup self update```

**移除** rustup 及其安装的工具链

```rustup self uninstall```

# SYNOPSIS

**rustup** **self** _command_

# PARAMETERS

**update**
> 更新 rustup 自身。

**uninstall**
> 移除 rustup 和所有工具链。

**upgrade-data**
> 升级内部数据。

# DESCRIPTION

**rustup self** 管理 rustup 的自身安装。可将 rustup 更新到最新版本，或彻底卸载 Rust 和 rustup。

# INSTALL

```apt: sudo apt install rustup```

```dnf: sudo dnf install rustup```

```pacman: sudo pacman -S rustup```

```zypper: sudo zypper install rustup```

```brew: brew install rustup```

```nix: nix profile install nixpkgs#rustup```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rustup](/man/rustup)(1), [rustup-update](/man/rustup-update)(1)
