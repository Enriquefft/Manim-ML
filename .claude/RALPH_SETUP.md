# Ralph Integration Setup for Manim-ML

## What Was Done

✅ **Cleanup**
- Removed all previous ralph-import attempts
  - Deleted `ralph-test/` directory
  - Removed root-level generated files: `PROMPT.md`, `@fix_plan.md`, `specs/`, `.ralph_conversion_prompt.md`

✅ **Setup**
- Created dedicated `ralph-workspace/` directory
- Ran `ralph-import` with proper stdin redirect to avoid terminal issues
- Generated complete Ralph project structure with:
  - `PROMPT.md` - Development instructions for autonomous agents
  - `@fix_plan.md` - Prioritized task list from requirements
  - `@AGENT.md` - Agent configuration and guidelines
  - `specs/` - Structured specifications extracted from requirements.md
  - `.git/` - Git repository for change tracking

✅ **Configuration**
- Added `ralph-workspace/` to `.gitignore`
- Created convenience script: `.claude/setup-ralph.sh`

## Directory Structure

```
Manim-ML/
├── .claude/
│   ├── CLAUDE.md              # Project guidelines
│   ├── RALPH_SETUP.md         # This file
│   ├── setup-ralph.sh         # Setup script (executable)
│   └── settings.local.json    # (ignored by git)
├── ralph-workspace/           # Ralph autonomous development workspace
│   ├── PROMPT.md              # Agent instructions
│   ├── @fix_plan.md           # Prioritized tasks
│   ├── @AGENT.md              # Agent configuration
│   ├── README.md              # Project overview
│   ├── specs/                 # Specifications
│   ├── src/                   # Generated source structure
│   ├── examples/              # Example implementations
│   ├── docs/                  # Documentation
│   ├── logs/                  # Execution logs
│   └── .git/                  # Independent git tracking
├── requirements.md            # Source specification (authoritative)
└── ... (rest of Manim-ML project)
```

## How to Use Ralph

### Option 1: View the Generated Plan
```bash
cd ralph-workspace
cat @fix_plan.md          # See prioritized tasks
cat PROMPT.md             # See agent instructions
```

### Option 2: Run Ralph in Monitor Mode (Autonomous Development)
```bash
cd ralph-workspace
ralph --monitor           # Starts autonomous agent with monitoring
```

### Option 3: Regenerate Ralph Workspace (if requirements.md changes)
```bash
bash .claude/setup-ralph.sh --regenerate
```

## What Ralph Does

Ralph is an autonomous AI development agent that:
1. **Reads** your requirements from `requirements.md`
2. **Plans** implementation phases in `@fix_plan.md`
3. **Tracks** what needs to be done and priorities
4. **Executes** implementations automatically when you run `ralph --monitor`
5. **Validates** code against specs and requirements

Ralph generates:
- Development instructions in `PROMPT.md`
- Task breakdowns in `@fix_plan.md`
- Structured specs in `specs/requirements.md`
- Templates and examples in `examples/`
- Execution logs in `logs/`

## Why Separate Directory?

Ralph creates its own git repository and working directory because:
- **Isolation**: Keeps autonomous development logs separate from main project
- **Safety**: Changes tracked independently before integration
- **Clarity**: Easy to review what Ralph generated vs. your code
- **Regenerability**: Can regenerate from `requirements.md` anytime
- **Multiple Workspaces**: Can have different ralph-workspace instances for different requirements

## Key Files to Review

1. **ralph-workspace/PROMPT.md** - How Ralph approaches the project
2. **ralph-workspace/@fix_plan.md** - Specific tasks to implement
3. **ralph-workspace/specs/requirements.md** - Your requirements in structured form
4. **requirements.md** - Source of truth (in project root)

## Integration with Main Project

When Ralph generates code you want to use:
1. Copy/move implementations from `ralph-workspace/src/` to your actual project
2. Adapt as needed for your code style and structure
3. Commit to main Manim-ML repository

Ralph's workspace is isolated to prevent accidental commits of generated/draft code.

## Troubleshooting

**Q: "ralph-import command not found"**
- Install: `npm install -g ralph-claude-code`

**Q: "Raw mode is not supported" error**
- Use the provided script: `bash .claude/setup-ralph.sh`
- It properly handles stdin redirection

**Q: Want to update based on changed requirements**
```bash
bash .claude/setup-ralph.sh --regenerate
```

**Q: Need to see what Ralph is planning**
```bash
cat ralph-workspace/@fix_plan.md
cat ralph-workspace/specs/requirements.md
```

## Success Checklist

- [x] ralph-workspace created with proper structure
- [x] PROMPT.md generated with agent instructions
- [x] @fix_plan.md created from requirements analysis
- [x] specs/ populated with structured specifications
- [x] .gitignore updated to exclude ralph-workspace
- [x] setup-ralph.sh created for easy regeneration
- [x] No conflicts with main project files

## Next Steps

1. **Review the plan**: `cat ralph-workspace/@fix_plan.md`
2. **Understand the specs**: `cat ralph-workspace/specs/requirements.md`
3. **Start autonomous work**: `cd ralph-workspace && ralph --monitor`
4. **Review generated code**: Check `ralph-workspace/src/` when done
5. **Integrate**: Copy approved code to main Manim-ML project

---

Generated: 2026-01-09
Ralph version: frankbria/ralph-claude-code
Setup method: Dedicated workspace with stdin redirect
