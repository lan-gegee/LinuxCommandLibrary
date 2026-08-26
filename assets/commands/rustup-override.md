# TAGLINE

设置目录级别的 Rust 工具链覆盖

# TLDR

**设置目录级覆盖**

```rustup override set nightly```

**移除目录级覆盖**

```rustup override unset```

**列出所有覆盖**

```rustup override list```

# SYNOPSIS

**rustup** **override** _command_ [_options_]

# PARAMETERS

**set** _toolchain_
> 为当前目录设置覆盖。

**unset**
> 移除当前目录的覆盖。

**list**
> 显示所有覆盖。

**--path** _path_
> 针对特定目录操作。

# DESCRIPTION

**rustup override** 管理目录级别的工具链覆盖。覆盖配置优先于默认工具链。对于需要特定 Rust 版本的项目很有用。

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
