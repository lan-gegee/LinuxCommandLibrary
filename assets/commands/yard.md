# TAGLINE

Ruby 文档生成器

# TLDR

**生成文档**

```yard doc```

**启动服务器**

```yard server```

**列出未文档化的对象**

```yard stats --list-undoc```

**为特定文件生成文档**

```yard doc [lib/**/*.rb]```

**为 gem 生成文档**

```yard gems```

**显示某个类或方法的文档**

```yard ri [ClassName]```

# SYNOPSIS

**yard** _command_ [_options_]

# PARAMETERS

**doc**
> 生成文档。

**server**
> 启动服务器。

**stats**
> 显示统计信息。

**gems**
> 为 gem 生成文档。

**ri**
> 显示文档。

**diff**
> 显示文档的变化。

**--list-undoc**
> 列出未文档化的对象。

# DESCRIPTION

**yard**（Yay! A Ruby Documentation Tool）从 Ruby 源代码生成 API 文档。它解析类、模块和方法上方特殊格式的注释，生成带有交叉引用和搜索功能的可浏览 HTML 文档。

YARD 在注释中使用自己的标签语法（如 **@param**、**@return**、**@example**）来描述方法签名、返回类型和用法示例。它还支持 Markdown 等标记格式，用于注释中的自由格式文档。

**server** 子命令会启动一个本地 Web 服务器，便于开发过程中实时浏览文档。**stats** 子命令报告文档覆盖率，**--list-undoc** 则识别未编写文档的代码。模板控制 HTML 输出的布局，可以自定义或完全替换。

# CAVEATS

仅适用于 Ruby。注释中使用 YARD 语法。需要安装 gem。

# HISTORY

**YARD**（Yay! A Ruby Documentation Tool）作为 RDoc 的现代化替代品而创建。

# SEE ALSO

[rdoc](/man/rdoc)(1), [ri](/man/ri)(1), [ruby](/man/ruby)(1), [gem](/man/gem)(1), [bundle](/man/bundle)(1)
