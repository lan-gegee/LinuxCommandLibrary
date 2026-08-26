# TAGLINE

从 crates.io 安装预构建的 Rust 二进制文件

# TLDR

**安装软件包的二进制文件**

```cargo binstall [ripgrep]```

**安装指定版本**

```cargo binstall [tokei@12.1.0]```

**只安装已签名的软件包**

```cargo binstall --only-signed [package]```

**无需确认直接安装**

```cargo binstall -y [package]```

**升级 cargo-binstall 自身**

```cargo binstall cargo-binstall```

**从指定目标平台安装**

```cargo binstall --targets [x86_64-unknown-linux-gnu] [package]```

# SYNOPSIS

**cargo binstall** [_options_] _crate_[@_version_]

# DESCRIPTION

**cargo binstall** 通过下载预构建发行版来安装 Rust 二进制文件，而不是从源码编译。它会从 crates.io 获取 crate 信息，搜索匹配的发行版；若找不到二进制文件则回退到 cargo install。

在性能受限的设备上比 cargo install 快得多。

# PARAMETERS

**-y**, **--no-confirm**
> 跳过确认提示

**--only-signed**
> 只安装已签名的软件包

**--targets** _targets_
> 覆盖目标平台

**--install-path** _path_
> 自定义安装目录

**--roots** _path_
> 包信息的根目录

**--force**
> 强制重新安装

**--no-symlinks**
> 不创建符号链接

**--dry-run**
> 显示将要安装的内容

**--log-level** _level_
> 设置日志详细程度

# FALLBACK ORDER

1. 关联仓库的发行版
2. quickinstall 制品托管服务
3. 其他受支持的目标平台
4. cargo install（源码构建）

# SIGNATURE VERIFICATION

维护者可在 Cargo.toml 中指定签名密钥。Binstall 在有签名可用时会下载并校验签名。

# CAVEATS

软件包必须有预构建的二进制文件或 binstall 元数据。找不到二进制文件时回退到 cargo install。

# INSTALL

```pacman: sudo pacman -S cargo-binstall```

```brew: brew install cargo-binstall```

```nix: nix profile install nixpkgs#cargo-binstall```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cargo](/man/cargo)(1), [cargo-install](/man/cargo-install)(1)

# RESOURCES

```[Source code](https://github.com/cargo-bins/cargo-binstall)```

<!-- verified: 2026-06-22 -->
