# TAGLINE

管理 twurl 的 Twitter API 账户

# TLDR

**列出已授权账户**

```twurl accounts```

**设置默认账户**

```twurl accounts -d [username]```

# SYNOPSIS

**twurl accounts** [_options_]

# PARAMETERS

**-d** _username_
> 设置默认账户。

# DESCRIPTION

**twurl accounts** 管理 twurl 中的 Twitter/X API 账户。列出已授权账户并在它们之间切换。是面向 Twitter API 的 OAuth 版 curl 工具 twurl 的一部分。

# INSTALL

```nix: nix profile install nixpkgs#twurl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[twurl](/man/twurl)(1), [curl](/man/curl)(1)
