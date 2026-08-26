# TAGLINE

显示所有 Jujutsu 配置值

# TLDR

列出所有配置值

```jj config list```

仅列出用户配置

```jj config list --user```

仅列出仓库配置

```jj config list --repo```

列出配置来源并包含被覆盖的值

```jj config list --include-overridden```

列出时包含默认值

```jj config list --include-defaults```

仅列出工作区级配置

```jj config list --workspace```

使用自定义模板列出值

```jj config list -T [template]```

# SYNOPSIS

**jj** **config** **list** [_options_]

# PARAMETERS

**--user**
> 仅显示用户配置。

**--repo**
> 仅显示仓库配置。

**--workspace**
> 仅显示工作区配置。

**--include-overridden**
> 包含被更高优先级配置覆盖的值。

**--include-defaults**
> 在输出中包含默认值。

**-T**, **--template** _TEMPLATE_
> 使用自定义模板渲染输出。

# DESCRIPTION

**jj config list** 显示所有 Jujutsu 配置值。默认显示来自所有来源（用户、仓库、工作区）合并后的配置。适合调试配置问题以及了解实际生效的设置。

可用的模板字段：**name**（配置名）、**value**（TOML 值）、**overridden**（布尔值）、**source**（来源）、**path**（配置文件路径）。

# INSTALL

```pacman: sudo pacman -S jujutsu```

```apk: sudo apk add jujutsu```

```zypper: sudo zypper install jujutsu```

```brew: brew install jujutsu```

```nix: nix profile install nixpkgs#jujutsu```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jj](/man/jj)(1), [jj-config-get](/man/jj-config-get)(1), [jj-config-set](/man/jj-config-set)(1), [jj-config-edit](/man/jj-config-edit)(1)
