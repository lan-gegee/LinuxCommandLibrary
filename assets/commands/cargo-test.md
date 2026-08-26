# TAGLINE

运行单元测试和集成测试

# TLDR

**运行所有测试**

```cargo test```

**运行指定测试**

```cargo test [test_name]```

**运行模块中的测试**

```cargo test [module_name]::**```

**运行被忽略的测试**

```cargo test -- --ignored```

**显示通过测试的输出**

```cargo test -- --show-output```

**只运行文档测试**

```cargo test --doc```

**失败时不停止继续运行**

```cargo test -- --no-fail-fast```

**只编译不运行**

```cargo test --no-run```

# SYNOPSIS

**cargo test** [_options_] [_testname_] [-- _test-options_]

# DESCRIPTION

**cargo test** 编译并运行 Rust 项目的测试套件。它会发现单元测试（`src/` 中标注 `#[test]` 的函数）、集成测试（`tests/` 目录中的文件）、文档测试（文档注释中的代码块）以及基准测试。可以提供测试名称过滤器，只运行匹配的测试。

`--` 之后的参数会直接传给测试框架而不是 Cargo。这样可以控制测试执行行为，例如线程数、输出捕获以及是否运行被忽略的测试。测试默认并行运行；当测试间存在共享状态时，可使用 `--test-threads=1` 进行顺序执行。

# PARAMETERS

**--no-run**
> 只编译不运行

**--no-fail-fast**
> 无论是否失败都运行全部测试

**--doc**
> 只运行文档测试

**--lib**
> 只测试库

**--bins**
> 测试所有二进制文件

**--tests**
> 测试所有测试目标

**--benches**
> 测试所有基准测试

**--all-targets**
> 测试所有目标

**-p**, **--package** _spec_
> 测试指定的软件包

**--workspace**
> 测试所有工作空间成员

**-j**, **--jobs** _n_
> 并行构建任务数

**--release**
> 以 release profile 测试

**--features** _features_
> 启用特性

**--all-features**
> 启用所有特性

# TEST BINARY OPTIONS

**-- --ignored**
> 运行被忽略的测试

**-- --show-output**
> 显示通过测试的标准输出

**-- --test-threads** _n_
> 并行测试线程数

**-- --nocapture**
> 不捕获测试输出

# CAVEATS

测试默认并行运行。需要顺序执行时请使用 --test-threads=1。

# INSTALL

```apt: sudo apt install cargo```

```dnf: sudo dnf install cargo```

```apk: sudo apk add cargo```

```zypper: sudo zypper install cargo```

```nix: nix profile install nixpkgs#cargo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cargo](/man/cargo)(1), [cargo-bench](/man/cargo-bench)(1)

# RESOURCES

```[Source code](https://github.com/rust-lang/cargo)```

```[Documentation](https://doc.rust-lang.org/cargo/commands/cargo-test.html)```

<!-- verified: 2026-06-22 -->
