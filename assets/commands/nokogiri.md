# TAGLINE

Ruby 的 HTML/XML 解析器 CLI

# TLDR

**解析 HTML 文件**

```nokogiri [file.html]```

**抓取并解析 URL**

```nokogiri [https://example.com]```

**使用 CSS 选择器解析**

```nokogiri [file.html] -e "[doc.css('h1').text]"```

**解析 XML**

```nokogiri [file.xml] --type xml```

**进入 IRB 会话**并将文档绑定为 `doc`

```nokogiri [file.html]```

**依据 RelaxNG schema 校验**

```nokogiri [file.xml] --rng [schema.rng]```

# SYNOPSIS

**nokogiri** [_options_] [_file_or_url_]

# PARAMETERS

_FILE_OR_URL_
> 要解析的 HTML/XML 文件路径或 URL。若省略，则从 stdin 读取文档。

**-e** _CODE_
> 对解析后的文档（绑定名为 **doc**）执行 Ruby 代码 _CODE_。

**--type** _TYPE_
> 文档类型：**xml** 或 **html**。默认根据内容类型/扩展名自动检测。

**-C** _FILE_
> 加载自定义的 Ruby 初始化文件。默认：**~/.nokogirirc**。

**-E**, **--encoding** _ENCODING_
> 以指定的字符编码读取输入（如 UTF-8、ISO-8859-1）。

**--rng** _URI_OR_PATH_
> 用给定的 RelaxNG schema 校验文档。

**-v**, **--version**
> 显示 Nokogiri 版本。

**-?**, **--help**
> 显示帮助。

# DESCRIPTION

**nokogiri** 是 Nokogiri Ruby gem 的命令行前端；Nokogiri 是由 libxml2 和 libxslt 支撑的高速 HTML/XML 解析器。该 CLI 会将文件、URL 或 stdin 解析为 **Nokogiri::HTML::Document** 或 **Nokogiri::XML::Document**（绑定为 **doc**），然后让你进入 IRB 会话，或运行通过 **-e** 提供的 Ruby 片段，以便用 CSS 选择器（**doc.css**）或 XPath（**doc.xpath**）进行查询。

# CAVEATS

需要 Ruby 和 **nokogiri** gem（`gem install nokogiri`）。**-i** 交互标志并不属于现代 CLI——在 TTY 上直接运行 **nokogiri** _file_ 默认会进入 IRB；传入 **-e** 则以非交互方式运行。抓取 URL 使用的是 **open-uri**，因此 HTTPS 站点要求底层 Ruby 构建支持 OpenSSL。

# HISTORY

**Nokogiri**（日语意为"锯"）由 **Aaron Patterson** 和 **Mike Dalessio** 于 **2008 年**创建，作为比 Hpricot 更快、基于 libxml2 的替代品。它是安装量最大的 Ruby gem 之一，并附带一个用于临时解析和校验的小型 CLI。

# INSTALL

```apt: sudo apt install ruby-nokogiri```

```pacman: sudo pacman -S ruby-nokogiri```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xmllint](/man/xmllint)(1), [pup](/man/pup)(1), [xidel](/man/xidel)(1)
