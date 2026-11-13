"""
`InsightUIUX™` React 19 & Async Anti-Slop Lint Cards (`insight_uiux.react19_anti_slop`, v1.2.0).

Detects modern frontend async/reactivity anti-patterns across React 19, TypeScript, and Web Components:
  1. `REACT19_ASYNC_WATERFALL_USE_PROMISE_ALL`: Sequential `await fetch(...)` calls in the same block without `Promise.all`.
  2. `REACT19_DERIVED_STATE_IN_USEEFFECT`: `useEffect(() => { setX(...) }, [...])` derived-state synchronization.
  3. `UX28_MISSING_ABORT_CONTROLLER`: Interactive `fetch(...)` inside submit/search handlers without `AbortController`.
  4. `UX28_MOBILE_INPUT_BELOW_16PX`: `<input>` / `<textarea>` with `< 16px` font-size causing iOS Safari auto-zoom.
"""

from __future__ import annotations

import re
from typing import Any, Dict, List

_SEQ_AWAIT_FETCH_RE = re.compile(r"await\s+fetch\([^)]+\)[\s\S]{1,180}?await\s+fetch\(", re.MULTILINE)
_DERIVED_USE_EFFECT_RE = re.compile(r"useEffect\(\s*\(\)\s*=>\s*\{[\s\S]{1,160}?\bset[A-Z][a-zA-Z0-9_]*\(", re.MULTILINE)
_SMALL_INPUT_FONT_RE = re.compile(r"<(?:input|textarea|select)[^>]*font(?:-size|Size)\s*[:=]\s*['\"]?(?:1[0-5]|\d)(?:px)?", re.IGNORECASE)


def audit_react19_async_anti_slop(code_snippet: str) -> Dict[str, Any]:
    """Audits React 19 / TypeScript / Web UI code against async waterfalls, derived-state effects, and UX 2.8 rules."""
    code = str(code_snippet or "").strip()
    if not code:
        return {"ok": False, "member": "InsightUIUX", "error": "EMPTY_REACT19_CODE_SNIPPET"}

    cards: List[Dict[str, str]] = []
    if _SEQ_AWAIT_FETCH_RE.search(code) and "Promise.all" not in code:
        cards.append({
            "rule": "REACT19_ASYNC_WATERFALL_USE_PROMISE_ALL",
            "severity": "HIGH",
            "remediation": "Parallelize independent requests with `await Promise.all([fetchA(), fetchB()])`.",
        })
    if _DERIVED_USE_EFFECT_RE.search(code):
        cards.append({
            "rule": "REACT19_DERIVED_STATE_IN_USEEFFECT",
            "severity": "MEDIUM",
            "remediation": "Compute derived values inline during render instead of syncing state inside `useEffect`.",
        })
    if "fetch(" in code and ("onSubmit" in code or "submit" in code) and "AbortController" not in code:
        cards.append({
            "rule": "UX28_MISSING_ABORT_CONTROLLER",
            "severity": "MEDIUM",
            "remediation": "Wire `AbortController` (`signal`) on interactive submit/chat `fetch()` calls (UX Engine 2.8 5-State Input).",
        })
    if _SMALL_INPUT_FONT_RE.search(code):
        cards.append({
            "rule": "UX28_MOBILE_INPUT_BELOW_16PX",
            "severity": "HIGH",
            "remediation": "Set `font-size: 16px` minimum on mobile inputs to prevent iOS Safari viewport auto-zoom.",
        })

    return {
        "ok": True,
        "member": "InsightUIUX",
        "react19_clean": len(cards) == 0,
        "lint_cards_count": len(cards),
        "lint_cards": cards,
    }
