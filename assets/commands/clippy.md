# TAGLINE

用于捕获常见错误的 Rust 代码检查器

# TLDR

在项目上**运行 clippy**

```cargo clippy```

**运行 clippy 并自动修复**问题

```cargo clippy --fix```

对所有目标**运行 clippy**

```cargo clippy --all-targets```

**拒绝所有警告**（视为错误）

```cargo clippy -- -D warnings```

**允许特定 lint**

```cargo clippy -- -A clippy::needless_return```

**显示所有可用的 lint**

```cargo clippy --list```

以 release 模式**运行 clippy**

```cargo clippy --release```

# SYNOPSIS

**cargo clippy** [_options_] [-- _clippy_options_]

# DESCRIPTION

**clippy** 是一组用于捕捉常见错误并改进 Rust 代码的 lint 集合。它提供数百个 lint，涵盖正确性、风格、性能、复杂度等方面。

Clippy 与 Cargo 集成，在编译期间分析代码并提供可操作的警告。lint 范围从简单的风格建议到检测隐蔽 bug 和性能问题。许多 lint 包含可用 `--fix` 应用的自动修复。

# PARAMETERS

**--fix**
> 自动应用 lint 建议。

**--all-targets**
> 检查所有目标，包括测试和示例。

**--all-features**
> 启用全部特性进行检查。

**--release**
> 以 release 模式检查。

**--list**
> 列出所有可用的 lint。

**-- -D** _lint_
> 拒绝特定 lint（视为错误）。

**-- -W** _lint_
> 对特定 lint 发出警告。

**-- -A** _lint_
> 允许（忽略）特定 lint。

**-- -F** _lint_
> 禁止特定 lint（不可被覆盖）。

# LINT CATEGORIES

**clippy::correctness**: Likely bugs
**clippy::suspicious**: Questionable code
**clippy::style**: Style improvements
**clippy::complexity**: Overly complex code
**clippy::perf**: Performance improvements
**clippy::pedantic**: Stricter lints
**clippy::nursery**: Experimental lints

# CAVEATS

某些 lint 可能产生误报。**pedantic** 类别有意保持高噪声，应按需选择性启用。来自 **--fix** 的自动修复在提交前应加以审查。Clippy 的建议偶尔可能与 **rustfmt** 格式化冲突。

# HISTORY

**clippy** 由 **Manish Goregaokar** 等人自 **2014 年**起作为第三方工具创建。名字影射微软的 Office 助手。它在 **2018 年**成为 Rust 的官方组件，通过 rustup 分发。Clippy 已发展到包含 600 多个 lint，在 Rust 生态中被广泛使用。

# INSTALL

```dnf: sudo dnf install clippy```

```brew: brew install clippy```

```nix: nix profile install nixpkgs#clippy```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cargo](/man/cargo)(1), [rustc](/man/rustc)(1), [rustfmt](/man/rustfmt)(1), [rustup](/man/rustup)(1)
