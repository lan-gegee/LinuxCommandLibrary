# TAGLINE

将 Sass 和 SCSS 样式表编译为 CSS

# TLDR

**将 SCSS 编译为 CSS**

```sass [input.scss] [output.css]```

**监视文件变化**

```sass --watch [input.scss]:[output.css]```

**监视目录**

```sass --watch [src/scss]:[dist/css]```

**编译时不生成 source map**

```sass --no-source-map [input.scss] [output.css]```

**压缩编译**（最小化）

```sass --style=compressed [input.scss] [output.css]```

**从标准输入编译**

```sass --stdin --style=compressed```

**使用指定的加载路径**

```sass --load-path=[node_modules] [input.scss] [output.css]```

# SYNOPSIS

**sass** [_options_] [_input.scss_] [_output.css_]

# PARAMETERS

**--watch**
> 监视文件变化并重新编译。

**--style** _STYLE_
> 输出风格：expanded、compressed。

**--source-map**
> 生成 source map。

**--no-source-map**
> 禁用 source map。

**--load-path** _PATH_
> 查找导入的路径。

**--charset**
> 为非 ASCII 内容输出 @charset。

**--no-charset**
> 不输出 @charset。

**--error-css**
> 在 CSS 输出中包含错误信息。

**--update**
> 只编译发生变化的文件。

**--stop-on-error**
> 遇到第一个错误后停止。

**--color** / **--no-color**
> 控制彩色输出。

**--quiet**
> 抑制警告。

**--trace**
> 出错时显示完整堆栈跟踪。

**--stdin**
> 从标准输入读取。

**--indented**
> 将标准输入按缩进语法解析。

# DESCRIPTION

**Sass**（Syntactically Awesome Style Sheets）是一款 CSS 预处理器，增加了变量、嵌套、mixin 等特性。它编译为浏览器可用的标准 CSS。

它有两种语法：SCSS（Sassy CSS，.scss）使用类似 CSS 的花括号和分号；Sass（.sass）使用缩进。SCSS 因与 CSS 兼容而更流行。

变量（$color: #333）支持可复用的值。嵌套让样式反映 HTML 结构。mixin（@mixin、@include）共享可复用的样式模式。函数用于执行计算和转换。

导入（@use、@import）将多个文件的样式组合起来。@use 规则提供带命名空间的访问和比旧式 @import 更好的封装。

监视模式会监控文件变化并自动重新编译，配合实时刷新工具可实现快速开发。Source map 将编译后的 CSS 与原始 Sass 关联起来以便调试。

输出风格控制格式化方式：expanded 适合开发，compressed 适合生产。

# CAVEATS

Node Sass 已被弃用，应改用 Dart Sass（sass 软件包）。@import 正逐步被 @use 取代。大型项目编译可能较慢。Source map 会增加文件体积。某些 CSS hack 可能无法正确编译。

# HISTORY

**Sass** 由 **Hampton Catlin** 和 **Natalie Weizenbaum** 于 **2006 年**前后创建。它最初基于 Ruby，开创了 CSS 预处理的先河。LibSass（C/C++）提升了性能。**Dart Sass** 于 **2018 年**成为主要实现，sass npm 包取代了 node-sass。**2010 年**推出的 SCSS 语法成为了主流写法。

# INSTALL

```apk: sudo apk add dart-sass-js```

```nix: nix profile install nixpkgs#sass```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[less](/man/less)(1), [postcss](/man/postcss)(1), [stylus](/man/stylus)(1), [tailwindcss](/man/tailwindcss)(1)
