# TAGLINE

从 Rust 项目构建 Debian 软件包

# TLDR

**创建 Debian 软件包**

```cargo deb```

**构建并在本地安装**

```cargo deb --install```

**指定输出位置**

```cargo deb --output [path/to/package.deb]```

**为指定目标平台构建**

```cargo deb --target [x86_64-unknown-linux-gnu]```

**设置软件包修订号**

```cargo deb --deb-revision [2]```

**不带默认特性构建**

```cargo deb --no-default-features```

**详细输出**

```cargo deb --verbose```

# SYNOPSIS

**cargo deb** [_options_]

# DESCRIPTION

**cargo deb** 自动从 Cargo 项目创建二进制 Debian 软件包（.deb）。它使用 Cargo.toml 元数据和可选的 [package.metadata.deb] 配置。

输出位于 target/debian/<name>_<version>-<revision>_<arch>.deb

# PARAMETERS

**--install**
> 构建后立即安装软件包

**-o**, **--output** _path_
> 自定义输出文件路径

**--target** _triple_
> 为指定目标平台构建

**--deb-revision** _rev_
> 设置 Debian 软件包修订号

**--no-build**
> 跳过 cargo build 步骤

**--no-strip**
> 不剥离调试符号

**--separate-debug-symbols**
> 创建独立的调试软件包

**--fast**
> 跳过部分优化以加快构建

**--variant** _name_
> 使用特定变体的配置

**-v**, **--verbose**
> 详细输出

# CONFIGURATION

在 Cargo.toml 中添加：

```toml
[package.metadata.deb]
maintainer = "Name <email>"
depends = "$auto"
section = "utility"
priority = "optional"
assets = [
    ["target/release/bin", "usr/bin/", "755"],
]
```

# INSTALLATION

```cargo install cargo-deb```

需要 Rust 1.76+。可选依赖：dpkg、dpkg-dev、liblzma-dev。

# CAVEATS

自动使用 Cargo 字段中的名称、版本、许可证和描述。$auto 依赖值会在 Debian 系统上自动检测库依赖。

# INSTALL

```pacman: sudo pacman -S cargo-deb```

```nix: nix profile install nixpkgs#cargo-deb```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cargo](/man/cargo)(1), [dpkg](/man/dpkg)(1), [dpkg-deb](/man/dpkg-deb)(1)

# RESOURCES

```[Source code](https://github.com/kornelski/cargo-deb)```

<!-- verified: 2026-06-22 -->
