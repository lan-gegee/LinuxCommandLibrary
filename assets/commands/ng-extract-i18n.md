# TAGLINE

从 Angular 模板提取国际化消息

# TLDR

**提取消息**

```ng extract-i18n```

**以指定格式提取**

```ng extract-i18n --format [xlf]```

**提取到指定输出路径**

```ng extract-i18n --output-path [locale/]```

**为指定项目提取**

```ng extract-i18n --project [my-app]```

# SYNOPSIS

**ng extract-i18n** [_options_]

# PARAMETERS

**--format** _format_
> 输出格式（xlf、xlf2、xmb、json、arb）。

**--output-path** _path_
> 输出目录。

**--out-file** _file_
> 输出文件名。

**--project** _name_
> 要从中提取消息的项目。

**--progress**
> 显示进度。

# DESCRIPTION

**ng extract-i18n** 从 Angular 模板中提取国际化消息，为本地化工作流程生成翻译源文件。支持 XLIFF、XMB 和 JSON 格式。

# SEE ALSO

[ng](/man/ng)(1), [ng-build](/man/ng-build)(1)
