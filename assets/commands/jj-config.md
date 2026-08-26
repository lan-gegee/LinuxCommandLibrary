# TAGLINE

管理 Jujutsu 配置

# TLDR

列出所有配置值

```jj config list```

读取特定配置值

```jj config get [user.name]```

设置配置值

```jj config set --user [key] "[value]"```

在编辑器中编辑配置

```jj config edit --user```

# SYNOPSIS

**jj** **config** _subcommand_ [_options_]

# PARAMETERS

**list**
> 列出配置值。

**get** _name_
> 读取一个配置值。

**set** _name_ _value_
> 设置一个配置值。

**unset** _name_
> 移除一个配置值。

**edit**
> 在编辑器中编辑配置。

**path**
> 显示配置文件路径。

# DESCRIPTION

**jj config** 管理 Jujutsu 配置。支持用户级配置（全局）和仓库级配置（每个仓库）。配置使用 TOML 格式，控制用户身份、别名和界面偏好等设置。

# INSTALL

```pacman: sudo pacman -S jujutsu```

```apk: sudo apk add jujutsu```

```zypper: sudo zypper install jujutsu```

```brew: brew install jujutsu```

```nix: nix profile install nixpkgs#jujutsu```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jj](/man/jj)(1), [jj-config-list](/man/jj-config-list)(1), [jj-config-set](/man/jj-config-set)(1)
