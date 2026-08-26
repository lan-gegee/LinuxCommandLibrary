# TAGLINE

捕捉文本中不敏感、欠考虑的表达。

# TLDR

**检查**文件中的不敏感用语

```alex [file.md]```

检查**多个文件**

```alex [file1.md] [file2.md]```

从 **stdin** 检查

```echo "This is crazy" | alex --stdin```

使用**自定义配置**检查

```alex --config [.alexrc] [file.md]```

以 **JSON** 输出

```alex --reporter json [file.md]```

# SYNOPSIS

**alex** [_options_] [_files_...]

# DESCRIPTION

**alex** 捕捉文本中不敏感、欠考虑的表达。它能帮你找出文本中偏向性别、制造对立、涉及种族、漠视宗教或其他不平等措辞。

该工具专为文档、README 文件及其他书面内容设计，帮助团队在项目中维护包容性语言。

# PARAMETERS

**--stdin**
> 从标准输入读取

**--text**
> 将输入视为纯文本（而非 markdown）

**--html**
> 查找并将输入视为 HTML（.html、.htm）文件

**--mdx**
> 查找并将输入视为 MDX（.mdx）文件

**--config** _file_
> 配置文件路径

**--reporter** _type_
> 输出格式：json、compact 或 default

**--quiet**
> 只报告错误，不显示没有问题的文件

**--why**
> 显示每条消息的来源（由哪条规则触发）

**--diff**
> 忽略未更改的行（在 CI 中只针对 diff 报告很有用）

**-v**, **--version**
> 显示版本

**-h**, **--help**
> 显示帮助文本

# CONFIGURATION

**.alexrc**
> 项目根目录下的 JSON 或 YAML 配置文件。定义允许的术语、自定义规则和语言偏好。

**.alexignore**
> 列出要排除检查的文件和目录，使用 gitignore 风格的模式。

# CAVEATS

可能产生误报；请结合上下文审查建议。技术术语或专有名词可能被错误标记。可通过配置将特定术语加入白名单。

# HISTORY

**alex** 由 Titus Wormer 创建，于 **2015** 年作为 unified.js 生态的一部分发布。它旨在把包容性语言的自动化检查引入开发工作流。

# INSTALL

```brew: brew install alexjs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[write-good](/man/write-good)(1), [proselint](/man/proselint)(1), [vale](/man/vale)(1)

# RESOURCES

```[Source code](https://github.com/get-alex/alex)```

```[Homepage](https://alexjs.com/)```

<!-- verified: 2026-06-11 -->
