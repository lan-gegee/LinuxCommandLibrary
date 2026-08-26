# TAGLINE

有主见的 JavaScript 和 TypeScript linter

# TLDR

**检查 JavaScript**

```xo```

**检查特定文件**

```xo [file.js]```

**修复问题**

```xo --fix```

**指定空格缩进**

```xo --space```

**打印配置**

```xo --print-config```

# SYNOPSIS

**xo** [_--fix_] [_--space_] [_options_] [_files_]

# PARAMETERS

**--fix**
> 自动修复问题。

**--space**
> 使用空格缩进。

**--semicolon**
> 要求分号。

**--prettier**
> 使用 Prettier。

**--print-config**
> 显示配置。

# DESCRIPTION

**xo** 是一个构建于 ESLint 之上的有主见的 JavaScript 和 TypeScript linter。它提供零配置的代码检查体验，内置一套精心挑选的严格规则，无需手动设置 ESLint 即可实现一致的高质量代码。

该工具内置 TypeScript 支持，并可选集成 Prettier 以同时进行代码检查和格式化。**--fix** 选项自动修复可修复的问题，而 **--space** 将默认的制表符缩进切换为空格缩进。通过默认采用严格且经过斟酌的规则，xo 免去了团队逐条讨论和配置 lint 规则的必要。

# CAVEATS

规则较为武断。需要 Node.js。基于 ESLint。

# HISTORY

**xo** 由 **Sindre Sorhus** 创建，是一个带有合理默认值的有主见的 ESLint 封装。

# SEE ALSO

[eslint](/man/eslint)(1), [standard](/man/standard)(1), [prettier](/man/prettier)(1)
