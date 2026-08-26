# TAGLINE

基于 Node.js 的 SVG 优化工具

# TLDR

**优化 SVG**

```svgo [input.svg] -o [output.svg]```

**原地优化**

```svgo [file.svg]```

**优化目录**

```svgo -f [./icons] -o [./optimized]```

**显示文件信息**

```svgo [file.svg] --show-plugins```

**使用配置文件**

```svgo --config [svgo.config.js] [file.svg]```

**禁用插件**

```svgo --disable=[removeViewBox] [file.svg]```

**启用插件**

```svgo --enable=[removeDimensions] [file.svg]```

**格式化输出**

```svgo --pretty [file.svg]```

# SYNOPSIS

**svgo** [_-o output_] [_-f folder_] [_--config file_] [_options_] _files_

# PARAMETERS

**-o**, **--output** _FILE_
> 输出文件。

**-f**, **--folder** _DIR_
> 输入文件夹。

**--config** _FILE_
> 配置文件。

**--disable** _PLUGIN_
> 禁用插件。

**--enable** _PLUGIN_
> 启用插件。

**--pretty**
> 格式化输出。

**--multipass**
> 多轮处理。

**-q**, **--quiet**
> 静默输出。

# DESCRIPTION

**svgo**（SVG Optimizer）是一款基于 Node.js 的 SVG 文件优化工具，采用插件架构。每个插件负责一项特定的优化，例如移除元数据、简化路径数据、合并冗余元素、清理属性或删除空容器。

可以通过配置文件或命令行参数单独启用或禁用插件，从而精细控制应用哪些优化。multipass 选项会反复运行优化，直到不再有任何改进为止。文件夹模式可批量处理整个目录中的 SVG 文件。

SVGO 广泛用于前端构建流水线和图标库工作流，在部署前尽量压缩 SVG 文件体积。当需要人工可编辑的 SVG 时，格式化模式会重新排版输出以提高可读性。

# CONFIGURATION

**svgo.config.js**
> 项目配置文件，定义启用/禁用的插件及其选项。

# CAVEATS

某些优化可能影响渲染效果。请目视检查输出。复杂 SVG 需谨慎处理。

# HISTORY

**SVGO**（SVG Optimizer）是一款用于 SVG 优化的 Node.js 工具。它广泛用于构建流程和图标库中。

# INSTALL

```pacman: sudo pacman -S svgo```

```brew: brew install svgo```

```nix: nix profile install nixpkgs#svgo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[imagemin](/man/imagemin)(1), [inkscape](/man/inkscape)(1)
