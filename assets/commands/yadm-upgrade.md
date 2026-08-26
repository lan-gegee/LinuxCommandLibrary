# TAGLINE

迁移 yadm 配置版本

# TLDR

**升级 yadm 配置**

```yadm upgrade```

# SYNOPSIS

**yadm** **upgrade**

# DESCRIPTION

**yadm upgrade** 将现有的 yadm 安装迁移到当前版本所使用的布局。具体而言，它会把 yadm 仓库和配置从旧式的 **~/.yadm** 目录迁移到符合 XDG 规范的位置，即 **$XDG_DATA_HOME/yadm** 和 **$XDG_CONFIG_HOME/yadm**（通常是 **~/.local/share/yadm** 与 **~/.config/yadm**）。

它还会规范化加密文件存储以及其他在 yadm 各版本间发生变化的磁盘布局。在升级 yadm 之后运行一次该命令，后续命令才能在预期的位置找到文件。

# CAVEATS

升级是一次性的、基本幂等的操作；对已升级过的仓库再次运行是安全的，但不会做任何事。在使用了自定义 yadm 钩子或特殊配置的系统上运行之前，请先备份你的 dotfiles 仓库。

# INSTALL

```pacman: sudo pacman -S yadm```

```apk: sudo apk add yadm```

```zypper: sudo zypper install yadm```

```brew: brew install yadm```

```nix: nix profile install nixpkgs#yadm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[yadm](/man/yadm)(1), [git](/man/git)(1)
