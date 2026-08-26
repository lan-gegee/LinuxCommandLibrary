# TAGLINE

管理 Jujutsu 仓库的 Git 远程

# TLDR

添加远程

```jj git remote add [name] [url]```

列出远程

```jj git remote list```

移除远程

```jj git remote remove [name]```

重命名远程

```jj git remote rename [old] [new]```

# SYNOPSIS

**jj git remote** _subcommand_ [_options_]

# PARAMETERS

**add** _NAME_ _URL_
> 添加新远程。

**list**
> 列出已配置的远程。

**remove** _NAME_
> 移除远程。

**rename** _OLD_ _NEW_
> 重命名远程。

**--help**
> 显示帮助信息。

# DESCRIPTION

**jj git remote** 管理 Jujutsu 仓库的 Git 远程。它配置抓取和推送变更的位置。

这些命令与 Git 远程管理一致。更改以 Git 格式存储以保持兼容性。

# CAVEATS

jj 的子命令。使用 Git 远程格式。标准的 Git 托管服务均可使用。

# HISTORY

jj git remote 是 **Jujutsu** 的一部分，提供与 Git 基础设施兼容的远程管理。

# INSTALL

```pacman: sudo pacman -S jujutsu```

```apk: sudo apk add jujutsu```

```zypper: sudo zypper install jujutsu```

```brew: brew install jujutsu```

```nix: nix profile install nixpkgs#jujutsu```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jj](/man/jj)(1), [jj-git](/man/jj-git)(1), [git-remote](/man/git-remote)(1)
