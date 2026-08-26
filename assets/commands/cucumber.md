# TAGLINE

行为驱动开发测试运行器

# TLDR

**运行所有 feature**

```cucumber```

**运行指定的 feature 文件**

```cucumber [features/login.feature]```

按行号**运行指定场景**

```cucumber [features/login.feature]:[10]```

**按标签运行**

```cucumber --tags @[smoke]```

排除某标签后运行

```cucumber --tags "not @[wip]"```

**生成 HTML 报告**

```cucumber --format html --out [report.html]```

**试运行**（只检查语法）

```cucumber --dry-run```

# SYNOPSIS

**cucumber** [_options_] [_files_|_dirs_]

# DESCRIPTION

**cucumber** 运行以 Gherkin 编写的行为驱动开发（BDD）测试。Gherkin 是一种人类可读、用于描述软件行为的语言。它将自然语言描述的场景连接到可执行的步骤定义。

Feature 以 Given/When/Then 格式描述行为，开发者和利益相关者都能看懂。步骤定义则用 Ruby（或其他语言）实现实际的测试逻辑。

# PARAMETERS

**-t**, **--tags** _expr_
> 运行匹配标签表达式的场景。

**-f**, **--format** _type_
> 输出格式（pretty、progress、html、json）。

**-o**, **--out** _file_
> 将输出写入文件。

**-r**, **--require** _path_
> 在执行前加载指定文件。

**-d**, **--dry-run**
> 只检查语法而不运行。

**-s**, **--strict**
> 遇到未定义或待实现的步骤时判定失败。

**--retry** _n_
> 将失败的场景重试 n 次。

**-p**, **--profile** _name_
> 使用 cucumber.yml 中具名的 profile。

**--order** _type_
> 运行顺序（defined、random）。

# CONFIGURATION

**cucumber.yml**
> 定义可复用的 profile，其中预置了适用于不同测试运行的配置项。

# CAVEATS

步骤定义必须与场景步骤精确匹配。步骤之间共享的状态可能导致测试不稳定。Gherkin 语法错误会中断执行。大型测试套件下速度较慢。

# HISTORY

**Cucumber** 由 **Aslak Hellesoy** 于 **2008 年**创建，灵感来自 RSpec 和 JBehave。它让规格说明能以平实语言直接执行，从而推广了 BDD。它最初基于 Ruby，如今已有 Java、JavaScript 等众多语言的实现。

# INSTALL

```nix: nix profile install nixpkgs#cucumber```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rspec](/man/rspec)(1), [jest](/man/jest)(1), [pytest](/man/pytest)(1)
