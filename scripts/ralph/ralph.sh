#!/bin/bash
# Ralph Wiggum - Model-Agnostic Autonomous AI Agent Loop
# Adapted from https://github.com/snarktank/ralph for multi-model workflows
#
# Usage:
#   ./scripts/ralph/ralph.sh [--tool amp|claude|codex|opencode|gemini] [max_iterations]
#   ./scripts/ralph/ralph.sh --cmd "your-agent-cli --flag" [max_iterations]

set -e

TOOL="amp"
CUSTOM_CMD=""
MAX_ITERATIONS=10

while [[ $# -gt 0 ]]; do
  case $1 in
    --tool)
      TOOL="$2"
      shift 2
      ;;
    --tool=*)
      TOOL="${1#*=}"
      shift
      ;;
    --cmd)
      CUSTOM_CMD="$2"
      TOOL="custom"
      shift 2
      ;;
    --cmd=*)
      CUSTOM_CMD="${1#*=}"
      TOOL="custom"
      shift
      ;;
    -h|--help)
      echo "Usage: ./scripts/ralph/ralph.sh [--tool amp|claude|codex|opencode|gemini] [--cmd '<cli>'] [max_iterations]"
      exit 0
      ;;
    *)
      if [[ "$1" =~ ^[0-9]+$ ]]; then
        MAX_ITERATIONS="$1"
      fi
      shift
      ;;
  esac
done

case "$TOOL" in
  amp|claude|codex|opencode|gemini|custom) ;;
  *)
    echo "Error: Invalid tool '$TOOL'. Must be 'amp', 'claude', 'codex', 'opencode', 'gemini', or use --cmd '<cli>'."
    exit 1
    ;;
esac

if [[ "$TOOL" == "custom" && -z "$CUSTOM_CMD" ]]; then
  echo "Error: --cmd requires a command string."
  exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROMPT_FILE="$SCRIPT_DIR/prompt.md"
PRD_FILE="$SCRIPT_DIR/prd.json"
PROGRESS_FILE="$SCRIPT_DIR/progress.txt"
ARCHIVE_DIR="$SCRIPT_DIR/archive"
LAST_BRANCH_FILE="$SCRIPT_DIR/.last-branch"

# Archive previous run if branch changed
if [ -f "$PRD_FILE" ] && [ -f "$LAST_BRANCH_FILE" ]; then
  CURRENT_BRANCH=$(jq -r '.branchName // empty' "$PRD_FILE" 2>/dev/null || echo "")
  LAST_BRANCH=$(cat "$LAST_BRANCH_FILE" 2>/dev/null || echo "")

  if [ -n "$CURRENT_BRANCH" ] && [ -n "$LAST_BRANCH" ] && [ "$CURRENT_BRANCH" != "$LAST_BRANCH" ]; then
    DATE=$(date +%Y-%m-%d)
    FOLDER_NAME=$(echo "$LAST_BRANCH" | sed 's|^ralph/||')
    ARCHIVE_FOLDER="$ARCHIVE_DIR/$DATE-$FOLDER_NAME"

    echo "Archiving previous run: $LAST_BRANCH"
    mkdir -p "$ARCHIVE_FOLDER"
    [ -f "$PRD_FILE" ] && cp "$PRD_FILE" "$ARCHIVE_FOLDER/"
    [ -f "$PROGRESS_FILE" ] && cp "$PROGRESS_FILE" "$ARCHIVE_FOLDER/"
    echo "   Archived to: $ARCHIVE_FOLDER"

    echo "# Ralph Progress Log" > "$PROGRESS_FILE"
    echo "Started: $(date)" >> "$PROGRESS_FILE"
    echo "---" >> "$PROGRESS_FILE"
  fi
fi

# Track current branch
if [ -f "$PRD_FILE" ]; then
  CURRENT_BRANCH=$(jq -r '.branchName // empty' "$PRD_FILE" 2>/dev/null || echo "")
  if [ -n "$CURRENT_BRANCH" ]; then
    echo "$CURRENT_BRANCH" > "$LAST_BRANCH_FILE"
  fi
fi

# Initialize progress file if it doesn't exist
if [ ! -f "$PROGRESS_FILE" ]; then
  echo "# Ralph Progress Log" > "$PROGRESS_FILE"
  echo "Started: $(date)" >> "$PROGRESS_FILE"
  echo "---" >> "$PROGRESS_FILE"
fi

echo "Starting Ralph - Tool: $TOOL - Max iterations: $MAX_ITERATIONS"

for i in $(seq 1 $MAX_ITERATIONS); do
  echo ""
  echo "==============================================================="
  echo "  Ralph Iteration $i of $MAX_ITERATIONS ($TOOL)"
  echo "==============================================================="

  case "$TOOL" in
    amp)
      OUTPUT=$(cat "$PROMPT_FILE" | amp --dangerously-allow-all 2>&1 | tee /dev/stderr) || true
      ;;
    claude)
      OUTPUT=$(claude --dangerously-skip-permissions --print < "$PROMPT_FILE" 2>&1 | tee /dev/stderr) || true
      ;;
    codex)
      OUTPUT=$(codex exec --full-auto - < "$PROMPT_FILE" 2>&1 | tee /dev/stderr) || true
      ;;
    opencode)
      OUTPUT=$(opencode run "$(cat "$PROMPT_FILE")" 2>&1 | tee /dev/stderr) || true
      ;;
    gemini)
      OUTPUT=$(gemini --yolo < "$PROMPT_FILE" 2>&1 | tee /dev/stderr) || true
      ;;
    custom)
      OUTPUT=$(bash -c "$CUSTOM_CMD" < "$PROMPT_FILE" 2>&1 | tee /dev/stderr) || true
      ;;
  esac

  if echo "$OUTPUT" | grep -q "<promise>COMPLETE</promise>"; then
    echo ""
    echo "Ralph completed all tasks!"
    echo "Completed at iteration $i of $MAX_ITERATIONS"
    exit 0
  fi

  echo "Iteration $i complete. Continuing..."
  sleep 2
done

echo ""
echo "Ralph reached max iterations ($MAX_ITERATIONS) without completing all tasks."
echo "Check $PROGRESS_FILE for status."
exit 1
