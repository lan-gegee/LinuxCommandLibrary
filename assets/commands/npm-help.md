# TAGLINE

显示 npm 命令的文档

# TLDR

**查看某个命令的帮助**

```npm help [install]```

**按关键字搜索帮助主题**

```npm help-search [dependency]```

**在浏览器中打开帮助**

```npm help [command] --viewer browser```

**阅读 npm 概览**

```npm help npm```

**打开帮助索引**

```npm help help```

# SYNOPSIS

**npm** **help** [_topic_]

# PARAMETERS

_TOPIC_
> npm 命令名或一般性主题。若找不到完全匹配的页面，多个单词会组成短语交给 **man** 搜索。

**--viewer** _TYPE_
> 要使用的帮助查看器：_man_（Unix 上的默认值）、_browser_ 或 _woman_（Emacs）。Windows 上默认为 _browser_。

**--help**
> 显示 **help** 命令本身的帮助。

# DESCRIPTION

**npm help** 显示某个主题的 npm 手册页。默认在 Unix 上调用 **man**(1)，但使用 **--viewer browser** 时会在 docs.npmjs.com 打开渲染后的 HTML 页面。

如果没有完全匹配的结果，**npm help** 会退回到 **npm help-search**，后者对所有 npm man 页面进行关键字搜索，并输出按相关度排序的摘录。

# CAVEATS

_man_ 查看器需要可用的 **man** 安装。可用 **npm config set viewer browser** 永久更改默认查看器。

# HISTORY

npm help 让你可以从命令行访问 **npm 的文档**体系。

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [npm-docs](/man/npm-docs)(1)
