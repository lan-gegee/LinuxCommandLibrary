# TAGLINE

用 Rust 编写的更快的实验性 Homebrew 替代品

# TLDR

**安装一个或多个软件包**

```zb install [ripgrep] [jq]```

**卸载软件包**

```zb uninstall [ripgrep]```

**从 Brewfile 安装软件包**

```zb bundle```

**将已安装的软件包导出到 Brewfile**

```zb bundle dump```

**运行软件包而不创建链接**

```zbx [jq] --version```

**垃圾回收未被引用的存储条目**

```zb gc```

**卸载所有软件包（重置）**

```zb reset```

# SYNOPSIS

**zb** _command_ [_options_]

**zbx** _package_ [_arguments_...]

# PARAMETERS

**install** _PACKAGE_...
> 安装一个或多个软件包。

**uninstall** _PACKAGE_...
> 删除软件包。

**bundle**
> 安装 Brewfile 中列出的软件包。

**bundle dump**
> 将已安装的软件包导出到 Brewfile。

**gc**
> 垃圾回收未使用的存储条目。

**reset**
> 卸载所有软件包。

**zbx**
> 运行软件包而不创建系统链接。

# DESCRIPTION

**zerobrew**（`zb`）是 Homebrew 的高性能重实现，使用内容寻址存储和 APFS clonefile 实现零开销复制，在 macOS 上安装速度比 Homebrew 快 5-20 倍。它复用 Homebrew 的 formula 定义和预构建的 bottle，为 Homebrew 软件包带来了 uv 风格的架构。

# CAVEATS

这是实验性软件；建议与 Homebrew 并行运行，而非完全取代。主要支持 bottle（预编译二进制），不支持源码构建。在采用 APFS clonefile 的 macOS 上性能最佳。

# HISTORY

**zerobrew** 由 **Lucas Gelfond**（lucasgelfond）创建，使用 **Rust** 编写。

# INSTALL

```aur: yay -S zerobrew```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[brew](/man/brew)(1), [nix](/man/nix)(1)
