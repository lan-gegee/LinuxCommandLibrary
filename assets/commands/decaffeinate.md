# TAGLINE

将 CoffeeScript 转换为现代 JavaScript

# TLDR

**将 CoffeeScript 文件转换为 JavaScript**

```decaffeinate [file.coffee]```

**以 CoffeeScript 2 兼容方式转换**

```decaffeinate --use-cs2 [file.coffee]```

**转换并使用 ES 模块语法（import/export）**

```decaffeinate --use-js-modules [file.coffee]```

**将输出写入指定文件**

```decaffeinate -o [output.js] [file.coffee]```

**一次转换多个文件**

```decaffeinate [file1.coffee] [file2.coffee]```

**使用宽松模式获得更简洁的输出**

```decaffeinate --loose [file.coffee]```

# SYNOPSIS

**decaffeinate** [_options_] _files..._

# PARAMETERS

**-o**, **--output** _file_
> 将输出写入指定的文件路径。

**--use-cs2**
> 将输入视为 CoffeeScript 2 代码（默认按 CoffeeScript 1 处理）。

**--use-js-modules**
> 将 `require`/`module.exports` 转换为 ES6 的 `import`/`export` 语法。

**--modernize-js**
> 将输入视为 JavaScript，仅应用 JS 到 JS 的转换（不做 CoffeeScript 转换）。

**--literate**
> 将输入视为 Literate CoffeeScript。

**--loose**
> 启用所有宽松转换选项以获得更简洁的输出（可能存在细微语义差异）。

**--prefer-let**
> 输出中对大多数变量使用 `let` 而非 `const`。

**--disable-suggestion-comment**
> 省略输出文件顶部的后续改进建议注释。

**--optional-chaining**
> 在生成的代码中使用 JavaScript 可选链（`?.`）。

**--nullish-coalescing**
> 在生成的代码中使用空值合并运算符（`??`）。

**--logical-assignment**
> 使用 ES2021 逻辑赋值运算符（`&&=`、`||=`、`??=`）。

**--disable-babel-constructor-workaround**
> 禁用 Babel 类构造函数的变通方案。

# DESCRIPTION

**decaffeinate** 将 CoffeeScript 转换为现代 JavaScript（ES6+）。它生成符合语言习惯的 JavaScript，包含规范的类语法、箭头函数、模板字面量和解构。

适用于将 CoffeeScript 代码库迁移到 JavaScript。

# CAVEATS

某些 CoffeeScript 模式可能需要手动清理。请检查生成代码中的边界情况。

# SEE ALSO

[coffee](/man/coffee)(1), [babel](/man/babel)(1)
