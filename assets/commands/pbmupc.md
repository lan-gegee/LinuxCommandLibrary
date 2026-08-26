# TAGLINE

创建 UPC-A 条形码 PBM 图像

# TLDR

**创建 UPC-A 条形码图像**

```pbmupc [0] [12345] [67890] [5] > [barcode.pbm]```

**以样式 1 创建条形码（高守护条）**

```pbmupc -s1 [0] [12345] [67890] [5] > [barcode.pbm]```

**以样式 2 创建条形码（短守护条）**

```pbmupc -s2 [0] [12345] [67890] [5] > [barcode.pbm]```

# SYNOPSIS

**pbmupc** [**-s1** | **-s2**] _type_ _manufacturer_ _product_ _check_

# PARAMETERS

_type_
> 单个数字，表示编号系统类型（标准 UPC-A 通常为 0）。

_manufacturer_
> 五位厂商代码。

_product_
> 五位产品代码。

_check_
> 单个校验位（其余 11 位数字的模 10 校验和）。

**-s1**
> 样式 1 输出，带高守护条（默认）。

**-s2**
> 样式 2 输出，带短守护条。

# DESCRIPTION

**pbmupc** 以 PBM（Portable Bitmap）格式创建 UPC-A（Universal Product Code，通用产品代码）条形码图像。它将 12 位 UPC-A 代码的四个组成部分作为单独的参数：编号系统类型位、五位厂商代码、五位产品代码和校验位。

输出的 PBM 图像可使用 Netpbm 转换工具转换为其他格式。UPC-A 条形码是美国和加拿大使用的标准零售条形码格式。

# CAVEATS

仅生成 UPC-A 格式的条形码。工具不会校验或自动计算校验位；用户必须提供正确的值。属于 Netpbm 工具集。

# HISTORY

**pbmupc** 属于 **Netpbm** 软件包，该软件包起源于 Jef Poskanzer 在 20 世纪 80 年代末开发的 PBMplus 工具包。

# INSTALL

```apt: sudo apt install netpbm```

```dnf: sudo dnf install netpbm```

```pacman: sudo pacman -S netpbm```

```apk: sudo apk add netpbm```

```zypper: sudo zypper install netpbm```

```brew: brew install netpbm```

```nix: nix profile install nixpkgs#netpbm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pbm](/man/pbm)(5), [netpbm](/man/netpbm)(1)
