# TAGLINE

显示 Cargo 的版本信息

# TLDR

**显示 Cargo 版本**

```cargo version```

**显示详细版本信息**

```cargo version --verbose```

**短格式**

```cargo -V```

**详细短格式**

```cargo -Vv```

# SYNOPSIS

**cargo version** [_options_]

**cargo** [_-V_ | _--version_]

# DESCRIPTION

**cargo version** 显示 Cargo 的版本及构建元数据。默认输出包含版本号、git 提交哈希和构建日期。加上 `--verbose` 标志后，还会显示更多细节，包括主机三元组、所链接库的版本（libgit2、libcurl、SSL）以及操作系统信息。

该命令适用于诊断构建问题、验证工具链安装，以及在 CI/CD 日志和错误报告中附上版本信息。它完全离线运行，没有任何副作用。

# PARAMETERS

**-v**, **--verbose**
> 显示额外的构建元数据

**--format-version** _n_
> 输出格式：1（旧式 JSON）、2（人类可读，默认）

# OUTPUT

**默认**
```
cargo 1.75.0 (1d8b05cdd 2023-11-20)
```

**详细**
```
cargo 1.75.0 (1d8b05cdd 2023-11-20)
release: 1.75.0
commit-hash: 1d8b05cdd
commit-date: 2023-11-20
host: x86_64-unknown-linux-gnu
libgit2: 1.7.1
libcurl: 7.88.1
ssl: OpenSSL 3.0.11
os: Linux [kernel 6.1.0]
```

# RELATED COMMANDS

**rustc --version**
> 显示 Rust 编译器版本

**rustup show**
> 显示已安装的工具链

# CAVEATS

离线运行，无副作用。适用于 CI/CD 和构建脚本检查。

# INSTALL

```apt: sudo apt install cargo```

```dnf: sudo dnf install cargo```

```apk: sudo apk add cargo```

```zypper: sudo zypper install cargo```

```nix: nix profile install nixpkgs#cargo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cargo](/man/cargo)(1), [rustc](/man/rustc)(1), [rustup](/man/rustup)(1)

# RESOURCES

```[Source code](https://github.com/rust-lang/cargo)```

```[Documentation](https://doc.rust-lang.org/cargo/commands/cargo-version.html)```

<!-- verified: 2026-06-22 -->
