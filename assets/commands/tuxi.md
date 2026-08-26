# TAGLINE

在终端快速获取 Google 答案

# TLDR

**搜索 Google 获取答案**

```tuxi [search_terms]```

**显示无格式的原始输出**

```tuxi -r [search_terms]```

**显示所有有效答案**

```tuxi -a [search_terms]```

**打印查询的前几条 URL**

```tuxi -u [search_terms]```

**隐藏建议只显示结果**

```tuxi -q [search_terms]```

**用指定语言搜索**

```tuxi -l LANG_[language_code] [search_terms]```

**显示版本**

```tuxi -v```

# SYNOPSIS

**tuxi** [_OPTIONS_] [_SEARCH_TERMS_...]

# PARAMETERS

**-r**
> 原始格式输出（无颜色和格式）。

**-q**
> 安静模式（抑制 "Did you mean?" 建议和问候语）。

**-a**
> 显示所有有效答案。

**-u**
> 打印查询的前几条 URL。

**-b**
> 根据查询关键词选择最佳答案（实验性）。

**-l** _LANG_code_
> 覆盖搜索语言（例如 LANG_en_US、LANG_fr_FR）。

**-d**
> 打印调试信息。

**-s**
> 将 HTML 结果保存到缓存。

**-c**
> 使用最近的缓存结果而不是重新抓取。

**-p**
> 禁用管道支持。

**-v**
> 显示版本信息。

**-h**
> 显示帮助信息。

# DESCRIPTION

**tuxi** 是一个命令行工具，它抓取 Google 搜索结果，为查询提供即时、简洁的答案。它会提取精选摘要（featured snippet）和知识面板信息，直接在终端中显示答案。

该工具适合快速核实事实，无需打开浏览器即可获得答案。它依赖 **pup**（HTML 解析器）、**recode**（字符集转换）和 **jq**（JSON 处理器）作为依赖项。

# ENVIRONMENT

**TUXI_LANG**=_lang_
> 设置默认搜索语言。

**TUXI_DELAY**=_int_
> 调整答案检测之间的延迟（默认：250ms）。

# CAVEATS

依赖于 Google 的 HTML 结构，后者可能随时变更。可能被 Google 的速率限制或 CAPTCHA 拦截。需要联网。结果是抓取的，不一定总是准确。需要安装 **pup**、**recode** 和 **jq**。

# HISTORY

**tuxi** 由 **Bugswriter** 创建，旨在提供一种快速轻量的方式，在终端中直接从 Google 获取答案，避免浏览器的开销。

# SEE ALSO

[ddgr](/man/ddgr)(1), [googler](/man/googler)(1), [curl](/man/curl)(1), [jq](/man/jq)(1)
