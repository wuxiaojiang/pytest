import pypng
tool = pypng.png_tool()
tool.load('1.png')
tool.cheak_header()
tool.IHDR_chunk()
