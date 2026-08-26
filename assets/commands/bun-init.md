# TAGLINE

搭建新项目脚手架

# TLDR

**交互式初始化新项目**

```bun init```

**以默认值初始化（跳过提示）**

```bun init -y```

**初始化 React 项目**

```bun init --react```

**初始化带 Tailwind 的 React 项目**

```bun init --react=tailwind```

**初始化带 shadcn/ui 的 React 项目**

```bun init --react=shadcn```

# SYNOPSIS

**bun init** [_options_]

# DESCRIPTION

**bun init** 以合理的默认配置搭建新的 Bun 项目。它会创建必要的项目文件，包括 package.json、tsconfig.json 或 jsconfig.json、入口文件、README 和 .gitignore。

多次运行该命令不会造成破坏，也不会覆盖已有文件。

# PARAMETERS

**-y, --yes**
> 接受默认值，不进行提示

**--react**
> 搭建 React 项目脚手架（可选值：tailwind、shadcn）

**--cwd** _directory_
> 在其他目录中初始化

# CREATED FILES

**package.json**
> 项目清单（名称默认取目录名）

**tsconfig.json / jsconfig.json**
> TypeScript/JavaScript 配置

**index.ts**
> 入口文件（或 index.tsx、index.js 等）

**README.md**
> 项目文档

**.gitignore**
> Git 忽略规则

**bun.lock**
> 锁文件（安装后生成）

# PROJECT STRUCTURE

```
my-project/
├── node_modules/
├── index.ts
├── .gitignore
├── README.md
├── bun.lock
└── package.json
```

# CAVEATS

会自动运行 **bun install** 安装 @types/bun。除非已存在其他 index 文件，入口文件默认为 index.ts。默认优先使用 TypeScript。

# INSTALL

```pacman: sudo pacman -S bun```

```brew: brew install bun```

```nix: nix profile install nixpkgs#bun```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bun](/man/bun)(1), [bun-create](/man/bun-create)(1), [npm-init](/man/npm-init)(1)

# RESOURCES

```[Source code](https://github.com/oven-sh/bun)```

```[Homepage](https://bun.sh)```

```[Documentation](https://bun.sh/docs)```

<!-- verified: 2026-06-22 -->
