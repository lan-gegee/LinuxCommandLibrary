# TAGLINE

显示纸张尺寸信息

# TLDR

**显示默认纸张尺寸**

```paperconf```

**显示纸张宽度**

```paperconf -w```

**显示纸张高度**

```paperconf -h```

**显示指定的纸张**

```paperconf -p [a4]```

**以毫米为单位显示**

```paperconf -m```

# SYNOPSIS

**paperconf** [_options_] [_paper_]

# PARAMETERS

**-p** _PAPER_
> 选择要查询的纸张名称（a4、letter、legal 等）。省略时使用系统默认值。

**-d**
> 使用 libpaper 内置的默认值，而不是系统设置。

**-a**
> 遍历所有已知纸张。

**-n**
> 打印纸张名称。

**-N**
> 打印纸张名称，并将首字母大写。

**-s**
> 按先宽后高的顺序打印尺寸。

**-w**
> 打印宽度。

**-h**
> 打印高度。

**-c**
> 以厘米表示尺寸。

**-m**
> 以毫米表示尺寸。

**-i**
> 以英寸表示尺寸（默认单位是 PostScript 点）。

**-z**
> 给定未知纸张时返回错误，而不是回退到默认值。

# DESCRIPTION

**paperconf** 显示纸张尺寸信息。查询系统的纸张设置。

该工具显示尺寸和名称。属于 libpaper。

# CAVEATS

属于 libpaper。读取的是系统纸张配置。各地区有不同的默认值。

# HISTORY

paperconf 是 **libpaper** 的组成部分，用于查询纸张尺寸配置。

# INSTALL

```apt: sudo apt install libpaper-utils```

```dnf: sudo dnf install libpaper```

```pacman: sudo pacman -S libpaper```

```apk: sudo apk add libpaper```

```zypper: sudo zypper install libpaper```

```brew: brew install libpaper```

```nix: nix profile install nixpkgs#libpaper```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[paperconfig](/man/paperconfig)(8), [lp](/man/lp)(1)
