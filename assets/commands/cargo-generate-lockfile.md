# TAGLINE

为 Rust 项目创建或重新生成 Cargo.lock

# TLDR

**生成锁文件**

```cargo generate-lockfile```

**以最新版本重新生成**

```cargo generate-lockfile```

**使用指定的清单文件生成**

```cargo generate-lockfile --manifest-path [path/to/Cargo.toml]```

**使用自定义锁文件路径生成**

```cargo generate-lockfile --lockfile-path [/tmp/Cargo.lock]```

# SYNOPSIS

**cargo generate-lockfile** [_options_]

# DESCRIPTION

**cargo generate-lockfile** 为当前软件包或工作空间创建或重建 Cargo.lock。若锁文件已存在，则以所有软件包的最新可用版本重新构建。

# PARAMETERS

**--manifest-path** _path_
> Cargo.toml 的路径

**--lockfile-path** _path_
> 自定义锁文件路径（必须以 Cargo.lock 结尾）

**--locked**
> 断言依赖与原锁文件完全一致

**--offline**
> 不访问网络

**--frozen**
> 等价于 --locked 和 --offline

**-v**, **--verbose**
> 详细输出（指定两次可获得非常详细的输出）

**-q**, **--quiet**
> 抑制日志消息

# BEHAVIOR

不存在 Cargo.lock 时创建新的。以最新的兼容版本重建已有锁文件。如需对版本更新做更精细的控制，请使用 cargo update。

# CAVEATS

通过锁定依赖版本来保证构建可复现。在 CI 流水线中可用于实现确定性构建。对于应用程序（而非库），建议将 Cargo.lock 提交到版本控制。

# INSTALL

```apt: sudo apt install cargo```

```dnf: sudo dnf install cargo```

```apk: sudo apk add cargo```

```zypper: sudo zypper install cargo```

```nix: nix profile install nixpkgs#cargo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cargo](/man/cargo)(1), [cargo-update](/man/cargo-update)(1), [cargo-fetch](/man/cargo-fetch)(1)

# RESOURCES

```[Source code](https://github.com/rust-lang/cargo)```

```[Documentation](https://doc.rust-lang.org/cargo/commands/cargo-generate-lockfile.html)```

<!-- verified: 2026-06-22 -->
