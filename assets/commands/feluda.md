# TAGLINE

Rust 依赖许可证使用检测工具

# TLDR

检查当前项目的依赖

```feluda```

**检查**指定的清单文件

```feluda [path/to/Cargo.toml]```

以 JSON 格式**输出**

```feluda --json```

# SYNOPSIS

**feluda** [_options_] [_manifest_]

# PARAMETERS

**--json**
> 以 JSON 格式输出结果

**--include-dev**
> 包含开发依赖

**--include-build**
> 包含构建依赖

**-h, --help**
> 显示帮助并退出

**-V, --version**
> 显示版本并退出

# DESCRIPTION

**feluda** 是一款 Rust 工具，用于分析项目依赖并检测其许可证。它帮助开发者了解 Rust 项目的许可证构成，并识别潜在的合规问题。

该工具读取 Cargo.toml 和 Cargo.lock 文件，从 crate 元数据中识别所有依赖及其对应的许可证。

# OUTPUT

显示包含以下内容的表格：
- Crate 名称
- 版本
- 许可证标识符
- 许可证文件路径

# CAVEATS

依赖于 crate 中准确的许可证元数据。许可证检测可能遗漏自定义或不常见的许可证。多选许可证（OR）会分别显示。需要存在 Cargo.toml 和 Cargo.lock。

# HISTORY

**feluda** 的创建旨在帮助 Rust 开发者对项目进行许可证审计，确保符合开源许可要求。

# INSTALL

```brew: brew install feluda```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cargo-license](https://github.com/onur/cargo-license), [cargo-deny](https://github.com/EmbarkStudios/cargo-deny), [cargo-tree](https://doc.rust-lang.org/cargo/commands/cargo-tree.html)
