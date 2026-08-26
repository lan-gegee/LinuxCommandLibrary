# TAGLINE

使用 JavaScript 插件转换 CSS

# TLDR

**处理 CSS 文件**

```postcss [input.css] -o [output.css]```

**使用配置文件**

```postcss [input.css] -o [output.css] -c [postcss.config.js]```

**监视变更**

```postcss [input.css] -o [output.css] --watch```

**处理目录**

```postcss [src/] -d [dist/]```

**使用特定插件**

```postcss [input.css] -o [output.css] -u [autoprefixer]```

**原地替换文件**

```postcss [style.css] --replace```

**生成 source map**

```postcss [input.css] -o [output.css] --map```

# SYNOPSIS

**postcss** [_-o output_] [_-d dir_] [_-c config_] [_-u plugins_] [_options_] _files_

# PARAMETERS

**-o**, **--output** _FILE_
> 输出文件。

**-d**, **--dir** _DIR_
> 输出目录。

**-c**, **--config** _FILE_
> 配置文件路径。

**-u**, **--use** _PLUGINS_
> 要使用的插件。

**-w**, **--watch**
> 监视模式。

**--map**
> 生成 source map。

**--replace**
> 替换输入文件。

**--no-map**
> 禁用 source map。

**-v**, **--verbose**
> 详细输出。

# DESCRIPTION

**postcss** 是一款通过 JavaScript 插件转换 CSS 的工具。它本身并不是预处理器，而是提供一个框架，由插件对 CSS 抽象语法树执行特定的转换。流行的插件包括用于添加厂商前缀的 Autoprefixer、用于压缩的 cssnano，以及让你今天就使用未来 CSS 语法的 postcss-preset-env。

插件在配置文件（postcss.config.js）中链接在一起，或在命令行上指定。每个插件接收解析后的 CSS，应用自己的转换，然后把结果传递给下一个插件。这种模块化方式让团队能够精确组合自己需要的处理流水线。

监视模式会在检测到变更时自动重新处理文件，可融入开发工作流。Source map 保留转换后 CSS 与原始 CSS 之间的映射关系，便于在浏览器开发者工具中调试。

# CONFIGURATION

**postcss.config.js**（或 **.postcssrc**、**postcss.config.mjs**）
> 定义处理流水线的插件配置文件。按顺序列出插件及其选项。会从输入文件所在目录向上查找。

**package.json** 的 `"postcss"` 字段
> 在项目清单文件中配置 PostCSS 的另一种位置。

# CAVEATS

功能依赖插件。需要 Node.js 环境。配置复杂度可能不断增长。

# HISTORY

**PostCSS** 由 **Andrey Sitnik** 于 **2013 年**创建。它开创了以 AST 方式处理 CSS 的先河，并孕育了丰富的插件生态。

# INSTALL

```nix: nix profile install nixpkgs#postcss```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sass](/man/sass)(1), [less](/man/less)(1), [autoprefixer](/man/autoprefixer)(1), [cssnano](/man/cssnano)(1)
