# TAGLINE

通过命令行从网站和本地工具获取结构化数据

# TLDR

**运行**站点命令（示例随目录更新而变化）

```autocli [site] [subcommand]```

通过安装脚本**安装**

```curl -fsSL https://raw.githubusercontent.com/nashsu/autocli/main/scripts/install.sh | sh```

**帮助** / 列出命令

```autocli --help```

# SYNOPSIS

**autocli** *command* [*args*]

# DESCRIPTION

**autocli** 是 OpenCLI 风格"公共命令"的 Rust 重写版，用一个二进制文件即可从众多网站（社交、视频、新闻等）抓取信息，并与本地工具（**gh**、**docker**、**kubectl**）集成。强调低内存占用和静态二进制安装。

命令目录会不断增长——请使用 **autocli --help** 和上游文档了解当前可用功能。

# PARAMETERS

*command*

> 站点或工具集成的名称。

全局选项涵盖 JSON 输出、基于浏览器的命令，以及必要时的身份验证。

# CAVEATS

网页抓取在 HTML 结构变化时会失效，且可能违反第三方服务条款。浏览器驱动的模式开销更大。抓取个人数据时请注意隐私问题。

# SEE ALSO

[curl](/man/curl)(1), [gh](/man/gh)(1), [http](/man/http)(1)

# RESOURCES

```[Source code](https://github.com/nashsu/AutoCLI)```

<!-- verified: 2026-07-19 -->
