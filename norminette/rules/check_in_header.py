from rules import Rule
from scope import *

allowed_in_header = [
    "IsVarDeclaration",
    "IsUserDefinedType",
    "IsPreprocessorStatement",
    "IsEmptyLine",
    "IsBlockStart",
    "IsBlockEnd",
    "IsComment",
    "IsEndOfLine",
    "IsFuncPrototype",
]

must_be_within_define = [
    "IsVarDeclaration",
    "IsUserDefinedType",
    "IsFuncPrototype",
]

class CheckInHeader(Rule):
    def __init__(self):
        super().__init__()
        self.depends_on = [
            "IsVarDeclaration",
            "IsUserDefinedType",
            "IsPreprocessorStatement",
            "IsEmptyLine",
            "IsBlockStart",
            "IsBlockEnd",
            "IsComment",
            "IsEndOfLine",
            "IsFuncPrototype",
        ]

    def run(self, context):
        if context.filetype != 'h':
            return False, 0
        if context.history[-1] not in allowed_in_header:
            context.new_error("FORBIDDEN_IN_HEADER", context.peek_token(0))
            return False, 0
        elif context.history[-1] in must_be_within_define and context.scope.header_protection != 1:
            context.new_error("HEADER_PROT_ALL", context.peek_token(0))
        return False, 0