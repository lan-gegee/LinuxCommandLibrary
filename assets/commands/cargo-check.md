# TAGLINE

检查 Rust 软件包的错误而不生成代码

# TLDR

**检查项目错误**

```cargo check```

**以 release profile 检查**

```cargo check --release```

**检查所有工作空间成员**

```cargo check --workspace```

**检查指定软件包**

```cargo check -p [package]```

**检查所有目标**

```cargo check --all-targets```

**连同测试一起检查**

```cargo check --profile test```

**以指定特性检查**

```cargo check --features [feature1,feature2]```

# SYNOPSIS

**cargo check** [_options_]

# DESCRIPTION

**cargo check** 检查软件包及其依赖中的错误，但不执行代码生成。由于跳过了最后的编译步骤，比 cargo build 更快。它还会保存元数据以支持增量编译。

# PARAMETERS

**-r**, **--release**
> 以 release profile 的优化进行检查

**--profile** _name_
> 以指定 profile 检查

**-p**, **--package** _spec_
> 只检查指定的软件包

**--workspace**
> 检查所有工作空间成员

**--all-targets**
> 检查所有目标（lib、bins、tests、benches、examples）

**--lib**
> 只检查库

**--bins**
> 检查所有二进制文件

**--tests**
> 检查测试目标

**--target** _triple_
> 为目标平台进行检查

**-j**, **--jobs** _n_
> 并行任务数

**--features** _features_
> 启用指定的特性

**--all-features**
> 启用所有特性

**--no-default-features**
> 禁用默认特性

**--message-format** _FMT_
> 错误格式：human、json、short

**--future-incompat-report**
> 输出未来不兼容性报告

# CAVEATS

有些错误只会在完整代码生成时出现，cargo check 无法捕获。要彻底检查错误，请使用 `cargo build`。`--profile test` 会启用 test cfg 并检查测试代码。对于快速迭代，它比 `cargo build` 快得多。

# INSTALL

```apt: sudo apt install cargo```

```dnf: sudo dnf install cargo```

```apk: sudo apk add cargo```

```zypper: sudo zypper install cargo```

```nix: nix profile install nixpkgs#cargo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cargo](/man/cargo)(1), [cargo-build](/man/cargo-build)(1), [cargo-fix](/man/cargo-fix)(1)
