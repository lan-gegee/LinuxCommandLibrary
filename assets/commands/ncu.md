# TAGLINE

检查 package 中过时的依赖

# TLDR

**检查更新**

```ncu```

**更新 package.json**

```ncu -u```

**检查特定软件包**

```ncu [lodash] [react]```

**检查匹配模式的软件包**

```ncu "/^@types/"```

**排除软件包**

```ncu --reject [typescript]```

**交互模式**

```ncu -i```

**仅检查次版本更新**

```ncu --target minor```

**显示对等依赖**

```ncu --peer```

# SYNOPSIS

**ncu** [_-u_] [_-i_] [_--target level_] [_--reject pattern_] [_options_] [_packages_]

# PARAMETERS

**-u**, **--upgrade**
> 更新 package.json。

**-i**, **--interactive**
> 交互模式。

**-t**, **--target** _LEVEL_
> 更新目标（latest、minor、patch、semver）。

**-f**, **--filter** _PATTERN_
> 仅包含匹配的软件包。

**-x**, **--reject** _PATTERN_
> 排除匹配的软件包。

**-g**, **--global**
> 检查全局软件包。

**-p**, **--packageManager** _PM_
> 包管理器（npm、yarn、pnpm）。

**--peer**
> 检查对等依赖。

**-d**, **--deep**
> 检查 workspaces。

**--pre**
> 包含预发布版本。

**--format** _FMT_
> 输出格式。

**--doctor**
> 逐个测试升级。

# DESCRIPTION

**ncu**（npm-check-updates）用于找出 package.json 中过时的依赖。它只显示可用更新，不会安装它们。

该工具将已安装的版本与 npm registry 对比。输出会显示每个软件包的当前版本、期望版本和最新版本。

更新模式（-u）会用新版本修改 package.json。之后需运行 npm install 才能真正安装更新。

交互模式让你选择要更新哪些软件包。这在增量升级或想跳过某些更新时很有用。

目标级别控制更新范围：patch 只允许补丁更新（1.0.x），minor 允许次版本更新（1.x.x），latest 允许任意版本。

过滤和排除模式用于聚焦特定软件包。正则表达式会匹配软件包名称。

# CAVEATS

只更新 package.json 但不执行安装。大版本更新可能包含破坏性变更。更新后请进行测试。它不会检查实际的兼容性。

# HISTORY

**npm-check-updates** 创建于 **2014 年**前后，填补了 npm 更新工作流的空白。npm update 会安装更新但不修改 package.json，而 ncu 会直接更新该文件以实现明确的版本控制。

# SEE ALSO

[npm](/man/npm)(1), [yarn](/man/yarn)(1), [pnpm](/man/pnpm)(1), [npm-outdated](/man/npm-outdated)(1)
