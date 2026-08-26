# TAGLINE

显示构建报告和诊断信息

# TLDR

**显示未来不兼容性报告**

```cargo report future-incompatibilities --id [1]```

**构建后显示报告**

```cargo build --future-incompat-report```

# SYNOPSIS

**cargo report** _type_ [_options_]

# DESCRIPTION

**cargo report** 生成关于项目的诊断报告。目前其主要子命令是 `future-incompatibilities`，用于显示依赖中将在未来 Rust 版本中被拒绝的代码模式相关的警告。

当 Cargo 在构建期间检测到未来不兼容警告时，会保存一份报告并显示通知，提示如何查看完整详情。这些警告表明某些代码模式可能表现出未定义行为、已被安排从 Rust 中移除，或缺乏明确定义的语义。查看这些报告有助于维护者在破坏性变更落地之前主动更新依赖。

# SUBCOMMANDS

**future-incompatibilities**
> 显示未来不兼容性报告

# PARAMETERS

**--id** _id_
> 之前构建的报告 ID

**--package** _spec_
> 要报告的软件包

**-v**, **--verbose**
> 详细输出

**-q**, **--quiet**
> 抑制输出

# FUTURE INCOMPATIBILITIES

Cargo 会检查依赖中是否存在以下模式：
- 可能表现出未定义行为
- 已被安排从 Rust 中移除
- 缺乏明确定义的语义

一旦检测到，构建结束后会出现一条警告，提示如何查看完整报告。

# CONFIGURATION

**.cargo/config.toml**
> 通过 `[future-incompat-report]` 区块控制报告频率（例如 `frequency = "always"`）。

# RESOLVING ISSUES

1. 将依赖更新为已修复的版本
2. 与依赖的维护者协作
3. 若已无人维护则考虑替代方案

# CAVEATS

该报告不是 lint，也不与 -Dwarnings 交互。这些警告不会使构建失败，但预示着未来会出现问题。

# INSTALL

```apt: sudo apt install cargo```

```dnf: sudo dnf install cargo```

```apk: sudo apk add cargo```

```zypper: sudo zypper install cargo```

```nix: nix profile install nixpkgs#cargo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cargo](/man/cargo)(1), [cargo-build](/man/cargo-build)(1)

# RESOURCES

```[Source code](https://github.com/rust-lang/cargo)```

```[Documentation](https://doc.rust-lang.org/cargo/commands/cargo-report.html)```

<!-- verified: 2026-06-22 -->
