# TAGLINE

下载依赖以支持离线构建

# TLDR

**获取所有依赖**

```cargo fetch```

**为指定目标平台获取**

```cargo fetch --target [x86_64-unknown-linux-gnu]```

**以锁定的版本获取**

```cargo fetch --locked```

**离线获取（使用缓存）**

```cargo fetch --offline```

# SYNOPSIS

**cargo fetch** [_options_]

# DESCRIPTION

**cargo fetch** 从网络下载所有依赖并存储到本地。若存在 Cargo.lock，则获取其中指定的确切版本；否则先生成锁文件。

适用于配合 --offline 选项提前准备离线开发环境。

# PARAMETERS

**--target** _triple_
> 为指定的目标架构获取依赖（可重复指定）

**--locked**
> 断言依赖与原 Cargo.lock 一致

**--offline**
> 只使用本地缓存的 crate

**--frozen**
> 等价于 --locked 和 --offline

**--manifest-path** _path_
> Cargo.toml 的路径

**-v**, **--verbose**
> 详细输出

**-q**, **--quiet**
> 抑制日志消息

# BEHAVIOR

不带 --target 时会获取所有目标平台的依赖。Git 依赖会连同子模块一起克隆。注册表 crate 会下载到 cargo 缓存。

# CAVEATS

执行 fetch 后，只要锁文件不变化，后续 cargo 命令即可离线运行。除非使用 --offline 且依赖已缓存，否则需要网络访问。

# INSTALL

```apt: sudo apt install cargo```

```dnf: sudo dnf install cargo```

```apk: sudo apk add cargo```

```zypper: sudo zypper install cargo```

```nix: nix profile install nixpkgs#cargo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cargo](/man/cargo)(1), [cargo-build](/man/cargo-build)(1), [cargo-update](/man/cargo-update)(1)

# RESOURCES

```[Source code](https://github.com/rust-lang/cargo)```

```[Documentation](https://doc.rust-lang.org/cargo/commands/cargo-fetch.html)```

<!-- verified: 2026-06-22 -->
