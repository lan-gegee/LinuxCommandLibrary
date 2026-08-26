# TAGLINE

交互式 Cargo 目标选择器

# TLDR

**交互式选择**并运行一个二进制目标

```cargo selector run```

**交互式选择**并运行一个测试

```cargo selector test```

**交互式选择**并运行一个基准测试

```cargo selector bench```

**交互式选择**并运行一个示例

```cargo selector example```

# SYNOPSIS

**cargo selector** _command_ [_options_]

# DESCRIPTION

**cargo-selector** 是一个 Cargo 子命令，提供交互式模糊搜索界面，用于在 Rust 项目中选择并运行目标。它不需要输入确切的目标名称，而是展示可用的二进制、测试、示例或基准测试的可搜索列表，并运行选中的那一项。

对于目标众多的大型工作空间或项目，记住确切的名称并不现实，此时尤为实用。该选择器使用模糊搜索界面实现快速过滤。

# CAVEATS

需要一个已定义目标的合法 Cargo 项目。对底层 cargo 命令的额外参数可能需要在选定目标之后再传入。

# INSTALL

```apt: sudo apt install cargo```

```dnf: sudo dnf install cargo```

```apk: sudo apk add cargo```

```zypper: sudo zypper install cargo```

```nix: nix profile install nixpkgs#cargo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cargo](/man/cargo)(1), [fzf](/man/fzf)(1)
