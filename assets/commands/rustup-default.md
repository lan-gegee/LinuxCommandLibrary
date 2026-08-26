# TAGLINE

设置默认的 Rust 工具链

# TLDR

**设置默认工具链**

```rustup default stable```

**将 nightly 设为默认**

```rustup default nightly```

**设置特定版本**

```rustup default [1.70.0]```

**显示当前默认值**

```rustup default```

# SYNOPSIS

**rustup** **default** [_toolchain_]

# PARAMETERS

_toolchain_
> 工具链名称：**stable**、**beta**、**nightly** 或诸如 **1.70.0** 的特定版本。可以包含目标三元组（例如 `nightly-x86_64-unknown-linux-gnu`）。

# DESCRIPTION

**rustup default** 设置或显示默认的 Rust 工具链。当没有生效的覆盖配置（通过 `rustup override` 或 `rust-toolchain.toml`）时，就会使用默认工具链。常见选择是 stable、beta 或 nightly。如果指定的工具链尚未安装，rustup 会自动下载并安装它。

# CAVEATS

项目级覆盖配置（来自 `rust-toolchain.toml` 或 `rustup override`）优先于默认工具链。更改默认值不会影响设置了覆盖配置的项目。

# INSTALL

```apt: sudo apt install rustup```

```dnf: sudo dnf install rustup```

```pacman: sudo pacman -S rustup```

```zypper: sudo zypper install rustup```

```brew: brew install rustup```

```nix: nix profile install nixpkgs#rustup```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rustup](/man/rustup)(1), [rustup-toolchain](/man/rustup-toolchain)(1), [rustup-override](/man/rustup-override)(1)
