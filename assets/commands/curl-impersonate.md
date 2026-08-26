# TAGLINE

带浏览器 TLS 指纹伪装的 curl

# TLDR

**伪装成 Chrome**

```curl_chrome124 [https://example.com]```

**伪装成 Firefox**

```curl_ff120 [https://example.com]```

**伪装成 Safari**

```curl_safari17_0 [https://example.com]```

输出到文件

```curl_chrome124 -o [output.html] [https://example.com]```

带自定义请求头

```curl_chrome124 -H "[Header: value]" [https://example.com]```

跟随重定向

```curl_chrome124 -L [https://example.com]```

# SYNOPSIS

**curl_chrome\*** [_curl_options_] _url_

**curl_ff\*** [_curl_options_] _url_

**curl_safari\*** [_curl_options_] _url_

# DESCRIPTION

**curl-impersonate** 是经过修改的 curl，能伪装浏览器的 TLS 和 HTTP 指纹。它发出的请求与 Chrome、Firefox、Edge 或 Safari 完全一致，可绕过基于 TLS 指纹的机器人检测。

# WRAPPER SCRIPTS

**curl_chrome110**, **curl_chrome124**
> 伪装成 Chrome

**curl_ff109**, **curl_ff120**
> 伪装成 Firefox

**curl_safari15_5**, **curl_safari17_0**
> 伪装成 Safari

**curl_edge101**
> 伪装成 Edge

# VERSIONS

**Chrome 版本**：伪装 Chrome、Edge、Safari

**Firefox 版本**：伪装 Firefox

# LIBCURL API

```c
curl_easy_impersonate(curl, "chrome116", 1);
```

设置目标浏览器以及是否使用默认请求头。

# DOCKER USAGE

```
docker run --rm lwthiker/curl-impersonate:0.6-chrome \
  curl_chrome124 https://example.com
```

# CAVEATS

某些 curl 选项会改变 TLS 特征，可能导致被检测到。封装脚本会设置必要的请求头。自定义选项可能破坏伪装效果。

# INSTALL

```pacman: sudo pacman -S curl-impersonate```

```nix: nix profile install nixpkgs#curl-impersonate```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[curl](/man/curl)(1), [httpie](/man/httpie)(1), [wget](/man/wget)(1)

# RESOURCES

```[Source code](https://github.com/lwthiker/curl-impersonate)```

<!-- verified: 2026-06-26 -->
