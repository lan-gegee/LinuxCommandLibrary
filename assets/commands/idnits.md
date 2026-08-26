# TAGLINE

检查 Internet-Draft 的格式问题

# TLDR

**检查 Internet-Draft**

```idnits [draft.txt]```

**详细输出**

```idnits --verbose [draft.txt]```

**按提交要求检查**

```idnits --submitcheck [draft.txt]```

**显示年份警告**

```idnits --year [2024] [draft.txt]```

# SYNOPSIS

**idnits** [_options_] _file_

# PARAMETERS

_FILE_
> 要检查的 Internet-Draft 文件。

**--verbose**
> 详细输出。

**--submitcheck**
> 严格的提交检查。

**--year** _YEAR_
> 设置版权年份。

**--nowarn** _WARN_
> 禁用特定警告。

**--help**
> 显示帮助信息。

# DESCRIPTION

**idnits** 检查 Internet-Draft 的格式问题。它在提交之前验证 IETF 文档的格式要求。

该工具检查 RFC 格式、样板文本、参考文献以及常见错误。它帮助作者准备用于 IETF 提交的草案。

# CAVEATS

IETF 专用工具。格式规则会变化。要求纯文本格式。

# HISTORY

idnits 由 **IETF** 开发，用于帮助作者验证 Internet-Draft 的格式。

# INSTALL

```brew: brew install idnits```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[aspell](/man/aspell)(1)
