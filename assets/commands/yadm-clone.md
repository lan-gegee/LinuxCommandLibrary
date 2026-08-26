# TAGLINE

用 yadm 克隆 dotfiles 仓库

# TLDR

**克隆 dotfiles 仓库**

```yadm clone [url]```

**克隆并运行引导程序**

```yadm clone --bootstrap [url]```

**克隆但不检出文件**

```yadm clone --no-checkout [url]```

# SYNOPSIS

**yadm** **clone** [_options_] _url_

# PARAMETERS

**--bootstrap**
> 克隆后运行引导程序。

**--no-checkout**
> 克隆但不检出文件。

**-f**, **--force**
> 强制覆盖已有文件。

**-w** _dir_
> 设置工作树目录。

# DESCRIPTION

**yadm clone** 克隆一个 dotfiles 仓库并交由 yadm 管理。它会下载仓库并将文件检出到主目录。这是在新系统上配置 dotfiles 的第一步。

# INSTALL

```pacman: sudo pacman -S yadm```

```apk: sudo apk add yadm```

```zypper: sudo zypper install yadm```

```brew: brew install yadm```

```nix: nix profile install nixpkgs#yadm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[yadm](/man/yadm)(1), [yadm-bootstrap](/man/yadm-bootstrap)(1)
