# TAGLINE

用 Go 编写的快速静态站点生成器

# TLDR

**创建新站点**

```hugo new site [site-name]```

**构建站点**

```hugo```

**创建新内容**

```hugo new content [posts/my-post.md]```

**启动开发服务器**

```hugo server```

**构建时包含草稿**

```hugo --buildDrafts```

**为生产环境进行压缩优化构建**

```hugo --minify```

**构建到指定目录**

```hugo -d [/path/to/output]```

# SYNOPSIS

**hugo** [_command_] [_options_]

# PARAMETERS

**new content**
> 创建新的内容文件。

**new site**
> 创建新的站点骨架。

**server**
> 启动内置的开发服务器。

**-b**, **--baseURL** _URL_
> 站点根路径的主机名和路径。

**-D**, **--buildDrafts**
> 包含标记为草稿的内容。

**-E**, **--buildExpired**
> 包含过期内容。

**-F**, **--buildFuture**
> 包含发布日期在未来的内容。

**-d**, **--destination** _DIR_
> 写入文件的文件系统路径。

**--minify**
> 压缩受支持的输出格式（HTML、XML 等）。

**--gc**
> 构建后运行清理任务（移除未使用的缓存文件）。

**--cleanDestinationDir**
> 从目标目录移除静态目录中不存在的文件。

**-t**, **--theme** _THEME_
> 要使用的主题。

**--logLevel** _LEVEL_
> 日志级别（debug、info、warn、error）。

# DESCRIPTION

**Hugo** 是一个用 Go 编写的快速静态站点生成器。它基于 Markdown 内容，借助模板和主题构建网站。

Hugo 速度极快，可在数秒内构建数千个页面。它通过主题、分类法和短代码（shortcode）支持复杂站点。

# CAVEATS

Go 模板语法有一定学习曲线。主题兼容性参差不齐。不支持动态内容。

# HISTORY

Hugo 由 **Steve Francia** 于 **2013 年**创建，使用 Go 编写，作为 Jekyll 的快速替代方案。注意：用于创建内容的 `hugo new` 已被弃用；请改用 `hugo new content`。

# INSTALL

```apt: sudo apt install hugo```

```dnf: sudo dnf install hugo```

```pacman: sudo pacman -S hugo```

```apk: sudo apk add hugo```

```zypper: sudo zypper install hugo```

```brew: brew install hugo```

```nix: nix profile install nixpkgs#hugo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[hugo-server](/man/hugo-server)(1), [jekyll](/man/jekyll)(1), [hexo](/man/hexo)(1)
