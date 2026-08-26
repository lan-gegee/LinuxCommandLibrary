# TAGLINE

显示已安装的 Rust 工具链和活动版本

# TLDR

**显示已安装的工具链**

```rustup show```

**显示活动的工具链**

```rustup show active-toolchain```

**显示主目录**

```rustup show home```

**显示安装 profile**

```rustup show profile```

# SYNOPSIS

**rustup** **show** [_command_]

# PARAMETERS

**active-toolchain**
> 当前活动的工具链。

**home**
> Rustup 主目录。

**profile**
> 默认安装 profile。

# DESCRIPTION

**rustup show** 显示 rustup 安装信息，包括已安装的工具链、活动工具链和已配置的设置。默认命令会显示全面的概览。

# INSTALL

```apt: sudo apt install rustup```

```dnf: sudo dnf install rustup```

```pacman: sudo pacman -S rustup```

```zypper: sudo zypper install rustup```

```brew: brew install rustup```

```nix: nix profile install nixpkgs#rustup```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rustup](/man/rustup)(1), [rustup-default](/man/rustup-default)(1)
