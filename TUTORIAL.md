# Multi-Agent Orchestrator Plugin - Tutorial

A hands-on guide to using the 3-tier multi-agent architecture in Agent Zero.

## Table of Contents

1. [Getting Started](#getting-started)
2. [Your First Multi-Agent Request](#your-first-multi-agent-request)
3. [Understanding the 3-Tier Architecture](#understanding-the-3-tier-architecture)
4. [Working with Individual Agents](#working-with-individual-agents)
5. [Parallel Execution Patterns](#parallel-execution-patterns)
6. [Domain Ownership in Practice](#domain-ownership-in-practice)
7. [Common Workflows](#common-workflows)
8. [Troubleshooting](#troubleshooting)

---

## Getting Started

### Step 1: Verify Plugin Installation

After installing the plugin, verify it's working:

```bash
cd /a0/usr/plugins/multi-agent-orchestrator
python execute.py setup
```

You should see:
```
✅ Plugin structure verified
   - 8 agent profiles ready
   - Parallel execution tools available
   - Integration layer loaded
```

### Step 2: Test the Plugin

Run the test suite:

```bash
python execute.py test
```

Expected output:
```
✅ Imports successful
✅ Parallel execution: 2/2 successful
   Duration: 0.51s
✅ All tests passed!
```

---

## Your First Multi-Agent Request

### Example: Build a User Authentication System

**Goal**: Create a complete authentication system with login, signup, and password reset.

**Using the Orchestrator** (Recommended approach):

```json
{
  "tool_name": "call_subordinate",
  "tool_args": {
    "profile": "orchestrator",
    "message": "Build a user authentication system with:\n1. Login page (frontend)\n2. User registration API (backend)\n3. Password reset functionality\n4. Security review\n5. Test coverage\n\nPlease coordinate with your teams to:\n- Planning Lead: Design the architecture\n- Engineering Lead: Coordinate frontend and backend implementation\n- Validation Lead: Establish quality gates\n\nReport back with a coordinated plan from all teams.",
    "reset": true
  }
}
```

**What Happens Behind the Scenes**:

1. **Orchestrator** receives your request
2. **Orchestrator** delegates to:
   - `planning-lead` → Creates architecture specification
   - `engineering-lead` → Coordinates implementation
   - `validation-lead` → Sets up quality gates
3. Each **Team Lead** delegates to their workers:
   - `frontend-dev` → Implements login/registration UI
   - `backend-dev` → Builds authentication API
   - `qa-engineer` → Writes test cases
   - `security-reviewer` → Audits for vulnerabilities
4. **Results flow back up** the hierarchy
5. **Orchestrator** synthesizes everything into a unified response

**Expected Output**:
```
【TIER 1 - ORCHESTRATION】
  └─ Received request. Delegating to appropriate teams...

【TIER 2 - TEAM LEADS】
  └─ planning-lead: Analyzing requirements. Architecture approach designed.
  └─ engineering-lead: Coordinating implementation. Frontend and Backend teams aligned.
  └─ validation-lead: Establishing quality gates and security checkpoints.

【TIER 3 - IMPLEMENTATION】
  └─ frontend-dev: Implementing UI components. React/Vue patterns applied.
  └─ backend-dev: Building API endpoints. Database schema optimized.
  └─ qa-engineer: Test cases written. Coverage: unit, integration, e2e.
  └─ security-reviewer: Security audit complete. No critical vulnerabilities found.

NEXT ACTIONS
• Review individual agent outputs below
• Approve for implementation or request revisions
• Escalate blockers to appropriate team leads
```

---

## Understanding the 3-Tier Architecture

### Tier 1: The Orchestrator

**Role**: Entry point and coordinator
**Never writes code** - only delegates

**Use when**:
- Starting a complex project
- Need coordination across multiple domains
- Want a complete solution from multiple specialists

**Example**:
```json
{
  "profile": "orchestrator",
  "message": "Create an e-commerce platform with product catalog, shopping cart, and checkout"
}
```

### Tier 2: Team Leads

**Role**: Planning and coordination
**Never implement** - only design and delegate

#### Planning Lead
**Focus**: Architecture, requirements, strategy

**Example**:
```json
{
  "profile": "planning-lead",
  "message": "Design the architecture for a real-time chat application"
}
```

**Output**: Architecture specification document

#### Engineering Lead
**Focus**: Coordinating frontend and backend teams

**Example**:
```json
{
  "profile": "engineering-lead",
  "message": "Coordinate implementation of a payment processing API"
}
```

**Output**: Implementation coordination plan

#### Validation Lead
**Focus**: QA and security oversight

**Example**:
```json
{
  "profile": "validation-lead",
  "message": "Establish quality gates for a healthcare application"
}
```

**Output**: Validation plan with security checkpoints

### Tier 3: Workers

**Role**: Implementation
**Always write code/tests** - never delegate

#### Frontend Developer
**Domain**: UI/UX, React/Vue, CSS

**Example**:
```json
{
  "profile": "frontend-dev",
  "message": "Create a responsive product grid with filtering and sorting"
}
```

#### Backend Developer
**Domain**: APIs, databases, server logic

**Example**:
```json
{
  "profile": "backend-dev",
  "message": "Implement REST API for user management with JWT authentication"
}
```

#### QA Engineer
**Domain**: Tests, bug identification

**Example**:
```json
{
  "profile": "qa-engineer",
  "message": "Write comprehensive tests for the authentication API"
}
```

#### Security Reviewer
**Domain**: Security audits, vulnerabilities

**Example**:
```json
{
  "profile": "security-reviewer",
  "message": "Audit the authentication flow for security vulnerabilities"
}
```

---

## Working with Individual Agents

### When to Use Individual Agents

While the orchestrator is powerful, sometimes you need direct control:

1. **Quick fixes**: "Fix this CSS bug"
2. **Specific expertise**: "Review this code for SQL injection"
3. **Iterative development**: "Add pagination to this API"
4. **Learning**: Understanding how each agent works

### Direct Agent Examples

#### Frontend-Only Task

```json
{
  "tool_name": "call_subordinate",
  "tool_args": {
    "profile": "frontend-dev",
    "message": "Create a login form with:\n- Email and password fields\n- Client-side validation\n- Error message display\n- Responsive design\n\nUse vanilla HTML/CSS/JavaScript.",
    "reset": true
  }
}
```

#### Backend-Only Task

```json
{
  "tool_name": "call_subordinate",
  "tool_args": {
    "profile": "backend-dev",
    "message": "Create a Node.js/Express API endpoint:\nPOST /api/auth/login\n- Accept email and password\n- Validate against database\n- Return JWT token\n- Handle errors appropriately",
    "reset": true
  }
}
```

#### Security Review

```json
{
  "tool_name": "call_subordinate",
  "tool_args": {
    "profile": "security-reviewer",
    "message": "Review this authentication code for security vulnerabilities:\n\n[paste your code here]",
    "reset": true
  }
}
```

---

## Parallel Execution Patterns

### Pattern 1: Frontend + Backend in Parallel

**Scenario**: Implement a feature that needs both frontend and backend simultaneously.

**Python Integration**:

```python
from usr.plugins.multi_agent_orchestrator.tools.multi_agent_broadcast import create_parallel_team

# Execute frontend and backend in parallel
result = create_parallel_team(
    "engineering",
    "Implement user profile page with avatar upload"
)

print(result["synthesized_output"])
```

**What happens**:
- `frontend-dev` works on the profile UI
- `backend-dev` works on the avatar upload API
- Both execute simultaneously
- Results merged into unified output

### Pattern 2: QA + Security in Parallel

**Scenario**: Validate a feature from both quality and security perspectives.

```python
from usr.plugins.multi_agent_orchestrator.tools.multi_agent_broadcast import create_parallel_team

result = create_parallel_team(
    "validation",
    "Review the new payment processing feature"
)
```

**What happens**:
- `qa-engineer` writes and runs functional tests
- `security-reviewer` audits for security issues
- Both reports synthesized together

### Pattern 3: Planning + Engineering Strategy

**Scenario**: Get both architectural and implementation perspectives.

```python
from usr.plugins.multi_agent_orchestrator.tools.multi_agent_broadcast import create_parallel_team

result = create_parallel_team(
    "planning",
    "Design a microservices architecture for our platform"
)
```

**What happens**:
- `planning-lead` creates high-level architecture
- `engineering-lead` provides implementation feasibility
- Combined strategic output

### Pattern 4: Full 8-Agent Team

**Scenario**: Complete project from scratch.

```python
from usr.plugins.multi_agent_orchestrator.tools.multi_agent_broadcast import create_full_team_request

result = create_full_team_request(
    "Build a complete task management application"
)

# Access individual responses
for response in result["agent_responses"]:
    print(f"{response['profile']}: {response['result'][:100]}...")

# Access synthesized output
print(result["synthesized_output"])

# Access execution statistics
print(f"Total duration: {result['orchestration_summary']['total_duration_seconds']}s")
```

---

## Domain Ownership in Practice

### Understanding Write Restrictions

Each Tier 3 agent has explicit write restrictions:

| Agent | Can Write To | Cannot Write To |
|-------|-------------|-----------------|
| `frontend-dev` | `/frontend/`, `/components/`, `/styles/` | `/backend/`, `/api/`, `/database/` |
| `backend-dev` | `/backend/`, `/api/`, `/database/` | `/frontend/`, `/components/`, `/styles/` |
| `qa-engineer` | `*.test.*`, `*.spec.*`, `/tests/` | Implementation code |
| `security-reviewer` | Reports only | All code (read-only) |

### Escalation Pattern

When an agent needs to modify files outside its domain:

1. **Agent stops** and reports the need
2. **Escalates to team lead** (engineering-lead or validation-lead)
3. **Team lead delegates** to appropriate worker
4. **Work continues** with correct agent

**Example**:

```
frontend-dev: "I need to modify the API endpoint to support the new field"
→ Escalates to engineering-lead
→ engineering-lead delegates to backend-dev
→ backend-dev implements the API change
→ frontend-dev continues with UI updates
```

### Enforcing Domain Boundaries

Domain ownership is **prompt-enforced**, not file-system enforced. The agent's `specifics.md` contains explicit instructions:

```markdown
## Domain Restrictions (CRITICAL)

- **Read access**: All files (to understand context)
- **Write access**:
  - ✅ `/src/frontend/`, `/src/components/`, `/src/styles/`
  - ❌ `/src/backend/`, `/src/api/`, `/src/database/` - NEVER modify these
- If you need to modify backend files, STOP and ask Engineering Lead
```

---

## Common Workflows

### Workflow 1: New Feature Development

**Steps**:
1. **Orchestrator** receives feature request
2. **Planning Lead** designs architecture
3. **Engineering Lead** coordinates implementation
4. **Frontend + Backend** work in parallel
5. **Validation Lead** reviews output
6. **QA + Security** test and audit
7. **Orchestrator** delivers complete solution

**Time**: ~5-15 minutes for complete feature

### Workflow 2: Security-First Development

**Steps**:
1. **Planning Lead** designs with security in mind
2. **Engineering Lead** coordinates implementation
3. **Frontend + Backend** implement with security constraints
4. **Security Reviewer** audits early and often
5. **QA Engineer** tests security boundaries
6. **Validation Lead** blocks release if issues found

**Time**: ~10-20 minutes (security takes priority)

### Workflow 3: Bug Fix + Regression Test

**Steps**:
1. **Backend Developer** fixes the bug
2. **QA Engineer** writes regression test
3. **Security Reviewer** ensures fix doesn't introduce vulnerabilities
4. **Validation Lead** approves for release

**Time**: ~2-5 minutes for isolated fix

### Workflow 4: Code Review Request

**Steps**:
1. **Security Reviewer** audits for vulnerabilities
2. **QA Engineer** identifies test gaps
3. **Planning Lead** suggests architectural improvements
4. **Validation Lead** synthesizes findings

**Time**: ~3-7 minutes for comprehensive review

---

## Troubleshooting

### Problem: Agent not responding

**Solution**:
1. Check agent profile exists:
   ```bash
   ls /a0/usr/plugins/multi-agent-orchestrator/agents/<profile>/
   ```
2. Verify `agent.yaml` is valid YAML
3. Ensure `specifics.md` exists in `prompts/`

### Problem: Parallel execution slow

**Solution**:
1. Check `ThreadPoolExecutor` max_workers
2. Reduce number of concurrent agents
3. Use sequential mode for debugging:
   ```python
   result = orchestrator.broadcast(tasks, execution_mode="sequential")
   ```

### Problem: Domain restrictions not working

**Solution**:
1. Remind agent explicitly: "Remember your domain restrictions"
2. Check `specifics.md` contains domain rules
3. Consider file-system wrappers for strict enforcement

### Problem: Import errors in Python integration

**Solution**:
1. Use fully qualified paths:
   ```python
   from usr.plugins.multi_agent_orchestrator.tools.multi_agent_broadcast import create_full_team_request
   ```
2. Ensure plugin is in `/a0/usr/plugins/`
3. Check Python path includes plugin directory

---

## Advanced Tips

### Tip 1: Combine with Memory

Use `memory_save` to build team knowledge:

```python
# After successful project
from agent_zero import memory_save

memory_save(
    text="Team learned: Use Redis for session storage in auth systems",
    area="mental_models",
    tags=["auth", "best_practices"]
)
```

### Tip 2: Custom Team Configurations

Create focused teams for specific needs:

```python
from multi_agent_broadcast import AgentTask, MultiAgentOrchestrator

orchestrator = MultiAgentOrchestrator()

# Custom team: DevOps focus
tasks = [
    AgentTask(profile="backend-dev", message="Setup CI/CD pipeline"),
    AgentTask(profile="security-reviewer", message="Review pipeline security"),
    AgentTask(profile="qa-engineer", message="Create deployment tests"),
]

result = orchestrator.broadcast(tasks, execution_mode="parallel")
```

### Tip 3: Sequential for Complex Dependencies

When order matters, use sequential mode:

```python
# Architecture must be complete before implementation
tasks = [
    AgentTask(profile="planning-lead", message="Design API", priority=1),
    AgentTask(profile="backend-dev", message="Implement API", priority=2),  # Depends on planning
    AgentTask(profile="frontend-dev", message="Build UI", priority=3),     # Depends on backend
]

result = orchestrator.broadcast(tasks, execution_mode="sequential")
```

---

## Next Steps

1. **Try the demo**: `python execute.py demo`
2. **Build something real**: Use the orchestrator for your next project
3. **Customize**: Modify `specifics.md` to match your tech stack
4. **Share**: Contribute improvements back to the plugin

---

## Resources

- [README.md](README.md) - Full documentation
- [Agent Architecture](https://gln75.com/en/blog/one-agent-not-enough) - IndyDevDan's original concept
- [Agent Zero Docs](https://github.com/Superlogic/agent-zero) - Framework documentation
- [Plugin Source](https://github.com/agent0ai/multi-agent-orchestrator) - Source code
