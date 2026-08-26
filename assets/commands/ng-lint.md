# TAGLINE

对 Angular 项目源代码执行静态检查

# TLDR

**检查项目**

```ng lint```

**检查指定项目**

```ng lint [project-name]```

**自动修复问题**

```ng lint --fix```

**以指定格式输出**

```ng lint --format json```

# SYNOPSIS

**ng** **lint** [_project_] [_options_]

# PARAMETERS

**--fix**
> 自动修复静态检查发现的问题。

**--format** _format_
> 输出格式（stylish、json 等）。

**--force**
> 即使存在检查错误也返回成功。

**--silent**
> 抑制输出。

**--cache**
> 复用检查缓存，跳过自上次运行后未变更的文件。

**--max-warnings** _N_
> 当报告的警告多于 _N_ 个时判定失败（退出码 1）。

# DESCRIPTION

**ng lint** 在 Angular 工作区上运行已配置的 linter。自 Angular 12 起，默认的 linter 是 **ESLint**（通过 **@angular-eslint** 插件提供）；更早版本使用的是 **TSLint**，现已被弃用。

该命令会遵循 **angular.json** 中定义的 **lint** 目标，因此各项目级的覆盖配置（自定义规则集、tsconfig 变体、文件 glob 匹配）都会被自动采用。不带项目名运行时，会对所有含有 **lint** 目标的项目进行检查。

# CAVEATS

需要在 **angular.json** 中配置好 lint 目标（从 TSLint 迁移时可由 **ng add @angular-eslint/schematics** 创建）。**--fix** 会直接改写源文件；请事先提交或暂存改动。**--force** 只是让构建流水线得以继续，并不会屏蔽检查报告。

# SEE ALSO

[ng](/man/ng)(1), [eslint](/man/eslint)(1)
