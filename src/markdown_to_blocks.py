def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    non_empty_blocks = []
    for block in blocks:
        block = block.strip()
        if block != "":
            non_empty_blocks.append(block)
    return non_empty_blocks