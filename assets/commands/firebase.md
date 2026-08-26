# TAGLINE

Firebase 平台管理 CLI

# TLDR

**登录 Firebase**

```firebase login```

**初始化项目**

```firebase init```

**部署所有服务**

```firebase deploy```

**只部署 hosting**

```firebase deploy --only hosting```

**只部署 functions**

```firebase deploy --only functions```

**启动本地模拟器**

```firebase emulators:start```

**列出项目**

```firebase projects:list```

# SYNOPSIS

**firebase** [_options_] _command_

# PARAMETERS

**login**
> 使用 Google 账户进行身份验证。

**logout**
> 登出。

**init**
> 在目录中初始化 Firebase 项目。

**deploy**
> 部署到 Firebase 服务。

**--only** _services_
> 只部署指定的服务。

**serve**
> 启动本地开发服务器。

**emulators:start**
> 启动 Firebase 模拟器。

**projects:list**
> 列出可用项目。

**use** _project_
> 切换当前活动的项目。

**functions:log**
> 查看 Cloud Functions 日志。

**hosting:disable**
> 停用项目的托管（hosting）。

# CONFIGURATION

**firebase.json**
> 项目配置，涵盖托管规则、函数设置和数据库规则。

**.firebaserc**
> 项目别名以及当前选择的活动项目。

# DESCRIPTION

**firebase** 是 Firebase——Google 的移动与 Web 应用平台——官方 CLI。它负责管理 Hosting、Cloud Functions、Firestore、Realtime Database、Authentication 等 Firebase 服务的部署。

该 CLI 承担项目初始化、借助模拟器进行的本地开发以及部署流程。它与 Google Cloud 集成，支持多环境配置。

# CAVEATS

需要 Node.js（可通过 `npm install -g firebase-tools` 安装）。身份验证需要 Google 账户。部分服务（Cloud Functions、更高用量的 Firestore）要求 Blaze 计费方案。Firestore 与 Realtime Database 模拟器需要 Java 支持。

# HISTORY

Firebase 创立于 **2011 年**，并在 **2014 年**被 **Google** 收购。Firebase CLI 从最初只能做基础的托管部署，逐步发展到支撑整个不断扩展的 Firebase 平台，包括 Cloud Functions、Firestore 以及完善的本地模拟体系。

# SEE ALSO

[gcloud](/man/gcloud)(1), [npm](/man/npm)(1), [node](/man/node)(1)
