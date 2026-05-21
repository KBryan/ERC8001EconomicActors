# Multi-Agent Orchestrator Plugin

<img width="1448" height="1086" alt="okay" src="https://github.com/user-attachments/assets/b9433be4-26c2-43c1-a39d-68510db7a008" />

A production-ready implementation of IndyDevDan's 3-tier multi-agent architecture for Agent Zero. Enables teams of specialized agents to work together on complex tasks with parallel execution, domain ownership, and persistent mental models.

## Features

- **8 Specialized Agent Profiles** organized across 3 tiers
- **Parallel Execution** across multiple agents via ThreadPoolExecutor
- **Domain Ownership** enforced via prompt-based file restrictions
- **Hierarchical Delegation** from Orchestrator → Team Leads → Workers
- **Result Synthesis** into unified tiered output
- **Integration Layer** connecting Python tools to actual Agent Zero subordinates

## Agent Architecture

### Tier 1 - Orchestrator
| Profile | Role |
|---------|------|
| `orchestrator` | Receives requests, delegates to teams, never writes code |

### Tier 2 - Team Leads (Delegation Only)
| Profile | Responsibility |
|---------|---------------|
| `planning-lead` | Architecture, requirements, strategic breakdown |
| `engineering-lead` | Coordinates frontend/backend developers |
| `validation-lead` | Oversees QA and security review |

### Tier 3 - Workers (Implementation)
| Profile | Domain | Write Access |
|---------|--------|--------------|
| `frontend-dev` | UI/UX, React/Vue, CSS | `/frontend/`, `/components/` only |
| `backend-dev` | APIs, databases, server logic | `/backend/`, `/api/` only |
| `qa-engineer` | Tests, bug identification | Test files only (`*.test.*`) |
| `security-reviewer` | Security audits, vulnerabilities | Reports only (read-only on code) |

## Installation

1. Copy this plugin to `/a0/usr/plugins/multi-agent-orchestrator/`
2. Run setup:
   ```bash
   cd /a0/usr/plugins/multi-agent-orchestrator
   python execute.py setup
   ```
3. Verify installation:
   ```bash
   python execute.py test
   ```

## Quick Start

### Option 1: Direct call_subordinate (Recommended)

```json
{
  "tool_name": "call_subordinate",
  "tool_args": {
    "profile": "orchestrator",
    "message": "Build a user authentication system with login, signup, and password reset",
    "reset": true
  }
}
```

The orchestrator will coordinate with planning-lead, engineering-lead, and validation-lead to deliver a complete solution.

### Option 2: Python Integration

```python
from usr.plugins.multi_agent_orchestrator.helpers.agent_zero_integration import execute_with_agent_zero

# Full 8-agent team
result = execute_with_agent_zero(
    "Build authentication system",
    team_type="full",        # "full", "engineering", "validation", "planning"
    execution_mode="parallel",  # "parallel" or "sequential"
    use_real=True            # Enable real Agent Zero subordinates
)

print(result["synthesized_output"])
```

### Option 3: Individual Specialists

```json
// Frontend implementation
{ "profile": "frontend-dev", "message": "Create login form with validation" }

// Backend API
{ "profile": "backend-dev", "message": "Implement JWT authentication API" }

// Security review
{ "profile": "security-reviewer", "message": "Audit authentication flow" }
```

## Usage Examples

### Example 1: Full Project Implementation

Request: Build a complete e-commerce system

```
Orchestrator → Planning Lead (designs architecture)
            → Engineering Lead (coordinates devs)
            → Validation Lead (establishes QA)
            
Results: Complete backend + frontend + tests + security audit
```

### Example 2: Parallel Engineering Team

```python
from tools.multi_agent_broadcast import create_parallel_team

result = create_parallel_team(
    "engineering",
    "Implement product catalog API with search"
)
# Executes frontend-dev and backend-dev in parallel
```

### Example 3: Security-First Workflow

```
1. Orchestrator delegates to Planning Lead
2. Engineering Lead coordinates implementation
3. Validation Lead runs QA + Security Review
4. Blockers escalated back to appropriate leads
```

