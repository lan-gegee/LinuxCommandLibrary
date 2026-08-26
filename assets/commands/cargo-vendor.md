# TAGLINE

将所有依赖 vendoring 到本地

# TLDR

**Vendor 依赖**

```cargo vendor```

**Vendor 到指定目录**

```cargo vendor [vendor/]```

**Vendor 并保存配置**

```cargo vendor > .cargo/config.toml```

**Vendor 时使用带版本号的目录**

```cargo vendor --versioned-dirs```

**Vendor 指定软件包**

```cargo vendor -s [package/Cargo.toml]```

# SYNOPSIS

**cargo vendor** [_options_] [_path_]

# DESCRIPTION

**cargo vendor** 将所有 crates.io 与 git 依赖下载并复制到本地目录（默认：`vendor/`）。它会输出将依赖解析重定向到这些 vendored 来源所需的 Cargo 配置。

这主要用于离线构建、隔离（air-gapped）环境，以及编译期间无法或不宜访问网络的可复现构建系统。Vendored 的来源是只读的；要修改某个 vendored crate，请使用 Cargo.toml 中的 `[patch]` 部分，而不是直接编辑 vendor 目录中的文件。

# PARAMETERS

**-s**, **--sync** _path_
> 需要一并同步的其他 Cargo.toml

**--no-delete**
> 不删除已有的 vendor 目录

**--versioned-dirs**
> 使用带版本号的目录名

**--respect-source-config**
> Vendor 时遵循 [source] 配置

**--manifest-path** _path_
> Cargo.toml 的路径

**-v**, **--verbose**
> 详细输出

**-q**, **--quiet**
> 抑制输出

# CONFIGURATION

**.cargo/config.toml**
> 将依赖解析重定向到 vendor 目录的来源替换设置。`cargo vendor` 的输出给出了需要添加的确切配置。

# OFFLINE BUILDS

Vendor 完成后：
```
cargo build --offline
```

# CAVEATS

Vendored 来源是只读的。修改请使用 [patch]。解析结果可能与在线模式不同。请先运行 cargo fetch 以完整下载依赖。

# INSTALL

```apt: sudo apt install cargo```

```dnf: sudo dnf install cargo```

```apk: sudo apk add cargo```

```zypper: sudo zypper install cargo```

```nix: nix profile install nixpkgs#cargo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cargo](/man/cargo)(1), [cargo-fetch](/man/cargo-fetch)(1)

# RESOURCES

```[Source code](https://github.com/rust-lang/cargo)```

```[Documentation](https://doc.rust-lang.org/cargo/commands/cargo-vendor.html)```

<!-- verified: 2026-06-22 -->
