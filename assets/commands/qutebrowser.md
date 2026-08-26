# TAGLINE

带 Vim 键位绑定的键盘驱动浏览器

# TLDR

**启动浏览器**

```qutebrowser```

**打开 URL**

```qutebrowser [https://example.com]```

**在新窗口中打开**

```qutebrowser --target window [https://example.com]```

**以临时 basedir 启动**

```qutebrowser --temp-basedir```

**设置配置项**

```qutebrowser --set [content.javascript.enabled] [false]```

# SYNOPSIS

**qutebrowser** [_options_] [_urls_...]

# DESCRIPTION

**qutebrowser** 是一款采用 Vim 风格键位绑定的键盘驱动 Web 浏览器。它基于 QtWebEngine，追求极简与键盘操作效率。

该浏览器可通过 Python 配置文件和命令进行深度定制，深受偏好键盘中心工作流的用户欢迎。

# PARAMETERS

**-t**, **--target** _type_
> URL 的打开方式（tab、tab-bg、window）。

**-T**, **--temp-basedir**
> 使用临时目录。

**-s** _opt_ _value_, **--set** _opt_ _value_
> 设置配置项。

**-r** _session_, **--restore** _session_
> 恢复会话。

**-B** _dir_, **--basedir** _dir_
> 基础目录。

**--debug**
> 调试模式。

# KEY BINDINGS

**o**: 打开 URL
**O**: 在新标签页打开
**d**: 关闭标签页
**j/k**: 滚动
**h/l**: 历史记录
**f**: 跟随提示链接
**yy**: 复制 URL
**/**: 搜索
**:**: 命令模式

# CAVEATS

部分网站可能无法正常工作（WebEngine 限制）。扩展支持有限。键位绑定有学习成本。Qt 依赖体积较大。

# HISTORY

**qutebrowser** 由 **Florian Bruhin** 自 **2013 年**起开发。它填补了 uzbl、vimperator 等键盘驱动浏览器的空缺，同时提供现代的网页引擎支持。

# INSTALL

```dnf: sudo dnf install qutebrowser```

```pacman: sudo pacman -S qutebrowser```

```apk: sudo apk add qutebrowser```

```zypper: sudo zypper install qutebrowser```

```nix: nix profile install nixpkgs#qutebrowser```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[firefox](/man/firefox)(1), [chromium](/man/chromium)(1), [surf](/man/surf)(1), [w3m](/man/w3m)(1)
