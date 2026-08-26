# TAGLINE

让终端下起雪来

# TLDR

**创建落雪动画**

```snowmachine snow```

**彩虹色并在底部堆积的雪**

```snowmachine snow --stack=pile --color=rainbow```

**渲染带经典星星的圣诞树**

```snowmachine tree --star=classic```

**减慢落雪速度**（数值越小越慢）

```snowmachine snow --speed=[20]```

**使用指定的粒子字符**

```snowmachine snow --particle="[*]"```

# SYNOPSIS

**snowmachine** _command_ [_options_]

# COMMANDS

**snow**
> 渲染落雪。

**tree**
> 渲染圣诞树。

# PARAMETERS

**--color** _NAME_
> 粒子颜色：_white_、_rainbow_ 等。

**--stack** _MODE_
> 在底部堆积粒子：_pile_ 会保留不断增高的积雪；默认不堆积。

**--speed** _N_
> 帧间隔（越小越快）。

**--particle** _CHAR_
> 覆盖雪花字符。

**--star** _STYLE_
> 树顶的星星（如 _classic_）。

# DESCRIPTION

**snowmachine** 是一个 Python 脚本，可在终端中渲染动态落雪或圣诞树动画。它支持自定义粒子颜色、积雪效果、速度调节，以及树模式下的星星装饰。

# HISTORY

**snowmachine** 由 **John Anderson**（sontek）创建，使用 **Python** 编写。

# INSTALL

```nix: nix profile install nixpkgs#snowmachine```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cmatrix](/man/cmatrix)(1), [asciiquarium](/man/asciiquarium)(1), [terminaltexteffects](/man/terminaltexteffects)(1)
