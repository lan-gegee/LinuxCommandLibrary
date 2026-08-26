# TAGLINE

原生基于 Vite 的 JavaScript 测试框架

# TLDR

以监视模式**运行测试**（开发时的默认行为）

```vitest```

**运行一次测试**后退出

```vitest run```

**带覆盖率运行测试**

```vitest --coverage```

**运行指定的测试文件**

```vitest [path/to/test.spec.ts]```

**运行名称匹配某模式的测试**

```vitest -t "[pattern]"```

**运行特定目录中的测试**

```vitest [path/to/tests]```

**以 UI 模式运行**（基于浏览器的界面）

```vitest --ui```

**更新快照**

```vitest -u```

# SYNOPSIS

**vitest** [**run**|**watch**|**bench**] [_options_] [_filters_...]

# PARAMETERS

**run**
> 运行一次测试，不进入监视模式。

**watch**
> 以监视模式运行测试，文件变更时重新执行。

**bench**
> 运行基准测试。

**--coverage**
> 启用代码覆盖率报告（v8 或 istanbul）。

**-t**, **--testNamePattern** _pattern_
> 只运行名称匹配该模式的测试。

**--ui**
> 在浏览器中打开 Vitest UI，以交互方式查看测试。

**-u**, **--update**
> 更新快照文件。

**--reporter** _name_
> 指定报告器：default、verbose、dot、json、junit。

**--config** _file_
> 配置文件的路径。

**--root** _dir_
> 项目的根目录。

**--environment** _env_
> 测试环境：node、jsdom、happy-dom。

**--threads**
> 启用多线程（默认：true）。

**--browser**
> 以浏览器模式运行测试。

**--passWithNoTests**
> 即使没有找到测试也成功退出。

**--bail** _n_
> 在 n 个测试失败后停止。

# DESCRIPTION

**Vitest** 是一个由 Vite 驱动的新一代 JavaScript/TypeScript 测试框架。它凭借原生 ES 模块支持实现快速的测试执行，提供类似 HMR 的智能监视模式，并提供与 Jest 兼容的 API 以便轻松迁移。

该框架与 Vite 共享配置、转换器、解析器和插件，使测试可以使用与应用相同的设置。它支持通过 JSDOM 或 happy-dom 进行 DOM 模拟，支持 Vue、React、Svelte 等框架的组件测试，还支持基于浏览器的测试。

Vitest 在开发环境中自动进入监视模式，在 CI 中则进入运行模式。配置可以放在 vitest.config.ts 中，也可以放在现有 vite.config.ts 的 test 属性下。内置功能包括快照测试、基于 Tinyspy 的模拟，以及通过 v8 或 istanbul 实现的代码覆盖率统计。

# CAVEATS

要求 Node.js 18 或更高版本。监视模式在大型项目上可能占用较高的 CPU；应合理配置忽略规则。部分 Jest 特性的实现略有差异。浏览器模式需要额外的设置。

# HISTORY

**Vitest** 由 **Anthony Fu** 和 **Vite** 团队创建，首个稳定版于 **2022 年 12 月**发布。它的诞生是为了满足与 Vite 开发服务器和构建流水线原生集成的测试框架这一需求。该项目迅速获得采用，成为基于 Vite 的应用的推荐测试方案。

# SEE ALSO

[jest](/man/jest)(1), [mocha](/man/mocha)(1), [npm](/man/npm)(1), [vite](/man/vite)(1)
