# TAGLINE

更新已安装的 Rust 工具链

# TLDR

**更新所有工具链**

```rustup update```

**更新特定工具链**

```rustup update stable```

**更新 nightly**

```rustup update nightly```

# SYNOPSIS

**rustup** **update** [_toolchain_...]

# PARAMETERS

**--no-self-update**
> 不更新 rustup 自身。

**--force**
> 强制重新安装。

**--force-non-host**
> 强制更新非本机主机的工具链。

# DESCRIPTION

**rustup update** 将已安装的 Rust 工具链更新到最新版本。不带参数时会更新所有已安装的工具链。默认情况下也会更新 rustup 自身。

# INSTALL

```apt: sudo apt install rustup```

```dnf: sudo dnf install rustup```

```pacman: sudo pacman -S rustup```

```zypper: sudo zypper install rustup```

```brew: brew install rustup```

```nix: nix profile install nixpkgs#rustup```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rustup](/man/rustup)(1), [rustup-check](/man/rustup-check)(1)
