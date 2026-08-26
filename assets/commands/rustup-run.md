# TAGLINE

使用特定的 Rust 工具链运行命令

# TLDR

**以指定工具链运行命令**

```rustup run stable cargo build```

**以 nightly 运行**

```rustup run nightly rustc --version```

**运行特定版本**

```rustup run [1.70.0] cargo test```

# SYNOPSIS

**rustup** **run** _toolchain_ _command_ [_args_...]

# PARAMETERS

**--install**
> 若工具链缺失则先安装。

# DESCRIPTION

**rustup run** 使用指定的 Rust 工具链执行命令。它会临时使用指定工具链，而不受默认工具链或覆盖配置的影响。

# INSTALL

```apt: sudo apt install rustup```

```dnf: sudo dnf install rustup```

```pacman: sudo pacman -S rustup```

```zypper: sudo zypper install rustup```

```brew: brew install rustup```

```nix: nix profile install nixpkgs#rustup```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rustup](/man/rustup)(1), [rustup-override](/man/rustup-override)(1)
