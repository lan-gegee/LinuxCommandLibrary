# TAGLINE

修改 Cargo.toml 中 Rust 软件包的版本号

# TLDR

**设置**精确版本

```cargo set-version [1.0.0]```

**递增主版本**

```cargo set-version --bump major```

**递增次版本**

```cargo set-version --bump minor```

**递增修订号**

```cargo set-version --bump patch```

**应用到整个工作空间**

```cargo set-version --workspace --bump patch```

**试运行**

```cargo set-version -n --bump minor```

# SYNOPSIS

**cargo set-version** [*options*] [*TARGET*]

# DESCRIPTION

**cargo set-version**（来自 **cargo-edit**）修改本地 **Cargo.toml** 中的 **version** 字段。你可以设置绝对版本，或按 major/minor/patch 递增。支持整个工作空间的批量更新。

使用 **cargo install cargo-edit** 安装。

# PARAMETERS

*TARGET*

> 要设置的绝对版本（例如 **1.2.3**），在不使用 **--bump** 时生效。

**--bump** major|minor|patch|...

> 递增相应的 semver 组成部分。

**-m**, **--metadata** *METADATA*

> 设置版本元数据字段（例如构建元数据）。

**-p**, **--package** *PKGID*

> 在工作空间中选择一个软件包。

**--workspace**

> 修改工作空间中的所有软件包。

**--exclude** *EXCLUDE*

> 工作空间模式下跳过指定的 crate。

**-n**, **--dry-run**

> 打印更改但不写入文件。

**--manifest-path** *PATH*

> 要编辑的清单文件路径。

**--offline**

> 不访问网络运行。

**--locked**

> 要求 Cargo.toml 与锁文件的配置保持同步。

完整选项集请参见 **cargo set-version --help**。

# CAVEATS

不会发布 crate；只负责编辑清单。版本递增需要另行与标签和变更日志流程协调。工作空间级别的递增会同时影响许多 crate；建议先使用 **--dry-run**。

# INSTALL

```pacman: sudo pacman -S cargo-edit```

```apk: sudo apk add cargo-edit```

```brew: brew install cargo-edit```

```nix: nix profile install nixpkgs#cargo-edit```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cargo-upgrade](/man/cargo-upgrade)(1), [cargo-add](/man/cargo-add)(1), [cargo](/man/cargo)(1)

# RESOURCES

```[Source code](https://github.com/killercup/cargo-edit)```

<!-- verified: 2026-07-19 -->
