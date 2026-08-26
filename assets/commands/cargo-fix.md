# TAGLINE

自动修复 Rust 代码中的编译器警告

# TLDR

**修复所有警告**

```cargo fix```

**修复所有目标**

```cargo fix --all-targets```

**启用所有特性进行修复**

```cargo fix --all-features```

**迁移到新的 edition**

```cargo fix --edition```

**即使存在编译错误也进行修复**

```cargo fix --broken-code```

**允许脏的工作目录**

```cargo fix --allow-dirty```

**允许已暂存的更改**

```cargo fix --allow-staged```

**修复工作空间中的特定软件包**

```cargo fix -p [package_name]```

# SYNOPSIS

**cargo fix** [_options_]

# DESCRIPTION

**cargo fix** 自动将 rustc 建议的修复应用到源代码。它内部运行 **cargo check**，并应用诊断信息中可机器应用的修复建议。

# PARAMETERS

**--edition**
> 应用 edition 迁移所需的修复。

**--edition-idioms**
> 为当前 edition 应用特定惯用法更改。

**--broken-code**
> 即使存在编译错误也修复代码。可能留下损坏的代码供人工检查。

**--allow-dirty**
> 允许在脏的工作目录（包括已暂存的更改）上进行修复。

**--allow-staged**
> 允许在存在已暂存更改时进行修复。

**--allow-no-vcs**
> 即使未检测到版本控制系统也允许修复。

**--all-targets**
> 修复所有目标（lib、bins、tests、benches、examples）。

**--all-features**
> 启用所有可用特性。

**--no-default-features**
> 不启用默认特性。

**-F**, **--features** _features_
> 要启用的特性列表，以空格或逗号分隔。

**--lib**
> 只修复库。

**--bins**
> 修复所有二进制文件。

**--tests**
> 修复所有测试目标。

**--benches**
> 修复所有基准测试目标。

**--examples**
> 修复所有示例目标。

**-p**, **--package** _spec_
> 修复指定的软件包。

**--workspace**
> 修复所有工作空间成员。

**--exclude** _spec_
> 排除指定软件包（需要 **--workspace**）。

**--target** _triple_
> 为指定的目标架构进行修复。

**-j**, **--jobs** _N_
> 并行任务数。

# EDITION MIGRATION

```cargo fix --edition```

将代码从一个 Rust edition 迁移到下一个（例如从 2021 到 2024）。运行后需手动更新 **Cargo.toml** 中的 **edition** 字段。

# CAVEATS

只能修复正常编译的代码。条件编译的代码需要相应的 **--features** 或 **--target** 选项。自 Rust 1.29 起内置于 Cargo。默认要求干净的 VCS 状态；可使用 **--allow-dirty** 或 **--allow-staged** 覆盖此限制。

# INSTALL

```apt: sudo apt install cargo```

```dnf: sudo dnf install cargo```

```apk: sudo apk add cargo```

```zypper: sudo zypper install cargo```

```nix: nix profile install nixpkgs#cargo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cargo](/man/cargo)(1), [cargo-check](/man/cargo-check)(1), [cargo-clippy](/man/cargo-clippy)(1), [cargo-build](/man/cargo-build)(1)
