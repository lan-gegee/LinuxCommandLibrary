# TAGLINE

用于裁剪 OpenAPI 规范的 TUI 工具

# TLDR

**打开本地 OpenAPI 规范文件**

```apisnip [input.yaml]```

**裁剪并保存到指定的输出文件**

```apisnip [input.yaml] [output.yaml]```

从 URL **打开远程 OpenAPI 规范**

```apisnip [https://petstore.swagger.io/v2/swagger.json] [output.yaml]```

# SYNOPSIS

**apisnip** _input_ [_output_]

# PARAMETERS

_input_
> OpenAPI 规范的本地文件路径或远程 URL（必填）

_output_
> 输出文件路径（默认：apisnip.out.yaml）

# DESCRIPTION

**apisnip** 是一个用于选择性裁剪 OpenAPI 规范的终端用户界面。它以交互式列表展示所有 API 端点，你可以切换每个端点的保留状态，然后生成一个只包含所选端点的更小的规范文件，同时保留所有必要的 $ref 引用和组件。

apisnip 使用 Rust 和 Ratatui 编写，支持 JSON 和 YAML 两种格式、带加权评分的模糊搜索、HTTP 方法语法高亮、自动主题检测、鼠标操作，以及将所选端点智能分组到列表顶部的功能。

# CAVEATS

输出会保留原始规范的结构和顺序。只有端点可以被选择性包含；组件 schema 会根据所选端点的引用自动解析。

# HISTORY

**apisnip** 由 **Michiel Roos**（Tuurlijk）创建，是一个采用 MIT 许可证的开源 Rust 项目。

# SEE ALSO

[jq](/man/jq)(1), [yq](/man/yq)(1), [curl](/man/curl)(1)
