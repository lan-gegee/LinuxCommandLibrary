# TAGLINE

自动格式化 Rust 源代码

# TLDR

**格式化 Rust 文件**

```rustfmt [main.rs]```

**格式化多个文件**

```rustfmt [src/*.rs]```

**检查格式**而不修改文件

```rustfmt --check [main.rs]```

**备份并格式化**

```rustfmt --backup [main.rs]```

**使用指定 edition 格式化**

```rustfmt --edition [2021] [main.rs]```

**从 stdin 格式化**

```cat [main.rs] | rustfmt```

**显示**格式化更改的 diff

```rustfmt --emit diff [main.rs]```

**使用配置文件**

```rustfmt --config-path [rustfmt.toml] [main.rs]```

# SYNOPSIS

**rustfmt** [_options_] [_files_...]

# DESCRIPTION

**rustfmt** 是官方的 Rust 代码格式化工具。它根据风格规范自动格式化 Rust 代码，确保整个项目的代码风格一致。

该工具可以集成到编辑器、CI 流水线和 pre-commit 钩子中。配置存储在项目根目录的 rustfmt.toml 或 .rustfmt.toml 中。

与 Cargo 配合使用时（`cargo fmt`），它会自动格式化项目中的所有文件。rustfmt 支持所有稳定的 Rust 语法，并可针对各种风格偏好进行配置。

# PARAMETERS

**--check**
> 检查格式是否正确，不修改文件。

**--backup**
> 为原始文件创建备份。

**--edition** _year_
> Rust 版本（2015、2018、2021、2024）。

**--emit** _type_
> 输出模式（files、stdout、diff）。

**--config** _key=value_
> 设置配置选项。

**--config-path** _file_
> 配置文件的路径。

**--print-config** _type_
> 打印配置（default、current、minimal）。

**--files-with-diff**
> 打印将会发生变化的文件。

**--verbose**
> 打印详细输出。

**--quiet**
> 打印最少输出。

**--color** _when_
> 彩色输出（auto、always、never）。

# CONFIGURATION

**rustfmt.toml** / **.rustfmt.toml**
> 位于项目根目录的项目级配置文件，定义诸如 max_width、tab_spaces、edition 和 use_small_heuristics 等格式化规则。

**max_width**
> 换行前的最大行宽（默认 100）。

**tab_spaces**
> 每个缩进级别的空格数（默认 4）。

**edition**
> 解析时使用的 Rust 版本（2015、2018、2021、2024）。

# CAVEATS

部分配置不稳定，需要 nightly 工具链。无法格式化会产生不可解析输出的宏。注释可能被移动位置。配置变更可能造成大范围 diff。

# HISTORY

**rustfmt** 由 **Nick Cameron** 自 **2015 年**开始开发，旨在为 Rust 代码提供官方格式化方案。它于 **2018 年**随 Rust 1.24 一同达到 1.0。该工具受 gofmt 影响，希望通过提供单一的规范格式来终结风格之争。目前由 Rust 风格团队维护。

# INSTALL

```apt: sudo apt install rustup```

```dnf: sudo dnf install rustup```

```pacman: sudo pacman -S rustup```

```apk: sudo apk add rustfmt```

```zypper: sudo zypper install rustup```

```brew: brew install rustup```

```nix: nix profile install nixpkgs#rustup```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cargo-fmt](/man/cargo-fmt)(1), [cargo](/man/cargo)(1), [rustc](/man/rustc)(1), [clippy](/man/clippy)(1)
