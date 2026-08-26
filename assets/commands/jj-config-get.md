# TAGLINE

从 Jujutsu 配置文件中读取配置值

# TLDR

读取一个配置值

```jj config get [user.name]```

读取用户的邮箱

```jj config get [user.email]```

# SYNOPSIS

**jj** **config** **get** _name_

# DESCRIPTION

**jj config get** 从 Jujutsu 配置文件中读取单个配置值。输出不带任何额外格式，适合在脚本中使用。当用户配置和仓库配置定义了相同的键时，仓库配置优先。

与 `jj config list` 不同，该命令只输出原始值，不带标签或引号。

# INSTALL

```pacman: sudo pacman -S jujutsu```

```apk: sudo apk add jujutsu```

```zypper: sudo zypper install jujutsu```

```brew: brew install jujutsu```

```nix: nix profile install nixpkgs#jujutsu```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jj](/man/jj)(1), [jj-config-set](/man/jj-config-set)(1), [jj-config-list](/man/jj-config-list)(1)
