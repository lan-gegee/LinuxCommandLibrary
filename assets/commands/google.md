# TAGLINE

从命令行搜索 Google（surfraw elvi）

# TLDR

**搜索 Google** 并在默认浏览器中打开结果页面

```google "[search query]"```

**手气不错**：直接跳到第一个结果

```google -lucky "[search query]"```

**搜索图片**

```google -images "[search query]"```

**搜索新闻**

```google -news "[search query]"```

**限制结果条数**

```google -results=[25] "[search query]"```

**搜索特定国家/地区的 Google 版本**

```google -country=[uk] "[search query]"```

# SYNOPSIS

**google** [_options_] _words_...

# PARAMETERS

**-l**, **-lucky**
> "手气不错"：直接跳转到第一个结果。

**-i**, **-images**
> 搜索 Google 图片（**-search=images** 的简写形式）。

**-v**, **-videos**
> 搜索 Google 视频。

**-m**, **-maps**
> 搜索 Google 地图。

**-n**, **-news**
> 搜索 Google 新闻。

**-G**, **-groups**
> 搜索 Google 网上论坛。

**-results=**_NUM_
> 要返回的搜索结果数量。

**-country=**_CODE_
> 要查询的地区性 Google 站点，使用 ISO 3166 两位字母国家代码表示（默认 **us**，即 google.com）。

**-safe=**_LEVEL_
> SafeSearch 过滤级别：**default**、**off**、**moderate** 或 **strict**。

# DESCRIPTION

**google** 是 **surfraw** 附带的"elvi"（搜索引擎配置）之一。运行它会根据参数拼出相应的 Google 搜索 URL，并在 **$BROWSER** 中打开，因此在浏览器未启动时不会发起任何查询。

不带查询词时，它会打开对应的 Google 首页（网页、图片、新闻等），而不是结果页面。如果没有安装独立的符号链接，也可以通过 **sr google** [_options_] _words_ 来调用。

# CAVEATS

需要安装 **surfraw** 软件包并配置好 **$BROWSER**。与 googler 或 ddgr 不同，它在浏览器中打开结果，而不是将结果打印到终端。

# HISTORY

**google** 是 **surfraw** 内置的 elvi 之一。surfraw 是面向多种网络搜索引擎的 Unix 命令行接口，最初由 **Julian Assange** 于 20 世纪 90 年代末编写，其后由 surfraw 社区维护。

# SEE ALSO

[googler](/man/googler)(1), [ddgr](/man/ddgr)(1)

# RESOURCES

```[Source code](https://gitlab.com/surfraw/Surfraw)```

```[Homepage](https://surfraw.org/)```

<!-- verified: 2026-07-17 -->
