# TAGLINE

将 JavaScript 代码从 ES5 转换为 ES6/ES2015+

# TLDR

**将 ES5 转换为 ES6**

```lebab [input.js] -o [output.js]```

**应用指定的转换规则**

```lebab [input.js] -o [output.js] --transform arrow,let```

**原地转换**

```lebab --replace [file.js] --transform arrow```

**列出可用的转换规则**

```lebab --help```

# SYNOPSIS

**lebab** [_options_] _file_

# PARAMETERS

**-o**, **--out-file** _file_
> 输出文件路径。

**-t**, **--transform** _transforms_
> 以逗号分隔的转换规则列表。

**-r**, **--replace** _glob_
> 匹配单个文件或 glob 模式，原地转换这些文件。

# TRANSFORMS

安全的转换规则可以高置信度地直接应用：**arrow**、**arrow-return**、**for-of**、**for-each**、**arg-rest**、**arg-spread**、**obj-method**、**obj-shorthand**、**no-strict**、**exponent**、**multi-var**。

不安全的转换依赖启发式判断，应一次只应用一条并仔细审查结果：**let**、**class**、**commonjs**、**template**、**default-param**、**destruct-param**、**includes**。

# DESCRIPTION

**lebab** 将 JavaScript 代码从 ES5 转换为 ES6/ES2015+。它会应用箭头函数、let/const、模板字符串和解构等转换。它的作用与 Babel 相反，用于现代化遗留的 JavaScript 代码。

默认情况下不会运行任何转换：必须通过 **--transform** 至少选择一条。推荐的工作流程是一次只应用一条转换并检查 diff，因为一次性组合多条转换可能生成损坏的代码。

# INSTALL

```aur: yay -S lebab```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[babel](/man/babel)(1), [eslint](/man/eslint)(1)
