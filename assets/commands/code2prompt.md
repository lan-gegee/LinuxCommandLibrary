# TAGLINE

源码转 LLM 提示词转换器

# TLDR

从源码**生成提示词**并复制到剪贴板

```code2prompt [path/to/project]```

**使用自定义 Handlebars 模板**

```code2prompt [path] -t [template.hbs]```

**将输出写入文件**

```code2prompt [path] --output-file [prompt.txt]```

**包含特定文件模式**

```code2prompt [path] --include "[*.py,*.js]"```

**排除模式**

```code2prompt [path] --exclude "[node_modules,*.log]"```

**显示 token 数量**

```code2prompt [path] --tokens```

**从 git 暂存更改生成**

```code2prompt [path] --diff```

# SYNOPSIS

**code2prompt** [_options_] _path_

# PARAMETERS

**-t**, **--template** _FILE_
> 自定义 Handlebars 模板文件的路径。

**--include** _PATTERNS_
> 要包含的文件的 glob 模式，逗号分隔。

**--exclude** _PATTERNS_
> 要排除的文件的 glob 模式，逗号分隔。

**--exclude-from-tree**
> 从源码树展示中移除被排除的文件。

**--output-file** _FILE_
> 将生成的提示词写入文件而非剪贴板。

**--tokens**
> 显示生成的提示词的 token 数量。

**--encoding** _NAME_
> 要使用的分词器：cl100k（默认）、p50k、p50k_edit、r50k_base。

**--json**
> 以 JSON 格式输出结果。

**--diff**
> 包含暂存文件的 git diff。

**--git-diff-branch** _BRANCH_
> 包含分支之间的差异。

**--git-log-branch** _BRANCH_
> 包含某个分支的 git log。

**--line-number**
> 为源码行添加行号前缀。

**--no-codeblock**
> 不用 markdown 围栏代码块包裹代码。

# DESCRIPTION

**code2prompt** 将源码树转换为面向大语言模型（LLM）的结构化提示词。它递归遍历代码库，遵循 `.gitignore`，并将各文件连同文件树概览一起格式化输出。默认情况下，输出会被复制到剪贴板。

Handlebars 模板让你可以为特定工作流定制生成的提示词，例如代码审查、文档编写、重构或 PR 描述草拟。基于 tiktoken 兼容编码的 token 计数有助于让提示词保持在模型上下文限制之内。

Git 集成（`--diff`、`--git-diff-branch`、`--git-log-branch`）使生成聚焦于近期变更而非整个代码库的提示词变得简单。

# INSTALL

```brew: brew install code2prompt```

```nix: nix profile install nixpkgs#code2prompt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tree](/man/tree)(1), [find](/man/find)(1), [git](/man/git)(1)
