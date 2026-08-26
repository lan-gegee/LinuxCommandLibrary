# TAGLINE

为已布局的图着色边以区分视觉效果

# TLDR

**为边着色**并写出结果

```edgepaint [graph.dot] -o [colored.dot]```

**设置最小**入射角（度）

```edgepaint --angle=15 [graph.dot] -o [out.dot]```

**使用指定的**配色方案

```edgepaint --color_scheme=accent8 [graph.dot] -o [out.dot]```

**允许共享端点的边**保持相同颜色

```edgepaint --share_endpoint [graph.dot] -o [out.dot]```

**通过管道交给 dot** 渲染 PNG

```dot graph.dot | edgepaint | dot -Tpng -o out.png```

# SYNOPSIS

**edgepaint** [_options_] [_input_] [**-o** _output_]

# PARAMETERS

_input_
> 已完成节点布局的输入 DOT 文件。省略时从 stdin 读取。

**-o** _FILE_
> 将输出写入 FILE 而不是 stdout。

**--accuracy**=_e_
> 在每个节点处查找最大差异配色时的精度。默认 0.01。

**--angle**=_a_
> 若两条边的入射角小于 _a_ 度，则为其着不同颜色。默认 15。

**--color_scheme**=_c_
> 配色板：`rgb`、`gray`、`lab`（默认）、十六进制颜色列表，或任何 Brewer 方案名（如 `accent8`、`set19`）。

**--lightness**=_l1,l2_
> 亮度范围，仅在 `lab` 下可用。取整数值 0-100。默认 `0,70`。

**--random_seed**=_s_
> 随机配色的种子。负值表示用不同的种子运行多次迭代。

**--share_endpoint**
> 共享节点且几乎反向平行（相差约 180 度）的边不视为冲突。

**-v**
> 详细输出。

**-?**
> 打印用法并退出。

# DESCRIPTION

**edgepaint** 为图的边分配颜色，使相邻或近似平行的边获得最大差异的颜色。它要求图已经过布局（例如由 **dot** 或 **neato** 完成），因为算法利用边的几何位置来决定哪些边对应当不同。

颜色会写入每条边的 `color` 属性，修改后的 DOT 会输出到 stdout（或 **-o** 指定的文件）。默认的 `lab` 配色方案产生感知上差异明显的色调；其他 Brewer 方案则提供一个固定的小型调色板。

# CAVEATS

输入必须已包含来自布局引擎的边几何信息，否则 edgepaint 无法确定角度。非常稠密的图可能耗尽调色板，仍会产生视觉上相似的边。Brewer 方案的颜色数量是固定的，因此大图应优先使用 `lab`。

# HISTORY

**edgepaint** 是 **Graphviz** 的一部分，最初由 **AT&T Labs Research** 开发。它实现了 Yifan Hu 关于面向图形可读性的边着色研究思想。

# INSTALL

```apt: sudo apt install graphviz```

```dnf: sudo dnf install graphviz```

```pacman: sudo pacman -S graphviz```

```apk: sudo apk add graphviz```

```zypper: sudo zypper install graphviz```

```brew: brew install graphviz```

```nix: nix profile install nixpkgs#graphviz```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dot](/man/dot)(1), [neato](/man/neato)(1), [graphviz](/man/graphviz)(7)
