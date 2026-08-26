# TAGLINE

升级 Cargo.toml 中的依赖版本

# TLDR

**将所有依赖升级**到最新的兼容版本

```cargo upgrade```

**升级指定** crate 到目标版本要求

```cargo upgrade -p [docopt@~0.9] -p [serde@>=0.9,<2.0]```

**升级所有但排除**列出的 crate

```cargo upgrade --exclude [docopt] --exclude [serde]```

**试运行**，不写入 Cargo.toml

```cargo upgrade -n```

**允许不兼容的**（破坏性）升级

```cargo upgrade --incompatible allow```

# SYNOPSIS

**cargo upgrade** [*options*]

# DESCRIPTION

**cargo upgrade**（来自 **cargo-edit** 项目）将 **Cargo.toml** 中的版本*要求*更新到更新的发行版。它与 **cargo update** 不同，后者只在现有要求范围内刷新 **Cargo.lock**。

使用 **cargo install cargo-edit** 安装。注意 **cargo add** 和 **cargo rm** 已集成进 Cargo 本身（分别为 1.62 和 1.66+）；**upgrade** 和 **set-version** 仍是 cargo-edit 的子命令。

# PARAMETERS

**-n**, **--dry-run**

> 打印计划的更改，而不修改清单文件。

**-p**, **--package** *PKGID[@VERSION]*

> 将升级限制在某个 crate，可附带目标版本要求。

**--exclude** *PKGID*

> 跳过某个 crate。

**--compatible** allow|ignore

> 是否在兼容版本范围内升级（默认 **allow**）。

**-i**, **--incompatible** allow|ignore

> 是否升级到最新的不兼容版本（默认 **ignore**）。

**--pinned** allow|ignore

> 是否将固定的版本要求升级到最新的不兼容版本（默认 **ignore**）。

**--manifest-path** *PATH*

> 要编辑的 Cargo.toml 的路径。

**--recursive** true|false

> 递归更新锁定的依赖。

**-v** / **-q**

> 增加 / 降低输出详细程度。

完整选项列表见 **cargo upgrade --help**。

# CAVEATS

不兼容的升级可能破坏构建；请检查差异并运行测试。除非适用离线标志，否则需要访问 crate 注册表的网络。工作区成员可能需要 **--manifest-path** 或包选择参数。

# INSTALL

```pacman: sudo pacman -S cargo-edit```

```apk: sudo apk add cargo-edit```

```brew: brew install cargo-edit```

```nix: nix profile install nixpkgs#cargo-edit```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cargo-add](/man/cargo-add)(1), [cargo-update](/man/cargo-update)(1), [cargo-set-version](/man/cargo-set-version)(1), [cargo](/man/cargo)(1)

# RESOURCES

```[Source code](https://github.com/killercup/cargo-edit)```

<!-- verified: 2026-07-19 -->
