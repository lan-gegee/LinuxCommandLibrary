# TAGLINE

在默认编辑器中打开 Jujutsu 配置文件

# TLDR

在编辑器中编辑用户配置

```jj config edit --user```

编辑仓库配置

```jj config edit --repo```

# SYNOPSIS

**jj** **config** **edit** [_options_]

# PARAMETERS

**--user**
> 编辑用户级配置。

**--repo**
> 编辑仓库级配置。

# DESCRIPTION

**jj config edit** 在默认编辑器中打开 Jujutsu 配置文件。用户配置全局生效，而仓库配置仅对当前仓库生效。配置使用 TOML 格式。

# INSTALL

```pacman: sudo pacman -S jujutsu```

```apk: sudo apk add jujutsu```

```zypper: sudo zypper install jujutsu```

```brew: brew install jujutsu```

```nix: nix profile install nixpkgs#jujutsu```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jj](/man/jj)(1), [jj-config-get](/man/jj-config-get)(1), [jj-config-set](/man/jj-config-set)(1)
