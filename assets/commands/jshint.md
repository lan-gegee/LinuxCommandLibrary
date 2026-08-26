# TAGLINE

JavaScript 代码质量工具

# TLDR

**对 JavaScript 文件做静态检查**

```jshint [file.js]```

**检查多个文件**

```jshint [file1.js] [file2.js]```

**使用配置文件**

```jshint --config [.jshintrc] [file.js]```

**检查所有 JS 文件**

```jshint [src/]```

**详细输出**

```jshint --verbose [file.js]```

**显示非错误数据**

```jshint --show-non-errors [file.js]```

**排除路径**

```jshint --exclude [node_modules/,vendor/] [src/]```

**使用自定义报告器**

```jshint --reporter [checkstyle] [src/]```

# SYNOPSIS

**jshint** [_options_] _file_...

# PARAMETERS

_FILE_
> 要检查的 JavaScript 文件。

**--config** _FILE_
> 配置文件路径（默认从被检查文件所在目录向上查找 .jshintrc）。

**--verbose**
> 在输出中包含警告/错误代码（如 W117）。

**--reporter** _NAME_
> 使用自定义报告器：jslint、checkstyle、unix，或报告器模块的路径。

**--extract** _MODE_
> 检查前从 HTML 中提取 JavaScript：auto、always、never（默认 never）。

**--extra-ext** _LIST_
> 需要检查的额外文件扩展名列表，以逗号分隔（默认 .js）。

**--exclude** _PATHS_
> 要跳过的目录或文件列表，以逗号分隔。

**--exclude-path** _FILE_
> 使用 .gitignore 语法的文件（如 .jshintignore）来跳过路径。

**--prereq** _FILES_
> 在每个被检查文件之前引入的文件，用于提供全局变量。

**--filename** _NAME_
> 将 stdin 输入视为具有此文件名，以便匹配配置。

**--show-non-errors**
> 显示额外的分析数据（函数、全局变量）。

**--version**
> 打印已安装的版本号。

**--help**
> 显示帮助信息。

# DESCRIPTION

**JSHint** 是一款 JavaScript 静态分析工具，可检测代码中的错误和潜在问题。它可以通过 **.jshintrc** JSON 文件（或 package.json 中的 **jshintConfig** 字段）进行配置，便于团队统一执行选定的编码风格。

CLI 接受文件、目录或 stdin（文件名用 **-** 表示）。给定目录时，JSHint 会递归检查每个扩展名匹配 **--extra-ext** 的文件（默认 .js）。忽略的路径可以列在 **.jshintignore** 中。

# CAVEATS

需要 Node.js。JSHint 的开发节奏已经放缓；新项目通常更推荐 **ESLint**，尤其是使用现代 ECMAScript 或 TypeScript 时。JSHint 原生不支持 JSX 和 TypeScript。

# HISTORY

JSHint 于 2011 年由 **Anton Kovalyov** 从 **JSLint** 分叉而来，旨在提供更具可配置性的 JavaScript 检查器。

# INSTALL

```nix: nix profile install nixpkgs#jshint```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[eslint](/man/eslint)(1), [prettier](/man/prettier)(1), [tslint](/man/tslint)(1), [node](/man/node)(1)
