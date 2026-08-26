# TAGLINE

构建并执行本地软件包的二进制文件

# TLDR

**构建并运行项目**

```cargo run```

**以 release 优化运行**

```cargo run --release```

**运行指定的二进制文件**

```cargo run --bin [binary_name]```

**运行示例**

```cargo run --example [example_name]```

**向二进制传递参数**

```cargo run -- [arg1] [arg2]```

**启用特性后运行**

```cargo run --features [feature1,feature2]```

**运行指定软件包**

```cargo run -p [package]```

# SYNOPSIS

**cargo run** [_options_] [-- _args_]

# DESCRIPTION

**cargo run** 构建并执行当前软件包的一个二进制目标。当源文件有改动时它会自动重新编译项目，然后运行生成的可执行文件。`--` 之后的所有参数都会直接转发给二进制文件，而不会被 Cargo 解析。

如果软件包包含多个二进制目标，必须用 `--bin` 或 `--example` 选择其中一个，也可以通过 Cargo.toml 中的 `default-run` 字段配置默认值。二进制的工作目录被设置为当前 shell 目录。

# PARAMETERS

**--bin** _name_
> 运行指定的二进制文件

**--example** _name_
> 运行指定的示例

**-r**, **--release**
> 以 release profile 的优化运行

**--profile** _name_
> 以指定 profile 构建

**-p**, **--package** _spec_
> 运行指定软件包中的目标

**--target** _triple_
> 为目标平台运行

**-j**, **--jobs** _n_
> 并行构建任务数

**--features** _features_
> 启用指定的特性

**--all-features**
> 启用所有特性

**--no-default-features**
> 禁用默认特性

**-v**, **--verbose**
> 详细输出

# WORKING DIRECTORY

将二进制的工作目录设为当前目录（与在 shell 中执行相同）。

# DEFAULT BINARY

在 Cargo.toml 的 [package] 区块中设置 default-run 以选择默认二进制。

# CAVEATS

存在多个二进制且未使用 --bin 时会报错。可使用清单中的 default-run 键设置默认值。

# INSTALL

```apt: sudo apt install cargo```

```dnf: sudo dnf install cargo```

```apk: sudo apk add cargo```

```zypper: sudo zypper install cargo```

```nix: nix profile install nixpkgs#cargo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cargo](/man/cargo)(1), [cargo-build](/man/cargo-build)(1), [cargo-test](/man/cargo-test)(1)

# RESOURCES

```[Source code](https://github.com/rust-lang/cargo)```

```[Documentation](https://doc.rust-lang.org/cargo/commands/cargo-run.html)```

<!-- verified: 2026-06-22 -->
