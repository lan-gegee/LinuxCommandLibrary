# TAGLINE

以 JSON 形式输出工作空间和依赖元数据

# TLDR

**输出项目元数据**

```cargo metadata```

**带格式版本输出**

```cargo metadata --format-version 1```

**不包含依赖**

```cargo metadata --no-deps```

**过滤到指定特性**

```cargo metadata --features [feature1,feature2]```

**美化打印 JSON**

```cargo metadata --format-version 1 | jq .```

# SYNOPSIS

**cargo metadata** [_options_]

# DESCRIPTION

**cargo metadata** 向标准输出 JSON，内容涵盖工作空间成员、解析后的依赖以及构建配置等信息。对工具链开发和 IDE 集成非常有用。

# PARAMETERS

**--format-version** _version_
> 模式版本（为保证稳定性请使用 1）

**--no-deps**
> 跳过依赖解析（更快，仅限工作空间本身）

**--features** _features_
> 启用指定的特性

**--all-features**
> 启用所有特性

**--no-default-features**
> 禁用默认特性

**--filter-platform** _triple_
> 过滤到指定平台

**--manifest-path** _path_
> Cargo.toml 的路径

**-v**, **--verbose**
> 详细输出

**-q**, **--quiet**
> 抑制日志消息

# OUTPUT FIELDS

**packages**
> 所有软件包及依赖的数组

**workspace_members**
> 工作空间成员的软件包 ID

**workspace_root**
> 工作空间根目录的绝对路径

**target_directory**
> 构建输出目录的路径

**resolve**
> 依赖解析图

**version**
> 模式版本号

# CAVEATS

输出格式可能随 Cargo 版本变化。在脚本中务必使用 --format-version。cargo_metadata crate 提供 Rust 解析支持。

# INSTALL

```apt: sudo apt install cargo```

```dnf: sudo dnf install cargo```

```apk: sudo apk add cargo```

```zypper: sudo zypper install cargo```

```nix: nix profile install nixpkgs#cargo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cargo](/man/cargo)(1), [cargo-locate-project](/man/cargo-locate-project)(1)

# RESOURCES

```[Source code](https://github.com/rust-lang/cargo)```

```[Documentation](https://doc.rust-lang.org/cargo/commands/cargo-metadata.html)```

<!-- verified: 2026-06-22 -->
