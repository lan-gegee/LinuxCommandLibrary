# TAGLINE

图的快速边捆绑

# TLDR

**对图中的边进行捆绑并写出输出**

```mingle -o [output.gv] [input.gv]```

**使用力导向方法进行捆绑**

```mingle -m 0 [input.gv]```

**设置边兼容性度量（基于距离）**

```mingle -c 0 [input.gv]```

**设置最大转折角度（度）**

```mingle -a [40] [input.gv]```

**以简单示意图格式输出**

```mingle -T simple -o [output.gv] [input.gv]```

**启用详细跟踪**

```mingle -v [input.gv]```

# SYNOPSIS

**mingle** [_options_] [_file_]

# PARAMETERS

**-m** _k_
> 捆绑方法：0 = 力导向，1 = 凝聚式墨水节省（若可用则为默认），2 = 聚类加墨水节省。

**-a** _k_
> 最大转折角度，单位为度（非负实数，默认 40）。

**-c** _v_
> 兼容性度量：0 = 距离（默认），1 = 完全兼容。仅用于力导向捆绑。

**-i** _k_
> 力导向捆绑中的最大迭代划分数。

**-r** _k_
> 凝聚式方法的最大递归层级（默认 100）。

**-T** _fmt_
> 输出格式："gv" 将绘图信息附加到输入图上，"simple" 输出示意表示。

**-v** [_k_]
> 跟踪的详细级别（未给值时默认 1）。

**-?**
> 打印用法后退出。

# DESCRIPTION

**mingle** 对图执行快速边捆绑。它通过将相似的边归组为束，减少密集图可视化中的视觉混乱。

作为 Graphviz 套件的一部分，mingle 读取 DOT 格式的图并生成带捆绑边的输出。它支持多种捆绑算法，包括力导向和凝聚式墨水节省方法。

# CAVEATS

属于 Graphviz。输出始终为 DOT 格式。在密集图中可能遮蔽单条边的路径。

# INSTALL

```apt: sudo apt install graphviz```

```dnf: sudo dnf install graphviz```

```pacman: sudo pacman -S graphviz```

```zypper: sudo zypper install graphviz```

```brew: brew install graphviz```

```nix: nix profile install nixpkgs#graphviz```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dot](/man/dot)(1), [neato](/man/neato)(1), [sfdp](/man/sfdp)(1), [fdp](/man/fdp)(1)
