# TAGLINE

将 SVG 文件转换为 React 组件

# TLDR

**将 SVG 转换为 React**

```svgr [icon.svg]```

**输出到文件**

```svgr [icon.svg] -o [Icon.jsx]```

**转换目录**

```svgr [icons/] -d [components/]```

**使用 TypeScript**

```svgr --typescript [icon.svg]```

**作为命名导出**

```svgr --export-type named [icon.svg]```

**使用自定义模板**

```svgr --template [template.js] [icon.svg]```

# SYNOPSIS

**svgr** [_-o file_] [_-d dir_] [_--typescript_] [_options_] _input_

# PARAMETERS

**-o** _FILE_
> 输出文件。

**-d** _DIR_
> 输出目录。

**--typescript**
> TypeScript 输出。

**--export-type** _TYPE_
> 导出方式。

**--template** _FILE_
> 自定义模板。

**--icon**
> 图标模式（1em 大小）。

# DESCRIPTION

**svgr** 将 SVG 文件转换为 React 组件，生成可直接在 React 应用中导入和使用的 JSX 代码。这样就无需单独管理 SVG 资源文件，还能对图标和插图进行动态样式设置和基于 prop 的定制。

该工具支持带完整类型定义的 TypeScript 输出、命名导出与默认导出以及多种组件模式。批量转换可以将整个目录的 SVG 文件转换为组件库，并自动生成 index 文件。自定义模板可以精确控制生成的组件代码形态。

SVGR 可作为 loader/插件集成到 webpack、Rollup 等打包工具中，也可以作为独立的 CLI 或 Node.js API 使用。它还可以选择在生成组件前先运行 SVGO 优化。

# CAVEATS

React 专用。需要 Node.js。输出 JSX。

# HISTORY

**SVGR** 的诞生是为了将 SVG 文件转换为 React 组件，简化 React 应用中图标的使用。

# SEE ALSO

[svgo](/man/svgo)(1), [react-scripts](/man/react-scripts)(1)
