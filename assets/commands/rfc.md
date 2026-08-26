# TAGLINE

在终端阅读 IETF RFC

# TLDR

按编号**打开** RFC

```rfc [791]```

按关键字**搜索** RFC（如果构建版本支持）

```rfc [search-term]```

# SYNOPSIS

**rfc** *number*|*query*

# DESCRIPTION

**rfc** 在终端中获取并显示 IETF 征求意见稿（Request for Comments）文档，让你无需浏览器即可阅读协议规范。各实现通常通过 **$PAGER** 分页显示文本。来自 **bfontaine/rfc** 的广泛打包版本是一个围绕远程 RFC 文本源的小型 shell 封装。

# PARAMETERS

*number*

> 要检索的 RFC 编号（例如 **7231**）。

关键字搜索、本地缓存和离线镜像的行为取决于具体版本——运行 **rfc -h** 或阅读脚本头部说明。

# CAVEATS

除非配置了本地 RFC 集合，否则需要网络访问。输出为纯文本格式；某些 RFC 更适合在 IETF 网站上以 PDF/HTML 阅读。

# INSTALL

```pacman: sudo pacman -S rfc```

```nix: nix profile install nixpkgs#rfc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[curl](/man/curl)(1), [less](/man/less)(1), [man](/man/man)(1)

# RESOURCES

```[Source code](https://github.com/bfontaine/rfc)```

<!-- verified: 2026-07-19 -->
