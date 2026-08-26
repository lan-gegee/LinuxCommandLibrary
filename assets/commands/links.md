# TAGLINE

终端下的文本模式网页浏览器

# TLDR

**访问**网站

```links https://example.com```

将渲染后的页面以纯文本形式**输出**到 stdout

```links -dump https://example.com```

**输出**时指定屏幕**宽度**

```links -width 80 -dump https://example.com```

以**匿名**模式浏览

```links -anonymous https://example.com```

查看页面**源**代码

```links -source https://example.com```

# SYNOPSIS

**links** [_options_] [_url_]

# DESCRIPTION

**links** 是终端下的文本模式网页浏览器。它支持表格、框架和基本表单的渲染，适合在没有图形环境的服务器上浏览文档或使用网页。

# PARAMETERS

**-anonymous**
> 应用匿名浏览的限制（不允许访问本地文件或下载）

**-dump**
> 将渲染后的页面以纯文本写入 stdout

**-source**
> 将页面源码写入 stdout

**-width** _number_
> 设置 dump 输出的屏幕宽度

**-codepage** _codepage_
> 将 dump 输出转换为指定字符集

**-enable-cookies** _0|1_
> 启用（1）或禁用（0）Cookie

**-force-html**
> 将类型未知的文件视为 HTML 而非纯文本

**-html-numbered-links** _0|1_
> 在文本模式下为链接编号以便快速选择

**-html-margin** _spaces_
> 设置文本模式的边距宽度

**-no-connect**
> 作为独立实例运行，而不是连接到已有实例

**-download-dir** _path_
> 设置默认下载目录

**-max-connections** _max_
> 最大并发连接数（默认：10）

**-receive-timeout** _sec_
> 接收超时时间（秒）（默认：120）

# NAVIGATION KEYS

**Up/Down**
> 滚动页面

**Tab/Shift+Tab**
> 在链接之间导航

**Left/Right**
> 在历史记录中后退/前进

**Enter**
> 跟随选中的链接

**g**
> 跳转到 URL

**/**
> 在页面中搜索文本

**Esc**
> 打开菜单

**d**
> 下载当前链接

**q**
> 退出浏览器

# INSTALL

```apt: sudo apt install links```

```dnf: sudo dnf install links```

```pacman: sudo pacman -S links```

```apk: sudo apk add links```

```zypper: sudo zypper install links```

```brew: brew install links```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[links2](/man/links2)(1), [lynx](/man/lynx)(1), [w3m](/man/w3m)(1)
