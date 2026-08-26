# TAGLINE

动画 ASCII 盆景树生成器

# TLDR

**生成随机盆景树**

```cbonsai```

**实时动画模式**

```cbonsai --live```

**屏幕保护模式**

```cbonsai --screensaver```

**无限模式**

```cbonsai --infinite```

**添加消息**

```cbonsai -m "[Your message]"```

**设置动画速度**（实时模式下每步的秒数）

```cbonsai -l -t [0.05]```

**自定义叶子字符**

```cbonsai -c "[&,*,o]"```

# SYNOPSIS

**cbonsai** [_options_]

# DESCRIPTION

**cbonsai** 在终端中生成以程序化方式创建的 ASCII 艺术盆景树。每次运行都会使用随机生长算法生成一棵独一无二的树，也可以指定种子值以便复现。

该工具支持树木生长的实时动画、持续重新生成树木的无限模式，以及屏幕保护模式。它使用 C 语言和 ncurses 编写，支持自定义叶子字符、颜色、植株底座，以及显示在树旁的消息。

# PARAMETERS

**-l**, **--live**
> 实时模式：显示生长的每一步

**-t** _TIME_, **--time** _TIME_
> 实时模式下两次生长步骤之间的秒数（默认 0.03）

**-i**, **--infinite**
> 无限模式：不断生成新的树木

**-w** _TIME_, **--wait** _TIME_
> 无限模式下每棵树之间的间隔秒数（默认 4.00）

**-S**, **--screensaver**
> 屏幕保护模式；等价于 -liWC，按任意键退出

**-m** _MSG_, **--message** _MSG_
> 在树旁附加一条消息

**-b** _N_, **--base** _N_
> 要使用的 ASCII 艺术植株底座；0 表示无

**-c** _LIST_, **--leaf** _LIST_
> 用于随机选取叶子的逗号分隔字符串（默认 &）

**-M** _MULT_, **--multiplier** _MULT_
> 分支倍率（0-20；默认 5）

**-L** _LIFE_, **--life** _LIFE_
> 初始生命值（0-200；默认 32）

**-s** _SEED_, **--seed** _SEED_
> 为随机数生成器设定种子

**-W** _FILE_, **--save** _FILE_
> 将进度保存到文件（默认 ~/.cache/cbonsai）

**-C** _FILE_, **--load** _FILE_
> 从文件加载进度

**-p**, **--print**
> 完成后将树打印到终端

**-v**, **--verbose**
> 增加输出详细程度

# CAVEATS

需要 ncurses 库。颜色支持取决于终端能力。

# INSTALL

```dnf: sudo dnf install cbonsai```

```apk: sudo apk add cbonsai```

```zypper: sudo zypper install cbonsai```

```brew: brew install cbonsai```

```nix: nix profile install nixpkgs#cbonsai```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cmatrix](/man/cmatrix)(1), [sl](/man/sl)(1), [cowsay](/man/cowsay)(1)
