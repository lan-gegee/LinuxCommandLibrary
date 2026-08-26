# TAGLINE

编译并运行 Rust 项目的基准测试

# TLDR

**运行所有基准测试**

```cargo bench```

**运行名称包含某子串的基准测试**

```cargo bench [bench_name]```

**只编译基准测试而不运行**

```cargo bench --no-run```

**在整个工作空间范围内运行基准测试**

```cargo bench --workspace```

**基准测试失败后继续运行**

```cargo bench --no-fail-fast```

**对指定的软件包进行基准测试**

```cargo bench -p [package]```

**测试指定的 bench 目标**

```cargo bench --bench [bench_target]```

**将参数透传给基准测试二进制**

```cargo bench -- --save-baseline [name]```

# SYNOPSIS

**cargo bench** [_options_] [_benchname_] [-- _bench-options_]

# DESCRIPTION

**cargo bench** 编译并执行当前软件包的基准测试目标。默认使用 `bench` profile（开启优化、调试信息最少）并串行运行各基准测试。

`--` 之后的参数会转发给编译出的基准测试二进制，Criterion 和 libtest 的选项（如 `--save-baseline` 或 `--test`）就是这样传入的。

# PARAMETERS

**--no-run**
> 编译基准测试但不执行。

**--no-fail-fast**
> 即使前面的基准测试失败也继续运行每一个。

**--all-targets**
> 对所有目标进行基准测试（等价于 `--lib --bins --tests --benches --examples`）。

**--workspace**
> 对工作空间中的所有软件包进行基准测试。

**--exclude** _SPEC_
> 在 `--workspace` 运行中排除指定软件包。

**-p**, **--package** _SPEC_
> 只对指定的软件包进行基准测试。

**--lib**
> 只对库目标进行基准测试。

**--bins**
> 对所有二进制目标进行基准测试。

**--bin** _NAME_
> 只对指定名称的二进制进行基准测试。

**--benches**
> 对所有 `bench = true` 的目标进行基准测试。

**--bench** _NAME_
> 只对指定名称的 bench 目标进行基准测试。

**--examples**
> 对所有示例目标进行基准测试。

**--profile** _NAME_
> 以指定 profile 构建（默认为 `bench`）。

**--target** _TRIPLE_
> 为给定的目标三元组构建。

**-j**, **--jobs** _N_
> 并行构建任务数（影响编译，不影响基准测试的执行）。

**-F**, **--features** _FEATURES_
> 要启用的特性列表，以空格或逗号分隔。

**--all-features**
> 启用所有已选软件包的全部特性。

**--no-default-features**
> 不启用 `default` 特性。

**--manifest-path** _PATH_
> `Cargo.toml` 的路径。

**--locked**
> 要求 `Cargo.lock` 保持不变。

**--offline**
> 不访问网络。

# BENCHMARKING FRAMEWORKS

**libtest bench**
> 内置的 `#[bench]` 测试框架，需要 nightly 版 Rust。

**Criterion**
> 流行的稳定测试框架，带统计分析和基线功能。

**Iai**
> 基于 Cachegrind 的指令计数基准测试。

# CAVEATS

内置的 `#[bench]` 属性尚不稳定，需要 nightly 版 Rust；在 stable 版上请使用自定义框架（如在 `Cargo.toml` 中以 `harness = false` 声明的 **Criterion**）。`--jobs` 选项控制的是构建并行度，而非基准测试的执行。在没有 CPU 绑核和安静系统的情况下，结果可能有噪声。

# INSTALL

```apt: sudo apt install cargo```

```dnf: sudo dnf install cargo```

```apk: sudo apk add cargo```

```zypper: sudo zypper install cargo```

```nix: nix profile install nixpkgs#cargo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cargo](/man/cargo)(1), [cargo-test](/man/cargo-test)(1), [cargo-build](/man/cargo-build)(1)
