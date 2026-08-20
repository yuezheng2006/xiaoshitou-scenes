# 老杨小剧场 · 快速检查清单

**视觉印记 · 路径 C**：① Confirm Gate 设定图 → ② 场景轻确认门 → ③ blueprint 编译 → ④ 设定图 + 段落/主题/金句出图。  
长文先 **Imprint Plan Card**。隐私：禁止真人照。路径 B 双 IP 用 `persona-quick-checklist.md`。

编译入口：`references/theater-prompt-blueprint.md` × `theater-styles/vinyl-theater` × `theater-shapes/{shape}`。  
校验：`python3 scene-skill-core/scripts/validate-theater-punk.py`

---

## 第 0 步：路径 C

| 触发 | 判断 |
| --- | --- |
| 含 **`小剧场`** | ✅ 路径 C |
| 无「小剧场」 | ❌ 不进 C |
| C + `小石头` / `Little Stone` | ✅ **C 组合**（不打回 B） |
| 仅 `老杨和小石头`（无小剧场） | → 路径 B |
| 仅「视觉印记」无「小剧场」 | ❌ 不进 C |

---

## 第 1 步：Imprint Plan Card

| 任务 | 做 |
| --- | --- |
| 长文 / 多点位 | **先出 Plan Card**（点位 + 图型 + 输入形态 + 设定图状态），确认后再渲 |
| 单主题 / 单金句 | 短卡即可（仍须标明图型与设定图状态） |
| 禁止 | 跳过 Plan 直接开批 |

---

## 第 2 步：设定图 Confirm Gate

| 状态 | 可否批场景 |
| --- | --- |
| DRAFT / PREVIEW | ❌ 只出或确认设定图 |
| APPROVED | ✅ 可进场景 |
| 返修脸发服鞋体态 | 退回 PREVIEW |
| 用户要自拍定妆 | ❌ 拒绝 → 风格化重生 |

用户说「设定图 / IP设定图」→ **只做 Gate**，不同时批场景。

---

## 第 2b 步：场景轻确认门

| 情况 | 做 |
| --- | --- |
| 已指定图型（拆解/动作/一鱼两吃）或用户说 `auto` | 继续编译 |
| 仅主题/段落、未指定图型 | **停**：推荐 2–3 图型 + 默认 16:9，等选择 |
| 参见 | `references/theater-prompt-blueprint.md`「场景轻确认门」 |

---

## 第 3 步：输入形态

| 输入 | 默认产出 | shape id |
| --- | --- | --- |
| 段落（120–400 字） | 流程拆解 ×1 | `process-breakdown` |
| 主题 | **一鱼两吃**（除非只要一张） | `one-theme-two-plates` |
| 金句 | 核心动作 ×1（可升级一鱼两吃） | `core-action` |

---

## 第 4 步：传图

| 步骤 | 必传 |
| --- | --- |
| 出设定图 | 有金样则确认金样；否则 flat-ip-sheet + handdrawn-body + face-lock（**无真人照**） |
| C 单人场景 | **APPROVED**：`author-persona-theater-expression-sheet.png`（脸）+ `face-lock` + `author-persona-theater-sheet.png`（服/体） |
| C 组合场景 | 上列金样 + `primary-character-reference.png`（必要时 + actions） |
| 多场景 / 一鱼两吃 | 先 1 张预览 |

不传真人照。C 单人不传小石头参考。

---

## 第 5 步：Prompt 编译（硬）

1. 读 `theater-prompt-blueprint.md` + `theater-styles/vinyl-theater/{META,STYLE}.md` + 一个 `theater-shapes/{shape}/META.md`  
2. 用 `persona-author-theater-prompts.md` 片段**改写填空**（勿原文多段 concat）  
3. Likeness Policy：保识别锚点；**不追照片级**  
4. Theater Lock：脸/发/眼镜/**服装/鞋/配件** 跟设定图，只改姿态；表情 E0–E4 选一  
5. 预算：拆解 = 1+3–5 模块、人物 ~25–40%；动作 = 1 主动作、道具≤2、文案≤3  
6. 一鱼两吃：**先 A 预览再 B**，同设定图  
7. 组合：小石头 flat 2D；不套路径 B 强制握手戏  
8. 先落盘 `scenes/prompts/{slug}-{shape}.md`，再生图  
9. Negatives：无真人、不换装、不半写实、小石头不 3D 同化；**禁止**把 Punk Cover 风格菜单当小剧场画风  

---

## 生成后快检

- [ ] 与 **APPROVED 设定图**同一人、同套 outfit（藏蓝 T + 宽松过膝卡其短裤 + NB **2002R** + 左手运动表 + 设定图同款眼镜）
- [ ] 正脸/侧面/背面同一颅骨；东方中国人骨相；潮玩哑光（非照片级全身）
- [ ] 体态结实约 180–182 观感；禁 1.9m 竹竿、禁 170 短腿；头肩比正常
- [ ] C 单人：无小石头；C 组合：flat 2D 小石头、无 3D 卵石
- [ ] 流程拆解：模块 3–5、人物非贴纸；核心动作：主动作唯一
- [ ] 每张附一句「这张让读者看见什么」
- [ ] prompt 文件已按 blueprint 编译（非 STYLE 二段粘贴）
