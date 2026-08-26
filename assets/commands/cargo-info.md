# TAGLINE

显示 Rust crate 的信息

# TLDR

**显示软件包信息**

```cargo info [serde]```

**显示指定版本的信息**

```cargo info [serde@1.0]```

**显示本地软件包信息**

```cargo info```

**带特性显示信息**

```cargo info [tokio]```

# SYNOPSIS

**cargo info** [_options_] [_spec_]

# DESCRIPTION

**cargo info** 显示来自 crates.io 或本地工作空间的软件包信息。展示 Cargo.toml 中的元数据，包括名称、版本、描述、许可证、依赖和特性。

对于本地工作空间的软件包，则显示本地清单中的信息。若 Cargo.lock 不存在会自动创建。

# PARAMETERS

**--registry** _name_
> 使用指定的注册表

**--index** _url_
> 使用指定的注册表索引

**--manifest-path** _path_
> Cargo.toml 的路径

**-v**, **--verbose**
> 详细输出

**-q**, **--quiet**
> 抑制输出

# OUTPUT

显示内容：
- 软件包名称与版本
- 描述
- 许可证
- 文档与仓库链接
- 依赖
- 特性
- 近期版本

# CAVEATS

未指定版本时，将基于最低支持的 Rust 版本（MSRV）选择版本。如需更详细的 crate 查询，可考虑 cargo-crate 或 cargo-information。

# INSTALL

```nix: nix profile install nixpkgs#cargo-info```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cargo](/man/cargo)(1), [cargo-search](/man/cargo-search)(1)

# RESOURCES

```[Source code](https://github.com/rust-lang/cargo)```

```[Documentation](https://doc.rust-lang.org/cargo/commands/cargo-info.html)```

<!-- verified: 2026-06-22 -->
