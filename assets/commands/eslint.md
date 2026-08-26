# TAGLINE

可插拔的 JavaScript 和 TypeScript 代码检查工具

# TLDR

**检查 JavaScript 文件**

```eslint [file.js]```

**递归检查目录**

```eslint [src/]```

**修复可自动修复的**问题

```eslint --fix [file.js]```

**指定配置文件**

```eslint -c [.eslintrc.json] [file.js]```

**以特定格式输出**

```eslint -f [json] [file.js]```

交互式**创建配置文件**

```npm init @eslint/config```

**检查从 stdin 管道传入的**文件

```cat [file.js] | eslint --stdin```

# SYNOPSIS

**eslint** [_options_] [_files_|_dirs_]

# PARAMETERS

_FILES_
> 要检查的文件或目录。

**--fix**
> 自动修复问题。

**-c**, **--config** _FILE_
> 配置文件。

**-f**, **--format** _FORMAT_
> 输出格式。

**--cache**
> 只检查自上次运行后发生变化的文件。

**--quiet**
> 只报告错误，不显示警告。

**--max-warnings** _N_
> 如果发现超过 N 个警告则以错误退出。

**--no-eslintrc**
> 忽略配置文件（仅旧版配置）。

**--rulesdir** _DIR_
> 从目录加载额外的自定义规则（已弃用）。

**--stdin**
> 检查从标准输入读取的源代码。

**--help**
> 显示帮助信息。

# DESCRIPTION

**ESLint** 是 JavaScript 和 TypeScript 的标准代码检查工具。它对代码进行静态分析，以发现问题、强制执行编码规范并在运行前捕获 bug。

规则高度可配置。插件可以为 React、Vue、TypeScript 及其他框架扩展功能。--fix 标志能自动修正许多问题。

ESLint 与编辑器和 CI 系统集成，是 JavaScript 开发工作流的核心工具。

# CONFIGURATION

**eslint.config.js**（flat config）
> ESLint v9 起的默认配置文件。它导出一组配置对象，定义文件、规则、插件和语言选项。也可使用 eslint.config.mjs 或 eslint.config.cjs。

**.eslintrc.js** / **.eslintrc.json** / **.eslintrc.yml**（旧版）
> v9 之前的 "eslintrc" 格式。已弃用，v9 中默认不再查找，计划在 v10 中移除。

# CAVEATS

自 ESLint v9 起，flat config（eslint.config.js）成为默认，旧版 .eslintrc 格式、--ext 标志、--no-eslintrc 以及内置的 `--init` 命令已被移除或替代；请使用 `npm init @eslint/config` 生成配置。两种配置体系下的插件兼容性各有差异。大型代码库建议使用 --cache。

# HISTORY

ESLint 由 **Nicholas C. Zakas** 于 **2013 年**创建，作为比 JSHint 更可插拔、更可配置的替代方案。凭借其可扩展性，它成为了主流的 JavaScript 代码检查工具。

# INSTALL

```pacman: sudo pacman -S eslint```

```brew: brew install eslint```

```nix: nix profile install nixpkgs#eslint```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[prettier](/man/prettier)(1), [tsc](/man/tsc)(1), [jshint](/man/jshint)(1)

# RESOURCES

```[Source code](https://github.com/eslint/eslint)```

```[Homepage](https://eslint.org/)```

```[Documentation](https://eslint.org/docs/latest/)```

<!-- verified: 2026-07-14 -->
