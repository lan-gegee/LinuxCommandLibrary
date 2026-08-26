# TAGLINE

以树状结构显示依赖图

# TLDR

**显示依赖树**

```cargo tree```

**显示某软件包的反向依赖树**

```cargo tree --invert [package]```

**显示重复的依赖**

```cargo tree --duplicates```

**显示由依赖启用的特性**

```cargo tree --edges features```

**显示时不做去重**

```cargo tree --no-dedupe```

**显示特定软件包的子树**

```cargo tree -p [package]```

**ASCII 输出**

```cargo tree --charset ascii```

# SYNOPSIS

**cargo tree** [_options_]

# DESCRIPTION

**cargo tree** 以树形可视化展示 Rust 项目的依赖图。它以缩进树的形式显示所有软件包及其传递依赖，标注 `(*)` 的软件包表示已在其他位置显示过、被去重处理。

该命令支持多种分析模式：`--invert` 用于追踪哪些软件包依赖某个给定的 crate，`--duplicates` 显示以不同版本多次出现的软件包，`--edges features` 则揭示特性如何在依赖图中传播。自 Rust 1.44 起内置于 Cargo，取代了早期的第三方插件 `cargo-tree`。

# PARAMETERS

**-i**, **--invert** _spec_
> 反转树，显示哪些包依赖于该软件包

**-p**, **--package** _spec_
> 作为树根的软件包

**-e**, **--edges** _kinds_
> 依赖类型：normal、dev、build、features、all

**-d**, **--duplicates**
> 显示被构建多次的软件包

**--no-dedupe**
> 不对重复出现的软件包去重

**--depth** _n_
> 最大显示深度

**--prune** _spec_
> 从显示中剪除指定软件包

**--charset** _set_
> 字符集：utf8、ascii

**--format** _fmt_
> 软件包显示格式字符串

**--prefix** _prefix_
> 前缀样式：indent、depth、none

**--target** _triple_
> 按目标平台过滤

**--all-features**
> 启用所有特性

**--features** _features_
> 启用指定特性

# OUTPUT SYMBOLS

**(*)** 该软件包已在其他位置显示过（已去重）

# CAVEATS

使用 --invert 可追踪某个依赖来自哪里。结合 --edges features 可了解特性的传播方式。

# INSTALL

```apt: sudo apt install cargo```

```dnf: sudo dnf install cargo```

```apk: sudo apk add cargo```

```zypper: sudo zypper install cargo```

```nix: nix profile install nixpkgs#cargo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cargo](/man/cargo)(1), [cargo-metadata](/man/cargo-metadata)(1)

# RESOURCES

```[Source code](https://github.com/rust-lang/cargo)```

```[Documentation](https://doc.rust-lang.org/cargo/commands/cargo-tree.html)```

<!-- verified: 2026-06-22 -->
