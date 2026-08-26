# TAGLINE

rustup 的引导安装脚本

# TLDR

**安装 rustup**

```curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh```

**免交互安装**

```curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y```

**安装 nightly 工具链**

```curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- --default-toolchain nightly```

**以 minimal profile 安装且不修改 PATH**

```curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y --profile minimal --no-modify-path```

**安装并添加交叉编译目标**

```curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- --target wasm32-unknown-unknown```

**安装并添加额外组件**

```curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- --component rustfmt clippy```

# SYNOPSIS

**rustup-init.sh** [_options_]

# PARAMETERS

**-y**
> 接受默认值，不进行提示。

**-q**, **--quiet**
> 禁用进度输出。

**-v**, **--verbose**
> 启用详细输出。

**--default-toolchain** _name_
> 安装特定工具链（stable、beta、nightly 或诸如 1.78.0 的版本）。

**--default-host** _triple_
> 设置默认主机三元组（例如 x86_64-unknown-linux-gnu）。

**--no-modify-path**
> 不修改 PATH 环境变量。

**--profile** _name_
> 安装 profile：minimal（rustc、cargo）、default（额外包含 rustfmt、clippy）或 complete（所有组件）。

**--component** _name_
> 添加特定组件（例如 rust-docs、rustfmt、clippy）。可多次指定。

**--target** _triple_
> 添加交叉编译目标（例如 wasm32-unknown-unknown）。可多次指定。

# DESCRIPTION

**rustup-init.sh** 是 Rust 工具链的安装脚本。它下载并运行 rustup-init 来安装 rustup 和 Rust 工具链。这是在 Unix 系统上安装 Rust 的官方方法。

选项也可以通过带有 RUSTUP_INIT_ 前缀的环境变量设置（例如 RUSTUP_INIT_DEFAULT_TOOLCHAIN=nightly）。

# INSTALL

```apt: sudo apt install rustup```

```dnf: sudo dnf install rustup```

```pacman: sudo pacman -S rustup```

```zypper: sudo zypper install rustup```

```brew: brew install rustup```

```nix: nix profile install nixpkgs#rustup```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rustup](/man/rustup)(1), [cargo](/man/cargo)(1), [rustc](/man/rustc)(1)
