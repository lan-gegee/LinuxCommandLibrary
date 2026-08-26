# TAGLINE

在终端中显示宝可梦 ANSI 艺术

# TLDR

**显示随机宝可梦**

```pokemon-colorscripts -r```

**显示特定宝可梦**

```pokemon-colorscripts -n [pikachu]```

**带名称显示**

```pokemon-colorscripts -r --no-title```

**异色变种**

```pokemon-colorscripts -n [charizard] -s```

**列出所有宝可梦**

```pokemon-colorscripts -l```

# SYNOPSIS

**pokemon-colorscripts** [_options_]

# PARAMETERS

**-n**, **--name** _name_
> 显示特定宝可梦。

**-r**, **--random**
> 显示随机宝可梦。

**-l**, **--list**
> 列出所有宝可梦。

**-s**, **--shiny**
> 显示异色变种。

**--no-title**
> 隐藏宝可梦名称。

**-f**, **--form** _form_
> 特定形态。

# DESCRIPTION

**pokemon-colorscripts** 在终端中以 ASCII/ANSI 艺术的形式显示宝可梦。它可以显示随机宝可梦、按名称显示特定宝可梦，以及显示异色变种。

常用于 shell 启动时的装饰。

# EXAMPLES

```bash
# Random Pokemon
pokemon-colorscripts -r

# Specific Pokemon
pokemon-colorscripts -n pikachu

# Shiny Mewtwo
pokemon-colorscripts -n mewtwo -s

# Random without name
pokemon-colorscripts -r --no-title

# In .bashrc or .zshrc
pokemon-colorscripts -r
```

# SHELL INTEGRATION

```bash
# Add to ~/.bashrc or ~/.zshrc
pokemon-colorscripts -r

# Or with specific Pokemon
pokemon-colorscripts -n eevee
```

# CAVEATS

需要支持 Unicode/ANSI 的终端。颜色准确性取决于终端。第 1-8 世代的覆盖情况不一。

# HISTORY

pokemon-colorscripts 由 **phoney badger** 创作，是一款有趣的终端装饰工具，灵感来自 ASCII 艺术传统。

# INSTALL

```nix: nix profile install nixpkgs#pokemon-colorscripts```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[neofetch](/man/neofetch)(1), [cowsay](/man/cowsay)(1), [lolcat](/man/lolcat)(1)
