# Casino Website Generator - Documentation Index

This directory contains comprehensive documentation for the Casino Website Generator project to ensure accurate understanding and prevent hallucination when working with AI assistants.

## 📚 Documentation Files

### 🎯 [PROJECT_OVERVIEW.md](PROJECT_OVERVIEW.md)

**Complete project understanding and architecture**

- Project purpose and core functionality
- Detailed file structure with verified facts
- Component system explanation
- Technical implementation details
- Development status and planned features

### 🚫 [CURSOR_RULES.md](CURSOR_RULES.md)

**Critical rules to prevent AI hallucination**

- Key project facts that must never be hallucinated
- Verified file structure and component details
- Development guidelines and error prevention
- Common mistakes to avoid
- Casino-specific requirements

### 🧩 [COMPONENT_SYSTEM.md](COMPONENT_SYSTEM.md)

**Template system and component architecture**

- Component directory structure
- Template marking system and numbering
- Processing order and selection algorithm
- Content standards and compliance requirements
- Development guidelines for templates

### 🔧 [DEVELOPMENT_WORKFLOW.md](DEVELOPMENT_WORKFLOW.md)

**Development guidelines and best practices**

- Project workflow understanding
- Working with different project areas
- Testing and validation procedures
- Common development scenarios
- Debugging and troubleshooting

### 📖 [API_REFERENCE.md](API_REFERENCE.md)

**Complete function documentation**

- All functions in `starter.py` with exact signatures
- File system operations and patterns
- Template system constants and data structures
- Error handling patterns
- Code examples and usage

## 🎯 Purpose of This Documentation

This documentation set serves multiple critical purposes:

### For Human Developers

- **Complete understanding** of the project architecture
- **Development guidelines** for consistent code quality
- **API reference** for all functions and data structures
- **Workflow guidance** for efficient development

### For AI Assistants (Cursor, etc.)

- **Prevent hallucination** of non-existent files or functions
- **Ensure accurate understanding** of project structure
- **Provide verified facts** about implementation details
- **Guide proper development** following established patterns

## 🚨 Critical Understanding Points

### This is a Generator Tool

- **NOT** a simple website project
- **Generates** casino websites using templates
- **Main functionality** is in `starter.py` (720 lines)
- **Output** goes to `web-folder/` directory

### Template System Facts

- Each component has **exactly 10 template variants**
- Templates use **specific comment syntax** for extraction
- **Regex patterns** are used for template parsing
- **Processing order** is fixed and critical

### File Structure Facts

- `web-components/` = **source templates**
- `web-folder/` = **generated output**
- `master/` = **country-specific content**
- `scripts-folder/` = **placeholder scripts (empty)**

### Country Support

- **Confirmed countries**: Denmark, France, Portugal, UK-IR
- **Footer support**: Denmark, France, Portugal, UK-IR, Croatia, Argentina
- **Offers support**: Denmark, France, Portugal, UK-IR only

## 🔍 How to Use This Documentation

### Before Making Changes

1. Read **CURSOR_RULES.md** for critical constraints
2. Review **PROJECT_OVERVIEW.md** for context
3. Check **API_REFERENCE.md** for function details
4. Follow **DEVELOPMENT_WORKFLOW.md** for procedures

### When Adding Features

1. Understand existing patterns from **COMPONENT_SYSTEM.md**
2. Follow development guidelines in **DEVELOPMENT_WORKFLOW.md**
3. Reference **API_REFERENCE.md** for implementation details
4. Test according to **DEVELOPMENT_WORKFLOW.md** procedures

### When Debugging

1. Check **CURSOR_RULES.md** for common mistakes
2. Verify file existence using **PROJECT_OVERVIEW.md** structure
3. Review **DEVELOPMENT_WORKFLOW.md** debugging section
4. Reference **API_REFERENCE.md** for function behavior

## ✅ Documentation Verification

All documentation in this directory has been created by thoroughly analyzing:

- ✅ Complete `starter.py` file (720 lines)
- ✅ Project directory structure
- ✅ Template system implementation
- ✅ Country-specific content organization
- ✅ Component processing logic
- ✅ File operations and data flow

**No information has been hallucinated** - all facts are verified against the actual codebase.

---

**Remember**: This project is a sophisticated website generation system. Always consider the generation workflow when making modifications or providing assistance.
