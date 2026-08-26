# TAGLINE

ProjectDiscovery 出品的新一代 web 爬行与爬取框架

# TLDR

**爬取一个 URL**

```katana -u [https://example.com]```

**使用无头浏览器爬取**

```katana -u [https://example.com] -headless```

**从文件爬取多个 URL**

```katana -list [urls.txt]```

**设置爬取深度**

```katana -u [https://example.com] -depth [3]```

**输出到文件**

```katana -u [https://example.com] -o [output.txt]```

**启用 JavaScript 解析**

```katana -u [https://example.com] -js-crawl```

# SYNOPSIS

**katana** [_options_]

# PARAMETERS

**-u** _url_
> 要爬取的目标 URL。

**-list** _file_
> 包含要爬取 URL 的文件。

**-headless**
> 使用无头浏览器进行爬取。

**-depth** _int_
> 最大爬取深度。

**-js-crawl**
> 启用 JavaScript 文件爬取。

**-o** _file_
> 结果输出文件。

**-json**
> 以 JSON 格式输出。

**-silent**
> 静默模式，最少输出。

# DESCRIPTION

**katana** 是 ProjectDiscovery 出品的新一代 web 爬行与爬取框架。它同时支持标准和无头浏览器两种爬取模式，对 JavaScript 密集型应用尤为有效。专为安全研究和信息收集而设计。

# INSTALL

```brew: brew install katana```

```nix: nix profile install nixpkgs#katana```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[httpx](/man/httpx)(1), [nuclei](/man/nuclei)(1), [subfinder](/man/subfinder)(1)
