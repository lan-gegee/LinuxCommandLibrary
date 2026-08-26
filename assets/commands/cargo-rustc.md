# TAGLINE

使用额外的 rustc 标志编译软件包

# TLDR

**带额外 rustc 标志编译**

```cargo rustc -- [rustc_flags]```

**带标志编译指定二进制**

```cargo rustc --bin [name] -- [flags]```

**带标志编译库**

```cargo rustc --lib -- [-C opt-level=3]```

**启用特定的代码生成选项**

```cargo rustc -- -C [target-cpu=native]```

**添加链接参数**

```cargo rustc -- -C [link-arg=-fuse-ld=lld]```

# SYNOPSIS

**cargo rustc** [_options_] [-- _args_]

# DESCRIPTION

**cargo rustc** 编译当前软件包，并将额外选项直接传递给 Rust 编译器。与作用于构建中所有 crate 的 `RUSTFLAGS` 不同，`--` 之后的参数只传递给指定目标的最后一次编译器调用，而不会传给它的依赖。

此命令适用于为单个 crate 启用特定的代码生成选项、更改优化级别、输出 LLVM IR 或汇编等中间表示，或传入自定义链接器参数，而不影响依赖图的其他部分。

# PARAMETERS

**--lib**
> 只编译库

**--bin** _name_
> 编译指定的二进制文件

**--bins**
> 编译所有二进制文件

**--example** _name_
> 编译指定的示例

**--test** _name_
> 编译指定的测试

**--bench** _name_
> 编译指定的基准测试

**-r**, **--release**
> 使用 release profile

**--profile** _name_
> 使用指定的 profile

**-p**, **--package** _spec_
> 要编译的软件包

**--target** _triple_
> 目标平台

**-j**, **--jobs** _n_
> 并行任务数

**--features** _features_
> 启用特性

**--all-features**
> 启用所有特性

# RUSTC OPTIONS

常用的 rustc 标志：
- **-C opt-level=N**: 优化级别
- **-C target-cpu=NAME**: 目标 CPU
- **-C link-arg=ARG**: 链接器参数
- **--emit=TYPE**: 输出类型（asm、llvm-ir、obj）

# ENVIRONMENT

**RUSTFLAGS**
> 将标志传递给所有 rustc 调用

# CAVEATS

传入额外参数时只能编译一个目标。请使用过滤器（--lib、--bin）选择目标。

# INSTALL

```apt: sudo apt install cargo```

```dnf: sudo dnf install cargo```

```apk: sudo apk add cargo```

```zypper: sudo zypper install cargo```

```nix: nix profile install nixpkgs#cargo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cargo](/man/cargo)(1), [rustc](/man/rustc)(1), [cargo-build](/man/cargo-build)(1)

# RESOURCES

```[Source code](https://github.com/rust-lang/cargo)```

```[Documentation](https://doc.rust-lang.org/cargo/commands/cargo-rustc.html)```

<!-- verified: 2026-06-22 -->
