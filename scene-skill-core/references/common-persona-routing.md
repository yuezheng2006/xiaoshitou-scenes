# 通用 Persona 路由规则

本文件只描述可选 persona 的通用机制。具体 persona 名称、触发词、外形锚点、资产路径、双 IP 分工和渲染风格由当前 `ip-profiles/<ip-id>/profile.md` 指向的 persona 文件定义。

## 触发

- 只有当前 profile 的 persona 触发词出现时，才加入 persona。
- 未触发时，不出现 persona；只使用 profile 主角色。
- persona 可以出现在任意模式中，但必须遵守当前模式的渲染语言和 profile persona 文件的资产路由。

## 双 IP 互动（默认 profile）

默认 profile 触发老杨后，不是「主角色 + 可选作者露脸」，而是**双 IP 互动**：

```text
persona（老杨）= 主讲 / 拆解 / 批注 / 调度
主角色（小石头）= 执行 Agent
```

必读（按序，不要一次全读）：

1. profile 的 `persona-author.md`：触发确认与最小读取链
2. `persona-author-assets.md`：三资产与传图组合
3. `persona-scene-patterns.md`：互动场景类型
4. `persona-author-modes.md`：当前模式权重（锁定模式后）
5. `persona-author-prompts.md`：写入 prompt 时
6. `persona-author-identity.md`：QA 或返修「不像」时

每张图必须有明确的双 IP 动作关系；不能只有 persona 肖像，也不能 persona 触发后只有小石头干活。

## 读取顺序

1. 读取当前 profile 的 `profile.md`。
2. 若命中 persona 触发词，读取 profile 指向的 persona 文件。
3. 读取 `persona-scene-patterns.md`，选定互动场景类型和分工。
4. 按 persona 文件中定义的模式路由读取对应资产。
5. **生成前**：写入 Character Lock + 2D Flat Lock；画面含 persona 肖像时另写 **Persona Identity Lock**（见 `common-character-lock.md`），并传 spec（+ handdrawn / actions 按场景）。
6. **生成后**：先做形象检查（主角色 + persona），再做模式 QA；文档/预览/仓库示例图无例外。

## 画面职责

- persona 触发时：persona 负责讲、拆、批注、指向；主角色负责执行动作（搬卡、贴标签、物理动作等）。
- 知识卡 / PPT / 手绘：persona 可占更高画面权重（约 40–55%），主角色 1–3 个执行分工。
- 实物图：物件 + 主角色物理动作优先，persona 调度 / 递工具 / 旁注（约 25–40%）。
- 不要做成头像展示、个人海报、证件照；也不要让 persona 替代主角色承担全部执行动作。

## 安全边界

- 不要把真人照片提交进公开仓库。
- 不要向生图请求传入未经确认可用的真人照片。
- 不要发明 persona 的单位、联系方式、履历或背书。
- 如果 persona 资产缺失，退回 profile 文件中的文字锚点，并在交付说明里标注资产缺失。
