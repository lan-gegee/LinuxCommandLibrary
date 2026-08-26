# TAGLINE

Bun 内置的 Jest 兼容测试运行器

# TLDR

**运行所有测试**

```bun test```

**运行特定文件中的测试**

```bun test [path/to/test.ts]```

**运行匹配模式的测试**

```bun test --test-name-pattern "[pattern]"```

**以监视模式运行测试**

```bun test --watch```

**更新快照**

```bun test --update-snapshots```

**运行并统计覆盖率**

```bun test --coverage```

**输出 JUnit XML 报告**

```bun test --reporter=junit --reporter-outfile=[results.xml]```

**使用超时时间运行**

```bun test --timeout [5000]```

# SYNOPSIS

**bun test** [_options_] [_files_]

# DESCRIPTION

**bun test** 是 Bun 内置的测试运行器，提供 Jest 兼容的 API。它开箱即用地支持 TypeScript 和 JSX、快照测试、mock、生命周期钩子以及监视模式。

测试在 Bun 运行时中执行，性能明显优于传统的 JavaScript 测试运行器。

# PARAMETERS

**--watch**
> 文件变化时重新运行测试

**--update-snapshots**
> 更新快照文件

**--coverage**
> 启用代码覆盖率报告

**--test-name-pattern** _pattern_
> 只运行匹配模式的测试

**--timeout** _ms_
> 测试超时时间（毫秒）

**--reporter** _type_
> 输出格式（default、junit 等）

**--reporter-outfile** _file_
> 将报告输出写入文件

**--bail** _n_
> 在 n 个测试失败后停止

**--rerun-each** _n_
> 将每个测试运行 n 次。

**--preload** _module_
> 在测试运行前预加载一个模块。

**--only**
> 只运行标记了 `test.only` 的测试。

# TEST FILE PATTERNS

测试运行器搜索匹配以下模式的文件：
- *.test.{js,jsx,ts,tsx}
- *_test.{js,jsx,ts,tsx}
- *.spec.{js,jsx,ts,tsx}
- *_spec.{js,jsx,ts,tsx}

# API

测试使用来自 bun:test 模块的 **describe**、**test/it**、**expect**、**beforeAll**、**beforeEach**、**afterEach**、**afterAll** 和 **mock** 函数。

# CAVEATS

虽然以 Jest 兼容为目标，但并非所有 Jest 特性都已实现。在 CI 中运行时会自动启用 GitHub Actions 注解。某些 Jest 特有的插件可能无法工作。

# INSTALL

```pacman: sudo pacman -S bun```

```brew: brew install bun```

```nix: nix profile install nixpkgs#bun```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bun](/man/bun)(1), [bun-run](/man/bun-run)(1), [jest](/man/jest)(1), [vitest](/man/vitest)(1)
