# QA Card · 质检卡

## 用途

质检卡记录候选图是否可以交付，以及失败发生在哪一层。它把返修从“重新试一次”变成可定位的修改。

## 字段

```text
任务名称：
本张编号：
状态：CONFIRMED / NEEDS_REVIEW / REJECT

Profile / Character Lock：PASS / FAIL / N/A
Persona Calibration：PASS / FAIL / N/A
Profile Contract：PASS / FAIL / N/A
Reference Protocol：none / single / dual / DEGRADED_TO_SINGLE
内容准确性：PASS / FAIL
模式质量：PASS / FAIL
文字与标签：PASS / FAIL / N/A
事实与授权：PASS / FAIL / N/A

失败层：内容 / 方案 / 资产 / Prompt / 生成 / QA
具体问题：
返修动作：
是否只返修当前张：是 / 否
```

## 交付规则

- `REJECT`：任一 Critical 角色、事实、授权或模式门禁失败，不得交付。
- `NEEDS_REVIEW`：非 Critical 问题需要标注后交给用户决定。
- `CONFIRMED`：公共 Confirm Gate 和当前模式 QA 均通过。

## 规则

1. 先做公共 Character / Persona 检查，再做模式 QA。
2. QA 不重新定义 Profile 身份；身份问题回到 Profile 或资产层。
3. 返修必须写出具体修改，不使用“再优化一下”作为唯一结论。
