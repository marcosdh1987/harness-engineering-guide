# Agentic Architectures and Best Practices

This document compiles the core architectural concepts, technical terminology, and design patterns recommended by Anthropic for building robust, production-grade agentic systems with **Claude**.

---

## 1. Agentic Loop Control Flow

An agent's lifecycle is based on **model-driven decision-making** as opposed to rigidly preconfigured decision trees. The model evaluates the conversation context at each turn to decide which tool to call next.

### The `stop_reason` Parameter
The agentic loop control flow must be managed cleanly by inspecting the `stop_reason` field in the API response:
- **`tool_use`**: Indicates that the model has decided to invoke a tool. The local orchestrator must execute the tool, format the result, and append it to the conversation history before calling Claude again.
- **`end_turn`**: The model has completed its reasoning and returns the final response to the user.

### Critical Anti-Patterns
- **Heuristic Termination**: Never attempt to control the loop by parsing free-form assistant text for keywords (e.g., searching for "task completed" or "done") as this is probabilistic and prone to failure.
- **Arbitrary Iteration Caps**: Setting a turn limit (e.g., maximum 5 iterations) as the *sole* loop control mechanism hides infinite loop errors instead of handling them programmatically.
- **Assuming Turn End from the First Block**: Claude can emit text explanations followed by tool calls in a single turn. The loop must continue if a tool use is requested, regardless of whether it was preceded by text content.

---

## 2. Multi-Agent Orchestration (Coordinator-Subagents Pattern)

For complex and unstructured workflows, the **Hub-and-Spoke** architecture is recommended. In this pattern, a coordinator agent (Hub) manages problem decomposition, information routing, and error handling, while delegating specific subtasks to specialized subagents (Spokes).

### Orchestration Design Rules
- **Strict Context Isolation (The Golden Rule)**: Subagents operate with completely isolated contexts. They **do not** automatically inherit the coordinator's conversation history. The coordinator must explicitly pass discovered facts, previous outputs, and the exact research goal in the subagent's prompt.
- **The `Task` Tool**: This is the standard mechanism for a coordinator to spawn subagents. The coordinator can invoke the `Task` tool multiple times in a single turn to run subagents in parallel, reducing overall latency.
- **Narrow Decomposition Risks**: A typical orchestration error is decomposing a query too narrowly, missing the overall scope (e.g., splitting "impact on creative industries" into graphic design and photography subtasks, completely omitting music and film). The coordinator must ensure broad and comprehensive plans.

---

## 3. Deterministic Guarantees vs. Probabilistic Compliance

When designing governance for AI agents, it is critical to distinguish between probabilistic guidance and deterministic enforcement:

- **System Prompt Instructions (Probabilistic)**: Writing restrictions in the system prompt (e.g., "do not delete files" or "always verify customer identity before processing refunds") provides probabilistic compliance. It has a non-zero failure rate under complex conditions.
- **Programmatic Hooks (Deterministic)**: Code-level interceptors are the only way to guarantee compliance for critical business rules or security safety gates:
  - **`PreToolUse` / Outgoing Interception**: Blocks outgoing tool calls that violate hard policies (e.g., blocking refunds exceeding $500 and forcing human escalation).
  - **`PostToolUse` / Normalization**: Intercepts external tool outputs before they reach Claude to normalize heterogeneous formats (e.g., converting Unix timestamps from different APIs to ISO 8601), preventing the model from having to resolve inconsistent data structures.
  - **Structured Handoff Protocols**: When transferring an agent's flow to a human, the system must compile a **structured summary** (customer ID, root cause, and recommended action), as human operators typically do not have the time to read the entire chat transcript.

---

## 4. Workflow Decomposition Strategies

Workflow design should match the nature of the task:

### Prompt Chaining
A fixed, predictable sequential pipeline. It is ideal for structured tasks with multiple aspects.
- *Code Review Example*: When reviewing a pull request modifying 15 files, a single-pass review tends to dilute model attention, missing obvious bugs. The correct architecture is running a sequential file-by-file local pass first, followed by a separate cross-file integration pass.

### Dynamic Adaptive Decomposition
A workflow that dynamically generates subtasks based on intermediate findings. This is the preferred approach for open-ended research or unstructured repository exploration.

---

## 5. Session State Management and Forking

As session history grows, keeping context clean and updated is essential to prevent degradation in Claude's reasoning quality.

- **Session Resumption (`--resume <session-name>`)**: Resuming a long session keeps conversation history intact. However, if the local codebase or environment has changed, it is much more reliable to start a **clean session** and inject a structured summary of the current state. This avoids Claude operating on stale or expired tool results.
- **Session Forking (`fork_session` or `context: fork`)**: Creates independent, parallel analysis branches from a shared baseline (e.g., comparing two different refactoring approaches). This prevents cross-context contamination and keeps session histories clean.
