# TAGLINE

可视化 DVC 流水线依赖关系

# TLDR

**显示流水线 DAG**

```dvc dag```

**以 dot 格式输出**

```dvc dag --dot```

**显示特定阶段**

```dvc dag [stage_name]```

**显示完整图**

```dvc dag --full```

# SYNOPSIS

**dvc** **dag** [_options_] [_target_]

# PARAMETERS

**--dot**
> 以 Graphviz DOT 格式输出。

**--full**
> 显示包含依赖项的完整图。

**-o**, **--out** _file_
> 输出到文件。

# DESCRIPTION

**dvc dag** 将 DVC 流水线的结构生成有向无环图（DAG）形式的可视化表示。它展示流水线中各阶段之间的依赖关系，以及数据在机器学习工作流中的流动方式。

图中的每个节点代表一个流水线阶段（数据处理、训练、评估等），边则表示阶段之间的依赖关系。这种可视化有助于理解流水线结构、识别瓶颈以及调试执行顺序问题。

默认输出是适合在终端查看的 ASCII 图形。--dot 选项可导出为 Graphviz DOT 格式，再使用 Graphviz 等工具或在线查看器渲染成图像。这对编写文档以及与团队成员共享流水线架构很有用。

# INSTALL

```brew: brew install dvc```

```nix: nix profile install nixpkgs#dvc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

