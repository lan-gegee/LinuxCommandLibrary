# TAGLINE

将 Markdown 和 HTML 报告发布到 Cloudflare Pages

# TLDR

**启动**本地管理界面

```npx pagecast```

**设置** Cloudflare Pages 项目

```npx pagecast pages setup --project [name]```

**发布** HTML 或 Markdown 文件

```npx pagecast publish "[/absolute/path/to/report.html]"```

以密码保护方式**发布**

```npx pagecast publish "[/absolute/path/to/report.html]" --password "[password]"```

**部署**静态站点目录

```npx pagecast pages deploy "[$(pwd)/dist]" --project [name]```

# SYNOPSIS

**npx pagecast** [_subcommand_] [_options_]

# PARAMETERS

**pages setup**
> 配置新的 Cloudflare Pages 项目

**publish** _file_
> 将单个 HTML 或 Markdown 报告发布到 Cloudflare Pages

**pages deploy** _dir_
> 部署完整的静态站点目录

**--project** _name_
> Cloudflare Pages 项目名称

**--account** _id_
> Cloudflare 账户 ID（用于多账户场景）

**--password** _pass_
> 为已发布的页面添加密码保护

**--no-password**
> 移除已发布页面的现有密码保护

**--branch** _name_
> 部署分支名称（默认：main）

**--json**
> 输出机器可读的 JSON，便于 CI/CD 和脚本处理

# DESCRIPTION

**pagecast** 将 Markdown 和 HTML 报告发布到用户自己的 Cloudflare Pages 账户，使其可通过公开 URL 访问。它既提供基于浏览器的管理界面（位于 `http://127.0.0.1:4173`）用于管理已发布的链接，也提供 CLI 接口用于自动化和 CI/CD 流水线。

可以为每次部署添加或移除密码保护。`--json` 标志可为智能体和脚本化工作流提供结构化输出。

无需全局安装：`npx pagecast` 会按需使用 Node.js 下载并运行该软件包。

# CAVEATS

需要 Node.js 20 或更高版本以及 Cloudflare 账户。传给 `publish` 子命令的路径必须是绝对路径。发布前必须先完成一次性的 Cloudflare Pages 项目设置。

# SEE ALSO

[npx](/man/npx)(1), [wrangler](/man/wrangler)(1)

# RESOURCES

```[Source code](https://github.com/Amal-David/pagecast)```

<!-- verified: 2026-06-20 -->
