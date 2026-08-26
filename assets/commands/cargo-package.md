# TAGLINE

将本地软件包打包为可分发的归档

# TLDR

**创建软件包归档**

```cargo package```

**不经验证打包**

```cargo package --no-verify```

**列出包内文件**

```cargo package --list```

**允许未提交的更改**

```cargo package --allow-dirty```

**打包指定的工作空间成员**

```cargo package -p [crate_name]```

# SYNOPSIS

**cargo package** [_options_]

# DESCRIPTION

**cargo package** 从源代码创建可分发的 `.crate` 归档。归档位于 `target/package/`，包含源文件、规范化后的 Cargo.toml，以及可选的 Cargo.lock 文件。默认情况下，会通过在临时目录中解压并构建该归档来验证软件包。

打包过程中会对 Cargo.toml 清单进行规范化：解析工作空间继承、移除 `[patch]`、`[replace]` 和 `[workspace]` 区块，并且路径依赖必须带有 version 键。Cargo.toml 中的 `include` 和 `exclude` 字段控制哪些文件被打包。此命令等价于 `cargo publish --dry-run`，可用于检查将要上传到注册表的内容。

# PARAMETERS

**-l**, **--list**
> 列出将被包含的文件

**--no-verify**
> 跳过解压和构建验证

**--allow-dirty**
> 允许未提交的 VCS 更改

**--no-metadata**
> 忽略关于缺少元数据的警告

**--exclude-lockfile**
> 不包含 Cargo.lock

**--target** _triple_
> 为目标平台构建（用于验证）

**-p**, **--package** _spec_
> 打包指定的工作空间成员

**--workspace**
> 打包所有工作空间成员

**-v**, **--verbose**
> 详细输出

# MANIFEST PROCESSING

Cargo.toml 会被规范化：
- 移除 [patch]、[replace]、[workspace] 区块
- 路径依赖必须带 version 键
- 默认包含 Cargo.lock

# FILE CONTROL

使用 Cargo.toml 中的 include/exclude 字段控制打包的文件。

# CAVEATS

crates.io 有 10MB 的大小限制。不允许缺少 version 键的路径依赖。等价于 cargo publish --dry-run。

# INSTALL

```apt: sudo apt install cargo```

```dnf: sudo dnf install cargo```

```apk: sudo apk add cargo```

```zypper: sudo zypper install cargo```

```nix: nix profile install nixpkgs#cargo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cargo](/man/cargo)(1), [cargo-publish](/man/cargo-publish)(1)

# RESOURCES

```[Source code](https://github.com/rust-lang/cargo)```

```[Documentation](https://doc.rust-lang.org/cargo/commands/cargo-package.html)```

<!-- verified: 2026-06-22 -->
