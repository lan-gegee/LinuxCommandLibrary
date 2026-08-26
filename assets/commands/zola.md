# TAGLINE

基于 Rust 的快速静态网站生成器

# TLDR

**创建新站点**

```zola init [site_name]```

**构建站点**

```zola build```

**启动开发服务器**

```zola serve```

**在指定端口上提供服务**

```zola serve -p [8080]```

**使用自定义输出目录构建**

```zola build -o [public]```

**只检查错误而不构建**

```zola check```

**检查站点结构，跳过外部链接校验**

```zola check --skip-external-links```

**启动服务并自动打开浏览器**

```zola serve --open```

**在非空目录中初始化站点**

```zola init --force [site_name]```

# SYNOPSIS

**zola** [_options_] _command_ [_arguments_]

# SUBCOMMANDS

**init** _name_
> 创建新站点骨架

**build**
> 构建静态网站

**serve**
> 启动支持实时重载的本地开发服务器

**check**
> 校验站点而不构建

**completion** _shell_
> 生成 Shell 补全

# PARAMETERS

**-c**, **--config** _file_
> 配置文件路径（默认：config.toml）

**-r**, **--root** _dir_
> 站点根目录

**-o**, **--output-dir** _dir_
> 构建的输出目录

**-p**, **--port** _port_
> serve 命令使用的端口（默认：1111）

**-i**, **--interface** _addr_
> 服务器绑定的网络接口（默认：127.0.0.1）

**-u**, **--base-url** _url_
> 覆盖配置中的 base URL

**--open**
> 自动在浏览器中打开网站（仅限 serve）

**--force**
> 直接覆盖已存在的输出目录，不做提示

**--drafts**
> 包含草稿内容

**--skip-external-links**
> 跳过外部链接校验（仅限 check）

# DESCRIPTION

**Zola** 是一个用 Rust 编写的快速静态网站生成器。它把内容（Markdown 文件）、模板（Tera 模板）和配置组合成静态网站。

站点结构包括：
- **content/** - 按分节组织的 Markdown 文件
- **templates/** - Tera HTML 模板
- **static/** - 直接复制的静态资源
- **themes/** - 可选的可下载主题
- **config.toml** - 站点配置

Zola 的特性包括语法高亮、自动目录、分类法（标签、分类）、短代码以及内置的 Sass 编译。

开发服务器提供实时重载，文件变化时会自动重新构建。

# CAVEATS

Zola 使用 Tera 模板引擎，与 Hugo、Jekyll 或其他静态网站生成器不同。模板迁移需要重写。

没有插件系统。可扩展性仅限于短代码和模板。

页面众多的大型站点构建耗时可能较为明显，不过 Zola 总体上比同类工具更快。

# HISTORY

**Zola** 由 **Vincent Prouillet** 创建，最初名为 **Gutenberg**。**2018 年**更名为 Zola（得名于 Emile Zola）。它用 Rust 编写，定位为 Hugo 和 Jekyll 等静态网站生成器的单二进制替代方案，强调简洁与构建速度。

# INSTALL

```pacman: sudo pacman -S zola```

```apk: sudo apk add zola```

```zypper: sudo zypper install zola```

```brew: brew install zola```

```nix: nix profile install nixpkgs#zola```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[hugo](/man/hugo)(1), [jekyll](/man/jekyll)(1), [mdbook](/man/mdbook)(1)
