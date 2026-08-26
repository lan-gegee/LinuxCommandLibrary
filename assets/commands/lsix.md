# TAGLINE

在终端中显示图片

# TLDR

**显示图片**

```lsix [*.jpg]```

**显示目录中的所有图片**

```lsix```

**显示指定图片**

```lsix [image1.png] [image2.png]```

**设置缩略图大小**

```LSIX_SIZE=[200x200] lsix```

**带边框显示**

```lsix -b [*.png]```

# SYNOPSIS

**lsix** [_options_] [_files_]

# PARAMETERS

_FILES_
> 要显示的图片文件。

**-b**
> 在图片周围显示边框。

**LSIX_SIZE**
> 控制大小的环境变量。

# DESCRIPTION

**lsix** 在终端中显示图片。它需要支持 sixel 图形的终端。

该工具在终端中创建缩略图，适用于 xterm、mlterm 和 foot 等终端。

# CAVEATS

需要支持 sixel 的终端。需要 ImageMagick。并非支持所有终端。

# HISTORY

lsix 的诞生是为了在支持 **sixel 图形**格式的终端中直接显示图片。

# INSTALL

```pacman: sudo pacman -S lsix```

```brew: brew install lsix```

```nix: nix profile install nixpkgs#lsix```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[img2sixel](/man/img2sixel)(1), [viu](/man/viu)(1), [chafa](/man/chafa)(1)
