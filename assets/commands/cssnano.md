# TAGLINE

基于 PostCSS 的模块化 CSS 压缩工具

# TLDR

压缩 CSS 文件

```cssnano [input.css] [output.css]```

使用默认预设进行压缩

```npx cssnano [input.css] > [output.min.css]```

用作 PostCSS 插件

```postcss [input.css] -o [output.css] --use cssnano```

带 source map 压缩

```cssnano [input.css] [output.css] -s```

禁用某项特定优化

```cssnano [input.css] [output.css] --no-[featureName]```

# SYNOPSIS

**cssnano** [_options_] _input.css_ [_output.css_]

# PARAMETERS

**--sourcemap, -s**
> 在压缩后的输出中生成 sourcemap。

**--no-[featureName]**
> 按名称禁用任意单个处理器模块。

**--config** _file_
> PostCSS 配置文件。

# PRESETS

**default**
> 安全的优化，适合大多数场景。

**lite**
> 最小化优化，处理速度最快。

**advanced**
> 激进的优化（可能改变行为）。

# DESCRIPTION

**cssnano** 是基于 PostCSS 构建的模块化 CSS 压缩工具，通过各种优化减小 CSS 文件体积：去除空白和注释、合并规则、优化取值以及清除冗余代码。

优化内容包括：规范化取值（颜色、长度）、合并重复规则、移除无用的浏览器前缀、优化字重和 z-index、丢弃重复声明，以及精简 calc() 表达式。

作为 PostCSS 插件，cssnano 可以集成到现有构建流水线（webpack、Vite、gulp 等）中，并可与 autoprefixer 等其他 PostCSS 插件组合使用。

# CONFIGURATION

**postcss.config.js**
> PostCSS 配置文件，在其中定义 cssnano 插件和预设。

**cssnano.config.js**
> cssnano 专用的配置文件，用于配置选项和自定义预设。

# CAVEATS

激进的压缩可能给依赖特定格式的 CSS 带来问题。advanced 预设在极端情况下可能改变行为。调试压缩后的 CSS 离不开 source map。某些优化会移除可能仍然需要的浏览器前缀。

# HISTORY

cssnano 由 **Ben Briggs** 创建，首次发布于 **2015** 年。它构建在 PostCSS 之上，采用模块化设计，每项优化都是一个独立插件。这种设计让用户可以精确定制应用哪些优化。cssnano 已成为最受欢迎的 CSS 压缩工具之一，被众多构建工具和框架集成。

# SEE ALSO

[postcss](/man/postcss)(1), [autoprefixer](/man/autoprefixer)(1)
