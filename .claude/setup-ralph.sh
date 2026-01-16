#!/bin/bash
# Ralph analysis workspace setup for Manim-ML
# This script initializes ralph for autonomous development analysis
#
# Usage: bash .claude/setup-ralph.sh [--regenerate]

set -e

RALPH_DIR="ralph-workspace"
REQUIREMENTS_FILE="requirements.md"

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${BLUE}🚀 Ralph Workspace Setup${NC}"
echo "=================================="

# Check if requirements.md exists
if [ ! -f "$REQUIREMENTS_FILE" ]; then
    echo -e "${YELLOW}⚠ Warning: $REQUIREMENTS_FILE not found${NC}"
    echo "Please ensure you're running this from the project root"
    exit 1
fi

# Handle regenerate flag
if [ "$1" = "--regenerate" ]; then
    echo -e "${YELLOW}Removing existing ralph-workspace...${NC}"
    rm -rf "$RALPH_DIR"
fi

# Create workspace if it doesn't exist
if [ ! -d "$RALPH_DIR" ]; then
    echo -e "${BLUE}Creating ralph-workspace directory...${NC}"
    mkdir -p "$RALPH_DIR"

    # Run ralph-import with stdin redirected
    echo -e "${BLUE}Running ralph-import...${NC}"
    (cd "$RALPH_DIR" && ralph-import "../$REQUIREMENTS_FILE" . < /dev/null)

    echo -e "${GREEN}✓ Ralph workspace initialized${NC}"
else
    echo -e "${YELLOW}Ralph workspace already exists${NC}"
fi

echo ""
echo -e "${GREEN}Setup complete!${NC}"
echo ""
echo "Next steps:"
echo "  1. Review: cd $RALPH_DIR && cat PROMPT.md"
echo "  2. Edit specs: nano $RALPH_DIR/specs/requirements.md"
echo "  3. Start autonomous mode: cd $RALPH_DIR && ralph --monitor"
echo ""
echo "To regenerate ralph workspace:"
echo "  bash .claude/setup-ralph.sh --regenerate"
