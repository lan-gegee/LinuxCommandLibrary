# TAGLINE

Ruby 行为驱动开发测试框架

# TLDR

**运行所有 spec**

```rspec```

**运行指定的文件**

```rspec [spec/models/user_spec.rb]```

**运行指定的行**

```rspec [spec/models/user_spec.rb:25]```

**按标签运行**

```rspec --tag [focus]```

**排除某个标签**

```rspec --tag ~[slow]```

**格式化输出**

```rspec --format documentation```

**运行失败的 spec**

```rspec --only-failures```

**随机顺序**

```rspec --order random```

# SYNOPSIS

**rspec** [_--format fmt_] [_--tag tag_] [_options_] [_files_]

# PARAMETERS

**--format** _FORMAT_
> 输出格式。

**--tag** _TAG_
> 运行带指定标签的示例。

**--only-failures**
> 只运行先前失败的示例。

**--order** _ORDER_
> 执行顺序。

**--fail-fast**
> 首次失败即停止。

**--profile** _N_
> 显示最慢的示例。

**--dry-run**
> 只展示任务而不真正执行。

**-e**, **--example** _PATTERN_
> 匹配示例名称。

# DESCRIPTION

**rspec** 是 Ruby 的行为驱动开发（BDD）测试框架。它提供易于阅读的测试语法。

spec 文件描述预期的行为。示例（example）验证代码是否符合这些期望。

匹配器（matcher）提供富有表现力的断言方式。包括 should、expect 以及各种比较方法。

标签用于组织和筛选测试。可以聚焦于特定类别，或跳过耗时的测试。

失败跟踪让你可以只重新运行失败的测试。从而加快调试循环。

格式化器（formatter）以多种样式输出结果。documentation 格式会显示嵌套的 describe 块。

# CAVEATS

需要安装 rspec gem。Rails 应用应使用 rspec-rails。大型测试套件可能运行缓慢。

# HISTORY

**RSpec** 由 **Steven Baker** 和 **David Chelimsky** 于 **2005 年**前后创建。它在 Ruby 中开创了 BDD 风格的测试，并影响了其他语言的测试框架。

# INSTALL

```pacman: sudo pacman -S ruby-rspec-core```

```apk: sudo apk add ruby-rspec-core```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ruby](/man/ruby)(1), [rake](/man/rake)(1), [minitest](/man/minitest)(1), [cucumber](/man/cucumber)(1)
