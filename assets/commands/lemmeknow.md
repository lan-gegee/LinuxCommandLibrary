# TAGLINE

识别神秘文本和编码字符串的最快方式

# TLDR

**识别字符串**

```lemmeknow "[string]"```

**从文件中识别字符串**

```lemmeknow [path/to/file]```

**以 JSON 格式输出结果**

```lemmeknow -j "[string]"```

# SYNOPSIS

**lemmeknow** [_options_] _input_

# PARAMETERS

**-j**, **--json**
> 以 JSON 格式输出结果。

**-b**, **--boundary**
> 仅匹配带有单词边界的字符串。

# DESCRIPTION

**lemmeknow** 是一个用于识别未知文本、编码字符串、哈希及其他数据模式的工具。它可以分析来自抓包数据、恶意软件或任何其他来源的硬编码字符串，判断它们代表什么类型的数据（例如 API 密钥、哈希值、编码值、IP 地址）。

它在文件分析上比 pywhat 快约 **33 倍**，对单个字符串快 **3 倍**。该工具还支持编译成 WebAssembly，以便在浏览器中使用。

# CAVEATS

识别基于模式匹配，对于含义模糊的字符串可能产生误报。

# HISTORY

**lemmeknow** 由 **swanandx** 创建，采用 **Rust** 编写。它同时以 CLI 工具和库两种形式提供。

# INSTALL

```brew: brew install lemmeknow```

```nix: nix profile install nixpkgs#lemmeknow```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[file](/man/file)(1)
