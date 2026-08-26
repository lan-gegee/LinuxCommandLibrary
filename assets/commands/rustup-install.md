# TAGLINE

安装 Rust 工具链

# TLDR

**安装** stable 工具链

```rustup install stable```

**安装** nightly 工具链

```rustup install nightly```

**安装固定版本**

```rustup install 1.78.0```

**安装特定日期的 nightly**

```rustup install nightly-2025-01-15```

**以 minimal profile 安装**（仅 rustc、rust-std、cargo）

```rustup install stable --profile minimal```

**安装并添加组件**

```rustup install nightly --component rust-src --component rust-analyzer```

**安装时不检查自身更新**

```rustup install stable --no-self-update```

# SYNOPSIS

**rustup** **install** [_options_] _toolchain_...

# DESCRIPTION

**rustup install** 下载并安装一个或多个 Rust 工具链。它是 **rustup toolchain install** 的别名。

工具链由渠道（**stable**、**beta**、**nightly**）、确切版本号（**1.78.0**）标识，还可选带日期（**nightly-2025-01-15**）和主机三元组（**stable-x86_64-unknown-linux-gnu**）。如果该工具链已安装，则会被更新到该渠道的最新发布版本。

# PARAMETERS

**--profile** _NAME_
> 安装 profile：**minimal**、**default** 或 **complete**。控制安装哪些组件。

**-c**, **--component** _NAME_
> 为工具链添加组件（例如 `rust-src`、`rust-analyzer`、`llvm-tools`、`miri`）。可重复使用。

**-t**, **--target** _TRIPLE_
> 添加交叉编译目标。可重复使用。

**--no-self-update**
> 安装工具链时不更新 rustup 自身。

**--force**
> 即使工具链看似最新也重新安装；对 nightly 而言，即使缺少部分请求的组件也照样安装。

**--force-non-host**
> 允许安装主机三元组与当前机器不匹配的工具链（rustup 1.28 引入）。

**--allow-downgrade**
> 若最新的 nightly 缺少所需组件，允许选择较旧的 nightly。

**-h**, **--help**
> 打印帮助信息。

# CAVEATS

默认情况下，每次安装工具链时 rustup 都会检查并应用自身的更新；在 CI 环境中可用 **--no-self-update** 禁用。安装时请求的组件和目标必须在该渠道/日期下可用，否则安装失败；使用 **--force** 时 rustup 仍会安装该工具链，只是跳过缺失的组件。

# HISTORY

**rustup** 是官方的 Rust 工具链安装器，由 **Brian Anderson** 创建，现由 **Rust 项目**维护。自 rustup 首次发布以来，**rustup install** 一直是添加新工具链的标准方式。

# INSTALL

```apt: sudo apt install rustup```

```dnf: sudo dnf install rustup```

```pacman: sudo pacman -S rustup```

```zypper: sudo zypper install rustup```

```brew: brew install rustup```

```nix: nix profile install nixpkgs#rustup```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rustup](/man/rustup)(1), [rustup-toolchain](/man/rustup-toolchain)(1), [rustup-uninstall](/man/rustup-uninstall)(1)
