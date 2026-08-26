# TAGLINE

GitHub Actions 安全静态分析工具

# TLDR

**审计当前目录中的所有 GitHub Actions**

```zizmor .```

**以 SARIF 格式输出**

```zizmor --format sarif [.github/workflows/]```

**完全离线运行**

```zizmor --offline .```

# SYNOPSIS

**zizmor** [_options_] [_path_]

# DESCRIPTION

**zizmor** 审计 GitHub Actions YAML 文件的安全问题，包括模板注入漏洞、可变标签固定以及已知安全公告的使用。它拥有约 24 条审计规则，可生成用于 GitHub code scanning 集成的 SARIF 输出，并且默认支持离线模式。

# HISTORY

**zizmor** 由 **William Woodruff**（Trail of Bits）创建，使用 **Rust** 编写。

# INSTALL

```pacman: sudo pacman -S zizmor```

```apk: sudo apk add zizmor```

```zypper: sudo zypper install zizmor```

```brew: brew install zizmor```

```nix: nix profile install nixpkgs#zizmor```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[semgrep](/man/semgrep)(1)
