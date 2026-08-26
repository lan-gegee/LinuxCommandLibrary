# TAGLINE

Firefox WebExtension 开发工具

# TLDR

**在 Firefox 中运行扩展**

```web-ext run```

**在指定的 Firefox 中运行**

```web-ext run --firefox=[/path/to/firefox]```

**构建扩展**

```web-ext build```

**对扩展进行 lint 检查**

```web-ext lint```

**签名扩展**

```web-ext sign --api-key=[key] --api-secret=[secret]```

**从指定目录运行**

```web-ext run -s [extension/]```

**以详细输出运行**

```web-ext run -v```

# SYNOPSIS

**web-ext** _command_ [_--source-dir dir_] [_options_]

# PARAMETERS

**run**
> 在浏览器中运行。

**build**
> 打包扩展。

**lint**
> 检查问题。

**sign**
> 签名以便分发。

**-s**, **--source-dir** _DIR_
> 扩展源码目录。

**--firefox** _PATH_
> Firefox 可执行文件。

**-v**, **--verbose**
> 详细输出。

**--api-key** _KEY_
> AMO API 密钥。

**--api-secret** _SECRET_
> AMO API 秘钥。

# DESCRIPTION

**web-ext** 是 Mozilla 官方用于开发、测试和发布 Firefox WebExtension 的命令行工具。它提供运行、构建、lint 检查和签名扩展的命令，简化了扩展开发工作流。

run 命令启动 Firefox 并临时加载扩展，当源文件变化时自动重新加载，实现快速开发迭代。build 命令将扩展打包为 .zip 文件，可直接提交到 addons.mozilla.org（AMO）；lint 命令检查常见问题，例如 manifest 错误和已弃用的 API 用法。

sign 命令将扩展提交给 Mozilla 签名，这是在 AMO 之外分发所必需的。身份验证需要从 Firefox 开发者门户获取的 AMO API 密钥和秘钥。

# CAVEATS

仅针对 Firefox 的工具。签名需要 AMO 账户。某些功能需要 Nightly 版本。

# HISTORY

**web-ext** 由 **Mozilla** 为 WebExtension 开发而创建。它简化了扩展开发工作流。

# INSTALL

```brew: brew install web-ext```

```nix: nix profile install nixpkgs#web-ext```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[firefox](/man/firefox)(1), [npm](/man/npm)(1)
