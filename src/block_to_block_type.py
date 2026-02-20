from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph",
    HEADING = "heading",
    CODE = "code",
    QUOTE = "quote",
    UNORDERED_LIST = "unordered list",
    ORDERED_LIST = "ordered list"

def block_to_block_type(block):
    first_char = block[0]
    match first_char:
        case '#':
            if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
                return BlockType.HEADING
            return BlockType.PARAGRAPH
        case '`':
            if block.startswith("```\n") and block.endswith("```"):
                return BlockType.CODE
            return BlockType.PARAGRAPH
        case '>':
            lines = block.split('\n')
            for line in lines:
                if not line.startswith('>'):
                    return BlockType.PARAGRAPH
            return BlockType.QUOTE
        case '-':
            lines = block.split('\n')
            for line in lines:
                if not line.startswith("-"):
                    return BlockType.PARAGRAPH
            return BlockType.UNORDERED_LIST
        case '1':
            lines = block.split("\n")
            for i in range(len(lines)):
                if not lines[i].startswith(f"{i+1}. "):
                    return BlockType.PARAGRAPH
            return BlockType.ORDERED_LIST
        case _:
            return BlockType.PARAGRAPH
