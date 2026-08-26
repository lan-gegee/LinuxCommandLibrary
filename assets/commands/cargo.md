# TAGLINE

Rust 软件包管理器和构建系统

# TLDR

**构建**项目

```cargo build```

**运行**项目

```cargo run```

**测试**项目

```cargo test```

**创建**新项目

```cargo new [project-name]```

**添加**依赖

```cargo add [dependency]```

**更新**依赖

```cargo update```

# SYNOPSIS

**cargo** _command_ [_options_]

# DESCRIPTION

**cargo** 是 Rust 的软件包管理器和构建系统。它负责依赖管理、编译软件包、运行测试、生成文档，以及向 crates.io 发布 crate。

该工具是 Rust 开发必不可少的组成部分，随 Rust 一同捆绑提供。

# PARAMETERS

**new** _name_
> 创建新项目

**build** [**--release**]
> 编译项目

**run**
> 构建并运行

**test**
> 运行测试

**check**
> 检查可编译性而不实际构建

**add** _crate_
> 添加依赖

**install** _crate_
> 安装二进制 crate

**publish**
> 发布到 crates.io

**doc** [**--open**]
> 构建文档

**clean**
> 删除构建产物

**update**
> 更新依赖

**bench**
> 运行基准测试（nightly 或由测试框架提供）。

**fmt**
> 通过 `rustfmt`（组件）格式化代码。

**clippy**
> 运行 Clippy 代码检查器（组件）。

# FEATURES

- 依赖解析
- 构建管理
- 测试运行器
- 文档生成器
- 基准测试
- 发布到 crates.io
- 工作区支持
- 自定义构建脚本

# PROJECT STRUCTURE

```
my_project/
├── Cargo.toml      # Project manifest
├── Cargo.lock      # Dependency lock file
└── src/
    └── main.rs     # Source code
```

# CARGO.TOML

```toml
[package]
name = "myproject"
version = "0.1.0"
edition = "2021"

[dependencies]
serde = "1.0"
tokio = { version = "1.0", features = ["full"] }
```

# WORKFLOW

```bash
# Create new binary project
cargo new myapp

# Create library
cargo new --lib mylib

# Build debug version
cargo build

# Build optimized release
cargo build --release

# Run project
cargo run

# Run tests
cargo test

# Check without building
cargo check

# Generate and open docs
cargo doc --open
```

# CAVEATS

首次构建需要下载依赖（较慢）。发布版构建明显慢于调试版。二进制项目应提交 Cargo.lock（库项目则不必）。大型项目编译耗时长。target 目录可能变得很大。

# HISTORY

**Cargo** 自 **2013** 年前后起与 Rust 同步开发，逐渐成为 Rust 生态的标准构建工具和软件包管理器。

# INSTALL

```apt: sudo apt install cargo```

```dnf: sudo dnf install cargo```

```apk: sudo apk add cargo```

```zypper: sudo zypper install cargo```

```nix: nix profile install nixpkgs#cargo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rustc](/man/rustc)(1), [rustup](/man/rustup)(1), [cargo-fmt](/man/cargo-fmt)(1), [cargo-clippy](/man/cargo-clippy)(1), [cargo-bench](/man/cargo-bench)(1)
