# TAGLINE

零配置的 JavaScript 风格检查器

# TLDR

**检查代码**

```standard```

**自动修复**

```standard --fix```

**检查指定文件**

```standard [file1.js] [file2.js]```

**使用解析器**

```standard --parser [babel-eslint]```

**详细输出**

```standard --verbose```

**声明全局变量**

```standard --global [globalName]```

# SYNOPSIS

**standard** [_--fix_] [_--parser name_] [_options_] [_files_]

# PARAMETERS

**--fix**
> 自动修复问题。

**--parser** _NAME_
> 自定义解析器。

**--verbose**
> 显示规则名称。

**--global** _NAME_
> 声明全局变量（可重复）。

**--plugin** _NAME_
> 引入 ESLint 插件。

**--fix-dry-run**
> 报告将被修复的内容但不写入更改。

**--env** _ENV_
> 环境全局变量。

**--stdin**
> 从标准输入进行检查。

# DESCRIPTION

**standard** 是一个零配置的 JavaScript 检查器和格式化工具，强制执行一套固定的风格规则。它构建在 ESLint 之上，通过提供单一而明确的风格指南，免除了项目专属 .eslintrc 文件的需要，其中包括不使用分号、2 空格缩进和使用单引号等规则。

**--fix** 标志会自动就地修复可修复的问题。该工具可以检查作为参数传入的文件，或递归扫描当前目录。对于使用实验性 JavaScript 语法的项目，可以指定 babel-eslint 等自定义解析器。

# CAVEATS

风格规则固定。不可定制。无分号风格。

# HISTORY

**standard** 由 **Feross Aboukhadijeh** 创建，是一个强制统一风格的零配置 JavaScript 检查器。

# INSTALL

```brew: brew install standard```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[eslint](/man/eslint)(1), [prettier](/man/prettier)(1), [jshint](/man/jshint)(1)
