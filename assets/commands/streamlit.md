# TAGLINE

用 Python 脚本构建数据 Web 应用

# TLDR

**运行 Streamlit 应用**

```streamlit run [app.py]```

**以指定端口运行**

```streamlit run [app.py] --server.port [8501]```

**带参数运行**

```streamlit run [app.py] -- [--arg1] [--arg2]```

**显示配置**

```streamlit config show```

**创建 hello 应用**

```streamlit hello```

**清除缓存**

```streamlit cache clear```

**显示版本**

```streamlit version```

# SYNOPSIS

**streamlit** [_run_] [_config_] [_cache_] [_options_] [_file_] [_-- args_]

# PARAMETERS

**run** _FILE_
> 运行 Streamlit 应用。

**hello**
> 运行演示应用。

**config show**
> 显示配置。

**cache clear**
> 清除缓存。

**version**
> 显示版本。

**--server.port** _PORT_
> 服务器端口。

**--server.address** _ADDR_
> 服务器地址。

**--server.headless** _BOOL_
> 不打开浏览器运行。

**--browser.serverAddress** _ADDR_
> 浏览器访问的服务器地址。

**--theme.base** _THEME_
> 主题（light/dark）。

**--global.developmentMode** _BOOL_
> 开发模式。

# DESCRIPTION

**streamlit** 从 Python 脚本创建 Web 应用。数据应用、仪表板和机器学习演示无需任何 Web 开发知识即可构建。

应用就是使用 Streamlit API 的 Python 脚本。滑块、按钮和文本输入等控件只需一次函数调用即可添加。

热重载会在代码更改时自动更新应用。开发工作流快速且具有交互性。

缓存装饰器可避免对昂贵操作的重复计算。数据加载和模型推理的结果在多次重跑之间会被缓存。

部署选项包括 Streamlit Community Cloud，它免费托管来自 GitHub 的应用。也支持自行托管。

组件（Components）可以扩展功能。生态系统提供自定义控件、可视化和集成方案。

# CAVEATS

不适合复杂的 Web 应用。布局控制有限。会话状态需要显式管理。大型应用可能出现性能问题。

# HISTORY

**Streamlit** 由 **Adrien Treuille**、**Thiago Teixeira** 和 **Amanda Kelly** 于 **2019 年**创建。它迅速成为数据科学原型开发的热门工具，并于 **2022 年**被 **Snowflake** 收购。

# INSTALL

```nix: nix profile install nixpkgs#streamlit```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gradio](/man/gradio)(1), [dash](/man/dash)(1), [flask](/man/flask)(1), [python](/man/python)(1)
