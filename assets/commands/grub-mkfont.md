# TAGLINE

将字体转换为 GRUB PF2 格式

# TLDR

**将字体转换为 GRUB 格式**

```grub-mkfont -o [output.pf2] [input.ttf]```

**指定字号**

```grub-mkfont -s [16] -o [font16.pf2] [input.ttf]```

**包含特定字符**

```grub-mkfont --range=[0x0-0xff] -o [font.pf2] [input.ttf]```

**转换时输出详细信息**

```grub-mkfont -v -o [output.pf2] [input.ttf]```

# SYNOPSIS

**grub-mkfont** [_options_] _font-file_

# PARAMETERS

_FONT-FILE_
> 输入字体（TTF、OTF、PF2）。

**-o**, **--output** _FILE_
> 输出的 PF2 文件。

**-s**, **--size** _N_
> 以像素为单位的字号。

**-i**, **--index** _N_
> TTC 字体的 face 索引。

**-n**, **--name** _NAME_
> 设置字体家族名称。

**-b**, **--bold**
> 转换为粗体字体。

**-r**, **--range** _FROM-TO_
> 要包含的 Unicode 范围（逗号分隔）。

**-v**, **--verbose**
> 详细输出。

**--help**
> 显示帮助信息。

# DESCRIPTION

**grub-mkfont** 将字体转换为 GRUB 的 PF2 位图格式，从而在 GRUB 启动菜单中使用自定义字体。该工具接受 TrueType、OpenType 及其他字体格式。

它可以按指定字号和字符范围生成字体，精细控制输出中包含哪些字形。

# CAVEATS

属于 GRUB 软件包的一部分。字体越大，启动时间越长。仅限位图转换。

# HISTORY

grub-mkfont 作为 **GNU GRUB 2** 的一部分开发，用于支持带有自定义字体的图形化启动菜单。

# INSTALL

```apt: sudo apt install grub-common```

```apk: sudo apk add grub-mkfont```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[grub](/man/grub)(8), [grub-mkconfig](/man/grub-mkconfig)(8), [fc-list](/man/fc-list)(1)

# RESOURCES

```[Homepage](https://www.gnu.org/software/grub/)```

```[Source code](https://git.savannah.gnu.org/cgit/grub.git)```

```[Documentation](https://www.gnu.org/software/grub/manual/grub/grub.html)```

<!-- verified: 2026-07-17 -->
