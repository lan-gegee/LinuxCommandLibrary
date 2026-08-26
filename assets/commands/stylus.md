# TAGLINE

表现力丰富的 CSS 预处理器编译器

# TLDR

**将 Stylus 文件编译为 CSS**

```stylus [style.styl]```

**编译到指定输出文件**

```stylus [style.styl] -o [style.css]```

**监视更改并编译**

```stylus -w [style.styl] -o [style.css]```

**以压缩方式编译**

```stylus -c [style.styl]```

**编译目录中的所有文件**

```stylus [src/] -o [dist/]```

**将 CSS 转换为 Stylus**

```stylus -C [style.css] [style.styl]```

**生成 source map**

```stylus --sourcemap [style.styl]```

# SYNOPSIS

**stylus** [_options_] [_file_|_dir_...]

# PARAMETERS

**-o**, **--out** _dir_
> 输出到指定目录或文件。

**-w**, **--watch**
> 监视文件更改并重新编译。

**-c**, **--compress**
> 压缩 CSS 输出。

**-C**, **--css** _src_ [_dest_]
> 将 CSS 输入转换为 Stylus。

**-m**, **--sourcemap**
> 生成 v3 source map。

**--sourcemap-inline**
> 将 source map 以 base64 内联到输出中。

**-l**, **--line-numbers**
> 在输出中添加行号注释。

**-i**, **--interactive**
> 启动交互式 REPL。

**-U**, **--inline**
> 将图像内联为 data URI。

**-u**, **--use** _plugin_
> 使用指定插件。

**-I**, **--include** _path_
> 向导入查找路径中添加路径。

**-r**, **--resolve-url**
> 解析导入中的相对 URL。

**--include-css**
> 在 @import 时包含常规 CSS。

**--import** _file_
> 编译前先导入文件。

**-p**, **--print**
> 将编译后的 CSS 打印到 stdout。

**-d**, **--compare**
> 同时显示输入与编译后的输出。

**-D**, **--deps**
> 显示依赖文件。

**-P**, **--prefix** _prefix_
> 为所有 CSS 类名添加前缀。

**-V**, **--version**
> 显示版本。

**-h**, **--help**
> 显示帮助。

# DESCRIPTION

**stylus** 是 Stylus CSS 预处理器的命令行编译器。Stylus 是为 Node.js 构建的表现力强、动态的 CSS 语言，具有灵活的语法、强大的函数和丰富的特性集。

该编译器将 Stylus 源文件（.styl）转换为标准 CSS。Stylus 语法灵活，冒号、分号和花括号均可省略，使样式表更具可读性。它支持变量、mixin、函数、迭代等众多扩展 CSS 能力的特性。

监视模式可在开发过程中自动重新编译。source map 通过将编译后的 CSS 映射回原始 Stylus 源码来辅助调试。CSS 转换功能有助于将现有样式表迁移到 Stylus。

# CAVEATS

安装需要 Node.js 和 npm。灵活的语法对缺乏统一约定的团队来说可能造成困扰。大型项目下性能可能不如其他预处理器。与 Sass/SCSS 相比，Stylus 的社区采用度较低。

# HISTORY

**Stylus** 由 TJ Holowaychuk（Express.js 的作者）创建并于 2010 年发布。它的设计目标是比现有 CSS 预处理器更有表现力和灵活性。虽然它获得了可观的采用，但 Sass/SCSS 最终在 CSS 预处理器生态中占据了更主导的地位。

# INSTALL

```pacman: sudo pacman -S stylus```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sass](/man/sass)(1), [less](/man/less)(1), [postcss](/man/postcss)(1), [npm](/man/npm)(1)
