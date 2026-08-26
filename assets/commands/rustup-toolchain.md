# TAGLINE

管理已安装的 Rust 工具链

# TLDR

**列出工具链**

```rustup toolchain list```

**安装工具链**

```rustup toolchain install stable```

**卸载工具链**

```rustup toolchain uninstall nightly```

**链接自定义工具链**

```rustup toolchain link [name] [path]```

# SYNOPSIS

**rustup** **toolchain** _command_ [_options_]

# PARAMETERS

**list**
> 列出已安装的工具链。

**install** _name_
> 安装工具链。

**uninstall** _name_
> 移除工具链。

**link** _name_ _path_
> 链接自定义工具链。

**--profile** _name_
> 安装 profile。

# DESCRIPTION

**rustup toolchain** 管理 Rust 工具链，可以安装、移除和列出工具链。支持 stable、beta、nightly 和特定版本。还可以链接自行构建的工具链。

# INSTALL

```apt: sudo apt install rustup```

```dnf: sudo dnf install rustup```

```pacman: sudo pacman -S rustup```

```zypper: sudo zypper install rustup```

```brew: brew install rustup```

```nix: nix profile install nixpkgs#rustup```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rustup](/man/rustup)(1), [rustup-default](/man/rustup-default)(1)
