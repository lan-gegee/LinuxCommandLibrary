# TAGLINE

已弃用的 TypeScript 代码检查工具

# TLDR

**检查文件**

```tslint [file.ts]```

**使用配置检查**

```tslint -c [tslint.json] [file.ts]```

**自动修复**

```tslint --fix [file.ts]```

**检查整个项目**

```tslint -p [tsconfig.json]```

**以 JSON 格式输出**

```tslint --format json [file.ts]```

**检查所有 TypeScript 文件**

```tslint -p . "[src/**/*.ts]"```

# SYNOPSIS

**tslint** [_-c config_] [_-p project_] [_--fix_] [_options_] _files_

# PARAMETERS

**-c** _FILE_
> 配置文件。

**-p** _FILE_
> 项目 tsconfig。

**--fix**
> 自动修复问题。

**--format** _FMT_
> 输出格式。

**-e** _PATTERN_
> 排除模式。

# DESCRIPTION

**TSLint** 曾是一个 TypeScript 静态分析工具，用于检查代码的可读性、可维护性和功能正确性。它通过可配置的规则来强制执行风格约定、发现潜在错误并推行最佳实践。

该工具支持自动修复许多规则违规，并与编辑器和 CI 系统集成。配置通过 tslint.json 文件管理，其中指定要启用的规则及其严重级别。

TSLint 于 2019 年被弃用，取而代之的是配合 **typescript-eslint** 插件的 **ESLint**，后者在采用更广泛的 ESLint 生态中提供了同样的 TypeScript 检查能力。

# CAVEATS

已被弃用，建议改用 ESLint。仅适用于 TypeScript。需要 Node.js。

# HISTORY

**TSLint** 曾是标准的 TypeScript 检查工具，直到 2019 年团队将其弃用，转向支持 TypeScript 的 **ESLint**。

# INSTALL

```aur: yay -S tslint```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[eslint](/man/eslint)(1), [tsc](/man/tsc)(1), [prettier](/man/prettier)(1)
