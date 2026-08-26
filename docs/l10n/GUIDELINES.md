# 汉化翻译规范（必读）

本规范适用于 Linux Command Library 简体中文汉化项目的**全部**翻译工作。
翻译任何文件前必须完整阅读本文档。

## 一、铁律（违反即返工）

1. **绝不修改 Markdown 结构**：
   - `#`/`##`/`###` 标记及其数量、顺序不变
   - 代码块（``` 围栏）的数量、内容、顺序不变
   - 表格结构不变
2. **绝不翻译 Section 大标题**：`# TAGLINE`、`# TLDR`、`# SYNOPSIS`、`# PARAMETERS`、
   `# DESCRIPTION`、`# CAVEATS`、`# HISTORY`、`# INSTALL`、`# SEE ALSO`、`# RESOURCES`、
   `# CONFIGURATION`、`# COMMANDS`、`# SUBCOMMANDS`、`# EXAMPLES`、`# WORKFLOW`
   等全大写标题原样保留（程序靠它们解析）。
3. **代码块内的命令、参数、路径、配置一律不改**。代码块内形如 `[ls](/man/ls)` 的
   链接：URL 部分绝对不动，方括号内文字也不动（保持命令名可见，便于对照）。
4. **正文中的行内链接** `[text](/man/cmd)`：URL 绝对不动；`text` 若是命令名则保留，
   若是普通英文短语可译为中文。
5. **占位符原样保留**：`[fileName]`、`[directory]`、`[query]`、`<file>`、`{x..y}` 等
   方括号/尖括号占位符不译（它们出现在代码块内时本来就不动）。
6. **不增不减**：不添加原文没有的段落、注释、示例；不删减内容。
7. 文件名、目录名一律不改。

## 二、术语表（强制统一）

| 英文 | 中文 |
|---|---|
| command | 命令 |
| option / flag | 选项 |
| parameter / argument | 参数 |
| directory | 目录 |
| folder | 文件夹 |
| file | 文件 |
| path | 路径 |
| recursive(ly) | 递归（地） |
| verbose | 详细输出 |
| force | 强制 |
| symlink / symbolic link | 符号链接 |
| hard link | 硬链接 |
| archive | 归档 |
| compress / compression | 压缩 |
| extract | 解压 |
| mount / unmount | 挂载 / 卸载 |
| daemon | 守护进程 |
| kernel | 内核 |
| shell | Shell（不译） |
| pipe | 管道 |
| redirect / redirection | 重定向 |
| permission(s) | 权限 |
| owner | 所有者 |
| group | 组 |
| executable | 可执行文件 |
| regular expression / regex | 正则表达式 |
| package | 软件包 |
| repository (软件源语境) | 软件仓库 |
| repository (Git 语境) | 仓库 |
| download / upload | 下载 / 上传 |
| network | 网络 |
| hostname | 主机名 |
| port | 端口 |
| socket | 套接字 |
| encryption | 加密 |
| hash | 哈希 |
| backup | 备份 |
| restore | 恢复 |
| snapshot | 快照 |
| process | 进程 |
| service | 服务 |
| boot | 启动 |
| shutdown | 关机 |
| log | 日志 |
| user | 用户 |
| password | 密码 |
| output | 输出 |
| input | 输入 |
| print (显示到终端) | 输出/打印（视语境） |
| search | 搜索 |
| find | 查找 |
| list | 列出 |
| copy | 复制 |
| move | 移动 |
| remove / delete | 删除 |
| create | 创建 |
| edit | 编辑 |
| view | 查看 |
| display | 显示 |
| set | 设置 |
| show | 显示 |
| enable / disable | 启用 / 禁用 |
| start / stop / restart | 启动 / 停止 / 重启 |
| install / uninstall | 安装 / 卸载 |
| update / upgrade | 更新 / 升级 |
| default | 默认 |
| example | 示例 |
| usage | 用法 |
| note | 注意 |

## 三、风格约定

1. 简体中文，技术文档语体，不用"您"（用"你"或无主语句式），不用感叹号滥用。
2. 命令名、文件名、包名首次出现保留英文原文，不加引号也可（与排版一致即可）。
3. 半角标点环境下的中英文之间加一个空格：`使用 ls 命令列出目录内容`。
4. 数字、单位、版本号保持半角：`4 GB`、`v2.1`。
5. TLDR 区的加粗小标题（如 `**List files**`）译为简洁动宾短语：`**列出文件**`。
6. PARAMETERS 区参数说明尽量一行内译完，保持 `> ` 引用格式。
7. 描述性长句优先拆分为短句，避免欧化长定语。
8. 疑难句宁可意译也不要生硬直译；但不得改变技术含义。

## 四、man page 各区的处理方式

- `TAGLINE`：一句话简介，直接翻译。
- `TLDR`：加粗小标题+代码块；只译加粗标题，代码块不动。
- `SYNOPSIS`：整体视为语法骨架；仅当含英文注释性词语才需处理，通常整块不动。
- `PARAMETERS`：参数名（加粗/大写者）不动，`>` 后的说明文字翻译。
- `DESCRIPTION` / `CAVEATS` / `HISTORY` / `CONFIGURATION` / `WORKFLOW`：正文翻译。
- `INSTALL`：说明文字可译；其中的安装命令/代码不动。
- `SEE ALSO`：命令名列表，一般无需翻译；若含说明文字则翻译。
- `RESOURCES`：链接列表，不译。
- `EXAMPLES`：同 TLDR 规则。

## 五、自检清单（提交前逐条过）

- [ ] 所有 `^# ` 一级标题与原文完全一致（man page 的 section 键）？
- [ ] man page 内 `##`/`###` 子标题：应译为中文，但层级数量不得变？
- [ ] 代码块数量与内容逐字节一致（歧义区域内散文译中可接受）？
- [ ] `/man/...` URL 集合一致？行内码 span 原样？
- [ ] 占位符未翻译？
- [ ] 无漏译的英文句子（纯命令/参数/SYNOPSIS 骨架除外）？
- [ ] 术语表已套用？
