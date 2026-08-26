# TAGLINE

在 npm registry 中搜索与给定关键词匹配的软件包

# TLDR

**搜索软件包**

```npm search [query]```

**使用多个关键词搜索**

```npm search [react] [router]```

**以 JSON 格式输出**

```npm search --json [query]```

**限制结果数量**

```npm search --searchlimit=[20] [query]```

**长格式输出**

```npm search --long [query]```

# SYNOPSIS

**npm search** [_options_] [_terms_...]

# PARAMETERS

**--json**
> JSON 输出。

**--long**
> 扩展信息。

**--searchlimit** _n_
> 限制结果数量。

**--searchopts** _opts_
> 搜索选项。

**--searchexclude** _terms_
> 排除的关键词。

**--registry** _url_
> 搜索指定的 registry。

# DESCRIPTION

**npm search** 在 npm registry 中搜索与给定关键词匹配的软件包。它会搜索软件包名称、描述和关键字。

结果包括软件包名、描述、作者、日期、版本和关键字。

# EXAMPLE OUTPUT

```
NAME         DESCRIPTION                    AUTHOR    DATE
lodash       Lodash modular utilities       jdalton   2023-01
express      Fast web framework             dougwilson 2022-10
```

# ALTERNATIVES

```bash
# Use npms.io for better search
# Web: https://www.npmjs.com/search?q=query

# Use npm-search-cli
npms query
```

# CAVEATS

registry 搜索可能较慢。结果可能与网站有所不同。复杂搜索建议使用网页界面。

# HISTORY

npm search 自早期版本起就是 npm 的一部分，让你可以从命令行访问 npm registry 的搜索功能。

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [npm-view](/man/npm-view)(1)
