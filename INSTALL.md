# Installing nh-stock-analyzer Skill

## Requirements
- Claude.ai or Claude Desktop app
- Access to web search tool
- Basic knowledge of stock market concepts

## Installation

### Method 1: Direct Copy (Easiest)
1. Download the skill package
2. Locate your Claude skills directory:
   - **Claude.ai**: `/mnt/skills/user/`
   - **Claude Desktop**: `~/.claude/skills/`
3. Copy the `nh-stock-analyzer` folder there
4. Restart Claude
5. Skill will auto-discover on next chat

### Method 2: ZIP Archive
1. Download `nh-stock-analyzer-v1.0.zip`
2. Extract to your skills directory
3. Restart Claude

### Method 3: .skill Package
1. Download `nh-stock-analyzer.skill`
2. Follow Anthropic's skill installation guide
3. Skill will integrate with your Claude instance

## Quick Test
After installation, 
try:
```
/nh-stock-analyzer MSFT
``` 
or
```
Should I buy Apple?
```

## Support
- For issues, see `references/IMPLEMENTATION_NOTES.md`
- For testing help, see `testing/TESTING_QUICK_START.md`