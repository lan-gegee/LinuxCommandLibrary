# TAGLINE

从文本描述生成 UML 图

# TLDR

**生成图表**

```plantuml [diagram.puml]```

**以 PNG 输出**

```plantuml -tpng [diagram.puml]```

**以 SVG 输出**

```plantuml -tsvg [diagram.puml]```

**输出到目录**

```plantuml -o [output_dir] [diagram.puml]```

**从 stdin 读取**

```echo "@startuml\nA -> B\n@enduml" | plantuml -pipe > [diagram.png]```

**监视文件变化**

```plantuml -gui```

# SYNOPSIS

**plantuml** [_options_] _files_...

# DESCRIPTION

**plantuml** 从文本描述生成 UML 图。它支持时序图、类图、活动图等多种图类型。

该工具使用简单的文本语法，便于版本控制并可集成到文档工作流中。

# PARAMETERS

**-t** _format_
> 输出格式（png、svg、eps、pdf、txt）。

**-o** _dir_
> 输出目录。

**-charset** _encoding_
> 输入文件编码。

**-pipe**
> 使用 stdin/stdout。

**-gui**
> 启动图形界面。

**-config** _file_
> 包含配置文件。

**-checkversion**
> 检查更新。

**-verbose**
> 详细输出。

# DIAGRAM TYPES

时序图、类图、活动图、用例图、组件图、状态图、对象图、部署图、计时图、线框图、甘特图、思维导图

# CAVEATS

需要 Java。某些图表需要 Graphviz。大型图表可能较慢。复杂布局需要调优。

# HISTORY

**PlantUML** 由 **Arnaud Roques** 自 **2009 年**起开发。它将基于文本的绘图方式带入 UML 领域，可与 wiki、文档工具和 IDE 集成。

# INSTALL

```dnf: sudo dnf install plantuml```

```pacman: sudo pacman -S plantuml```

```apk: sudo apk add plantuml```

```zypper: sudo zypper install plantuml```

```brew: brew install plantuml```

```nix: nix profile install nixpkgs#plantuml```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[graphviz](/man/graphviz)(1), [mermaid](/man/mermaid)(1), [ditaa](/man/ditaa)(1), [drawio](/man/drawio)(1)
