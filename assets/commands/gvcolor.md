# TAGLINE

为分层有向图中的节点着色的 graphviz 过滤器

# TLDR

**按层级为图着色**

```dot -Tcanon [graph.gv] | gvcolor | dot -Tpng -o [output.png]```

**着色并输出到文件**

```dot -Tcanon [graph.gv] | gvcolor > [colored.gv]```

# SYNOPSIS

**gvcolor** [_files_]

# PARAMETERS

_FILES_
> 已由 dot 完成布局的输入图文件。未指定时从标准输入读取。

# DESCRIPTION

**gvcolor**（旧名 **colorize**）是一个 Graphviz 过滤器，用于在分层有向图上根据初始种子值为节点设置颜色。颜色沿边从尾流向头，在每个节点处以 HSB 向量形式取平均，从而在整张图上形成视觉上的渐变效果。

图必须已经由 **dot** 完成布局（即节点带有位置/层级信息），初始颜色通过种子节点上的 **color** 属性设置。图属性 **flow=back** 可反转颜色的传播方向，**saturation=**_min_**,**_max_ 可跨层级线性调整饱和度，**Defcolor** 用于为未着色节点指定回退颜色。

# CAVEATS

要求图已被 dot 处理过；如果节点缺少位置信息则以状态码 1 退出。彼此相近但可区分的种子颜色（如蓝绿色、绿色、浅黄色）效果最佳。

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

[dot](/man/dot)(1), [gc](/man/gc)(1), [gvpr](/man/gvpr)(1), [ccomps](/man/ccomps)(1), [sccmap](/man/sccmap)(1), [tred](/man/tred)(1)

# RESOURCES

```[Homepage](https://graphviz.org/)```

```[Source code](https://gitlab.com/graphviz/graphviz)```

```[Documentation](https://graphviz.org/doc/info/command.html)```

<!-- verified: 2026-07-17 -->
