# TAGLINE

更新 Cargo.lock 中的依赖

# TLDR

**更新所有依赖**

```cargo update```

**更新指定软件包**

```cargo update -p [package]```

**更新到指定版本**

```cargo update -p [package] --precise [1.2.3]```

**只更新工作空间内的软件包**

```cargo update --workspace```

**预览更新**

```cargo update --dry-run```

**更新软件包及其依赖**

```cargo update -p [package] --recursive```

# SYNOPSIS

**cargo update** [_options_]

# DESCRIPTION

**cargo update** 将 Cargo.lock 中记录的依赖更新为满足 Cargo.toml 版本要求的最新版本。若 Cargo.lock 不存在，则会创建。不带 `-p` 标志时，会更新所有依赖。

配合 `-p` 使用时，只保守地更新指定软件包。`--precise` 标志可将软件包固定到确切版本。锁文件保证了跨环境的可复现构建；在遵循 semver 约束的前提下拉取依赖的 bug 修复和次要更新，运行 `cargo update` 是标准做法。

# PARAMETERS

**-p**, **--package** _spec_
> 只更新指定软件包

**--precise** _version_
> 设置精确版本（与 -p 搭配）

**--recursive**
> 更新软件包及其传递依赖（与 -p 搭配）

**--workspace**
> 只更新工作空间内的软件包

**--dry-run**
> 显示更新内容但不写入锁文件

**--locked**
> 断言锁文件无需更新

**--offline**
> 不访问网络

**--frozen**
> 等价于 --locked --offline

**-v**, **--verbose**
> 详细输出

**-q**, **--quiet**
> 抑制输出

# BEHAVIOR

**带 -p**
> 保守更新：仅更新指定软件包

**不带 -p**
> 完整更新：将所有依赖更新到最新

# CAVEATS

Cargo.lock 由 Cargo 自动维护。想要更新的兼容版本时执行更新即可。锁文件确保构建可复现。

# INSTALL

```pacman: sudo pacman -S cargo-update```

```brew: brew install cargo-update```

```nix: nix profile install nixpkgs#cargo-update```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cargo](/man/cargo)(1), [cargo-generate-lockfile](/man/cargo-generate-lockfile)(1)

# RESOURCES

```[Source code](https://github.com/rust-lang/cargo)```

```[Documentation](https://doc.rust-lang.org/cargo/commands/cargo-update.html)```

<!-- verified: 2026-06-22 -->
