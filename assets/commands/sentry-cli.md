# TAGLINE

Sentry 官方命令行界面

# TLDR

**登录** / 配置身份验证令牌

```sentry-cli login```

**创建 release**

```sentry-cli releases new [version]```

**为 release 上传 source map**

```sentry-cli sourcemaps upload -r [version] [path]```

**上传调试符号**（原生）

```sentry-cli debug-files upload [path]```

**列出最近的问题**

```sentry-cli issues list```

**显示子命令的帮助**

```sentry-cli [command] --help```

# SYNOPSIS

**sentry-cli** [*global-options*] *command* [*args*]

# DESCRIPTION

**sentry-cli** 是 [Sentry](https://sentry.io/) 的官方 CLI。它自动化管理 release、source map 和调试文件上传、部署，以及 CI/CD 中用到的各种账户/项目操作。配置使用环境变量（**SENTRY_AUTH_TOKEN**、**SENTRY_ORG**、**SENTRY_PROJECT** 等）和/或配置文件；参见 https://docs.sentry.io/cli/。

一个更新的面向智能体的 Sentry CLI 正在 https://cli.sentry.dev/ 开发中；在官方迁移路径公布之前，现有的 **sentry-cli** 仍是流水线中的稳定工具。

# PARAMETERS

常用的高级命令（具体集合会随时间增长）：

**login**

> 交互式身份验证设置。

**releases**

> 创建、定稿并管理 release。

**sourcemaps** / **debug-files**

> 上传客户端 source map 或原生调试信息文件。

**deploys**

> 为 release 记录部署事件。

**issues**

> 列出或管理问题。

**send-event**

> 发送测试/手动事件。

**info** / **projects** / **organizations**

> 查看账户元数据。

全局标志通常包括 **--auth-token**、**--log-level**，以及用于自托管服务器的 **--url**。对于已安装的主版本，请优先使用 **sentry-cli --help** 和在线文档。

# CAVEATS

需要具有相应权限范围的 Sentry 身份验证令牌。早于 24.11.1 的自托管 Sentry 版本可能需要 **sentry-cli** &lt; 3.x。部分功能仅限 SaaS。切勿提交身份验证令牌。

# INSTALL

```pacman: sudo pacman -S sentry-cli```

```brew: brew install sentry-cli```

```nix: nix profile install nixpkgs#sentry-cli```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[curl](/man/curl)(1), [npm](/man/npm)(1)

# RESOURCES

```[Source code](https://github.com/getsentry/sentry-cli)```

```[Documentation](https://docs.sentry.io/cli/)```

<!-- verified: 2026-07-19 -->
