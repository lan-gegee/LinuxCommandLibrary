# TAGLINE

显示 Jujutsu 配置文件的文件系统路径

# TLDR

显示用户配置路径

```jj config path --user```

显示仓库配置路径

```jj config path --repo```

# SYNOPSIS

**jj** **config** **path** [_options_]

# PARAMETERS

**--user**
> 显示用户级配置文件路径（通常为 ~/.config/jj/config.toml）。

**--repo**
> 显示仓库级配置文件路径（.jj/repo/config.toml）。

**--help**
> 显示帮助信息。

# DESCRIPTION

**jj config path** 显示 Jujutsu 配置文件的文件系统路径。适合在手动编辑、脚本处理或故障排查时定位配置文件。如果目标配置文件尚不存在，该命令仍会打印它将被创建的路径。

# CAVEATS

必须且只能指定 **--user** 或 **--repo** 之一。**--repo** 变体必须在 Jujutsu 仓库内运行。

# INSTALL

```pacman: sudo pacman -S jujutsu```

```apk: sudo apk add jujutsu```

```zypper: sudo zypper install jujutsu```

```brew: brew install jujutsu```

```nix: nix profile install nixpkgs#jujutsu```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jj](/man/jj)(1), [jj-config-edit](/man/jj-config-edit)(1)
