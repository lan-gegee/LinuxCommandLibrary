# TAGLINE

嵌入式 Ruby（ERB）模板处理器

# TLDR

**处理 ERB 模板**

```erb [template.erb]```

**配合 Ruby 变量处理**

```erb -r [./vars.rb] [template.erb]```

**输出到文件**

```erb [template.erb] > [output.html]```

**使用修剪模式获得更整洁的输出**

```erb -T - [template.erb]```

**打印结果且不带换行符**

```erb -P [template.erb]```

# SYNOPSIS

**erb** [_options_] [_file_...]

# PARAMETERS

**-r** _library_
> 处理前先加载（require）Ruby 库。

**-T** _mode_
> 修剪模式：0、1、2 或 -。

**-P**
> 输出后不打印换行符。

**-e**
> 忽略 RUBYOPT 环境变量。

**-x**
> 打印 Ruby 脚本而不执行。

**-n**
> 在输出中打印行号。

**-v**
> 详细模式。

**--version**
> 显示版本。

# DESCRIPTION

**erb** 处理 ERB（Embedded Ruby）模板，允许在文本文件中嵌入 Ruby 代码。ERB 常用于 Rails 视图和配置文件生成。

模板使用特殊标签：`<%= expr %>` 输出表达式结果，`<% code %>` 执行代码但不产生输出，`<%# comment %>` 用于注释。

# TEMPLATE SYNTAX

```erb
<h1><%= @title %></h1>
<ul>
<% @items.each do |item| %>
  <li><%= item %></li>
<% end %>
</ul>
<%# This is a comment %>
```

# TRIM MODES

```
-T 0  - No trimming
-T 1  - Trim lines ending with %>
-T 2  - Trim lines containing only <% %>
-T -  - Trim newlines after -%>
```

# CAVEATS

嵌入的 Ruby 以完全权限执行。输入必须可信。复杂逻辑应放在代码中而非模板里。空白处理可能需要调整修剪模式。

# HISTORY

ERB 由 **Masatoshi Seki** 创建，并纳入 Ruby 标准库。它曾作为默认视图模板引擎随 Ruby on Rails 流行起来，不过 Rails 现在常改用 Slim 或 Haml 等替代方案。

# INSTALL

```apt: sudo apt install ruby```

```dnf: sudo dnf install ruby```

```pacman: sudo pacman -S ruby```

```apk: sudo apk add ruby```

```zypper: sudo zypper install ruby```

```brew: brew install ruby```

```nix: nix profile install nixpkgs#ruby```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ruby](/man/ruby)(1), [irb](/man/irb)(1), [haml](/man/haml)(1)

# RESOURCES

```[Source code](https://github.com/ruby/erb)```

```[Documentation](https://docs.ruby-lang.org/en/master/ERB.html)```

<!-- verified: 2026-07-14 -->
