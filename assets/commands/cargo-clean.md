# TAGLINE

清除 Rust 项目的构建产物

# TLDR

**删除整个 target 目录**

```cargo clean```

**只删除 release 构建产物**

```cargo clean --release```

**只删除文档**

```cargo clean --doc```

**清理指定软件包**

```cargo clean -p [package]```

**预览而不实际删除**

```cargo clean --dry-run```

**清理指定 profile**

```cargo clean --profile [dev]```

**针对指定目标架构**清理

```cargo clean --target [x86_64-unknown-linux-gnu]```

**带详细文件列表的**预览

```cargo clean --dry-run -v```

# SYNOPSIS

**cargo clean** [_options_]

# DESCRIPTION

**cargo clean** 删除 Cargo 在 target 目录中生成的构建产物。不带任何选项时，会删除整个 target 目录。当使用 **-p** 选定软件包时，只删除这些软件包的产物。

# PARAMETERS

**--release**
> 删除 release 目录中的产物。

**--profile** _name_
> 删除指定构建 profile 的产物。

**--doc**
> 只删除 target 目录中的 doc 目录。

**-p**, **--package** _spec_
> 只清理指定的软件包。可多次指定。

**--target** _triple_
> 针对指定的目标架构进行清理。可多次指定。

**--target-dir** _dir_
> 自定义 target 目录路径。

**--dry-run**
> 显示将要删除的内容但不真正删除。

**-v**, **--verbose**
> 使用详细输出。指定两次可获得非常详细的输出。

**-q**, **--quiet**
> 不打印 cargo 日志消息。

**--color** _WHEN_
> 控制何时使用彩色输出（auto、always、never）。

**--manifest-path** _path_
> Cargo.toml 的路径。

# CAVEATS

不选定软件包时，会清理工作空间中的所有软件包和依赖。target 目录可能增长得非常大；定期清理能释放大量磁盘空间，但之后需要完整重新构建。

# INSTALL

```apt: sudo apt install cargo```

```dnf: sudo dnf install cargo```

```apk: sudo apk add cargo```

```zypper: sudo zypper install cargo```

```nix: nix profile install nixpkgs#cargo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cargo](/man/cargo)(1), [cargo-build](/man/cargo-build)(1), [cargo-test](/man/cargo-test)(1)
