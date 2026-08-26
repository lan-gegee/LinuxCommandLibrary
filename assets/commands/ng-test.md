# TAGLINE

为 Angular 项目运行单元测试

# TLDR

**运行单元测试**

```ng test```

**为指定项目运行测试**

```ng test [project-name]```

**运行测试但不监视**文件变更

```ng test --no-watch```

**运行测试并生成代码覆盖率**

```ng test --code-coverage```

**在指定浏览器中运行测试**

```ng test --browsers [ChromeHeadless]```

**执行单次测试后退出**

```ng test --watch=false```

# SYNOPSIS

**ng test** [_project_] [_options_]

# PARAMETERS

_project_
> 要为其运行单元测试的项目。默认为默认项目。

**--code-coverage**
> 在 coverage/ 目录下生成代码覆盖率报告。

**--watch**
> 文件变化时重新运行测试（默认：true）。

**--browsers** _browsers_
> 覆盖测试时要启动的浏览器（例如 ChromeHeadless）。

**--configuration** _name_
> 目标构建配置。

**--karma-config** _path_
> Karma 配置文件的路径。

**--include** _glob_
> 要纳入测试范围的文件的 glob 匹配模式。

**--help**
> 显示帮助信息。

# DESCRIPTION

**ng test** 会编译应用并使用已配置的测试运行器运行单元测试。默认情况下，Angular CLI 使用 **Karma** 作为测试运行器、**Jasmine** 作为测试框架。测试在浏览器中执行，源代码发生变化时会自动重新运行。

该命令默认监视文件变更，从而在开发过程中提供持续测试的工作流。

# CAVEATS

需要先配置好测试运行器。默认使用 Karma，但也可以配置 Jest 等替代方案。基于浏览器的测试要求已安装相应浏览器。CI 环境建议使用无头模式。属于 Angular CLI 的一部分。

# HISTORY

**ng test** 自 Angular CLI 首次发布起就是其中一员，默认采用 **Karma** 加 **Jasmine** 的测试组合。后续 Angular 版本陆续探索了 **Jest**、**Web Test Runner** 等替代测试运行器的支持。

# SEE ALSO

[ng](/man/ng)(1), [ng-e2e](/man/ng-e2e)(1), [jest](/man/jest)(1)
