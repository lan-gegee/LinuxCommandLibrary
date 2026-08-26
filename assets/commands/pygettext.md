# TAGLINE

从 Python 代码中提取可翻译字符串

# TLDR

**提取可翻译字符串**

```pygettext [script.py]```

**指定输出文件**

```pygettext -o [messages.pot] [script.py]```

**从目录中提取**

```pygettext -d [domain] [src/]```

**包含 docstring**

```pygettext -D [script.py]```

# SYNOPSIS

**pygettext** [_options_] _files_...

# PARAMETERS

**-o**, **--output** _file_
> 输出文件名。

**-d**, **--domain** _name_
> 文本域名称。

**-p**, **--output-dir** _dir_
> 输出目录。

**-D**, **--docstrings**
> 提取 docstring。

**-k** _keyword_
> 额外要查找的关键字。

**-n**, **--add-location**
> 包含 file:line 注释。

# DESCRIPTION

**pygettext** 从 Python 源代码中提取可翻译字符串。它搜索以 _()、gettext() 及类似函数标记的字符串，并创建 POT 模板文件。

属于 Python 标准库的一部分。

# EXAMPLES

```bash
# Basic extraction
pygettext -o messages.pot *.py

# From directory
pygettext -d myapp -p locale src/*.py

# Include docstrings
pygettext -D -o docs.pot module.py

# Custom keywords
pygettext -k N_ -k ngettext:1,2 app.py
```

# MARKING STRINGS

```python
from gettext import gettext as _

message = _("This will be translated")
print(_("Hello, world!"))
```

# OUTPUT FORMAT (POT)

```
#: script.py:10
msgid "Hello, world!"
msgstr ""
```

# CAVEATS

属于 Python 自带工具。需要更多功能请使用 xgettext 或 Babel。输出的是模板文件，翻译人员据此创建 .po 文件。

# HISTORY

pygettext 是 **Python** 国际化工具集的一部分，为 Python 实现 gettext 字符串提取。

# SEE ALSO

[xgettext](/man/xgettext)(1), [msgfmt](/man/msgfmt)(1), [gettext](/man/gettext)(1), [babel](/man/babel)(1)
