# TAGLINE

查找并管理最低支持的 Rust 版本

# TLDR

**查找最低支持的 Rust 版本**

```cargo msrv find```

**使用线性搜索查找**

```cargo msrv find --linear```

**验证当前 MSRV 可用**

```cargo msrv verify```

**显示已声明的 MSRV**

```cargo msrv show```

**在 Cargo.toml 中设置 MSRV**

```cargo msrv set [1.56.0]```

**列出各依赖的 MSRV**

```cargo msrv list```

**为指定路径查找**

```cargo msrv --path [/path/to/project] find```

# SYNOPSIS

**cargo msrv** [_options_] _command_

# DESCRIPTION

**cargo msrv** 为 Rust 项目查找并管理最低支持的 Rust 版本（MSRV）。它通过在可用工具链上逐一测试，确定能够成功构建 crate 的最老 Rust 编译器版本。默认采用二分搜索来高效缩小兼容版本范围。

对于希望支持较旧 Rust 版本用户的库作者而言，维护准确的 MSRV 非常重要。该工具可在找到最小版本后自动设置 Cargo.toml 中的 `rust-version` 字段，并随着代码库演进而验证已声明的 MSRV 是否仍然有效。

# COMMANDS

**find**
> 通过测试各版本来发现 MSRV

**verify**
> 检查项目能否用已声明的 MSRV 构建

**show**
> 显示 Cargo.toml 中的 MSRV

**set** _version_
> 更新 Cargo.toml 中的 rust-version

**list**
> 显示各依赖的 MSRV

# PARAMETERS

**--path** _dir_
> 项目目录路径

**--linear**
> 使用线性搜索而非二分搜索

**--min** _version_
> 要考虑的最小版本

**--max** _version_
> 要考虑的最大版本

**--target** _triple_
> 目标平台

**--manifest-path** _path_
> Cargo.toml 的路径

**--write-msrv**
> find 结束后将找到的 MSRV 写入 Cargo.toml

**--ignore-lockfile**
> 确定 MSRV 时忽略锁文件

# REQUIREMENTS

工具链管理需要 rustup。

# CAVEATS

面对众多的 Rust 小版本，二分搜索比线性搜索快得多。下载和管理工具链需要 rustup。`find` 命令会用每个候选版本编译项目，大型项目可能较慢。自 Rust 1.56 起，Cargo.toml 中的 `rust-version` 字段只支持两段式版本号（如 1.56）。

# INSTALL

```pacman: sudo pacman -S cargo-msrv```

```brew: brew install cargo-msrv```

```nix: nix profile install nixpkgs#cargo-msrv```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cargo](/man/cargo)(1), [rustup](/man/rustup)(1)
