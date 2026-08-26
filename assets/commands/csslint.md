# TAGLINE

CSS 代码质量检查工具

# TLDR

对 CSS 文件进行**检查**

```csslint [file.css]```

按指定规则作为错误进行检查

```csslint --errors=[rule1,rule2] [file.css]```

按指定规则作为警告进行检查

```csslint --warnings=[rule1,rule2] [file.css]```

以指定格式输出

```csslint --format=[compact|json|text] [file.css]```

忽略指定规则

```csslint --ignore=[rule1,rule2] [file.css]```

# SYNOPSIS

**csslint** [_options_] _file.css_ [_files..._]

# PARAMETERS

**--errors** _rules_
> 以逗号分隔、视为错误的规则列表。

**--warnings** _rules_
> 以逗号分隔、视为警告的规则列表。

**--ignore** _rules_
> 以逗号分隔、要忽略的规则列表。

**--format** _format_
> 输出格式：text、compact、json、checkstyle-xml、lint-xml、junit-xml。

**--list-rules**
> 显示所有可用规则。

**--quiet**
> 抑制 `csslint: There are <n> problems` 这一行汇总信息。

**--version**
> 打印 csslint 版本后退出。

**--help**
> 显示用法信息。

# DESCRIPTION

**csslint** 是一款检查 CSS 代码质量的工具。它能发现低效选择器、浏览器兼容性问题和风格错误等潜在问题。该工具会检查可能导致跨浏览器问题、性能问题或维护困难的模式。

规则按严重程度分类，涵盖选择器性能、盒模型兼容性、已知浏览器缺陷和最佳实践等主题。csslint 可以集成到构建流程和持续集成工作流中。

# CONFIGURATION

**.csslintrc**
> JSON 配置文件，用于自定义规则和严重级别。

# SEE ALSO

[sass](/man/sass)(1), [prettier](/man/prettier)(1), [postcss](/man/postcss)(1)
