# TAGLINE

卸载由 cargo install 安装的 Rust 二进制文件

# TLDR

**卸载软件包**

```cargo uninstall [package]```

**卸载指定的二进制文件**

```cargo uninstall [package] --bin [binary]```

**从自定义根目录卸载**

```cargo uninstall [package] --root [~/.local]```

**卸载多个软件包**

```cargo uninstall [pkg1] [pkg2]```

# SYNOPSIS

**cargo uninstall** [_options_] [_spec_...]

# DESCRIPTION

**cargo uninstall** 移除之前通过 `cargo install` 安装的软件包。默认会移除与该软件包关联的所有二进制文件。`--bin` 标志可用于只移除某个特定的二进制文件，同时保留同一软件包的其他文件。

安装根目录由 `--root` 标志、`CARGO_INSTALL_ROOT` 环境变量、`install.root` 配置项或 `$CARGO_HOME`（默认为 `~/.cargo`）决定。此命令只移除已安装的二进制文件；target 目录中缓存的构建产物不会被清理。

# PARAMETERS

**-p**, **--package** _spec_
> 要卸载的软件包

**--bin** _name_
> 只卸载指定的二进制文件

**--example** _name_
> 只卸载指定的示例

**--root** _dir_
> 要从中卸载的目录

**-v**, **--verbose**
> 详细输出（指定两次可获得非常详细的输出）

**-q**, **--quiet**
> 抑制输出

**--color** _when_
> 控制彩色输出：auto、always 或 never

# INSTALLATION ROOT

按以下顺序确定：
1. --root 选项
2. CARGO_INSTALL_ROOT 环境变量
3. install.root 配置项
4. CARGO_HOME 环境变量
5. ~/.cargo

# CAVEATS

只移除二进制文件，不清理缓存的构建产物。软件包标识可以是名称或 name@version。

# INSTALL

```apt: sudo apt install cargo```

```dnf: sudo dnf install cargo```

```apk: sudo apk add cargo```

```zypper: sudo zypper install cargo```

```nix: nix profile install nixpkgs#cargo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cargo](/man/cargo)(1), [cargo-install](/man/cargo-install)(1)
