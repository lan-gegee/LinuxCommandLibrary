# TAGLINE

转义 XML 特殊字符

# TLDR

**转义 XML 特殊字符**

```xml escape [text]```

**从 stdin 转义**

```echo "[<text>]" | xml escape```

# SYNOPSIS

**xml escape** [_options_] [_text_]

# PARAMETERS

_text_
> 要转义的文本。

# DESCRIPTION

**xml escape** 转义 XML 特殊字符。属于 xmlstarlet 工具集。将 <、>、&、'、" 转换为对应的 XML 实体，以便安全地嵌入 XML 文档。

# INSTALL

```dnf: sudo dnf install xmlstarlet```

```pacman: sudo pacman -S xmlstarlet```

```apk: sudo apk add xmlstarlet```

```zypper: sudo zypper install xmlstarlet```

```brew: brew install xmlstarlet```

```nix: nix profile install nixpkgs#xmlstarlet```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xml-unescape](/man/xml-unescape)(1), [xml-format](/man/xml-format)(1)
