# TAGLINE

在 Jujutsu 配置文件中设置配置值

# TLDR

设置用户配置值

```jj config set --user [user.name] "[John Doe]"```

设置仓库配置值

```jj config set --repo [key] "[value]"```

设置用户邮箱

```jj config set --user user.email "[email@example.com]"```

# SYNOPSIS

**jj** **config** **set** [_options_] _name_ _value_

# PARAMETERS

**--user**
> 设置到用户配置。

**--repo**
> 设置到仓库配置。

# DESCRIPTION

**jj config set** 在 Jujutsu 配置文件中设置配置值。用户配置全局生效，而仓库配置仅对当前仓库生效。值以 TOML 格式存储。

# INSTALL

```pacman: sudo pacman -S jujutsu```

```apk: sudo apk add jujutsu```

```zypper: sudo zypper install jujutsu```

```brew: brew install jujutsu```

```nix: nix profile install nixpkgs#jujutsu```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jj](/man/jj)(1), [jj-config-get](/man/jj-config-get)(1), [jj-config-unset](/man/jj-config-unset)(1)
