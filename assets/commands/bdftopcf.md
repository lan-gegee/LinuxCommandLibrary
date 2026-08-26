# TAGLINE

将 BDF 位图字体转换为 PCF 格式

# TLDR

**将 BDF 字体转换为 PCF**

```bdftopcf [font.bdf] > [font.pcf]```

**转换并指定输出文件**

```bdftopcf -o [font.pcf] [font.bdf]```

**创建终端字体**

```bdftopcf -t [font.bdf] > [font.pcf]```

**设置 MSB 在前的位序**

```bdftopcf -m [font.bdf] > [font.pcf]```

**设置字形填充**

```bdftopcf -p4 [font.bdf] > [font.pcf]```

# SYNOPSIS

**bdftopcf** [_options_] _fontfile.bdf_

# DESCRIPTION

**bdftopcf** 是一个 X11 字体编译器，用于将 Bitmap Distribution Format（BDF）字体转换为 Portable Compiled Format（PCF）。PCF 字体可被任何架构读取，同时在目标机器上能快速加载。

# PARAMETERS

**-o** _outputfile_
> 将输出写入文件而非标准输出

**-t**
> 创建字形尺寸统一的终端字体，以加快渲染速度

**-i**
> 不计算 ink metrics（着墨度量）

**-p**_n_
> 将字形填充设为 n 字节（1、2、4 或 8）

**-u**_n_
> 将扫描线单位设为 n 字节（1、2 或 4）

**-m**
> 将字体的位序设为 MSB 在前

**-l**
> 将字体的位序设为 LSB 在前

**-M**
> 将字体的字节序设为 MSB 在前

**-L**
> 将字体的字节序设为 LSB 在前

# CAVEATS

属于 X.Org 字体工具集。输出字体是可移植的，但在架构匹配的机器上读取更快。终端字体（-t）渲染更快，但要求字形尺寸统一。

# INSTALL

```apt: sudo apt install xfonts-utils```

```dnf: sudo dnf install bdftopcf```

```apk: sudo apk add bdftopcf```

```zypper: sudo zypper install bdftopcf```

```brew: brew install bdftopcf```

```nix: nix profile install nixpkgs#bdftopcf```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[xfontsel](/man/xfontsel)(1), [xlsfonts](/man/xlsfonts)(1), [fc-cache](/man/fc-cache)(1)
