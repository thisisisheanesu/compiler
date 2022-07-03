class Dataset():
    # Initialize
    def __init__(self, text: str):
        self.text = text
        self.lines = self.text.split("\n")
        # Update keywords
        self.updateKeywords()
        # Split into lines
        self.updateDataset(True)

    def updateKeywords(self):
        commandsDict = {
            "ADD": "&A",
            "SELECT": "&S",
            "WHERE": "&W",
            "GET": "&G",
            "<END>": "&E",
            "BOOK": "&B"
        }
        # Go through each line and replace commands
        ammendedLines = []
        for line in self.lines:
            if line.startswith("## QUERY:" or "## API:"):
                updatedLine = line
                for command in commandsDict:
                    updatedLine = updatedLine.replace(command, commandsDict[command])
                ammendedLines.append(updatedLine)
                print(updatedLine)
            else:
                ammendedLines.append(line)
        self.lines = ammendedLines
        self.updateDataset(False)
        # Replace keywords
        keywordsDict = {
            "## <--TRANSCRIPT-META-START--> ##": "&@Z$TMS",
            "## <--TRANSCRIPT-META-END--> ##": "&@Z$TME",
            "## <--USER-META-START--> ##": "&@Z$UMS",
            "## <--USER-META-END--> ##": "&@Z$UME",
            "## <--ZSH-RESULT-START--> ##": "&@Z$RS",
            "## <--ZSH-RESULT-END--> ##": "&@Z$RE",
            "## QUERY:": "&@Z$Q",
            "## API:":"&@Z$A"
        }
        for keyword in keywordsDict:
            self.text = self.text.replace(keyword, keywordsDict[keyword]) 

    # Removes comments
    def removeComments(self):
        # List to store lines without comments
        amendedLines = []
        for line in self.lines:
            # Check if line is a comment
            if not line.startswith('## //'):
                # Remove everything after the comment
                if len(line.split('## //')) > 1:
                    lineBeforeComment = line.split('## //')[0]
                    amendedLines.append(lineBeforeComment)
                else:
                    amendedLines.append(line)
        # Store lines without comments and update raw text
        self.lines = amendedLines
        self.updateDataset(False)
        
    # Removes trailing whitespace and keeps text and lines in sync
    def updateDataset(self, useText: bool):
        # Remove trailing whitespace
        self.text = self.text.rstrip()
        # useText true if text is to update lines
        if useText:
            self.lines = self.text.split("\n")
        else:
            self.text = ''
            for line in self.lines:
                self.text += f"{line}\n"
        # Remove last line if empty
        lastLineIndex = len(self.lines) - 1
        if self.lines[lastLineIndex] == '' or ' ' or '\n':
            self.lines.pop(lastLineIndex)

