# TAGLINE

管理 Rust 交叉编译目标

# TLDR

**列出目标**

```rustup target list```

**添加目标**

```rustup target add [wasm32-unknown-unknown]```

**添加 ARM 目标**

```rustup target add aarch64-unknown-linux-gnu```

**移除目标**

```rustup target remove [target]```

# SYNOPSIS

**rustup** **target** _command_ [_options_]

# PARAMETERS

**list**
> 列出可用目标。

**add** _target_
> 安装目标。

**remove** _target_
> 卸载目标。

**--toolchain** _name_
> 针对特定工具链操作。

# DESCRIPTION

**rustup target** 管理交叉编译目标。添加目标后，可以从当前系统为不同平台（ARM、WebAssembly、Windows 等）进行编译。

# INSTALL

```apt: sudo apt install rustup```

```dnf: sudo dnf install rustup```

```pacman: sudo pacman -S rustup```

```zypper: sudo zypper install rustup```

```brew: brew install rustup```

```nix: nix profile install nixpkgs#rustup```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rustup](/man/rustup)(1), [rustup-toolchain](/man/rustup-toolchain)(1)
