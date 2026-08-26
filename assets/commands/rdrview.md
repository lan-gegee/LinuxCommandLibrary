# TAGLINE

从网页提取正文内容（阅读模式）

# TLDR

从 URL **提取**可读内容

```rdrview "[url]"```

**在文本浏览器中打开**提取出的 HTML

```rdrview -B [lynx] "[url]"```

**禁用沙箱**（仅限不支持的平台；请了解相关风险）

```rdrview --disable-sandbox "[url]"```

# SYNOPSIS

**rdrview** [*options*] *URL*

# DESCRIPTION

**rdrview** 从网页中提取正文内容，类似于现代浏览器的阅读视图。其算法改编自 Mozilla 的 Readability（后者基于 Arc90 的 readability.js）。输出面向 **lynx** 等终端浏览器或更干净的 HTML 归档，在终端 RSS 工作流中很受欢迎。

在 Linux 上，HTML 解析在使用 **seccomp** 沙箱的子进程中运行（OpenBSD 上为 Pledge，FreeBSD 上为 Capsicum），以降低恶意 HTML 带来的风险。依赖包括 libxml2、libcurl 以及平台沙箱库。

# PARAMETERS

*URL*

> 要获取并处理的页面。

**-B** *browser*

> 用于显示结果的浏览器/命令（在没有 mailcap 默认项时需要）。

**--disable-sandbox**

> 不使用沙箱运行（不推荐；在某些不支持沙箱的平台上必需）。

安装后请查看 **man rdrview** 以了解你所构建版本的完整选项集。

# CAVEATS

提取质量取决于网站布局和繁重的客户端渲染。这个工具是较年轻的 C 代码——优先使用带沙箱的构建版本。macOS 可能缺少沙箱实现。将不受信任的 URL 送入本地工具时务必小心。

# INSTALL

```nix: nix profile install nixpkgs#rdrview```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lynx](/man/lynx)(1), [w3m](/man/w3m)(1), [curl](/man/curl)(1), [readable](/man/readable)(1)

# RESOURCES

```[Source code](https://github.com/eafer/rdrview)```

<!-- verified: 2026-07-19 -->
