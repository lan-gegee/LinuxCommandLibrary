# TAGLINE

以简洁为特色的 JavaScript 测试框架

# TLDR

**运行所有测试**

```jest```

**运行指定的测试文件**

```jest [path/to/test.js]```

**运行匹配模式的测试**

```jest -t "[pattern]"```

**以监视模式运行**

```jest --watch```

**生成覆盖率报告**

```jest --coverage```

**更新快照**

```jest -u```

**并行运行测试**

```jest --maxWorkers=[4]```

**只运行有改动的测试**

```jest --onlyChanged```

# SYNOPSIS

**jest** [_options_] [_files_...]

# DESCRIPTION

**jest** 是一款以简洁为特色的 JavaScript 测试框架。它在单个软件包中提供了测试运行器、断言、mock 和代码覆盖率功能。

该工具具有快照测试、并行执行和智能测试选择等特性。它适用于 React、Vue、Node.js 以及大多数 JavaScript 项目。

# PARAMETERS

**--watch**
> 监视模式，只关注有改动的文件。

**--watchAll**
> 监视所有文件。

**--coverage**
> 收集代码覆盖率。

**-t** _pattern_
> 运行名称匹配的测试。

**-u**, **--updateSnapshot**
> 更新快照。

**--maxWorkers** _n_
> 最大并行工作进程数。

**--onlyChanged**
> 只运行有改动的测试。

**--bail**
> 首次失败即停止。

**--verbose**
> 显示每个测试的结果。

**--config** _file_
> 配置文件。

**--ci**
> CI 模式设置。

# CAVEATS

默认的测试正则可能遗漏文件。快照需要人工审查。覆盖率统计可能漏掉边界情况。测试很多时内存占用较高。

# HISTORY

**Jest** 由 **Facebook**（Meta）创建，最初用于测试 React 应用。它于 **2014 年**前后发布，从 Jasmine 的基础演进而来，如今已成为最受欢迎的 JavaScript 测试框架之一，以其零配置理念著称。

# SEE ALSO

[npm](/man/npm)(1), [mocha](/man/mocha)(1), [vitest](/man/vitest)(1), [playwright](/man/playwright)(1)
