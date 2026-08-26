# TAGLINE

从 Cargo.toml 清单中移除依赖

# TLDR

**移除依赖**

```cargo remove [serde]```

**移除开发依赖**

```cargo remove --dev [mockall]```

**移除构建依赖**

```cargo remove --build [cc]```

**移除多个依赖**

```cargo remove [serde] [tokio] [regex]```

**移除针对特定平台的依赖**

```cargo remove --target [x86_64-pc-windows-gnu] [winapi]```

**试运行**

```cargo remove --dry-run [package]```

# SYNOPSIS

**cargo remove** [_options_] _dep_...

# DESCRIPTION

**cargo remove** 从 Cargo.toml 清单文件中移除一个或多个依赖。它可以作用于常规依赖、dev-dependencies、build-dependencies 或特定平台的依赖区块。

该命令直接修改 Cargo.toml，但在下一次构建或执行 `cargo update` 之前不会更新 Cargo.lock。一次调用可以移除多个依赖。可先用 `--dry-run` 预览更改再实际应用。

# PARAMETERS

**--dev**, **-D**
> 从 dev-dependencies 中移除

**--build**, **-B**
> 从 build-dependencies 中移除

**--target** _triple_
> 从特定平台的依赖中移除

**-p**, **--package** _spec_
> 要修改的软件包

**--dry-run**
> 显示更改但不修改清单

**--manifest-path** _path_
> Cargo.toml 的路径

**-v**, **--verbose**
> 详细输出

**-q**, **--quiet**
> 抑制输出

# CAVEATS

在下一次构建之前不会从 Cargo.lock 中移除依赖。可使用 cargo-machete 检测未使用的依赖。

# INSTALL

```apt: sudo apt install cargo```

```dnf: sudo dnf install cargo```

```apk: sudo apk add cargo```

```zypper: sudo zypper install cargo```

```nix: nix profile install nixpkgs#cargo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cargo](/man/cargo)(1), [cargo-add](/man/cargo-add)(1), [cargo-update](/man/cargo-update)(1)

# RESOURCES

```[Source code](https://github.com/rust-lang/cargo)```

```[Documentation](https://doc.rust-lang.org/cargo/commands/cargo-remove.html)```

<!-- verified: 2026-06-22 -->
