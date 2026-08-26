# TAGLINE

实用优先 CSS 框架的命令行工具

# TLDR

从输入文件**构建 CSS**

```tailwindcss -i [src/input.css] -o [dist/output.css]```

**构建并监视变更**

```tailwindcss -i [src/input.css] -o [dist/output.css] --watch```

压缩构建

```tailwindcss -i [src/input.css] -o [dist/output.css] --minify```

**初始化**配置文件

```tailwindcss init```

以完整配置**初始化**

```tailwindcss init --full```

通过 npx 构建

```npx tailwindcss -i [src/input.css] -o [dist/output.css]```

# SYNOPSIS

**tailwindcss** [_-i input_] [_-o output_] [_--watch_] [_--minify_] [_--config path_]

# PARAMETERS

**-i** _file_, **--input** _file_
> 要处理的输入 CSS 文件

**-o** _file_, **--output** _file_
> 编译后的 CSS 输出文件

**-w**, **--watch**
> 监视变更并自动重新构建

**-m**, **--minify**
> 压缩输出的 CSS

**-c** _file_, **--config** _file_
> tailwind.config.js 文件的路径

**--content** _paths_
> 要扫描类名使用情况的内容文件

**-h**, **--help**
> 显示帮助信息

# SUBCOMMANDS

**init**
> 创建 tailwind.config.js 文件

**init --full**
> 创建包含所有默认值的配置

# DESCRIPTION

**Tailwind CSS** 是一个实用优先（utility-first）的 CSS 框架，它通过扫描源文件中的类使用情况来生成优化的 CSS。该 CLI 将 Tailwind 的工具类编译为标准 CSS。

构建过程会扫描模板文件（HTML、JSX、Vue 等）中的 Tailwind 类，只生成实际用到的 CSS 规则，并输出可用于生产环境的样式表。**--watch** 标志可在开发过程中实时重新构建。

输入的 CSS 文件应包含 @tailwind base、@tailwind components 和 @tailwind utilities 等 Tailwind 指令。配置通过 tailwind.config.js 自定义。

# CAVEATS

此 CLI 需要 Node.js。生产环境构建时务必使用 **--minify** 来减小文件体积。确保配置中的 content 路径正确指向所有模板文件，以免样式缺失。

# HISTORY

Tailwind CSS 由 **Adam Wathan** 创建，于 **2017 年 11 月**首次发布。第 4 版（2024 年）通过 @tailwindcss/cli 软件包带来了显著的性能提升。该框架让实用优先的 CSS 编写方式广为流行。

# INSTALL

```brew: brew install tailwindcss```

```nix: nix profile install nixpkgs#tailwindcss```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[postcss](/man/postcss)(1), [sass](/man/sass)(1), [npm](/man/npm)(1)
