# TAGLINE

管理 Rust 工具链组件

# TLDR

**列出可用组件**

```rustup component list```

**添加组件**

```rustup component add [component]```

**添加 rust-src**

```rustup component add rust-src```

**移除组件**

```rustup component remove [component]```

# SYNOPSIS

**rustup** **component** _command_ [_options_]

# PARAMETERS

**list**
> 列出组件。

**add** _component_
> 安装组件。

**remove** _component_
> 卸载组件。

**--toolchain** _name_
> 指定目标工具链。

# DESCRIPTION

**rustup component** 管理 Rust 工具链组件。组件包括 rust-src、rustfmt、clippy 等。添加组件可获得额外的开发工具。

# INSTALL

```apt: sudo apt install rustup```

```dnf: sudo dnf install rustup```

```pacman: sudo pacman -S rustup```

```zypper: sudo zypper install rustup```

```brew: brew install rustup```

```nix: nix profile install nixpkgs#rustup```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rustup](/man/rustup)(1), [rustup-toolchain](/man/rustup-toolchain)(1)
