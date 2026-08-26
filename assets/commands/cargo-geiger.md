# TAGLINE

检测依赖树中不安全的 Rust 代码

# TLDR

**扫描**当前项目中的不安全代码

```cargo geiger```

**以 JSON 格式输出**

```cargo geiger --output-format json```

**只包含构建依赖**

```cargo geiger --build-dependencies```

**不启用默认特性进行扫描**

```cargo geiger --no-default-features```

# SYNOPSIS

**cargo geiger** [_options_]

# PARAMETERS

**--all-dependencies**
> 在扫描中包含所有依赖。

**--build-dependencies**
> 包含构建依赖。

**--dev-dependencies**
> 包含开发依赖。

**--output-format** _FORMAT_
> 输出格式：ascii-tree（默认）或 json。

**--no-default-features**
> 不启用默认特性。

**--features** _FEATURES_
> 要启用的特性列表，以空格或逗号分隔。

**--update-readme**
> 更新项目 README 中的安全报告。

**--forbid-only**
> 只报告未使用 `#![forbid(unsafe_code)]` 的 crate。

# DESCRIPTION

**cargo-geiger** 是一个 Cargo 子命令，用于扫描 Rust 项目的依赖树，检测并报告 **unsafe** Rust 代码的使用情况。它会统计项目及其全部依赖中的 unsafe 表达式、函数声明、trait 实现和方法调用。

输出以树状视图展示依赖图，并标注 unsafe 代码使用计数，帮助开发者评估其依赖链的安全状况。使用了 `#![forbid(unsafe_code)]` 的 crate 会被明确标记为已验证安全。

这个名字是对**盖革计数器（Geiger counter）**的致敬——盖革计数器探测辐射，而 cargo-geiger 探测潜在危险的 unsafe 代码。

# CAVEATS

分析基于源码级检测，可能无法捕获所有形式的不安全行为（例如隐藏在宏背后或在构建时生成的 unsafe 代码）。大型依赖树的分析可能耗时较长。需要所有依赖的源代码可用。

# HISTORY

**cargo-geiger** 由 **Anders Kaseorg** 和 Rust 社区创建，是一款安全审计工具。它针对的问题是：Rust 的安全性保证仅对安全代码成立，依赖中的 unsafe 块可能破坏整个应用的安全性。

# INSTALL

```pacman: sudo pacman -S cargo-geiger```

```brew: brew install cargo-geiger```

```nix: nix profile install nixpkgs#cargo-geiger```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cargo](/man/cargo)(1)
