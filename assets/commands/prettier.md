# TAGLINE

固执己见的多语言代码格式化工具

# TLDR

**格式化一个文件**

```prettier --write [file.js]```

**格式化多个文件**

```prettier --write "[**/*.js]"```

**检查格式**

```prettier --check [file.js]```

**使用指定解析器格式化**

```prettier --parser [typescript] [file]```

**列出与 Prettier 格式不一致的文件**

```prettier --list-different "[**/*.js]"```

**以无分号**和单引号的风格格式化

```prettier --write --no-semi --single-quote [file.js]```

# SYNOPSIS

**prettier** [_options_] [_files_]

# PARAMETERS

_FILES_
> 要格式化的文件。

**--write**
> 就地编辑文件。

**--check**
> 检查是否已按规范格式化。

**--parser** _NAME_
> 强制使用指定解析器。

**--config** _FILE_
> 配置文件路径。

**--single-quote**
> 使用单引号。

**--tab-width** _N_
> 每级缩进的空格数（默认：2）。

**--print-width** _N_
> 换行行宽（默认：80）。

**--trailing-comma** _MODE_
> 尾随逗号：all、es5 或 none（默认：all）。

**--no-semi**
> 不输出分号。

**--use-tabs**
> 使用制表符而非空格缩进。

**--list-different**, **-l**
> 打印与规范格式不一致的文件名。

**--no-config**
> 不查找配置文件。

**--ignore-unknown**, **-u**
> 忽略被模式匹配到的未知文件。

**--prose-wrap** _MODE_
> Markdown 中的换行方式：always、never 或 preserve（默认：preserve）。

# DESCRIPTION

**prettier** 是一个固执己见的代码格式化工具，通过解析代码并按自己的规则重新输出来强制统一的代码风格。它支持 JavaScript、TypeScript、CSS、HTML、JSON、Markdown、YAML、GraphQL，并可通过插件支持更多语言。

该工具刻意限制配置选项，以减少团队中的风格争论。文件可以用 **--write** 就地格式化，或用 **--check** 检查是否符合规范，因此既适合本地开发也适合 CI 管道。

# CONFIGURATION

**.prettierrc**（或 **.prettierrc.json**、**.prettierrc.yaml**、**prettier.config.js**）
> 项目配置文件，定义制表符宽度、分号、引号风格、尾随逗号、打印宽度等格式化选项。从被格式化的文件向上逐级查找。

**.prettierignore**
> Prettier 应跳过的文件和目录的 glob 模式，格式类似 .gitignore。

# CAVEATS

需要 Node.js。风格固执己见，刻意限制配置选项以减少风格争论。默认忽略 node_modules 中的文件。

# HISTORY

Prettier 由 **James Long** 于 **2017 年**创建，用于实现跨项目的统一代码格式化。

# INSTALL

```pacman: sudo pacman -S prettier```

```apk: sudo apk add prettier```

```brew: brew install prettier```

```nix: nix profile install nixpkgs#prettier```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[eslint](/man/eslint)(1), [biome](/man/biome)(1)
