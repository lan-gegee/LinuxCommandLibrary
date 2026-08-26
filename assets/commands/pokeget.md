# TAGLINE

在终端中显示宝可梦像素图

# TLDR

**显示宝可梦像素图**

```pokeget [pokemon_name]```

**按编号显示**

```pokeget [number]```

**显示异色版本**

```pokeget [pokemon] --shiny```

**显示特定形态**

```pokeget [pokemon] --form [form]```

# SYNOPSIS

**pokeget** [_options_] _pokemon_

# PARAMETERS

_POKEMON_
> 宝可梦名称或编号。

**--shiny**
> 显示异色变种。

**--form** _FORM_
> 特定形态名称。

**--big**
> 大尺寸像素图。

# DESCRIPTION

**pokeget** 在终端中以彩色 ASCII 艺术的形式显示宝可梦像素图。可以通过名称或图鉴编号指定宝可梦。像素图从 PokeAPI 获取。

**--shiny** 标志显示异色变种，**--form** 显示替代形态（超级进化、地区形态），**--big** 渲染更大的像素图。常用于自定义终端启动画面。

# CAVEATS

需要支持颜色的终端。获取像素图需要联网。

# HISTORY

pokeget 为在终端中**显示宝可梦**像素图而创建。

# INSTALL

```aur: yay -S pokeget```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pokemon-colorscripts](/man/pokemon-colorscripts)(1)
