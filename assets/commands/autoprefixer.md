# TAGLINE

自动为 CSS 添加厂商前缀

# TLDR

**处理 CSS 文件并添加厂商前缀**

```autoprefixer [input.css] -o [output.css]```

**从标准输入处理 CSS**

```cat [input.css] | autoprefixer > [output.css]```

**指定浏览器目标**

```autoprefixer [input.css] -o [output.css] --browsers "last 2 versions, > 1%"```

原地**处理多个文件**

```autoprefixer [file1.css] [file2.css]```

**生成 source map**

```autoprefixer [input.css] -o [output.css] --map```

**显示将添加哪些前缀**

```autoprefixer --info```

# SYNOPSIS

**autoprefixer** [_options_] [_files_]

# PARAMETERS

**-o**, **--output** _file_
> 将输出写到指定文件。

**-d**, **--dir** _directory_
> 输出到目录（用于多个文件）。

**--map**
> 生成 source map。

**--no-map**
> 禁用 source map 生成。

**-b**, **--browsers** _list_
> 浏览器目标（Browserslist 查询）。

**--ignore** _pattern_
> 要忽略文件的 glob 模式。

**--replace**
> 原地修改文件（多文件时的默认行为）。

**--info**
> 显示浏览器列表和前缀信息。

**--no-inline**
> 不内联 source map。

**--env** _environment_
> 指定 Browserslist 环境。

# DESCRIPTION

**Autoprefixer** 是一个 PostCSS 插件，可根据最新的浏览器使用数据自动为 CSS 属性添加厂商前缀。它会解析 CSS，并在跨浏览器兼容所需之处添加 **-webkit-**、**-moz-**、**-ms-** 等前缀。

该工具借助 Browserslist 根据目标浏览器规格确定所需的前缀。它不仅添加必要的前缀，还会删除不再需要的过时前缀，保持 CSS 干净高效。

Autoprefixer 能处理 CSS 属性、值、@规则和选择器。它了解哪些浏览器支持哪些特性，只根据指定的浏览器目标添加必要的前缀；目标浏览器通常在 **browserslist** 文件或 **package.json** 中配置。

# CONFIGURATION

**.browserslistrc**
> 使用 Browserslist 查询语法定义前缀生成的目标浏览器。

**postcss.config.js**
> PostCSS 配置文件，可将 Autoprefixer 作为带选项的插件加载。

# CAVEATS

浏览器支持数据依赖 Can I Use 数据库的更新。非常新的 CSS 特性可能无法立即识别。该工具无法修复非标准的浏览器行为，只能添加标准前缀。某些前缀存在行为差异，加前缀无法解决。

# HISTORY

Autoprefixer 由 **Andrey Sitnik** 于 **2013 年**创建，用以解决手动添加厂商前缀的繁琐流程。它成为使用最广泛的 PostCSS 插件之一，并集成进 webpack、Vite、Parcel 等大多数现代构建工具。该工具利用来自 **caniuse.com** 的真实浏览器使用数据消除了手动前缀管理，革新了 CSS 工作流。

# INSTALL

```nix: nix profile install nixpkgs#autoprefixer```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[postcss](/man/postcss)(1), [cssnano](/man/cssnano)(1)
