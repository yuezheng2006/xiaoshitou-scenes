# Logo Safety · Mark Demo

## 本 Profile 的标是谁

`mark-demo` 使用的是**项目自有的公开示意品牌标**（深青绿圆角方标 + 路径折角图形），用于演示 `input_kind=brand_mark` 录入与多模式配图流程。

- 该示意标可进入 `public_assets`，可提交到公开仓库。
- 它不是 Claude Code、Anthropic 或任何第三方的商标。
- 它不是默认小石头（Little Stone）的企业 Logo 资产。

## 客户真标 vs 公开演示

| 类型 | 默认归属 | 公开仓 |
| --- | --- | --- |
| 客户真实 Logo / App Icon | `private_assets` | 禁止 |
| mark-demo 示意标 | `public_assets` | 允许 |
| default-little-stone 雷石 Logo | 授权资产 / 本地 | 按品牌规范，不混入 mark-demo |

**硬规则：**

- 不得把客户商标写入公开示例、Prompt 模板或 git 历史。
- 不得在 mark-demo 文档或资产中替换为客户提供的真实标识。
- 不得自动把 `default-little-stone` 的雷石 Logo 贴到 mark-demo 或 brand_mark 录入流程中。

## brand_mark 与 logo-safety 分工

- **logo-safety（默认流程）**：普通配图不要乱出未授权的真 Logo；小石头场景用工牌/道具规范见 `default-little-stone/logo-safety.md`。
- **brand_mark 录入**：客户**主动**用自家标当 IP 身份时，走 `profile_enrollment`，创建或切换到客户 profile；不是「把 Logo 贴到小石头身上」。

录入或切换 profile 期间，以及客户 profile 未 `AVAILABLE` 前，默认小石头不得作为当前 IP 出镜。

## 本地私有验证

Claude Code 或其他第三方标识**仅可用于本地私有验证**（例如对比「不要画成 Claude 形象」的 QA），**不得提交**到公开仓库或写入 `public_assets`。

## QA 失败信号（商标相关）

```text
- 出现 Anthropic / Claude 星爆或剪影
- 出现客户或第三方未授权商标
- 画成小石头 + 企业 Logo 混搭
- 把示意标改成橙色胶囊或字母 C
```

修复：回到 `brand-mark-primary.png` 锚点重生成；不通过改场景文案掩盖身份漂移。
