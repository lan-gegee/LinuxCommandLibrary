# TAGLINE

用于捕获常见错误的 Rust 代码检查器

# TLDR

**运行 clippy 检查**

```cargo clippy```

**检查所有目标**

```cargo clippy --all-targets```

**以所有特性进行检查**

```cargo clippy --all-features```

**出现警告即失败（用于 CI）**

```cargo clippy -- -D warnings```

**允许特定 lint**

```cargo clippy -- -A clippy::[lint_name]```

**对特定 lint 发出警告**

```cargo clippy -- -W clippy::[lint_name]```

**自动修复问题**

```cargo clippy --fix```

**完整的 CI 检查**

```cargo clippy --all-targets --all-features -- -D warnings```

# SYNOPSIS

**cargo clippy** [_options_] [-- _clippy_options_]

# DESCRIPTION

**cargo clippy** 是 Rust 的代码检查器（linter），能够捕获常见错误并提出改进建议。它通过 rustup 随 Rust 工具链提供。默认运行 clippy::all lint 组。

# PARAMETERS

**--all-targets**
> 检查所有目标（lib、bin、tests、examples、benches）

**--all-features**
> 启用所有可用特性

**--features** _features_
> 启用指定的特性

**--release**
> 以 release 模式检查

**--workspace**
> 检查所有工作空间成员

**--fix**
> 自动应用建议的修复

**-- -A** _lint_
> 允许指定的 lint

**-- -W** _lint_
> 对指定的 lint 发出警告

**-- -D** _lint_
> 禁止指定的 lint（视为错误）

# LINT GROUPS

**clippy::correctness**
> 默认禁止，捕获明显的 bug

**clippy::style**
> 惯用写法建议

**clippy::complexity**
> 简化代码建议

**clippy::perf**
> 性能改进建议

**clippy::pedantic**
> 更严格、更主观武断的 lint

# INSTALLATION

随 Rust 工具链附带。安装/更新方式：

```rustup component add clippy```

# CAVEATS

部分 lint 较为主观。可通过 lint 配置按项目需求定制。--fix 选项会直接修改文件。

# INSTALL

```apt: sudo apt install rustup```

```dnf: sudo dnf install rustup```

```pacman: sudo pacman -S rustup```

```apk: sudo apk add rust-clippy```

```zypper: sudo zypper install rustup```

```brew: brew install rustup```

```nix: nix profile install nixpkgs#rustup```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cargo](/man/cargo)(1), [cargo-check](/man/cargo-check)(1), [rustfmt](/man/rustfmt)(1)

# RESOURCES

```[Source code](https://github.com/rust-lang/rust-clippy)```

```[Documentation](https://doc.rust-lang.org/clippy/)```

<!-- verified: 2026-06-22 -->
