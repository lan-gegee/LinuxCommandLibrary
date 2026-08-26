# TAGLINE

从 Jujutsu 配置文件中移除配置值

# TLDR

移除用户配置值

```jj config unset --user [key]```

移除仓库配置值

```jj config unset --repo [key]```

# SYNOPSIS

**jj** **config** **unset** [_options_] _name_

# PARAMETERS

**--user**
> 从用户配置中移除。

**--repo**
> 从仓库配置中移除。

# DESCRIPTION

**jj config unset** 从 Jujutsu 配置文件中移除配置值。该值会从指定的配置文件中删除，让默认值或更低优先级的配置得以生效。

# INSTALL

```pacman: sudo pacman -S jujutsu```

```apk: sudo apk add jujutsu```

```zypper: sudo zypper install jujutsu```

```brew: brew install jujutsu```

```nix: nix profile install nixpkgs#jujutsu```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jj](/man/jj)(1), [jj-config-set](/man/jj-config-set)(1)
