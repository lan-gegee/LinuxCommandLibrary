# TAGLINE

用于编写 shell 脚本的 JavaScript 工具链

# TLDR

**运行** zx 脚本文件

```zx [script.mjs]```

**用 npx 直接运行**

```npx zx [script.mjs]```

**安装**软件包

```npm install -g zx```

脚本头部与命令执行示例：

```js
#!/usr/bin/env zx
await $`git status`
const branch = await $`git branch --show-current`
```

# SYNOPSIS

**zx** [*options*] *script*

# DESCRIPTION

**zx**（来自 Google）让你用 JavaScript 编写复杂 shell 脚本变得轻松愉快。它封装了 Node 的 **child_process**，借助 **$`cmd`** 标签模板实现安全的参数转义、合理的默认值和跨平台行为。脚本可以使用 async/await、**Promise.all** 处理并行任务，并享受整个 npm 生态。

可与 Node.js、Bun、Deno 及类似运行时配合使用。文档和各种安装变体（含 lite 版本）见 https://google.github.io/zx/。

# PARAMETERS

*script*

> **.mjs**/**.js** 脚本（在支持的环境下也可为 TypeScript）的路径。通常以 **#!/usr/bin/env zx** 开头。

**-h**, **--help** / **--version**

> 帮助与版本信息（已安装 CLI 的可用标志请查看 **zx --help**）。

在脚本内部，核心 API 就是 **$`command`**，外加游文档所载的各种辅助函数（**cd**、**fetch**、**question**、**sleep**、**nothrow** 等）。

# CAVEATS

并非 Google 官方支持的产品。需要 PATH 上有 JS 运行时。应优先用 **$** 模板做引号包裹/转义，避免字符串拼接带来的注入风险。复杂管道的行为仍受宿主 shell 影响。

# INSTALL

```brew: brew install zx```

```nix: nix profile install nixpkgs#zx```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[node](/man/node)(1), [bash](/man/bash)(1), [npm](/man/npm)(1)

# RESOURCES

```[Source code](https://github.com/google/zx)```

```[Homepage](https://google.github.io/zx/)```

```[Documentation](https://google.github.io/zx/)```

<!-- verified: 2026-07-19 -->
