# TAGLINE

基于 Chromium 的终端浏览器

# TLDR

**打开一个 URL**

```carbonyl [https://example.com]```

**无需本地安装，在 Docker 中运行**

```docker run --rm -ti fathyb/carbonyl [https://youtube.com]```

**通过 npm 全局安装**

```npm install --global carbonyl```

**退出**正在运行的浏览器

```press [q]```

# SYNOPSIS

**carbonyl** [_url_]

# DESCRIPTION

**carbonyl** 是一款完全运行在终端中的基于 Chromium 的浏览器。它是 Chromium 的一个分支，其渲染管线被改造为输出 Unicode 方块字符和 ANSI 颜色转义序列，而不是把像素推送到窗口服务器。这使它能够通过 SSH 会话或在无图形显示的 kiosk 模式控制台中，以 60 FPS 运行音频、视频、WebGL、WebGPU、JavaScript 和动画。

与传统文本浏览器（lynx、w3m、elinks）不同，carbonyl 会像 Chromium 一样完整渲染 DOM 和 CSS，因此页面布局的表现与桌面浏览器一致。每个终端单元格使用 U+2584（下半方块）配合前景色和背景色编码两个上下堆叠的像素，从而实现（列数 x 2）乘以（行数 x 2）像素的有效分辨率。

# CAVEATS

尚不支持浏览器扩展或直接下载文件。广告拦截和密码管理需借助外部代理或其他浏览器完成。CPU 占用随 FPS 和页面复杂度而变化；包含持续动画的页面会让终端不断重绘而持续忙碌。

# HISTORY

**carbonyl** 由 **Fathy Boundjadj** 于 **2022 年**发布，是一个实验性的 Chromium 分支。作为在终端模拟器中运行现代 Web 应用（包括视频和游戏）的概念验证，它引起了广泛关注。

# INSTALL

```aur: yay -S carbonyl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[browsh](/man/browsh)(1), [lynx](/man/lynx)(1), [w3m](/man/w3m)(1), [elinks](/man/elinks)(1)
