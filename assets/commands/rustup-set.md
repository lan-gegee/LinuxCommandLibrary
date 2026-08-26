# TAGLINE

配置 rustup 设置与默认值

# TLDR

**设置默认主机三元组**

```rustup set default-host [x86_64-unknown-linux-gnu]```

**将安装 profile 设为 minimal**

```rustup set profile minimal```

**将安装 profile 设为 default**（包含 rustfmt 和 clippy）

```rustup set profile default```

**启用自动自我更新**

```rustup set auto-self-update enable```

**禁用自动自我更新**

```rustup set auto-self-update disable```

# SYNOPSIS

**rustup** **set** _setting_ _value_

# SUBCOMMANDS

**default-host** _triple_
> 设置工具链安装的默认主机三元组（例如 x86_64-unknown-linux-gnu）。

**profile** _name_
> 设置默认的组件安装 profile。**minimal** 仅包含 rustc、rust-std 和 cargo；**default** 额外添加 rust-docs、rustfmt 和 clippy；**complete** 安装所有可用组件。

**auto-self-update** _mode_
> 控制 rustup 的自动自我更新行为：**enable**、**disable** 或 **check-only**。

# DESCRIPTION

**rustup set** 配置影响新工具链安装和更新默认行为的 rustup 设置。profile 设置控制默认安装哪些组件，auto-self-update 设置控制运行 `rustup update` 时 rustup 是否更新自身。

# INSTALL

```apt: sudo apt install rustup```

```dnf: sudo dnf install rustup```

```pacman: sudo pacman -S rustup```

```zypper: sudo zypper install rustup```

```brew: brew install rustup```

```nix: nix profile install nixpkgs#rustup```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rustup](/man/rustup)(1), [rustup-show](/man/rustup-show)(1)
