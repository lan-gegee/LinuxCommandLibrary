# TAGLINE

基于正则表达式的交互式代码库重构工具

# TLDR

在目录中**交互式地进行正则替换**

```codemod -m -d [directory] '[old_pattern]' '[new_pattern]'```

**替换特定文件类型**

```codemod --extensions [php,html] '[pattern]' '[replacement]'```

**只搜索不替换（编辑模式）**

```codemod -m -d [directory] '[pattern]'```

**不经询问接受所有更改**

```codemod --accept-all '[pattern]' '[replacement]'```

**仅统计匹配数**

```codemod --count '[pattern]' [directory]```

# SYNOPSIS

**codemod** [_options_] _pattern_ [_replacement_] [_path_]

# DESCRIPTION

**codemod** 协助完成需要人工监督和判断的大规模代码库重构。与全自动的查找替换工具不同，codemod 以交互方式呈现每一个潜在更改，显示彩色 diff 并询问是接受、拒绝还是手动编辑该修改。

这种交互方式非常适合复杂的重构任务，例如跨数百个文件重命名函数、更新 API 调用，或在上下文很重要的场景中现代化代码模式。该工具使用 Python 正则表达式进行模式匹配，并显示足够的周边代码以便做出明智决定。

codemod 由 Facebook 开发并作为开源软件发布，专为该公司庞大的 PHP 和 JavaScript 代码库设计。虽然原始项目现已归档，但它开创了交互式重构工作流，后来被 fastmod 和 jscodeshift 等工具借鉴。

# PARAMETERS

**-m**
> 显示匹配处更多的上下文

**-d** _directory_
> 从指定目录开始搜索

**--extensions** _list_
> 只处理具有这些扩展名的文件

**--accept-all**
> 不经询问接受所有更改

**--count**
> 只统计匹配数，不做修改

**--editor** _editor_
> 用于手动编辑的编辑器

**--exclude-paths** _pattern_
> 排除匹配模式的路径

**--include-extensionless**
> 处理没有扩展名的文件

# INTERACTIVE PROMPTS

**y** - 接受更改
**n** - 拒绝更改
**e** - 在 $EDITOR 中编辑
**q** - 退出
**a** - 接受所有剩余更改

# RELATED TOOLS

**jscodeshift**
> 基于 JavaScript/TypeScript AST 的 codemod 工具包

**fastmod**
> Facebook 出品的快速 Rust 实现

# CAVEATS

使用 Python 正则表达式语法。复杂的转换可能需要通过 Python API 编写脚本。项目已归档；新项目请考虑 fastmod 或 jscodeshift。

# SEE ALSO

[sed](/man/sed)(1), [perl](/man/perl)(1), [fastmod](/man/fastmod)(1)

# RESOURCES

```[Source code](https://github.com/facebookarchive/codemod)```

<!-- verified: 2026-06-22 -->
