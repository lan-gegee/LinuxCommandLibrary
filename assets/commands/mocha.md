# TAGLINE

JavaScript 测试框架

# TLDR

**运行测试**

```mocha```

**运行指定文件**

```mocha [test/spec.js]```

**监视模式**

```mocha --watch```

**使用 grep 过滤运行**

```mocha --grep "[pattern]"```

**报告器样式**

```mocha --reporter [spec]```

**递归测试**

```mocha --recursive```

# SYNOPSIS

**mocha** [_options_] [_files_]

# PARAMETERS

_FILES_
> 要运行的测试文件。

**--watch**
> 监视文件变更。

**--grep** _PATTERN_
> 过滤测试。

**--reporter** _NAME_
> 输出格式。

**--recursive**
> 包含子目录。

**--timeout** _MS_
> 测试超时时间。

**--help**
> 显示帮助信息。

# DESCRIPTION

**mocha** 是一个 JavaScript 测试框架。它可以在 Node.js 和浏览器中运行。

该工具提供 BDD/TDD 两种测试风格，支持异步测试和多种报告器。

# CAVEATS

需要 Node.js。需要配合断言库使用。通过 .mocharc 进行配置。

# HISTORY

Mocha 由 **TJ Holowaychuk** 创建，是一个功能丰富的 JavaScript 测试框架。

# INSTALL

```nix: nix profile install nixpkgs#mocha```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jest](/man/jest)(1), [npm](/man/npm)(1)
