# TAGLINE

编译 Rust 软件包及其依赖

# TLDR

**构建项目**

```cargo build```

**以 release 优化构建**

```cargo build --release```

**构建指定软件包**

```cargo build -p [package]```

**构建所有工作空间成员**

```cargo build --workspace```

**以指定特性构建**

```cargo build --features [feature1,feature2]```

**启用所有特性构建**

```cargo build --all-features```

**为指定目标平台构建**

```cargo build --target [x86_64-unknown-linux-gnu]```

**离线构建**

```cargo build --offline```

# SYNOPSIS

**cargo build** [_options_]

# DESCRIPTION

**cargo build** 编译本地软件包及其全部依赖。默认在 target/debug/ 中生成可执行文件，使用 --release 选项时则在 target/release/ 中生成。

Debug 构建编译更快但运行较慢。Release 构建经过优化但编译耗时更长。

# PARAMETERS

**-r**, **--release**
> 以优化方式构建（release profile）

**--profile** _name_
> 以指定 profile 构建

**-p**, **--package** _spec_
> 只构建指定的软件包

**--workspace**
> 构建所有工作空间成员

**--all-targets**
> 构建所有目标（lib、bins、tests、benches、examples）

**--lib**
> 只构建库

**--bins**
> 构建所有二进制文件

**--examples**
> 构建所有示例

**--target** _triple_
> 为目标平台构建

**--target-dir** _dir_
> 输出目录

**-j**, **--jobs** _n_
> 并行构建任务数

**--features** _features_
> 启用指定的特性

**--all-features**
> 启用所有特性

**--no-default-features**
> 禁用默认特性

**--offline**
> 不访问网络进行构建

**--timings**
> 输出构建耗时信息

# OUTPUT LOCATIONS

**target/debug/**
> Debug 构建（默认）

**target/release/**
> Release 构建（--release）

# CAVEATS

相同的命令在所有操作系统上均可使用。首次构建会下载并编译依赖。

# INSTALL

```apt: sudo apt install cargo```

```dnf: sudo dnf install cargo```

```apk: sudo apk add cargo```

```zypper: sudo zypper install cargo```

```nix: nix profile install nixpkgs#cargo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cargo](/man/cargo)(1), [cargo-run](/man/cargo-run)(1), [cargo-check](/man/cargo-check)(1)

# RESOURCES

```[Source code](https://github.com/rust-lang/cargo)```

```[Documentation](https://doc.rust-lang.org/cargo/commands/cargo-build.html)```

<!-- verified: 2026-06-22 -->
