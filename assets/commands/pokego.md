# TAGLINE

在终端中显示宝可梦 ASCII 艺术

# TLDR

打印特定的 **Pokémon**

```pokego --name [charizard]```

打印 **异色** 变种

```pokego --name [spheal] -s```

打印 **替代形态**

```pokego --name [blastoise] --form mega```

从第 1-3 世代中打印 **随机** 宝可梦

```pokego --random 1-3```

打印时不带 **名称标题**

```pokego --random 1-3 --no-title```

# SYNOPSIS

**pokego** [**--name** _pokemon_] [**--random** _range_] [**-s**|**--shiny**] [**--form** _form_] [**--no-title**]

# PARAMETERS

**--name _pokemon_**
> 按名称显示特定的 Pokémon

**--random _range_**
> 在指定世代范围内随机显示 Pokémon

**-s, --shiny**
> 显示异色变种

**--form _form_**
> 显示替代形态（mega、gmax 等）

**--no-title**
> 不显示 Pokémon 名称

# DESCRIPTION

**pokego** 在终端中以彩色 ASCII 艺术的形式显示宝可梦像素图。它是一个有趣的小工具，可用于自定义终端提示符或为 shell 会话增添个性。

该工具包含所有宝可梦的像素图，包括地区形态、超级进化和异色变种。它用 Go 编写，性能出色。

# CAVEATS

需要支持颜色的终端。深色背景下效果最佳。像素图质量取决于终端字体。过大的像素图在小尺寸终端中可能显示不佳。

# HISTORY

**pokego** 由 **rubiin** 创建，作为 pokemon-colorscripts 的更快替代品。它使用 Go 编写，在保持终端显示宝可梦乐趣的同时提供了更好的性能。

# SEE ALSO

[neofetch](/man/neofetch)(1), [fastfetch](/man/fastfetch)(1), [cowsay](/man/cowsay)(1)