## File Structure

```
multi-agent-orchestrator/
├── plugin.yaml                    # Plugin manifest
├── execute.py                     # Setup, test, demo scripts
├── hooks.py                       # Lifecycle hooks
├── agents/                        # 8 agent profiles
│   ├── orchestrator/
│   ├── planning-lead/
│   ├── engineering-lead/
│   ├── validation-lead/
│   ├── frontend-dev/
│   ├── backend-dev/
│   ├── qa-engineer/
│   └── security-reviewer/
├── tools/
│   └── multi_agent_broadcast.py   # Parallel execution tool
└── helpers/
    └── agent_zero_integration.py  # Integration layer
```

## Domain Restrictions

Domain ownership is enforced via prompt instructions. Each Tier 3 agent has explicit write restrictions:

- **frontend-dev**: Can read all code, but only writes to `/frontend/`, `/components/`, `/styles/`
- **backend-dev**: Can read all code, but only writes to `/backend/`, `/api/`, `/database/`
- **qa-engineer**: Read-only on implementation, writes test files only
- **security-reviewer**: Read-only on all code, writes reports only

If an agent needs to modify files outside its domain, it must escalate to the appropriate team lead.

## Comparison with IndyDevDan's Pi

| Feature | Pi (IndyDevDan) | Agent Zero (This Plugin) |
|---------|-----------------|--------------------------|
| **9 agents parallel** | ✅ Native | ✅ Via ThreadPoolExecutor |
| **Chat room** | ✅ Shared conversation | ✅ AgentContext history |
| **Domain ownership** | ✅ File boundaries | ✅ Prompt-enforced |
| **Mental models** | ✅ 10K-line files | ✅ memory_save/load |
| **YAML config** | ✅ Single file | ✅ Multiple agent.yaml |
| **User intervention** | ❌ Orchestrator only | ✅ **You as root** |

**Key advantage**: In Agent Zero, you remain the root orchestrator. You can override any agent decision, access all tools directly, and intervene at any level.

## Configuration

### Plugin Settings

No additional configuration required. Agent profiles are automatically discovered from the `agents/` directory.

### Per-Project Settings

Set `per_project_config: true` in `plugin.yaml` to enable project-specific agent configurations.

## API Reference

### `execute_with_agent_zero()`

```python
def execute_with_agent_zero(
    user_request: str,
    team_type: str = "full",
    execution_mode: str = "parallel",
    use_real: bool = False
) -> Dict[str, Any]
```

**Parameters:**
- `user_request`: The task to execute
- `team_type`: `"full"`, `"engineering"`, `"validation"`, or `"planning"`
- `execution_mode`: `"parallel"` or `"sequential"`
- `use_real`: Enable real Agent Zero subordinate calls

**Returns:**
```python
{
    "orchestration_summary": {
        "total_agents": 8,
        "successful": 8,
        "total_duration_seconds": 4.2
    },
    "agent_responses": [...],
    "synthesized_output": "...",
    "execution_log": [...]
}
```

## Troubleshooting

### Agent profiles not appearing
- Check `agent.yaml` is valid YAML
- Directory name matches `^[a-z0-9_-]+$`
- Located in correct plugin `agents/` directory

### Parallel execution errors
- Ensure Python 3.11+
- Check `concurrent.futures` is available
- Verify `use_real=True` requires Agent Zero environment

### Domain restrictions not working
- Domain ownership is prompt-enforced, not file-system enforced
- Agents may need explicit reminders about restrictions
- Consider adding file system wrappers for strict enforcement

## Contributing

1. Fork the repository
2. Create a feature branch
3. Test with `python execute.py test`
4. Submit pull request

## License

MIT License - See LICENSE file

## References

- [IndyDevDan's Video](https://www.youtube.com/watch?v=M30gp1315Y4) - One Agent Is NOT ENOUGH
- [Agent Zero Documentation](https://github.com/Superlogic/agent-zero)
- [Pi Coding Agent](https://pi.dev/) - Minimal agent harness
