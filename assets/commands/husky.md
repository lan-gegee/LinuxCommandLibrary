# TAGLINE

改进 JavaScript 项目的 Git hooks 管理

# TLDR

**初始化 husky**（创建 .husky/pre-commit 并设置 "prepare" 脚本）

```npx husky init```

**添加 pre-commit hook**（hook 现在就是普通的 shell 脚本）

```echo "npm test" > .husky/pre-commit```

**添加 pre-push hook**

```echo "npm run lint" > .husky/pre-push```

**单次提交时跳过 hooks**

```git commit -m "[message]" -n```

**在整个会话中禁用 husky**（在 CI/Docker 中很有用）

```export HUSKY=0```

# SYNOPSIS

**husky** [_init_]

# PARAMETERS

**init**
> 在当前仓库中初始化 husky：创建 **.husky/pre-commit**，并在 package.json 中添加 **"prepare": "husky"** 脚本。

_不带参数_
> 作为 **prepare** 脚本运行；将 **core.hooksPath** 设置为 **.husky/_**，让 git 从 **.husky/** 目录调用 hooks。

**HUSKY=0**（环境变量）
> 跳过安装/运行 husky hooks；适用于 CI 和 Docker 构建。

# DESCRIPTION

**Husky** 改进了 JavaScript 项目的 Git hooks 管理。它让你可以在 commit、push 及其他 git 事件发生时自动运行 linter、测试和其他脚本。

自 **v9** 起，husky 的 CLI 大幅简化：唯一真正的子命令是 **init**，它会生成一个起始 hook 并接好 **prepare** npm 脚本。hook 本身就是直接放在 **.husky/** 目录下的普通可执行 shell 脚本（例如 **.husky/pre-commit**），不再通过命令来管理。husky v4-v8 中较旧的 **add**、**set** 和 **install** 子命令已被移除。它常与 **lint-staged** 搭配用于 pre-commit 代码质量检查。

# CAVEATS

Node.js 软件包，作为开发依赖安装（**npm install --save-dev husky**）。5-8 版本使用 **husky add**/**husky set**/**husky install**，这些命令在 v9+ 中已不再支持；现在直接创建 hook 文件。出于安全考虑，Husky 不会向父目录安装 hooks，这会影响 monorepo 配置。在某些系统/软件包管理器上，hook 脚本必须具有可执行权限（**chmod +x**）。

# HISTORY

Husky 由 **Typicode** 创建，用于简化 JavaScript 项目中的 Git hook 管理，后来成为事实上的标准开发依赖。版本 9（2024 年）重写了该工具，使其零依赖，并将 API 缩减为单一的 **init** 命令，倾向于使用普通 shell 脚本而非自定义 DSL。

# INSTALL

```nix: nix profile install nixpkgs#husky```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lint-staged](/man/lint-staged)(1), [git](/man/git)(1), [npm](/man/npm)(1)

# RESOURCES

```[Source code](https://github.com/typicode/husky)```

```[Documentation](https://typicode.github.io/husky/)```

<!-- verified: 2026-07-19 -->
