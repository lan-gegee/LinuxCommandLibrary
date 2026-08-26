# TAGLINE

instancez 的 CLI，instancez 是单二进制的 Supabase 替代品

# TLDR

**安装** inz CLI

```curl -fsSL https://get.instancez.ai | sh```

**初始化**新项目（创建 instancez.yaml）

```inz init```

**以内嵌 Postgres 启动开发服务器**

```inz dev --embedded-pg```

**针对已有数据库启动开发服务器**

```inz dev```

**以生产模式提供服务**

```inz serve```

**将 instancez.yaml 部署到** instancez Cloud

```inz cloud deploy```

# SYNOPSIS

**inz** \<command\> [_options_]

# DESCRIPTION

**inz** 是 **instancez** 的命令行界面。instancez 是一个对 LLM 友好的单二进制后端，可作为许多 Supabase 用例的直接替代品。Schema、认证策略、存储桶和函数都在一个 **instancez.yaml** 文件中声明。文件发生变化时，instancez 会将其与线上数据库做差量比较，仅应用变化部分（包括删除），无需手写迁移脚本。

该二进制内嵌了一个控制台面板，支持 PostgREST 风格的 REST、认证（密码、魔法链接、OTP、匿名、OAuth、TOTP MFA）、SQL RPC、Node.js edge functions 以及带行级安全性的存储（本地或 S3）。现有的 **@supabase/supabase-js** 客户端可以直接指向 instancez 的 API URL 和 publishable key。**inz dev** 会预置角色、应用 schema 并提供 API 服务（默认 **http://localhost:8080**）；配合 **--embedded-pg** 则无需外部安装 Postgres。首次运行时会把 publishable key 和 secret key 写入 **.development.env**；若存在 **.production.env**，生产密钥将从其中加载。

# PARAMETERS

**init**
> 创建脚手架项目，包含 **instancez.yaml** 及示例表/函数。

**dev** [**--embedded-pg**]
> 运行支持实时 schema 重载的开发 API。**--embedded-pg** 会启动内嵌的 Postgres；否则需设置 **INSTANCEZ_DATABASE_URL**。

**serve**
> 运行生产服务器（自托管）。

**cloud deploy**
> 将 **instancez.yaml** 推送到托管的 instancez Cloud 项目。

# CAVEATS

尚不支持 Realtime/websockets。存储图像缩放仅支持 JPEG/PNG（不支持 WebP/AVIF）。不提供手机/SMS 认证。生产环境仍需要 Postgres（或云托管）；单二进制并非完整的多区域 Supabase 套件。从源码构建需要 Go 1.25+ 和 Node 22+ 才能内嵌控制台面板。

# HISTORY

**instancez** 是一个 Apache-2.0 项目，发布便携式 Go 二进制（**cmd/inz**），目标是声明式、AI 友好的后端脚手架，并与 Supabase 客户端兼容。

# SEE ALSO

[supabase](/man/supabase)(1), [curl](/man/curl)(1), [docker](/man/docker)(1)

# RESOURCES

```[Source code](https://github.com/instancez/instancez)```

```[Homepage](https://instancez.ai)```

```[Documentation](https://instancez.github.io)```

<!-- verified: 2026-07-21 -->
