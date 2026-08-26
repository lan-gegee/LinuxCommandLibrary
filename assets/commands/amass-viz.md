# TAGLINE

可视化攻击面枚举数据

# TLDR

**生成 D3.js HTML 可视化**

```amass viz -d3 -d [example.com]```

**导出为 Graphviz DOT 格式**

```amass viz -dot -d [example.com] -o [graph.dot]```

**生成供 Gephi 使用的 GEXF 文件**

```amass viz -gexf -d [example.com] -o [graph.gexf]```

**导出为 Maltego 格式**

```amass viz -maltego -d [example.com] -o [graph.csv]```

**使用数据库中的特定枚举记录**

```amass viz -d3 -enum [1] -d [example.com]```

# SYNOPSIS

**amass viz** [_-d3_|_-dot_|_-gexf_|_-graphistry_] [_-d domain_] [_options_]

# DESCRIPTION

**amass viz** 根据 amass 数据库中存储的枚举数据生成可视化。它可以创建交互式的网页图表、导出为标准图形格式，或与可视化平台集成。

可视化的呈现方式有助于理解已发现资产之间的关系、识别规律，并向相关方传达发现结果。

# PARAMETERS

**-d3**
> 生成 D3.js HTML 可视化

**-dot**
> 以 Graphviz DOT 格式导出

**-gexf**
> 以 GEXF 格式导出（供 Gephi 使用）

**-graphistry**
> 生成 Graphistry 可视化

**-maltego**
> 导出为 Maltego 格式

**-d** _domain_
> 按域名过滤

**-enum** _index_
> 使用特定的枚举记录

**-o** _file_
> 输出文件路径

**-dir** _path_
> 数据库目录

# CAVEATS

大规模枚举会产生复杂的可视化结果，渲染可能较慢。D3 可视化需要网页浏览器。某些格式需要特定软件才能查看。

# HISTORY

**amass viz** 的加入是为了帮助安全专业人员对枚举结果进行可视化和交流，支持多种输出格式以满足不同的使用场景。

# INSTALL

```aur: yay -S amass```

```brew: brew install amass```

```nix: nix profile install nixpkgs#amass```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[amass](/man/amass)(1), [amass-enum](/man/amass-enum)(1), [amass-db](/man/amass-db)(1), [amass-track](/man/amass-track)(1), [dot](/man/dot)(1)
