# TAGLINE

使用 rustfmt 格式化 Rust 源代码

# TLDR

**格式化当前软件包**

```cargo fmt```

**格式化工作空间中的所有软件包**

```cargo fmt --all```

**只检查格式而不修改**

```cargo fmt --check```

**格式化指定软件包**

```cargo fmt -p [package]```

**显示更改的 diff**

```cargo fmt -- --emit diff```

**以详细输出格式化**

```cargo fmt --verbose```

# SYNOPSIS

**cargo fmt** [_options_] [-- _rustfmt_options_]

# DESCRIPTION

**cargo fmt** 使用 rustfmt 格式化当前 crate 的所有 bin 和 lib 文件。会格式化 src/、tests/、examples/ 以及集成测试中的 .rs 文件。默认直接原地重新排版代码。

# PARAMETERS

**--all**
> 格式化工作空间中的所有软件包

**--check**
> 检查格式但不修改文件（用于 CI）

**-p**, **--package** _name_
> 格式化指定软件包

**--manifest-path** _path_
> Cargo.toml 的路径

**-v**, **--verbose**
> 详细输出

**-q**, **--quiet**
> 抑制输出

**-- --emit** _mode_
> 输出模式：files、stdout、diff

**-- --edition** _year_
> 覆盖 Rust edition

# CONFIGURATION

**rustfmt.toml** 或 **.rustfmt.toml**
> 项目级的 rustfmt 配置，涵盖 max_width、tab_spaces、edition 等选项。

# CAVEATS

edition 会自动从 Cargo.toml 读取。直接调用 rustfmt 时默认为 2015 edition。为保持一致，请在配置中设置 style_edition。

# INSTALL

```apt: sudo apt install rustup```

```dnf: sudo dnf install rustup```

```pacman: sudo pacman -S rustup```

```apk: sudo apk add rustfmt```

```zypper: sudo zypper install rustup```

```brew: brew install rustup```

```nix: nix profile install nixpkgs#rustup```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cargo](/man/cargo)(1), [rustfmt](/man/rustfmt)(1), [cargo-clippy](/man/cargo-clippy)(1)
